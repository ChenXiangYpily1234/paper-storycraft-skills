---
name: pptx-paper-figure-story
description: Design and revise editable PowerPoint research diagrams with reviewer-first visual semantics, consistent scientific terms, and evidence-bound claims.
---

# Editable Research Diagrams with PPTX

Read [PRINCIPLES.md](../PRINCIPLES.md) and [Figure Story](../07-figure/SKILL.md). PowerPoint is an editing format—not permission to invent components, data, arrows, or results.

## Appropriate use
Use editable PPTX for architecture summaries, algorithm flows, study protocols, comparison diagrams, ablation schematics, and conceptual maps. For measured numeric results, start with [Research Plotting](../11-research-plot/SKILL.md). For numerical tables, use [LaTeX Tables](../10-latex-table/SKILL.md).

## Narrative-first design process
1. **Define one reader question.** What should the diagram clarify that prose alone does not?
2. **Ground all objects.** Extract actual inputs, outputs, module roles, training/inference boundaries, shared parameters, and decision conditions from verified source material.
3. **Plan the logical reading path.** Typically context/input → central operation → output/evidence, unless real feedback, iteration, or parallelism requires another form.
4. **Use canonical terminology.** Every label must match the manuscript ledger. Explain a new acronym or named operation in the figure/caption or at its first adjacent mention.
5. **Declare visual semantics.** Arrows must have accurate data, control, logical, or causal meanings. Distinguish a shared module from duplicate modules and an external comparator from an in-model replacement.
6. **Keep shapes editable where feasible.** Maintain alignment, sensible grouping, readable type, and reproducible export dimensions; retain source artifacts.
7. **Audit the manuscript integration.** Compare PPTX, exported image, caption, first body reference, and Methods or Results definitions line by line.

## Scientific and visual acceptance gates
- A reviewer understands the figure's question from the title/caption without internal project knowledge.
- New module names are locally decipherable; no symbol silently changes meaning.
- No arrow suggests causality or access to information not supported by the actual system.
- The design does not erase negative conditions, unsupported branches, or data dependencies.
- Exported visuals remain readable at final paper size and in grayscale.
- Captions, text, and figure do not disagree on performance, sample unit, or scope.

## Tooling and redistribution
This public repository provides visual-story guidance, not proprietary PPTX editing software or third-party manuals. Use authorized tools for editing, rendering, and exporting PPTX files; do not imply that a source presentation has been edited unless it has.

## Required outputs
Provide scientific purpose, element-to-terminology mapping, layout plan, caption, editable file/export only if created, and explicit verification status for rendering and embedding.
