---
name: abstract-story
description: Build or revise research abstracts around a verifiable question, a specific gap, a contribution, evidence, and scoped conclusions without imposing a venue template.
---

# Abstract Storytelling and Revision

**Global rule:** Read [PRINCIPLES.md](../PRINCIPLES.md) first. Apply its reviewer-first narrative, first-use definitions, terminology ledger, and claim–evidence–scope checks.

## Scope and inputs
Applies to methodological, theoretical, systems, empirical, dataset, benchmark, replication, negative-result, and mechanism studies. Obtain the paper's actual title, core claims, introduction, method, key results, and conclusion where available. If only the abstract is supplied, identify facts that cannot be verified instead of inventing supporting evidence.

## Build the story before writing sentences
Answer six questions: (1) What precise task, phenomenon, or object is being studied? (2) What genuine limitation of existing methods or evidence motivates the work? (3) What is the research question? (4) What was actually introduced, tested, or demonstrated? (5) Which result most directly answers the question? (6) Under which conditions can the conclusion hold?

Draft a one-sentence *story spine* without unexplained method acronyms. Check that the proposed contribution and evidence directly address the same problem.

## Choose a structure suited to the contribution
- **Algorithm/method:** concrete task → supported bottleneck → core idea → discriminating experiments → limits.
- **System:** operating requirement and constraints → design decisions → measured efficiency/reliability and trade-offs → environment limits.
- **Theory:** formal question and assumptions → theorem/algorithm or counterexample → what is established and what is not.
- **Dataset/benchmark:** evaluation gap → construction/validation → demonstrated utility → coverage and bias.
- **Mechanism/causal audit:** competing explanation → identifying comparison → observed evidence → identification boundary.
- **Replication/negative result:** target claim → reproduction conditions → findings and uncertainty → bounded interpretation.

No fixed sentence count, experiment count, conference, or word limit is assumed.

## Sentence-level narrative rules
1. **Open concretely.** Name the task or observable challenge before abstract framework vocabulary.
2. **Specify the gap.** Distinguish practical failure, conceptual uncertainty, absence of a controlled comparison, and missing external validity. Do not assert that "no prior work" exists without evidence.
3. **Explain the contribution before branding it.** Describe the action, key design difference, or test in clear language, then give the canonical method name.
4. **Select relevant evidence.** Include meaningful metric, comparison object, evaluation scope, and uncertainty when needed. Do not turn the abstract into a baseline catalog.
5. **Close the loop.** Say what the evidence establishes about the opening question; do not merely repeat "We propose X."
6. **Respect limits.** Separate relative change from percentage points, conditional from universal claims, and non-significance from equivalence.

Define any specialized term or abbreviation at first use in the abstract, even if it is explained later in the paper. Reuse the same names as the main text and figures.

## Common failures
- Broad promotional opening → replace with a concrete object and challenge.
- Multiple internal method names before the problem → explain the idea first.
- "SOTA", "best", or "significant" without justified comparison and test → qualify or remove.
- Claim that a method proves a mechanism unnecessary everywhere → restrict to evaluated conditions.
- Number reported differently from a table → correct against verified results.
- Long list of datasets and seeds → highlight only evidence that advances the central argument.

## Required outputs
Provide (1) narrative diagnosis, (2) ordered story outline, (3) full revised abstract in the manuscript's language, (4) claims/numbers/citations needing verification, and (5) concise revision notes. If the user requests only an audit, omit unsolicited rewriting.

**Acceptance:** A reader can explain the question, difference, evidence, and scope after one reading, without guessing what a newly introduced term means.
