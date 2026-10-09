---
name: figure-story
description: Design and review research figures that explain a scientific mechanism, comparison, or finding accurately using consistent terminology, visual semantics, and captions.
---

# Figures That Advance the Paper's Argument

Read [PRINCIPLES.md](../PRINCIPLES.md). Coordinate with [Research Plotting](../11-research-plot/SKILL.md) for quantitative plots and [Editable PPTX Visuals](../12-pptx-visual/SKILL.md) for conceptual diagrams.

## 1. Give every figure a scientific job

Before drawing, state one question that the figure must answer. Examples: What information enters the system? Which design step is novel? How are groups compared? Where does an observed improvement disappear?

Choose the visual form to match that question:
- **System or method overview:** depict actual inputs, transformations, outputs, and sharing.
- **Comparison diagram:** reveal conditions held constant and the variable that changes.
- **Evidence plot:** display observed trends, uncertainty, distributions, or boundaries.
- **Concept map:** distinguish definitions, logical dependencies, and conjectured relations.

A figure that only repeats the prose without making structure or evidence clearer may be unnecessary.

## 2. Use a precise visual grammar

Declare the meanings of arrows (data flow, control flow, logical dependence, or causal effect). Never use a causal arrow for mere correlation or draw a connection absent from the described method.

Keep shapes and line styles semantically stable. Distinguish a shared component from two copies, a trained module from a deterministic rule, and an independent comparison system from an ablation inside the target.

Color cannot be the sole carrier of meaning. Use labels, shapes, line styles, or markers that remain interpretable in grayscale and for color-vision differences.

## 3. Explain terms at first appearance

Every new module label, abbreviation, metric, parameter, and protocol condition must be explained either in the figure, its caption, or nearby first-reference text. Standalone figures require enough caption detail for a reader to understand their scientific object and central contrast.

Use **exactly the same canonical names** as the manuscript's terminology ledger. Do not invent shorter labels inside the figure if they change a concept's meaning. A legitimate abbreviation must map unambiguously to the same term.

## 4. Structure for first-pass reading

Use natural reading order where compatible with the real computation. Place shared context before branch-specific operations; align comparisons; group related objects; reserve visual emphasis for the central scientific step.

Remove decorative icons, repeated text, or excessive boxed modules while preserving scientifically necessary conditions. Do not simplify iterations, feedback, or parallel operations into an inaccurate left-to-right chain.

## 5. Quantitative and statistical integrity

Preserve actual data, observation units, denominators, uncertainty, axis scales, missing values, and experiment scope. Plotting choices must not invent significance or hide failure cases.

Avoid deceptive truncation, inconsistent normalizations, unsupported connecting lines, unlabeled dual axes, and symbol choices that confuse comparisons with participants or observations.

When statistical intervals are shown, name their meaning and computation; when absent, do not imply quantified uncertainty. Check all main numbers against Results, Abstract, and Conclusion.

## 6. Pair every figure with the paper

Prepare a mapping:

| Visual element | Scientific meaning | Exact manuscript term | Evidence or method source |
| --- | --- | --- | --- |
| [arrow/panel/label] | [role] | [canonical name] | [section/equation/dataset] |

The body should introduce a figure before asking the reader to interpret it. The caption should explain the question, objects, significant visual conventions, and essential conditions; interpretation belongs primarily in nearby prose.

Check exported and **embedded** renderings at actual publication size: labels, math, symbols, legend, panel order, and line distinctions must remain readable.

## 7. Review gates

1. **Scientific:** every node, connection, comparison, and result is accurate.
2. **Semantic:** labels, captions, and text refer to identical concepts and scopes.
3. **Visual:** main comparison is clear without zooming; annotations are legible and accessible.

## Decide whether a STEM framework figure is necessary

Use system architecture, apparatus, workflow, proof-dependency, solver or experiment-design diagrams only when they explain something prose does not. If the Introduction already contains a useful overview, prioritize improving its shared-input → distinct method branch → result flow before creating a second figure. Arrows must correctly distinguish data flow, control flow and causal evidence. The repository's Skills flowchart is available in [WORKFLOW.md](../WORKFLOW.md).

## Required outputs

Provide figure purpose, a content/layout plan, element-to-term map, caption draft, scientific/visual risk list, and created editable/rendered files only if actually produced. Clearly label any visual inspection or export step not performed.

**Acceptance:** A reviewer can answer what the figure is about, what each key arrow/curve means, and what the visual supports—without supplying missing definitions from imagination.
