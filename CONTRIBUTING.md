# Contributing
<!-- Human review required: changes need a code owner's approval (.github/CODEOWNERS). -->

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
  `ci:`, `chore:`, and `review:` for recorded human reviews.
- Commits written by a coding agent end with two trailers, which the PR
  advisory reads:

  ```
  Agent-Model: <model name>
  Agent-Tier: small | standard | large
  ```

  Human-written commits may add `Agent-Tier: none`; a commit without the
  trailer is assumed to be human-written.

## Choosing a model

The human picks the model; each skill's `index.json` gives a `model_tier`
hint.

| Work | Tier |
|---|---|
| BOOTSTRAP, SPECIFY, DESIGN, ADRs: judgement and trade-offs | large |
| DEVELOP against a failing test, VALIDATE, DEPLOY | standard |
| Fast Track, single commits, docs, small refactors | small |

Start one tier lower than you think. If the same test still fails after two
fix attempts, or the agent asks questions the spec already answers, move up a
tier. Move down when a task turns out to be Fast Track.

## Checks and what they mean

| Severity | Effect | Used for |
|---|---|---|
| Block | CI fails; the PR cannot merge | Real breakage: missing or inconsistent lifecycle files, a filled-in UC or ADR template, duplicate UC/ADR numbers, failing tests |
| Warn | Yellow annotation on the PR; merging is allowed | A small-tier commit changed use cases, ADRs, `AGENTS.md`, `CONTRIBUTING.md`, workflows or rulesets; any agent commit changed a review-gated file (`docs/INDEX.json`); a Fast Track branch exceeded its scope; a skill lacks `model_tier` |
| Info | Shown in the CI summary only | An agent commit without `Agent-Tier`; a large tier on a Fast Track branch |

Checks run on GitHub: the `structure` job blocks, the `advisory` job only
informs. Run the same blocking checks locally with the VS Code task
**AI-SDLC: Run checks** or `bash scripts/test.sh`.

## Human review report

When a set of agent loops or a conversation has concluded and you want your
check on record, run the VS Code task **AI-SDLC: Human review report** or
`python3 scripts/sdlc.py review`. It is optional and never blocks anyone.

It summarises the commits since your last report, asks five questions (what
changed, whether you read every file, whether the tests check the acceptance
criteria, what you checked yourself, what the PR reviewer should look at) and
records your answers as a `review:` commit ending in `Reviewed-by:`. Specific
answers to "what did you check yourself" are the evidence; "looked fine" is
not. Answering "partly" is fine and tells the PR reviewer where to look.

A review recorded after a flagged commit marks it as human-reviewed: the PR
advisory then shows "human-reviewed by <name>" instead of a warning. This
only settles the advisory; the teammate's approval is still required.

## Review and merge

- Every change to `main` goes through a PR with one teammate's approval and
  passing CI, and the branch must be up to date with `main`.
- Files listed in `.github/CODEOWNERS` also need a code owner's review.
- The author merges after approval, using **Rebase and merge**.
- If the `advisory` job warns, the reviewer looks harder at the flagged files,
  ideally with a second review by a larger model (Copilot code review on the
  PR, or an agent's code-review command), and leaves a one-to-three line
  "what I checked" comment with the approval.

## Coding agents

Agent rules live in `AGENTS.md` → "Git and review", which every agent loads.
This file is written for humans.

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
