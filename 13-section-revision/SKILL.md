---
name: 13-section-revision
description: Use for coordinated revisions or argument audits across adjacent manuscript sections while preserving existing LaTeX, figures, tables, equations, labels, citations and empirical claims. Diagnose only unless rewriting is requested.
---

# Cross-Section Revision: From Formula and Experiment Stacks to an Argument

## Execute this skill

**Typical request:** “重写第 3–5 节，保留所有表格、公式和 label。”

**Mode gate:** A question such as “Are these sections a stack of formulas and experiments?” requests diagnosis unless the user also asks for rewriting. In audit mode, return the argument map, located problems and a revision proposal; do not rewrite sections or modify files. Apply the editing procedure below only to authorized revisions.

**Procedure**

1. Inventory immutable source artifacts and create a before-change manifest.
2. Rebuild section-to-section argument dependencies without silently rewriting protected data or citing invented work.
3. Produce the revised sections and mechanically compare protected items, then check claim/figure/paragraph linkages.

**Deliver:** For an authorized revision, return revised sections, an artifact change manifest and separate source/PDF/results verification statuses. For diagnosis only, return the audit findings and proposal without edited content.

**Evidence boundary:** If a genuine scientific contradiction appears, flag it for author decision rather than 'fixing' an experiment.

Read [PRINCIPLES.md](../PRINCIPLES.md) first. Then use [04 Method](../04-method/SKILL.md), [05 Experiment](../05-experiment/SKILL.md), and [09 Consistency Validation](../09-consistency-validation/SKILL.md) as needed. This skill coordinates existing skills; it does not replace their domain-specific checks.

**Trigger:** a user requests changes to multiple connected paper sections, asks whether the writing is a "stack of formulas / experiments", or requires a full LaTeX rewrite **without deleting tables or figures**.

## Section-specific editorial judgement

**Editorial choice:** Reverse-outline linked sections as question → design reason → operations → direct evidence → bounded interpretation. Foreground the strongest supported result and, with authorization, move extended secondary unfavorable findings to appendices or supplements. Keep claim-changing failed controls visible in the main argument. Stronger writing means a more precise claim, not suppression of contradictory evidence. Verify numerical and LaTeX invariants after every move.

Consult [EDITORIAL_PLAYBOOK.md](../EDITORIAL_PLAYBOOK.md) only for relevant editorial work; scientific and source-preservation rules in [PRINCIPLES.md](../PRINCIPLES.md) take priority.

### Decision and failure test

- Inventory before rewriting: equation environments, citations, labels, table/figure content, caption text, numerical values and scientific qualifications.
- Treat an exact count match as insufficient: changed values, swapped rows, missing caption sentences or different statistical scopes break the preservation contract.
- New verified citations may be added within the authorized edit scope with an explicit change log. If citations are explicitly frozen, propose corrections without editing them; do not hide unresolved references or claim successful LaTeX compilation when the build was not executed.

## 1. State the scientific argument, not the contents list

Read the *latest* supplied manuscript rather than an older draft. For each section, build:

| Section job | Question | Must establish | Next unresolved question | Scope |
| --- | --- | --- | --- | --- |
| Framework/formal question | What exactly is being tested or optimized? | Objects, estimand, criterion, assumptions | What construction makes the criterion testable? | Identification/statistical limits |
| Method/construction | Why can this design address the question? | Information access, operations, core math, interfaces | Which measurable prediction follows? | Resource/design limits |
| Direct evidence | Does that prediction hold under a valid comparison? | Target, baseline, protocol, statistics | Why does it hold? | Evaluated conditions |
| Diagnosis and boundary | What alternative explanations and failure cases remain? | Controls, ablations, perturbations, shifts | What qualified conclusion survives? | Generalization limits |

Change the questions and section count to match the actual study. The goal is a **dependency between sections**, not forced symmetry or a predetermined success story.

### Reallocate supplementary evidence without silently deleting it

When a user authorizes restructuring, create a **placement ledger** for every proposed move: claim, exhibit/number, original section, new appendix/supplement path, whether the result is prespecified or exploratory, its effect on the paper's headline conclusion, and updated textual reference. Move *secondary* unfavorable details to appendix/supplement when the main-text account remains complete; **retain a main-text qualification** for any outcome that changes the core claim. Preserve exact float content, metric names, labels, citation keys and data; ensure files are included in the output. If the user requested no movement or the supplemental artifact cannot be generated, present a relocation proposal instead. Never silently move or drop a claim-critical failed control.

## 2. Freeze the author-prescribed artifacts

Before rewriting, inventory every relevant `table`, `table*`, `figure`, `figure*`, `algorithm`, `longtable` and custom float; contents, captions, notes, placement, labels, figure paths and references. Inventory displayed mathematics, citations, numerical literals, exact experiment configurations, statistical conclusions and source macros.

**Default no-deletion contract:** keep full LaTeX tables and images, all supplied values, mathematical definitions, source citations and `\label` identifiers. Reordering intact exhibits is permissible only if their text references, meaning and float reading order remain valid. The user may permit a different level of change, but do not silently "fix" an unverified datum or manufacture an experiment.

**Experiment provenance matters:** the same method name, metric and rounded mean do not demonstrate that two reports use identical runs. Record run IDs/seeds, pairing and candidate pools where known. Distinguish an unresolved mismatch from a verified contradiction.

**Citation correction exception:** preserving existing citations does not excuse missing provenance for imported models, benchmarks, datasets or prior methods. Apply [CITATION_GUIDE.md](../CITATION_GUIDE.md): retain valid existing citations/keys, add **verified** missing attributions within the authorized edit scope adjacent to entity names or supported claims, and record additions/relocations in the preservation manifest. If citations or bibliography content are explicitly frozen, report the defect and proposed correction without changing the protected material. If the source cannot be verified, list a specific missing citation instead of inventing a reference or silently altering the bibliography.

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
- multiset of figure/table/algorithm environments, `\label`, caption content, figures paths and citation keys;
- math environments and equations that the author instructed to preserve;
- numerical cells, units, method/dataset names, threshold statements and inferential qualifiers;
- first mention/citation order, section pointers, duplicated and undefined labels.

**Counts alone are not enough**: equal numbers of tables do not establish equal content. Distinguish **source-text integrity**, **rendered-PDF inspection**, **compilation/source-to-PDF verification**, **statistical validity**, and **raw-result reproducibility** as separate verification statuses. Only mark performed tests PASS. A supplied PDF permits checks of its visible layout; verifying that the revised source reproduces that PDF requires an actual build from the relevant source and assets. Numerical agreement in a .tex file cannot verify raw experiment logs.

## Acceptance check

**Acceptance:** a reviewer can explain the necessity of each core formula, the distinct role of each experiment, and the limits of the conclusion; no user-protected LaTeX artifact or scientific result was silently lost or changed.
