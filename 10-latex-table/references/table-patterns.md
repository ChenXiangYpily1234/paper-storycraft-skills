# Table Patterns and Validation

## Table construction order
1. State the exact scientific comparison and the independent unit.
2. Choose the minimum rows and columns needed to make that comparison.
3. Define metrics and abbreviated model roles before first substantive use.
4. Separate panels when data populations, uncertainty estimates, or protocols differ.
5. Optimize readability before compactness; never omit counterexamples to save space.
6. Compare all values and labels with verified source data after editing.

## When panels are useful
Panels are appropriate when groups differ in sample population, study condition, treatment, or statistical procedure. Each panel must identify its own population and denominator. Do not put two distinct intervals under one ambiguous "Bound" heading without explaining what each means.

Typical layouts depend on purpose:
- Method overview: `Approach | Key assumption | Input access | Output`.
- Core comparison: `Method | Metric A | Metric B | Cost`.
- Subgroup analysis: `Group | N | Estimate | Uncertainty`.
- System trade-off: `Configuration | Throughput | Latency | Memory`.
- Theorem summary: `Setting | Assumptions | Guarantee | Limitation`.

Replace placeholders with paper-specific, actually verified values. These are formats, not required measurements.

## Statistical and naming checks
- State relative versus absolute changes and preserve precision.
- Match row to run, dataset, metric, and aggregate; correct values in incorrect positions still mislead.
- Define statistical unit and pairing; report which values are means, intervals, or hypothesis-test bounds.
- For different subgroups, never conceal changed sample sizes or filtering.
- An interval including zero does not establish equivalence.
- Keep captions concise but independently interpretable.
- Preserve the manuscript's canonical method and metric names.

## LaTeX compilation workflow
Determine the project's own build system and document class. An example command is `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` **only when compatible with the user's project**.

Inspect the resulting PDF for overflow, alignment, float placement, unresolved references, and readable statistics at actual display size. If source files or a compiler are missing, report validation as incomplete.

Use [../assets/compact_tables.tex](../assets/compact_tables.tex) only as a **symbolic layout example**; its values are not scientific results.
