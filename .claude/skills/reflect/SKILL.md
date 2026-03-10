---
name: reflect
description: Capture learnings from the current session into the brain vault. Use at the end of a work session, after receiving corrections, or when valuable patterns emerge during contract review, drafting, negotiation, or startup operations work.
---

# Reflect

Capture learnings from the current session into the brain vault.

## When to run

- End of a work session
- After receiving a correction or preference
- After a non-obvious discovery about a document, process, or domain

## Process

1. **Load context**: Read `brain/index.md`

2. **Scan the conversation** for:
   - Mistakes and corrections (you got something wrong, user fixed it)
   - User preferences (formatting, tone, clause style, risk tolerance)
   - Domain knowledge (contract patterns, legal nuances, deal structures)
   - Process knowledge (how the user sequences work, who reviews what)
   - Edge cases and gotchas (unusual clause interactions, jurisdiction quirks)
   - Negotiation patterns (what the user concedes on, what they hold firm on)
   - Template opportunities (repeated manual steps that could be standardized)

3. **Filter aggressively**:
   - Skip trivial or obvious items
   - Skip items already captured in the brain
   - Apply the durability test: "Would this matter in a different session?"

4. **Route each learning** to the right destination:
   - **Can it be a template or checklist?** → `brain/templates/` (structural > textual)
   - **Is it a durable principle?** → `brain/principles/`
   - **Is it domain knowledge?** → appropriate brain section
   - **Does it improve a skill?** → update the relevant SKILL.md directly
   - **Is it a preference or quirk?** → brain file with clear label

5. **Update indexes**: After writing, update `brain/index.md` and relevant entrypoints

6. **Output summary**: List what was created, updated, or deleted, with one-line rationale each

## Quality bar

Every item must pass: **durable** (lasts beyond this session), **actionable** (changes future behavior), and **non-obvious** (Claude wouldn't know this without being told).
