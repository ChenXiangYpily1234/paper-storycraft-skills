---
name: latex-table-design
description: Create scientifically faithful, readable LaTeX tables that support a research claim and match the paper's metrics, labels, statistical units, and terminology.
---

# Evidence-Centered LaTeX Tables

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

## References and deliverables
- [Table patterns and audit checklist](references/table-patterns.md).
- [Illustrative table layout](assets/compact_tables.tex): placeholder symbols, **not data**.

Return an evidence mapping, table revision, explanation of layout changes, metric/denominator checks, and an explicit list of unverified compilation or PDF checks.
