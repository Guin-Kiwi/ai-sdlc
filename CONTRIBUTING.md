# Contributing

How people and coding agents work together in this repository. The lifecycle
itself is defined in `AGENTS.md`; this file covers team workflow.

## How big is this change?

Pick the lowest level that fits. Only use cases need an issue.

| Level | What qualifies | Record it in | Issue? |
|---|---|---|---|
| 1. Commit | A step inside already-scoped work: a test, an implementation step, a refactor | The commit, on the use case's branch | No |
| 2. Fast Track | A small correction within existing behaviour: a bug fix (start with a failing test), wording, config, docs | One line in the PR description or `docs/TASKS.md` | No |
| 3. Use case | Anything that adds or changes observable behaviour, i.e. something an acceptance criterion would describe | Issue → `docs/specs/UC-<issue>-<NAME>.md` → branch → PR | Yes |
| 4. ADR | A consequential decision that is hard to reverse or spans use cases: data store, auth approach, framework, a break in the layer rules | `docs/adr/ADR-NNN-<title>.md`, Proposed until a human accepts it | Usually inside a use case's PR |

Fast Track never covers new features, API or data changes, security,
dependencies or architecture. If a Fast Track grows into any of these, stop,
open a use-case issue and continue in the regular flow.

Borderline? If a teammate would need to agree on *what* it should do before
you build it, it is a use case. If they only need to check *how* you did it,
it is Fast Track.

## Use cases, branches and pull requests

- Open a **Use case** issue. Its number is the use-case number: issue #42 →
  `docs/specs/UC-042-<NAME>.md` on branch `uc-042-<short-name>`.
- Fast Track branches: `fix-<short-name>` or `docs-<short-name>`.
- One use case per branch and per PR. The PR body says `Closes #42`.
- On a branch, `docs/TASKS.md` describes that branch's use case only. Before
  merging, update the branch from `main` and reconcile `docs/TASKS.md` and
  any UC or ADR numbers with what `main` already has.
- ADR numbers: take the next unused number on `main`. CI rejects duplicates.
- Change shared files (`AGENTS.md`, `docs/PROJECT.md`, `docs/INDEX.json`,
  `.github/`) in their own small PR, not mixed into feature work.

## Commits

- Keep the TDD steps as separate commits (failing test, then implementation,
  then refactor). PRs are **rebase-merged** so this history stays on `main`
  as evidence.
- Use conventional prefixes: `feat:`, `fix:`, `test:`, `refactor:`, `docs:`,
  `ci:`, `chore:`.
- Commits written by a coding agent carry a `Co-Authored-By:` trailer naming
  the agent.

## Review and merge

- Every change to `main` goes through a PR with one teammate's approval and
  passing CI, and the branch must be up to date with `main`.
- Files listed in `.github/CODEOWNERS` also need a code owner's review.
- The author merges after approval, using **Rebase and merge**.

## Coding agents

- Work only on the branch for the current use case or Fast Track; never
  commit to `main`.
- Never push, merge, force-push or delete branches unless a human asks for it
  in the current session.
- Run `bash scripts/test.sh` before proposing a PR and report the result.
- To run two agents at once, give each its own worktree:
  `git worktree add ../<repo>-uc-042 uc-042-<short-name>`.

## Repository setup

Rulesets are not copied when a repository is created from the template.
Import them once under **Settings → Rules → Rulesets → New ruleset → Import a
ruleset**, from `.github/rulesets/`:

- `main-team.json` for team repositories: PRs with one approval, code-owner
  review, up-to-date branches, passing CI, rebase-merge only, no force pushes.
- `main-solo.json` for single-person repositories: no force pushes or
  deletion of `main`.
- `release-tags.json`: only admins create, move or delete `v*` tags.

Rulesets on private repositories need GitHub Pro on the owner's account
(included in the GitHub Student Developer Pack). Also enable secret scanning
with push protection and Dependabot alerts under **Settings → Code security**,
and **Automatically delete head branches** under **Settings → General**.
