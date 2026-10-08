# Plotting Patterns, Semantics, and Visual Review

## Ordered categorical series template
The companion [plot_ordered_series.py](../scripts/plot_ordered_series.py) reads UTF-8 CSV with columns `series,category,value`. Each `(series, category)` pair must appear once, and the provided sequence defines the order. The script expects values already aggregated according to the experimental protocol; it does **not** compute means or uncertainty intervals.

Example usage (replace paths and units with actual data):

    python3 scripts/plot_ordered_series.py --input /path/to/verified.csv --output /path/to/figure/output --xlabel "Evaluation condition" --ylabel "Verified metric (unit)"

It writes PDF/PNG files. Adapt dimensions, category order, series count, error representation, and dependencies to the manuscript. Verify the selected Python environment has `pandas`, `matplotlib`, and `seaborn`.

## Choose visual form from measurement
| Question | Useful display | Must clarify |
| --- | --- | --- |
| Ordered conditions or time | line/point plot | order, intervals, aggregation |
| Independent task comparisons | grouped point/bar plot | dataset, metric, independent units |
| Stability across runs | raw run points and justified interval | seed policy and uncertainty estimator |
| Boundary/failure regime | threshold plot | origin of threshold, all failures |
| Distribution | box/violin/ECDF | sample unit and sampling frame |
| Two-dimensional sensitivity | heatmap/facets | color scale, omitted cells |
| Efficiency trade-off | scatter/Pareto display | hardware, runtime and cost units |

Avoid connecting unordered categorical values with lines. Never invent an error bar by treating non-independent runs as independent samples.

## Export and inspect
- Check overlapping markers and every near-zero/negative point.
- Ensure different series remain distinguishable in grayscale.
- Verify PDF text fonts, symbols, minus signs, legends, and axis units.
- Review actual PNG/PDF and the final manuscript placement.
- Compare any annotated numbers with the source table and claims.
- Report missingness and uncertainty if they materially change interpretation.

## Publication integration
A figure should be introduced by the main text and interpreted near its first occurrence. Keep caption terminology consistent with the central ledger. If a supplementary figure becomes necessary for a headline claim, move the corresponding essential evidence or explanation into the main narrative regardless of page-layout convenience.
