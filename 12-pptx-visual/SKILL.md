---
name: 12-pptx-visual
description: Use when a researcher needs an editable PowerPoint diagram for a verified pipeline, conceptual mechanism, experiment setup or paper figure.
---

# Editable Research Diagrams with PPTX

## Execute this skill

**Typical request:** “把算法结构图做成可编辑的 PPTX。”

**Procedure**

1. Identify verified entities and relationships and decide whether an editable diagram answers a useful question.
2. Choose slide dimensions, shapes, labels and arrows that express the actual data/control/causal semantics.
3. Check readability in final size, editability, captions and consistency with manuscript terminology.

**Deliver:** Return editable PPTX only when creation tools are available; otherwise provide an implementable layout specification and NOT CREATED status.

**Evidence boundary:** Do not claim an editable file was built merely from a static rendering.

Read [PRINCIPLES.md](../PRINCIPLES.md) and [Figure Story](../07-figure/SKILL.md). PowerPoint is an editing format—not permission to invent components, data, arrows, or results.

### Decision and failure test

- A static rendered image is **not** an editable PowerPoint diagram. Verify the deliverable is a real PPTX containing manipulable elements, if that is what the user requested.
- Do not imply experimental causality via arrows or invent unprovided internal architecture details.
- State separately whether the file was created, opened, and visually inspected. Tool or file unavailability must be reported, not masked by a conceptual drawing.

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

## STEM editable visual forms

Beyond ML architectures, editable diagrams may show laboratory apparatus, sampling procedures, numerical methods, proof relationships, mechanical/electrical systems or engineering workflows. Draw only grounded objects and actual information/material/control paths. First decide whether an existing overview diagram should be improved instead of duplicated. Match all labels with the manuscript and verify export readability.
