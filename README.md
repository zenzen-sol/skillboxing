# Skillboxing

Persistent project memory for Claude. A CoWork plugin that maintains a `brain/` folder in your project, capturing what matters across sessions.

## The problem

Every time you start a new Claude session on a project, you lose context. You re-explain the background, re-state your preferences, re-describe decisions you already made. If someone else picks up the project, they start from zero.

## What skillboxing does

Skillboxing gives your project a memory. It creates and maintains a `brain/` folder — a collection of short markdown files that capture the important stuff: decisions, key facts, open questions, preferences, and anything else someone would need to know.

At the start of every session, Claude reads the brain. As you work, it stays in sync. The result: your second session on a project starts where the first one left off. And anyone who opens the project can say "review the brain" and be caught up in seconds.

## Install

```
claude plugin install skillboxing@skillboxing
```

Or install from the CoWork plugin browser.

## Usage

### Starting a session

Just start working. Skillboxing automatically loads `brain/index.md` at the beginning of every session. If no brain exists yet, it tells you how to create one.

### Capturing knowledge

At the end of a session (or any time something important happens):

```
/skillboxing:reflect
```

Claude scans the conversation for things worth remembering — decisions, corrections, key facts, open questions — and writes them to `brain/`. It filters aggressively: only durable, non-obvious, useful information makes it in.

### Cleaning up

Periodically, or after a major milestone:

```
/skillboxing:meditate
```

Claude reads the entire brain and audits it. It proposes changes — deleting stale notes, merging duplicates, tightening verbose files, filling gaps — and waits for your approval before applying them.

### Getting someone up to speed

When you (or someone else) opens the project in a new session:

```
Review the brain and summarize where things stand.
```

Claude reads `brain/index.md`, follows the links to relevant files, and gives a summary. No re-explaining needed.

## What ends up in the brain

Whatever matters for your project. Skillboxing has no opinions about your domain. Examples:

- **A contracts project**: key terms, party positions, open issues, concession history
- **A startup project**: formation status, cap table decisions, hiring pipeline
- **A research project**: sources, key findings, open questions
- **A product launch**: timeline, stakeholders, blockers, decisions made

The brain organizes itself around your project, not a predetermined schema.

## How it works

Skillboxing has four components:

### Two hooks (automatic)

**SessionStart** — When a session begins, `inject-brain.sh` loads `brain/index.md` into Claude's context. Claude sees what knowledge exists and reads relevant files before acting.

**PostToolUse** — When any tool modifies a file in `brain/`, `auto-index-brain.sh` checks whether `brain/index.md` is out of sync with the actual files on disk. If it is, it rebuilds the index automatically.

### Two skills (user-invoked)

**`/skillboxing:reflect`** — Scans the current conversation and writes what's worth remembering to `brain/`. Creates the brain folder on first use. Each item must be durable (matters in future sessions), non-obvious (Claude wouldn't know without being told), and useful (changes behavior or provides essential context).

**`/skillboxing:meditate`** — Reads the entire brain and proposes cleanup: delete stale notes, merge duplicates, tighten verbose files, fill coverage gaps, link orphans. Presents all proposed changes for approval before applying.

## Brain structure

The brain is just markdown files. There's no required structure — it adapts to your project. A typical brain might look like:

```
brain/
├── index.md              # Auto-maintained table of contents
├── project-context.md    # Background and objectives
├── key-decisions.md      # What was decided and why
├── open-questions.md     # Unresolved items
├── stakeholders.md       # Who's involved and their roles
└── templates/
    └── weekly-update.md  # Reusable formats
```

Files are short (under 50 lines), scannable (bullets over prose), and connected (wikilinks like `[[open-questions]]` link related files). The index rebuilds itself automatically.

## Plugin structure

```
skillboxing/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── hooks/
│   └── hooks.json               # SessionStart + PostToolUse event handlers
├── scripts/
│   ├── inject-brain.sh          # Loads brain index into context
│   └── auto-index-brain.sh     # Keeps index in sync with files
└── skills/
    ├── reflect/
    │   └── SKILL.md             # Capture learnings
    └── meditate/
        ├── SKILL.md             # Audit the brain
        └── scripts/
            └── snapshot.sh      # Concatenate brain files for review
```

## License

MIT
