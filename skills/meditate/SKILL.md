---
name: meditate
description: Audit and clean up the project brain. Prunes stale notes, merges duplicates, tightens verbose files, and fills gaps. Use when the brain feels cluttered, after a major project milestone, or periodically to keep it sharp.
---

# Meditate

Audit the project's `brain/` folder for quality and coherence.

## Process

1. **Read everything** in `brain/`, starting from `index.md`

2. **Audit each file** against:
   - **Still true?** Has the project moved past this? Are facts outdated?
   - **Still useful?** Would someone picking up the project need this?
   - **Redundant?** Does another file already cover this?
   - **Scannable?** Can you get the point in 10 seconds?
   - **Connected?** Are related files linked via wikilinks?

3. **Check the whole** for:
   - Contradictions between files
   - Gaps — important aspects of the project with no coverage
   - Orphan files not linked from `index.md`
   - Files that should be merged (overlapping topics)
   - Files that should be split (covering too much)

4. **Present findings** before making changes. Group by action type — deletions, merges, tightening, gaps, orphans — with a one-line rationale for each. Example:

   > **Delete:** `brain/initial-timeline.md` — superseded by `brain/revised-timeline.md`
   > **Merge:** `brain/vendor-a-notes.md` + `brain/vendor-b-notes.md` → `brain/vendor-comparison.md`
   > **Tighten:** `brain/project-context.md` — 3 paragraphs can be reduced to 6 bullets
   > **Gap:** No record of budget constraints discussed last week
   > **Orphan:** `brain/meeting-notes-jan.md` — not linked from index

   Ask the user to confirm before applying any changes

5. **Apply** approved changes only

6. **Rebuild `brain/index.md`** to reflect the current state
