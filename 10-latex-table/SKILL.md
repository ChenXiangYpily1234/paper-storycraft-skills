---
name: 10-latex-table
description: Use when creating, fixing or reviewing LaTeX research tables with scientific measurements, benchmark scores, significance markers or captions.
---

# Evidence-Centered LaTeX Tables

## Execute this skill

**Use for:** creating, fixing or reviewing LaTeX research tables with scientific measurements, benchmark scores, significance markers or captions.

**Typical request:** “把这张 LaTeX 表格排得紧凑但不能更改数值。”

**Procedure**

1. State the comparison, unit and metric direction before touching formatting.
2. Preserve every sourced value, uncertainty, citation and label; check groups, denominators and significance notation.
3. Improve alignment, whitespace and caption readability; compile/inspect only if LaTeX tooling is available.

**Deliver:** Return valid table source or a precise patch, with a values-preserved and compilation-status note.

**Evidence boundary:** Formatting does not authorize rounding or changing statistics unless the user requests and verifies it.

**Scope control:** If the user requests diagnosis only, do not rewrite the manuscript. If the request covers only one paragraph, table, figure or subsection, return the relevant artifact and blockers rather than a full-paper report. Follow [PRINCIPLES.md](../PRINCIPLES.md) and use [CITATION_GUIDE.md](../CITATION_GUIDE.md) where external sources are involved.

Read [PRINCIPLES.md](../PRINCIPLES.md) and [Figure Story](../07-figure/SKILL.md). Use this guide for manuscript tables, not for inventing experimental results.

## 1. Identify the question answered by the table
State what the reader must compare (methods, groups, interventions, resource trade-offs, or uncertainty). Choose rows, columns, and panels to expose that contrast. Every column should serve a scientific purpose.

Treat a table as evidence, not a compressed database export. Explanatory background belongs in the body; essential metric definitions, denominator/population, uncertainty convention, and abbreviations belong in the caption or notes.

## 2. Preserve data and statistical semantics
Before and after reformatting, compare every `dataset / model / group / metric / seed / value / unit` mapping. A correct number in the wrong row is an error.

Distinguish mean from best-seed score, confidence interval from standard deviation, relative gain from percentage-point difference, and subgroup denominator from all-sample denominator. Never erase negative rows or selection rules to gain space.

For panels with different populations or protocols, state their separate scope and sample size. Shared headers are fine only when their meanings truly match across panels.

## 3. Typography and layout
- Begin with readable text sizes and conventional column alignment; prefer clear labels over many narrow wrapped columns.
- Use `booktabs` when already compatible with the host template; avoid excessive vertical rules.
- Shorten repeated prose before shrinking fonts. Adjust spacing locally rather than modifying manuscript-wide typography.
- Use `l/c/r` for short data; use fixed-width or flexible-width columns when explanatory text actually needs wrapping.
- If a table is still too wide, split scientifically distinct panels, rotate only when justified, or use an allowed wide-table environment.
- Do not impose a specific journal/conference table style or page limit.

## 4. Citation, reference, and caption discipline
Cite named external baselines where first explained and again when a nontrivial claim requires it. Place `\label` and `\ref` according to the host document's conventions. Do not assume a universal ban on citations or cross-references in captions/notes.

The caption should communicate **what is compared, on what data/setting, with what metric and essential statistical interpretation**. Decode specialized abbreviations locally because tables are often read independently.

## 5. Compile and inspect
Follow the project's real build command and document class. Do not assume `pdflatex`, `latexmk`, `biber`, or a particular page layout without checking. Inspect the *actual compiled PDF* for overflow, missing glyphs, float order, clipped columns, unresolved references, and the first-mention reading path.

No successful compilation or rendered inspection → label these checks **not verified**.

## STEM table cases

Use tables for measurement conditions, instrument accuracy, units and uncertainties; solver convergence; benchmark comparisons; component studies; engineering operating conditions; or theorem assumptions. Tables are optional for theory-only research. Explicitly label panels from independent experimental run groups so readers do not infer an invalid paired comparison. Preserve scientific notation, units and provenance.

## References and deliverables
- [Table patterns and audit checklist](references/table-patterns.md).
- [Illustrative table layout](assets/compact_tables.tex): placeholder symbols, **not data**.

Return an evidence mapping, table revision, explanation of layout changes, metric/denominator checks, and an explicit list of unverified compilation or PDF checks.
