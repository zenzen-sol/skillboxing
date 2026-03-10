---
name: review
description: Principle-grounded review of documents, contracts, plans, or business decisions. Use when reviewing a contract draft, evaluating a business document, auditing a plan, or assessing any knowledge work output for quality, risk, and completeness.
---

# Review

Review documents, contracts, plans, or decisions against brain principles and domain best practices.

## Process

1. **Load principles**
   - Read `brain/principles.md` and all linked principle files
   - These are the review criteria

2. **Determine scope**
   - What's being reviewed? (contract, plan, memo, decision, process)
   - Auto-detect review size:
     - **Light** (single document, <10 pages): inline review
     - **Full** (multi-document, complex deal, >10 pages): structured review with sections

3. **Read the full document**
   - Per [[read-the-whole-thing]]: never review a section in isolation
   - Note defined terms, cross-references, exhibits, and schedules

4. **Assessment dimensions**

   For **contracts**:
   - **Completeness**: Are all essential terms present? Missing clauses?
   - **Risk exposure**: Indemnities, limitations of liability, reps & warranties — who bears what risk?
   - **Ambiguity**: Per [[ambiguity-is-risk]] — flag vague terms, undefined references, subjective standards
   - **Consistency**: Do terms align across sections? Do defined terms match their usage?
   - **Obligations**: Per [[minimize-future-obligations]] — what are we committing to, and for how long?
   - **Standard deviation**: Per [[default-to-standard]] — what departs from market norms, and why?

   For **plans and decisions**:
   - **Scope clarity**: Is scope well-defined, with explicit exclusions?
   - **Dependency mapping**: Per [[sequence-dependencies]] — are dependencies identified and ordered?
   - **Verification**: How will we know each phase succeeded?
   - **Risk identification**: What could go wrong, and what's the mitigation?
   - **Optionality**: Per [[minimize-future-obligations]] — does this preserve or foreclose options?

   For **all documents**:
   - **Source verification**: Per [[verify-against-source]] — are facts, dates, names, amounts correct?
   - **Principle compliance**: Check against all applicable brain principles

5. **Issue format**
   ```
   ### [N]. [Issue title]
   **Severity**: High / Medium / Low
   **Location**: Section/clause reference
   **Issue**: What's wrong or risky
   **Options**:
     a) [Option] — effort: [low/med/high], risk: [description]
     b) [Option] — effort: [low/med/high], risk: [description]
   **Recommended**: [letter] — [rationale tied to a principle]
   ```

6. **Verdict**
   - **Accept**: No high-severity issues, document is sound
   - **Accept with notes**: Minor issues that should be addressed but don't block
   - **Revise**: High-severity issues that must be resolved before proceeding

## Constraints

- The reviewer does NOT make changes — findings and options are the deliverable
- Always cite the specific principle that supports each finding
- Flag things you're uncertain about rather than guessing
