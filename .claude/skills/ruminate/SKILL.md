---
name: ruminate
description: Mine past conversation history for uncaptured patterns, preferences, and domain knowledge. Use when the brain vault might be missing learnings from previous sessions — especially after many sessions without reflecting.
---

# Ruminate

Mine past conversation history for learnings that `/reflect` missed.

## Process

1. **Build brain snapshot**: Run `bash .claude/skills/meditate/scripts/snapshot.sh brain/` to know what's already captured

2. **Locate conversations**: Find conversation files in `~/.claude/projects/` for this project

3. **Extract conversations**: Run `python3 .claude/skills/ruminate/scripts/extract-conversations.py` to parse JSONL files into readable batches
   - Supports `--after YYYY-MM-DD` to filter by date
   - Supports `--batches N` to control parallelism (default: 5)

4. **Analyze each batch** for:
   - User corrections ("no, actually...", "that's wrong", "I prefer...")
   - Recurring preferences (style, tone, risk tolerance, process)
   - Domain knowledge (contract patterns, legal nuances, operational procedures)
   - Workflow patterns (how work is sequenced, who reviews, what gets escalated)
   - Frustrations and friction (repeated complaints, workarounds)
   - Edge cases discovered during real work

5. **Filter aggressively**:
   - Must appear 2+ times across conversations OR be clearly high-impact
   - Must be factually accurate (not a misunderstanding that was later corrected)
   - Must not already exist in the brain vault
   - Must pass the durability test

6. **Present findings** in table format:

   | Finding | Evidence | Frequency | Destination |
   |---------|----------|-----------|-------------|
   | ... | conv 3, conv 7 | 3x | brain/principles/ |

7. **Wait for approval**: User reviews and approves before any brain updates

8. **Apply approved items** and update indexes

9. **Cleanup**: Remove temp files created during extraction
