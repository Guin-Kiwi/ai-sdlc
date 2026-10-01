---
name: ai-sdlc-0-bootstrap
description: Initialize or align a repository for AI-SDLC based on the intended system.
---

# PHASE 0 — BOOTSTRAP

## Goal

Align the repository with the **intended system** and prepare it for AI-SDLC.

---

## Required Input

Clarify with the user:

- system / app purpose
- language
- framework
- runtime

If unclear → ask before proceeding.

---

## Actions

### 1. Inspect repository

Check existing:

- structure (src/, tests/, docs/)
- dependency files
- existing code and tests

---

### 2. Align structure (minimal changes)

Ensure Clean Architecture:

src/app/domain  
src/app/application  
src/app/interfaces  
src/app/infrastructure  

tests/unit  
tests/integration  
tests/e2e  

Rules:

- create only missing directories; do not add directory-marker files such as
  `__init__.py` unless required by the selected language or framework
- reuse existing structure if compatible
- do not duplicate or restructure unnecessarily

---

### 3. Dependencies

Check for:

requirements.txt  
pyproject.toml  
package.json  

Rules:

- reuse if present
- create minimal file only if missing

---

### 4. Documentation

Ensure:

docs/PROJECT.md

Rules:

- update if exists
- create minimal version if missing

Content:

- purpose
- architecture
- structure
- commands
- dependencies

---

### 5. Cleanup (only with user confirmation)

Identify:

- unused files
- irrelevant boilerplate
- mismatching structure
- template-only meta commentary that no longer applies once the project is
  established (e.g. `docs/PROJECT.md`'s "Complete this document during
  BOOTSTRAP" instruction line, README's template setup/"Create a project"
  steps) — replace with the real project's own content instead of removing
  the file
- template identity: README badges (AI-SDLC, DOI, arXiv), `CITATION.cff` and
  `.zenodo.json` describe the template, not the derived project — replace or
  remove them for the project

Ask the user before removing anything.

---

## Output

Repository aligned with intended system.

Record phase 0 and status in `docs/TASKS.md` per `AGENTS.md`.

---
