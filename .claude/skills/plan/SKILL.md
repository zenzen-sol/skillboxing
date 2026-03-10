---
name: plan
description: Break down medium-to-large knowledge work projects into phased plans. Use for contract negotiations, company formation, hiring processes, document drafting projects, or any multi-step business initiative that benefits from structured sequencing.
---

# Plan

Break knowledge work projects into phased, dependency-aware plans.

## Process

1. **Triage complexity**
   - If the task is a single document or straightforward action, skip planning — just do it
   - Planning is for multi-step projects with dependencies, stakeholders, or sequencing risk

2. **Load principles**
   - Read `brain/principles.md` and all linked principle files
   - Pay special attention to [[sequence-dependencies]] and [[define-before-you-draft]]

3. **Define scope**
   - Use AskUserQuestion to resolve ambiguity:
     - Who are the parties / stakeholders?
     - What's the desired outcome?
     - What are the constraints (timeline, budget, jurisdiction, existing agreements)?
     - What's already done?

4. **Map dependencies**
   - Identify what blocks what
   - Flag external dependencies (third-party review, government filings, counterparty responses)
   - Distinguish between hard dependencies (must complete first) and soft ones (should complete first)

5. **Write the plan** to `brain/plans/`
   - **Overview file** (`brain/plans/[project-name].md`):
     - Context: parties, objectives, constraints
     - Scope: what's in and what's explicitly out
     - Applicable principles from the brain vault
     - Phase summary with dependency arrows
     - Open questions and risks
   - **Phase files** (`brain/plans/[project-name]-phase-N.md`):
     - Goal: one sentence
     - Deliverables: specific documents, filings, or decisions
     - Inputs: what's needed before starting
     - Outputs: what this phase produces for downstream phases
     - Verification: how to confirm the phase is complete and correct
     - Estimated stakeholder touchpoints (reviews, approvals, signatures)

6. **Phase sizing guidelines**
   - Each phase should produce 1-2 concrete deliverables
   - Prefer 5-8 small phases over 2-3 large ones
   - Group by natural checkpoints (e.g., "draft ready for review" is a phase boundary)

7. **Update plans index**: Add to `brain/plans/index.md`

8. **Present to user** — do NOT execute the plan. The plan is the deliverable.

## Example phase structures

**Contract negotiation**: Research → Term sheet → First draft → Internal review → Send to counterparty → Negotiate → Final draft → Execution
**Company formation**: Jurisdiction selection → Entity formation → Governance docs → Tax elections → Bank accounts → Equity plan
**Hiring**: Role definition → Offer terms → Offer letter draft → Background check → Employment agreement → Onboarding docs
