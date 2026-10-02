#!/usr/bin/env python3
"""Advisory checks for a pull request. Prints warnings and notices; never fails.

Usage: python3 scripts/pr_advisory.py BASE_SHA HEAD_SHA BRANCH
"""

import os
import re
import subprocess
import sys

TIERS = ("small", "standard", "large")

HIGH_JUDGEMENT = (
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/specs/UC-",
    "docs/adr/ADR-",
    ".github/workflows/",
    ".github/rulesets/",
)

FAST_TRACK_EXCLUDED = (
    "requirements",
    "pyproject.toml",
    ".github/workflows/",
    ".github/rulesets/",
    "docs/adr/",
)

AGENT_CO_AUTHOR = re.compile(
    r"^co-authored-by:.*\b(claude|copilot|codex|gpt|gemini|cursor|agent)\b",
    re.IGNORECASE | re.MULTILINE,
)


def _trailer(message, name):
    match = re.search(rf"^{name}:\s*(.+?)\s*$", message, re.IGNORECASE | re.MULTILINE)
    return match.group(1) if match else None


def tier_of(message):
    value = _trailer(message, "Agent-Tier")
    return value.lower() if value else None


def model_of(message):
    return _trailer(message, "Agent-Model")


def is_agent_commit(message):
    tier = tier_of(message)
    if tier is not None:
        return tier in TIERS
    return bool(AGENT_CO_AUTHOR.search(message))


def _matches(path, prefixes):
    return any(path == p or path.startswith(p) for p in prefixes)


def _is_fast_track(branch):
    return branch.startswith(("fix-", "docs-"))


def advise(commits, changed, branch):
    findings = []

    for c in commits:
        short = c["sha"][:7]
        tier = tier_of(c["message"])
        if tier == "small":
            risky = [f for f in c["files"] if _matches(f, HIGH_JUDGEMENT)]
            if risky:
                findings.append((
                    "warning",
                    f"Commit {short} (Agent-Tier: small) changed high-judgement files: "
                    f"{', '.join(risky)}; review thoroughly, ideally with a second review "
                    "by a larger model (CONTRIBUTING.md).",
                ))
        elif tier is None and is_agent_commit(c["message"]):
            findings.append((
                "notice",
                f"Commit {short} looks agent-written but has no Agent-Tier trailer; "
                "model tier unknown.",
            ))

    if _is_fast_track(branch):
        excluded = [
            path for status, path in changed
            if _matches(path, FAST_TRACK_EXCLUDED)
            or (status == "A" and path.startswith("docs/specs/UC-"))
        ]
        if excluded:
            findings.append((
                "warning",
                f"Fast Track scope exceeded on '{branch}': {', '.join(excluded)}. "
                "Fast Track excludes dependencies, workflows, ADRs and new use cases; "
                "open a use-case issue (CONTRIBUTING.md).",
            ))
        if any(tier_of(c["message"]) == "large" for c in commits):
            findings.append((
                "notice",
                "A large model was used on a Fast Track branch; a smaller tier is "
                "usually enough here.",
            ))

    return findings


def _git(args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, check=True,
                          capture_output=True, text=True).stdout


def collect(base, head, cwd=None):
    log = _git(["log", "--no-merges", "--format=%x1e%H%x1f%B%x1f", "--name-only",
                f"{base}..{head}"], cwd)
    commits = []
    for record in log.split("\x1e")[1:]:
        sha, message, files = record.split("\x1f")
        commits.append({
            "sha": sha,
            "message": message,
            "files": [f for f in files.splitlines() if f.strip()],
        })
    diff = _git(["diff", "--name-status", "--no-renames", f"{base}...{head}"], cwd)
    changed = [tuple(line.split("\t", 1)) for line in diff.splitlines() if line.strip()]
    return commits, changed


def report(findings):
    on_actions = bool(os.environ.get("GITHUB_ACTIONS"))
    if not findings:
        print("✓ No advisory findings.")
    for level, text in findings:
        print(f"{'⚠' if level == 'warning' else 'ℹ'} {text}")
        if on_actions:
            print(f"::{level}::{text}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as fh:
            fh.write("## PR advisory\n\n")
            if not findings:
                fh.write("No advisory findings.\n")
            for level, text in findings:
                fh.write(f"- **{level}:** {text}\n")


def main(argv):
    if len(argv) != 4:
        print(__doc__.strip())
        return 0
    _, base, head, branch = argv
    commits, changed = collect(base, head)
    report(advise(commits, changed, branch))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
