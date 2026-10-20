---
name: 09-consistency-validation
description: Use for independent full-paper or pre-submission audits of claims, references, formulas, statistics, cross-references, figures and document integrity. Review only unless edits are explicitly requested.
---

# Full-Paper Scientific and Narrative Validation

## Execute this skill

**Typical request:** “投稿前检查引用、公式、表格和实验结论的一致性。”

**Procedure**

1. Read the latest manuscript and accessible evidence; record what artifacts are missing before checking.
2. Audit claims, entity citations, metrics, figure/table references, values and terminology with exact file/section locations.
3. Prioritize scientific blockers over prose; separate source-only, compiled-PDF and raw-result checks.

**Deliver:** Return location → risk → evidence → precise fix, ranked P0/P1/P2, plus PASS/NOT CHECKED by verification class.

**Evidence boundary:** Inspect the actual rendered artifact before reporting layout PASS. Report source-to-PDF consistency and reproducible compilation separately; claim a successful build only if it was executed. Distinguish inspecting recorded results, recomputing statistics from raw outputs, and reproducing results by rerunning experiments; report only the level actually completed.

Read [PRINCIPLES.md](../PRINCIPLES.md). This is an **independent audit**, not a cosmetic language polish. Do not accept "already fixed" without checking the actual latest artifact.

## Section-specific editorial judgement

**Editorial choice:** Audit both overstatement **and** needless defensive weakening. Check whether the paper makes its strongest supported contribution recognizable, whether major contradictory evidence is disclosed, and whether limitation phrasing is proportional rather than generic. Treat a Nature-style journal claim or blanket punctuation rule as unverified until the actual venue guidance is checked. Do not confuse persuasive clarity with selective reporting.

Consult the [Editorial Playbook](../EDITORIAL_PLAYBOOK.md) **only** when narrative focus, paragraph flow, Nature-style framing or defensive wording is relevant; keep scientific and source-preservation rules in [PRINCIPLES.md](../PRINCIPLES.md) higher priority.

### Decision and failure test

- This Skill is **review-only by default**. Do not rewrite manuscript source or change files unless the user explicitly authorizes edits.
- Classify each finding as **confirmed in supplied artifacts**, **plausible risk requiring verification**, or **not checked**. Never upgrade a keyword-search hit to a scientific error without inspecting context.
- An absent PDF, bibliography database or experiment log limits the audit: explicitly distinguish source/text checks from rendered-layout and empirical-reproducibility checks.

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
- Fabricated references, wrong citations, unsupported numbers, or post-hoc selection presented as prespecified or independently confirmed evidence. Transparent exploratory analyses are allowed, but must retain material outcomes and account for selection when making inferential claims.
- Data contamination, test leakage, invalid filtering, pseudo-replication, misleading uncertainty, or multiplicity issues where relevant.
- Headline figures differing between Abstract, Introduction, Results, plots, and Conclusion.

A finding from one paper should not become a universal instruction. For example, performance recovered by a separate method is not recovery of an original model, and failure to reproduce a result does not prove the original mechanism necessary.

### Check fair placement of unfavorable evidence

Compare the main Results/Discussion with all available appendices and submitted supplements. **PASS** only if the strongest supported finding is clear **and** a main-text-only reader is not misled. Secondary unfavorable figures, additional metrics, exploratory analyses and per-seed tables may be in supplements; flag them only when their omission changes interpretation, violates preregistered reporting or venue requirements, or the cited files are absent. A primary endpoint failure, decisive unfairly omitted baseline, claim-critical ablation or major safety/cost drawback must be acknowledged in the main paper, even if the detailed table is supplemental. Record a cross-reference and location audit separately from statistical validity and source-integrity checks. Do not treat "all negative results in main text" as a universal requirement.

## 4. Citations and bibliographic integrity

Verify each used reference against an authoritative record when possible: title, authors, year, venue, DOI/URL, and claimed contribution. Do not guess unknown metadata or invent BibTeX keys.

Attach citations near the entity or smallest substantive claim supported. A cited paper must truly support the statement. First meaningful mentions of external methods, models, datasets, tools, and evaluation protocols require appropriate attribution; repeated claims may require repeated citations.

Detect duplicate keys, duplicated records, undefined citations, and stale unused entries. Separate a novel argument made by this paper from work it cites as motivation.

Run the [CITATION_GUIDE.md](../CITATION_GUIDE.md) **entity–source audit**, not just a reference-count scan. Inventory every named external method, **model/checkpoint, benchmark, dataset**, evaluation protocol, and adapted resource across prose, tables, captions and supplements. Cross-check original/official sources, versions, bibliography keys, and which claims the sources establish. Attribute benchmark and underlying dataset separately when they have different sources. Check that first meaningful mentions carry accurate adjacent attribution, but do **not** require citations at sentence ends.

Check the **actual reference list**, not only syntax: the bibliography resource/path and output command must fit the document format; inspect undefined and duplicate BibTeX entries, missing keys and author–year mismatches where source is available. Inspect the supplied or newly rendered PDF's References section; if compilation is performed, also inspect undefined-citation warnings. Report **entity coverage**, **claim support**, **key/bibliography integrity**, **rendered reference-list inspection**, and **compilation/source-to-PDF verification** as separate PASS / issue / NOT CHECKED outcomes. Inspecting a supplied PDF can verify its visible reference list without a local build; it does not verify that current source reproduces that PDF.

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

## Lossless revision verification

For a source-level rewrite with no-deletion requirements, compare **the latest input LaTeX** against the output: the full contents of each float (not only counts), citations, labels, figure paths, captions, displayed equations, values, units, and material qualifiers. Record any authorized moved or modified environment explicitly. Check that every preserved exhibit still has a correctly scoped textual reference.

Report two independent statuses: **internal manuscript consistency** (same dataset/metric/configuration/aggregation/provenance means matching reported numbers) versus **empirical reproducibility** (raw records, run IDs, predictions, statistical code substantiate those results). A clean manuscript is not verified experimental provenance. Without source artifacts, use **NOT CHECKED**.

Audit narrative fidelity too: the key formulas must have motivating questions; related experiments must answer distinct questions; section bridges must not imply stronger causal, equivalence, or mechanism-necessity conclusions than the evidence supports. See [13 Cross-Section Revision](../13-section-revision/SKILL.md).


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

## Select discipline-appropriate verification

**Mathematics:** hypotheses, quantifiers, proof steps, references and counterexamples. **Physical and life sciences:** measurement units, calibration, experimental units, uncertainties and ethics where relevant. **Engineering:** operating conditions, hardware/workloads, failure boundaries and cost. **Numerical:** model assumptions, convergence, reproducibility and validation. **Computational experiments:** data leakage, seeds, model access, multiplicity and statistical units.

Also audit the complete story in actual reading order: opening → literature gap → method rationale → sequential experimental evidence → Results versus Discussion versus Conclusion. Do not mark a statistical or visual check PASS without the original data or rendered artifact.

## Acceptance check

**Acceptance:** A reviewer can follow the complete scientific argument and check its evidence without being misled by inconsistent terminology, numbers, references, or presentation.
