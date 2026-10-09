---
name: research-plotting
description: Produce or review reproducible scientific plots from verified data, protecting statistical meaning, traceability, accessible design, and manuscript terminology.
---

# Reproducible Research Plots

Read [PRINCIPLES.md](../PRINCIPLES.md) and [Figure Story](../07-figure/SKILL.md) first.

## 1. State the scientific question before choosing the chart
Choose a graph that reveals the needed comparison: paired points for paired experiments, distributions for heterogeneity, line plots for ordered or continuous progression, scatter for relationships, and heat maps only for justified two-dimensional comparisons.

Do not use a trend line for unordered categories or an area chart when the area has no scientific meaning. A graph is not evidence of causation without a design supporting causal inference.

## 2. Protect source values and estimands
Record source file, version, filtering steps, aggregation function, missing-value handling, statistical unit, denominator, and number of independent runs. The plotting process must never quietly calculate a new statistical criterion or substitute mean for median or worst-case statistics.

Do not manufacture confidence intervals, append synthetic observations, silently drop failed runs, smooth away important outliers, or use unjustified axis truncation.

For uncertainty plots, specify how intervals are computed, what is treated as independent, and whether the interval is descriptive, bootstrap, confidence, or predictive.

## 3. Graphical conventions
Prioritize readability at final manuscript dimensions: legible axes, units, legend, symbols, mathematical fonts, and tick marks. Use color plus marker/line-style differences so figures remain meaningful when printed in grayscale or viewed with color-vision deficiencies.

Avoid misleading dual axes, excessive decorative grids, unexplained offsets, and inconsistent scales across panels. Use compact panels or facets when too many series obscure one another.

## 4. Tools and dependencies
Use the user's installed plotting environment and project conventions where possible. Confirm dependency availability before running scripts; do not claim successful export without actual generated files.

An illustrative [ordered-series script](scripts/plot_ordered_series.py) accepts UTF-8 CSV columns `series,category,value` and exports PDF/PNG. It expects verified **already aggregated** values and does not create confidence intervals. Adapt its assumptions to the actual data; it is not a universal plotter.

See [Plotting patterns](references/plotting-patterns.md) for data checks, chart choice, and validation.

## 5. Integrate the plot into the paper
Use canonical names from the manuscript. Provide a caption stating population/conditions, metric, units, visual encodings, and uncertainty if relevant. Reference the figure in the narrative before drawing conclusions from it.

Inspect the exported image and its final manuscript placement; check non-overlapping markers, label clipping, small negative/zero points, and text readability. A successfully executed script is not sufficient visual validation.

## STEM plot routes

Choose spectra, time series, calibration curves, residuals, distributions, convergence graphs, phase relationships, workload trade-offs or paired comparisons **according to the verified data and scientific question**. State units, uncertainty, model/measurement distinction and meaningful scales. Never synthesize numeric evidence or include a graph only for visual decoration.

## Deliverables
Provide plotted files and code only when actually generated, verified data provenance, transformations performed, caption draft, consistency check against paper results, and any unresolved assumptions.
