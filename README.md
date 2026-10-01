# AI-SDLC Project Template

[![AI-SDLC](https://img.shields.io/badge/AI--SDLC-v1.0.0-blue)](https://ai-sdlc.aisl.science)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22833065.svg)](https://doi.org/10.5281/zenodo.22833065)
[![arXiv](https://img.shields.io/badge/arXiv-2609.24348-b31b1b.svg)](https://doi.org/10.48550/arXiv.2609.24348)

Starter repository for student and teaching projects that use the AI-Assisted
Software Development Life Cycle (AI-SDLC).

The method is documented canonically in [AISL Docs](https://docs.aisl.science/learning-and-resources/ai-sdlc). This repository contains only the executable, repository-local
workflow artefacts. It does not contain a complete copy of the method or
application-specific code.

## Create a project

1. Select **Use this template** on GitHub and create a new repository. A
   one-time **"Define the project (BOOTSTRAP)"** issue opens with a checklist.
2. Open the new repository in GitHub Codespaces. Setup runs automatically and
   ends with `scripts/check-setup.sh`; run it again any time to confirm agents
   can find the skills.
3. Start BOOTSTRAP with your agent:
   - GitHub Copilot Chat: `/ai-sdlc`, then choose `bootstrap`
   - Claude Code: `/ai-sdlc-0-bootstrap`
   - Other agents: ask them to follow `AGENTS.md` and start phase 0
   BOOTSTRAP completes `docs/PROJECT.md`, then proposes removal or replacement
   of this template's own commentary, badges and citation files. The agent
   asks for confirmation before removing or replacing template identity.
4. For each feature, open a **Use case** issue and ask your agent to start
   SPECIFY from it. Progress is recorded in `docs/TASKS.md`. Smaller changes
   need no issue; `CONTRIBUTING.md` explains which level a change belongs to
   and how branches, PRs and reviews work in a team.

The included GitHub Actions workflows run `scripts/check-lifecycle.sh` (are
the AI-SDLC artefacts present and consistent?) and `scripts/test.sh`, the
project's test entrypoint. It ships running only the lifecycle checks; extend
it with your project's tests during VALIDATE. `.github/CODEOWNERS` marks the
files that need human review; turn on "Require review from Code Owners" in
branch protection to enforce it. `.github/workflows/cd.yml` is an inactive template,
configured during DEPLOY.

## Agent setup

The default stack profile is **Python + FastAPI**: Codespaces creates a Python
development container with Python, Pylance, debugging and GitHub Copilot
extensions, and `scripts/setup-python.sh` prepares `.venv`. This template
assumes Python ([ADR-000](docs/adr/ADR-000-python-as-project-language.md));
BOOTSTRAP keeps the profile and adjusts the framework. The default
terminal locale is English; the VS Code UI uses its own user display-language
setting.

Codespaces links the skills for all supported agents. Run
`bash scripts/setup-skills.sh` yourself when working outside Codespaces. Run
`bash scripts/setup-python.sh` again when the Python environment needs to be
recreated or refreshed.
Choose `copilot`, `codex`, `claude`, `cline`, `opencode`, `cursor`, `kiro`,
`junie`, `devin` or `all`. The script links to the canonical `skills/` directory and
falls back to copying if links are unavailable. Existing destinations are kept;
copies must be refreshed manually after skill changes. Verify discovery in your
agent; setup does not install or configure the agent itself.

For non-interactive setup, pass the same selection, for example `bash scripts/setup-skills.sh copilot`. `CLAUDE.md` (which imports `AGENTS.md`) is included in the repository; the `claude` and `all` selections recreate it if missing. Skill links are per-machine and ignored by git.

## Repository artefacts

- `AGENTS.md` — lifecycle router and guardrails (`CLAUDE.md` imports it)
- `CONTRIBUTING.md` — team workflow: change-size ladder, branches, PRs, agent
  git rules, repository setup
- `docs/INDEX.json` — machine-readable map of phases, skills and edit policy
- `docs/PROJECT.md` — project context and commands
- `docs/TASKS.md` — current lifecycle state
- `docs/specs/` — executable use-case specifications
- `docs/adr/` — architecture decision records and their template
- `docs/STANDARDS.md` — security and quality references (NIST SSDF, OWASP ASVS)
- `docs/AGENT-GUIDANCE.md` — worked examples for applying the agent rules
- `docs/future/` — non-binding roadmap notes
- `skills/ai-sdlc-*` — phase-specific execution guidance
- `.devcontainer/` — Codespaces and VS Code baseline
- `environments/python/` — default Python + FastAPI profile, including the
  source VS Code debug configuration
- `scripts/setup-skills.sh`, `scripts/setup-python.sh` — agent and environment setup
- `scripts/check-setup.sh` — confirms local setup worked
- `scripts/check-lifecycle.sh` — artefact consistency checks run by CI
- `scripts/test.sh` — project test entrypoint run by CI and release;
  `scripts/test-lifecycle.sh` holds scenario tests for the lifecycle checker
- `.github/` — Copilot instructions and `/ai-sdlc` prompt, CODEOWNERS, PR and
  use-case issue templates, CI, release, bootstrap-issue and CD workflows,
  importable rulesets
