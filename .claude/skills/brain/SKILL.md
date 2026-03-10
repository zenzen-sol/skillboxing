---
name: brain
description: Read and write to the persistent brain vault for contracts, startup operations, and business knowledge. Use when capturing learnings, looking up principles, checking past decisions, or managing the knowledge base in the brain/ directory.
---

# Brain

Read and write to the `brain/` directory — a persistent knowledge vault that survives across sessions.

## Reading

1. Start with `brain/index.md` — it links to everything
2. Follow the relevant `[[wikilink]]` to the topic you need
3. Read before acting — existing knowledge should inform your work

## Writing

1. **Durability test**: "Would I include this in a prompt for a *different* task?"
   - Yes → brain file
   - No → it's session-specific, skip it
2. One topic per file
3. Filenames: lowercase, hyphenated, `.md` (e.g., `indemnity-patterns.md`)
4. Keep notes under ~50 lines
5. Wikilinks format: `[[section/file-name]]`
6. Bullets over prose, no YAML frontmatter in brain files
7. After writing, update `brain/index.md` and the relevant section entrypoint

## Routing guide

- **Principles**: `brain/principles/` — durable heuristics that guide decisions
- **Plans**: `brain/plans/` — phased project breakdowns
- **Templates**: `brain/templates/` — reusable checklists, clause banks, document skeletons

## Maintenance

- Delete notes that are outdated or subsumed by newer ones
- Merge overlapping notes into a single file
- If a note can be encoded as a template or checklist, do that instead
