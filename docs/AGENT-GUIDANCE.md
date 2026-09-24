# Agent Guidance

This document captures practical guidance for better agentic work in this
repository.

It is intentionally lightweight.
The goal is not to maximize autonomy.
The goal is to maximize useful, reviewable, reality-based progress.

---

## 1. Start from a concrete goal
An agent should not begin by “doing work” in the abstract.

It should first identify:

- the requested outcome
- the relevant repo-local instructions
- the current phase or task status
- the smallest viable next step

If the task cannot be stated clearly in one or two sentences, it is probably
not ready for execution.

---

## 2. Prefer grounded execution over improvisation
Useful agentic work is grounded in the repository’s own artifacts first.

Read in the defined order:
1. `docs/TASKS.md`
2. `docs/PROJECT.md`
3. active spec or fast-track task entry

Then use outside knowledge only to support implementation or evaluation.

### Good grounding signals
- cites the active requirement
- references the current phase
- names the affected files or artifacts
- defines what success looks like

### Weak grounding signals
- generic best-practice output
- large unsolicited rewrites
- implied requirements with no source
- claiming completion without validation

---

## 3. Make success criteria explicit
Before making changes, identify what would count as success.

Examples:
- a document now includes specific missing guidance
- a use case has testable acceptance criteria
- a code change is covered by tests and passes them
- a risky change is escalated instead of silently applied

An agent should not rely on “this seems better” as the only completion
standard.

---

## 4. Decompose work into small steps
Smaller steps improve correctness, reviewability, and recovery from mistakes.

Use decomposition especially when:
- tasks involve multiple files
- requirements are incomplete
- architecture could be affected
- implementation and validation are both needed

A good step is:
- independently understandable
- easy to review
- easy to validate
- easy to revert

---

## 5. State assumptions instead of hiding them
Agents often need to infer missing details.
That is acceptable only when assumptions are visible.

When assumptions are necessary:
- label them clearly
- keep them minimal
- avoid irreversible decisions based on weak assumptions
- ask for confirmation if the assumption changes behavior, scope, or
  architecture

Hidden assumptions reduce trust and make review harder.

---

## 6. Stop when confidence is not justified
Good agentic behavior includes knowing when not to proceed.

Stop and ask when:
- requirements conflict
- the next step is not clearly authorized
- a decision changes architecture materially
- security or privacy impact is unclear
- available evidence is too weak to justify action

The correct move is often to narrow the task, present options, and request
direction.

---

## 7. Prefer evidence-backed completion
Completion claims should be supported by evidence appropriate to the phase.

Examples of evidence:
- acceptance criteria added
- checklist completed
- tests written and passing
- changed files listed
- risks and open questions documented
- review-trigger conditions identified

Do not treat file creation alone as proof of progress.

---

## 8. Optimize for human review
The repository is designed for human-plus-agent collaboration.

That means outputs should be:
- small
- clear
- traceable
- easy to inspect
- explicit about uncertainty

A reviewer should be able to answer:
- what changed?
- why did it change?
- how was it validated?
- what remains unknown?

---

## 9. Use external guidance carefully
External guidance can improve results, but it should not override repo-local
intent.

Use external sources to support:
- task structuring
- prompt/instruction quality
- verification and review practices
- security considerations
- risk identification

Do not use external guidance to:
- expand scope without approval
- inject heavyweight process unnecessarily
- replace the repository’s defined operating model

---

## 10. Security-sensitive work deserves extra friction
For security-relevant work, agents should be more conservative, not less.

Apply extra care when changes affect:
- auth or authorization
- secrets or credentials
- trust boundaries
- external integrations
- data handling
- deployment or release behavior

In such cases, clearly flag the risk and prefer human confirmation before broad
changes.

---

## 11. Recommended default output pattern
When completing a task, use this compact pattern when appropriate:

### Goal
What is being changed and why?

### Context used
What repo files or requirements were consulted?

### Plan
What is the smallest next step?

### Result
What changed?

### Validation
How was the result checked?

### Assumptions / questions
What still needs confirmation?

### Next step
What should happen next?

---

## 12. Practical anti-patterns to avoid
Avoid these common failure modes:

- doing more than was asked
- silently broadening scope
- skipping validation
- presenting assumptions as facts
- rewriting large sections without necessity
- producing polished but ungrounded documentation
- using standards language without practical effect
- making risky decisions without escalation

---

## References
These sources informed the guidance in this file:

- Anthropic guidance on effective agent/task instruction, including clear
  success criteria and source-grounded work
- Microsoft guidance on system instructions, scoped behavior, boundaries,
  evaluation, and iteration
- Google guidance emphasizing decomposition and human-in-the-loop review for
  agentic systems
- NIST guidance as supporting context for trustworthy and governed
  software/AI development

See also:
- `docs/STANDARDS.md`
