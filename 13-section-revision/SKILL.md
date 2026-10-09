---
name: section-argument-revision
description: Revise adjacent STEM manuscript sections into a question-driven scientific argument while preserving supplied LaTeX formulas, figures, tables, citations, values, and claims.
---

# Cross-Section Revision: From Formula and Experiment Stacks to an Argument

Read [PRINCIPLES.md](../PRINCIPLES.md) first. Then use [04 Method](../04-method/SKILL.md), [05 Experiment](../05-experiment/SKILL.md), and [09 Consistency Validation](../09-consistency-validation/SKILL.md) as needed. This skill coordinates existing skills; it does not replace their domain-specific checks.

**Trigger:** a user requests changes to multiple connected paper sections, asks whether the writing is a "stack of formulas / experiments", or requires a full LaTeX rewrite **without deleting tables or figures**.

## 1. State the scientific argument, not the contents list

Read the *latest* supplied manuscript rather than an older draft. For each section, build:

| Section job | Question | Must establish | Next unresolved question | Scope |
| --- | --- | --- | --- | --- |
| Framework/formal question | What exactly is being tested or optimized? | Objects, estimand, criterion, assumptions | What construction makes the criterion testable? | Identification/statistical limits |
| Method/construction | Why can this design address the question? | Information access, operations, core math, interfaces | Which measurable prediction follows? | Resource/design limits |
| Direct evidence | Does that prediction hold under a valid comparison? | Target, baseline, protocol, statistics | Why does it hold? | Evaluated conditions |
| Diagnosis and boundary | What alternative explanations and failure cases remain? | Controls, ablations, perturbations, shifts | What qualified conclusion survives? | Generalization limits |

Change the questions and section count to match the actual study. The goal is a **dependency between sections**, not forced symmetry or a predetermined success story.

## 2. Freeze the author-prescribed artifacts

Before rewriting, inventory every relevant `table`, `table*`, `figure`, `figure*`, `algorithm`, `longtable` and custom float; contents, captions, notes, placement, labels, figure paths and references. Inventory displayed mathematics, citations, numerical literals, exact experiment configurations, statistical conclusions and source macros.

**Default no-deletion contract:** keep full LaTeX tables and images, all supplied values, mathematical definitions, source citations and `\\label` identifiers. Reordering intact exhibits is permissible only if their text references, meaning and float reading order remain valid. The user may permit a different level of change, but do not silently "fix" an unverified datum or manufacture an experiment.

**Experiment provenance matters:** the same method name, metric and rounded mean do not demonstrate that two reports use identical runs. Record run IDs/seeds, pairing and candidate pools where known. Distinguish an unresolved mismatch from a verified contradiction.

## 3. Give formulas a narrative purpose

For **each central formula**, provide:
1. A sentence **before** it that names the scientific or computational requirement.
2. The expression and local definitions of its objects, units, assumptions and indices.
3. A sentence **after** it explaining what it enables, what it does not prove, and what operation or test uses it.

Classify equations as: question-defining, mechanism-defining, inference/decision-defining, or implementation/derivation. Keep the first three prominent. Move extended derivations only if permission and venue constraints allow; when all math must remain, fix density by **better ordering and shorter surrounding prose**, not deletion or semantic alteration.

A statistical audit condition is not the same as a model-scoring formula. A system's intended property is not evidence that the property holds.

## 4. Give every experiment one evidentiary role

Create an exhibit ledger:

| Existing exhibit | Scientific question | Protocol / unit | Evidence role | Alternative explanation | Text location |
| --- | --- | --- | --- | --- | --- |
| [real label] | [specific question] | [real comparison] | primary / direct test / explanatory / robustness / boundary | [confound] | [section] |

Common distinctions:
- **Benchmark capability** shows comparative task performance; it is not necessarily the paper's exact statistical hypothesis.
- **Direct audit/test** requires an explicit comparator, margin/decision rule, unit, pairing and uncertainty as relevant.
- **Ablation or targeted intervention** may explain an alternative model's sensitivity; it does not automatically identify an internal mechanism of the reference model.
- **Robustness** tests protocol variation; **boundary** reports where recovery, performance or validity weakens.

Order by **question and inferential strength**, not by chronological experiment log. Within each subsection write: **question → informative control → decisive observation → narrow interpretation → unresolved rival explanation → next question**. Explain a table's meaning rather than reading every cell aloud. Avoid presenting multiple reiterations of one result as independent evidence.

Agreement on sparse positive labels can be dominated by joint negative outcomes: candidate coverage, base rates and conditional performance may matter. A failure to establish equivalence or non-inferiority is not proof of the opposite mechanism's necessity.

## 5. Connect sections without inventing causality

Use transitions to explain an **information dependency**, not just to announce a new topic:

- **Framework → Method:** The criterion specifies what must be tested but not how to build a valid comparator; the construction supplies that missing object.
- **Method → Results:** The construction yields a testable prediction; data and controls determine whether the prediction holds.
- **Result → Diagnosis:** A headline result does not identify its explanation; the next experiment challenges competing explanations.
- **Diagnosis → Boundary:** An explanatory test does not establish generalization; the next result tests scope and failures.
- **Boundary → Conclusion:** State the strongest claim supported under the observed conditions, not a universal claim.

These are prompts for reasoning, **not mandatory sentence templates**. Preserve important negative findings and qualifications.

## 6. Revise without changing the study

First reorganize section responsibilities and paragraphs. Second motivate technical definitions. Third foreground decisive exhibit interpretations. Fourth shorten redundant cell-by-cell recitations and repeated claims. Finally align heading names with the scientific questions.

Maintain one canonical term per concept. Clearly distinguish independently built substitute systems from ablations inside the original; prediction, correlation and statistical recovery from causality or necessity; proposed additional tests from tests actually performed.

If data or text seem contradictory, **flag the discrepancy** with source locations rather than rewriting results to match. Retain the manuscript language, bibliographic keys, macros and existing scientific scope unless explicitly asked to change them.

## 7. Verify the before/after invariants

When the source is available, compare:
- multiset of figure/table/algorithm environments, `\\label`, caption content, figures paths and citation keys;
- math environments and equations that the author instructed to preserve;
- numerical cells, units, method/dataset names, threshold statements and inferential qualifiers;
- first mention/citation order, section pointers, duplicated and undefined labels.

**Counts alone are not enough**: equal numbers of tables do not establish equal content. Distinguish **source-text integrity**, **PDF rendering**, **statistical validity**, and **raw-result reproducibility** as four separate verification statuses. Only mark performed tests PASS. PDF layout cannot be confirmed without the rendered output and required compilation assets; numerical agreement in a .tex file cannot verify raw experiment logs.

## 8. Required outputs

For an actual revision, return (a) an argument map, (b) revised stand-alone section LaTeX, (c) a merged manuscript when full original source exists, (d) artifact preservation/change manifest, (e) qualified claim–evidence–boundary notes, and (f) P0/P1/P2/PASS/NOT CHECKED report.

**Acceptance:** a reviewer can explain the necessity of each core formula, the distinct role of each experiment, and the limits of the conclusion; no user-protected LaTeX artifact or scientific result was silently lost or changed.
