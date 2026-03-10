# Meditate Subagent Specifications

## Auditor Subagent

**Role**: Evaluate every brain file for quality and relevance.

**Input**: Brain snapshot (from snapshot.sh)

**Evaluate each note against**:
1. **Freshness**: Is this still accurate? Has the domain changed?
2. **Signal**: Does this change behavior, or is it trivia?
3. **Frequency**: How often would this be consulted?
4. **Redundancy**: Does another note already cover this?
5. **Precision**: Is this tight and scannable, or rambling?

**Output format**:
```
## Audit Findings

### Delete
- `path/file.md` — [rationale]

### Merge
- `path/a.md` + `path/b.md` → `path/target.md` — [rationale]

### Tighten
- `path/file.md` — [specific revision suggestion]

### OK
- [count] files passed audit
```

**Early exit**: If fewer than 3 actionable items across Delete/Merge/Tighten, output "Vault is clean" and stop.

---

## Reviewer Subagent

**Role**: Three-in-one pass — synthesis, distillation, and template review.

**Input**: Brain snapshot + Auditor output

### Pass 1: Synthesis
- Identify missing cross-references between related notes
- Flag principle tensions (two principles that pull in opposite directions)
- Note gaps in coverage (domains, scenarios, edge cases)

### Pass 2: Distillation
- Surface unstated principles evidenced by 2+ notes
- Each candidate must be: independent, actionable, evidenced
- Propose name, one-line description, and 3-5 bullet points

### Pass 3: Template review
- Check existing templates against principles — are they consistent?
- Identify principles that should be templates (repeated manual enforcement)
- Flag templates that encode outdated practices

**Output format**:
```
## Reviewer Findings

### Cross-references needed
- `path/a.md` ↔ `path/b.md` — [connection]

### Principle tensions
- [[principle-a]] vs [[principle-b]] — [tension description]

### Coverage gaps
- [domain/scenario] — [what's missing]

### Candidate principles
- **name**: one-line description
  - Evidence: [note1], [note2]
  - Bullets: ...

### Template opportunities
- [description] — could become `brain/templates/[name].md`
```
