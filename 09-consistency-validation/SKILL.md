---
name: paper-consistency-validation
description: Conduct a submission-level scientific, narrative, citation, statistical, LaTeX, visual, and terminology consistency audit independent of any conference template.
---

# Full-Paper Scientific and Narrative Validation

Read [PRINCIPLES.md](../PRINCIPLES.md). This is an **independent audit**, not a cosmetic language polish. Do not accept "already fixed" without checking the actual latest artifact.

## 1. Evidence and artifacts

Read the latest available manuscript and, where supplied, LaTeX source, bibliography, compiled PDF, figures, tables, supplementary materials, statistical protocol, and underlying results.

For visual/layout claims, inspect the **rendered PDF**; use source files to locate causes and bibliography metadata to check references. If no compiled PDF or actual experiment data is available, mark that class of verification as **not performed** rather than PASS.

Venue formatting, anonymity, artifact packaging, and length checks apply only if the user supplies or identifies the actual current submission requirements; impose **no AAMAS, year, page count, or global template rule** by default.

## 2. Global narrative audit

Trace each title, abstract, and Introduction claim to an actual theorem, experiment, dataset validation, or appropriate source. Test whether the proposed method directly addresses the stated gap and whether the conclusion correctly reflects the result.

Review in reading order to find unexplained first-use terms and missing transitions. Maintain the same canonical vocabulary across abstract, body, figures, captions, formulas, appendix, and README-like supplements.

## 3. P0: scientific and factual blockers

Check:
- Incorrect mathematical assumptions, variable definitions, units, denominator, or sampling unit.
- Claim broader than what a comparison, proof, or experimental condition establishes.
- Relative percent mistaken for absolute percentage points.
- Correlation reported as causation or non-significance reported as equivalence.
- Baselines compared with unequal information, extra pretraining, unequal search space, or incomparable tuning budgets without disclosure.
- Fabricated references, wrong citations, unsupported numbers, or evidence selected only after seeing test performance.
- Data contamination, test leakage, invalid filtering, pseudo-replication, misleading uncertainty, or multiplicity issues where relevant.
- Headline figures differing between Abstract, Introduction, Results, plots, and Conclusion.

A finding from one paper should not become a universal instruction. For example, performance recovered by a separate method is not recovery of an original model, and failure to reproduce a result does not prove the original mechanism necessary.

## 4. Citations and bibliographic integrity

Verify each used reference against an authoritative record when possible: title, authors, year, venue, DOI/URL, and claimed contribution. Do not guess unknown metadata or invent BibTeX keys.

Attach citations near the entity or smallest substantive claim supported. A cited paper must truly support the statement. First meaningful mentions of external methods, models, datasets, tools, and evaluation protocols require appropriate attribution; repeated claims may require repeated citations.

Detect duplicate keys, duplicated records, undefined citations, and stale unused entries. Separate a novel argument made by this paper from work it cites as motivation.

## 5. LaTeX and cross-reference integrity

Where LaTeX source is available, inspect:
- Undefined references/citations, duplicate labels, misleading or stale section pointers.
- Figure/table first-reference order and correct target identifiers.
- Equation numbers only where useful, consistent references and symbol definitions.
- Orphan labels, malformed math, missing units, and reused variables with different meanings.
- Figure legends, captions, table notes, and statistics decoded for independent reading.
- Actual compiled float order, text overflow, visual holes, typography, and legibility.

Do not impose a blanket ban on citations or cross-references inside table notes; respect the document class, venue rules, and author style where appropriate.

## 6. Quantitative claim pressure test

For every important number ask: Which groups/objects were compared? Which denominator? What is the unit of independence? Is the effect absolute or relative? Which runs/seeds and uncertainty method? What was pre-specified? What data access and resource budget differed? Can the comparison survive a stronger fair baseline?

Check paired versus unpaired inference, one- versus two-sided intervals, coverage/censoring effects, and threshold origins when applicable. Do not conflate a statistical bound with an observed value.

## 7. Figure/table audit

Cross-check visual labels, model names, metric definitions, evaluation scope, units, sampling units, and main results with manuscript language. Inspect colors in grayscale and verify that images do not imply an unsupported count or causal relation. Check the actual figure source and rendered manuscript independently when possible.

## 8. Submission hygiene when relevant

If a double-blind review is required, audit author metadata, acknowledgments, source comments, paths, repository identities, figure metadata, supplements, and stale submission identifiers in **all** distributed files, not just the PDF. If anonymity is not required, do not treat visible authorship as an error.

If a venue requires formatting, verify its *current* rules independently; never assume a specific page limit or year.

## 9. Mechanical search starters

Search for unresolved references, `TODO`, `FIXME`, deprecated method names, abandoned venue identifiers, unqualified `best`/`first`/`significant` claims, inconsistent percentage formatting, unexplained acronyms, and vague directional language like `above` or `next section`. Findings require semantic inspection, not automatic deletion.

## Reporting format

Use four categories:

- **P0 — Must fix:** scientific error, unsupported core claim, broken evidence or citation, invalid inference, major missing definition.
- **P1 — Strongly recommended:** terminology conflicts, unfair comparisons, missing information, misleading figure/table, broken narrative progression.
- **P2 — Optional polish:** local expression, layout, navigation, or noncritical metadata.
- **PASS — Actually verified:** checks completed with named artifacts and evidence.

For each finding, report **location → current issue → why it matters → precise fix → whether the fix changes the scientific claim**. Preserve user-provided results and citations unless verification warrants an explicit correction.

## Required outputs

Return claim–evidence–scope audit, terminology/first-use audit, per-file or per-section P0/P1/P2/PASS issues, optional proposed patch, and an explicit **not checked / cannot verify** list.

**Acceptance:** A reviewer can follow the complete scientific argument and check its evidence without being misled by inconsistent terminology, numbers, references, or presentation.
