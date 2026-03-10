---
name: meditate
description: Audit and evolve the brain vault. Prunes low-value notes, synthesizes principles, identifies gaps, and distills new patterns. Use periodically to maintain brain quality, after significant project milestones, or when the vault feels cluttered.
---

# Meditate

Audit and evolve the brain vault. Quality bar: notes must be **high-signal**, **high-frequency**, or **high-impact**.

## Process

1. **Build snapshot**: Run `bash .claude/skills/meditate/scripts/snapshot.sh brain/` to concatenate all brain files into a single reviewable document

2. **Audit** the snapshot for:
   - **Stale notes**: Information that's no longer accurate or relevant
   - **Redundancy**: Multiple notes covering the same ground
   - **Low-value content**: Notes that fail the durability test
   - **Verbosity**: Notes that can be tightened without losing meaning
   - **Orphans**: Files not linked from any index
   - **Contradictions**: Principles or notes that conflict with each other
   - Early-exit if fewer than 3 actionable items found

3. **Synthesize** across the vault:
   - Missing wikilinks between related notes
   - Principle tensions that need resolution or acknowledgment
   - Gaps: domains or scenarios with no coverage
   - Patterns that appear across multiple notes but lack a unifying principle

4. **Distill** new principles:
   - Must be independent (not a restatement of an existing principle)
   - Must be evidenced by 2+ existing notes or repeated session patterns
   - Must be actionable (changes future behavior)

5. **Review templates**: Cross-reference `brain/templates/` against principles
   - Do templates encode the right principles?
   - Are there principles that should be templates?

6. **Present findings** as a consolidated report:
   - Items to delete (with rationale)
   - Items to merge (with proposed target)
   - Items to tighten (with proposed revision)
   - New principles to add (with evidence)
   - Template opportunities
   - Wait for user approval before applying changes

7. **Apply changes** and update all indexes

## Subagent prompts

See [references/agents.md](references/agents.md) for detailed auditor and reviewer subagent specifications.
