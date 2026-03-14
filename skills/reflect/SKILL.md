---
name: reflect
description: Capture what matters from the current session into the project brain. Use at the end of a work session, after important decisions, corrections, or discoveries, or when the user says to update or add to the brain.
---

# Reflect

Capture learnings from the current session into the project's `brain/` folder.

## First run

If `brain/` doesn't exist yet, create it:

```
brain/
└── index.md
```

Start `index.md` with `# Brain` and build it as you add files.

## Process

1. **Read `brain/index.md`** to see what's already captured

2. **Scan the conversation** for things worth remembering:
   - Decisions made and why
   - Key facts about the project (parties, terms, constraints, contacts)
   - Corrections ("no, actually..." — the user fixed a misunderstanding)
   - Preferences and working style
   - Open questions and unresolved issues
   - Anything someone picking up this project would need to know

3. **Filter**. Each item must pass:
   - **Durable**: Would this matter in a future session? (Not just "we discussed X")
   - **Non-obvious**: Would a new person or fresh Claude session know this without being told?
   - **Actionable or informational**: It either changes how you'd work or provides essential context

4. **Write** brain files:
   - One topic per file
   - Filenames: lowercase, hyphenated, `.md` (e.g., `key-terms.md`, `open-questions.md`)
   - Keep files under ~50 lines — scannable, not exhaustive
   - Bullets over prose
   - Use wikilinks `[[file-name]]` to connect related files
   - Organize into subdirectories when a category has 3+ files

5. **Update `brain/index.md`** with wikilinks to any new files, including a brief description after each link (e.g., `[[analysis/owner-servicer-framing]] — Unified theory resolving silent participant vs. receivables purchaser tension`). Descriptions help humans scanning the brain in Obsidian. Keep them to one phrase.

6. **Report** what was added, updated, or removed, with a one-line rationale for each

## What goes where

- Facts, context, decisions → top-level brain files
- Recurring checklists or processes → `brain/templates/`
- Project phases or milestones → `brain/plan.md` or `brain/plan/`
- Open questions → `brain/open-questions.md`

Use whatever structure fits the project. The brain should reflect how the project is actually organized, not a predetermined schema.

## Updating existing files

If new information supersedes or extends an existing brain file, update it in place rather than creating a new file. Delete files that are no longer relevant.
