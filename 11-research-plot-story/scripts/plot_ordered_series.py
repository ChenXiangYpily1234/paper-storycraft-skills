#!/usr/bin/env python3
"""Plot verified, pre-aggregated CSV data; never aggregate or invent intervals."""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path, help="Output stem, without suffix")
    parser.add_argument("--xlabel", required=True)
    parser.add_argument("--ylabel", required=True, help="Include the metric and its unit")
    args = parser.parse_args()
    data = pd.read_csv(args.input, dtype={"series": str, "category": str})
    required = ["series", "category", "value"]
    if not set(required).issubset(data.columns) or data.empty:
        parser.error("CSV must contain nonempty series,category,value columns")
    if data[required].isna().any().any() or data.duplicated(["series", "category"]).any():
        parser.error("Missing values and duplicate series/category pairs need explicit treatment")
    data["value"] = pd.to_numeric(data["value"], errors="raise")
    if not data["value"].map(lambda value: float("-inf") < value < float("inf")).all():
        parser.error("Values must be finite")
    series = data["series"].drop_duplicates().tolist()
    categories = data["category"].drop_duplicates().tolist()
    if len(series) > 3:
        parser.error("This compact template supports at most three series; adapt it or use facets")
    for name in series:
        if data.loc[data["series"] == name, "category"].tolist() != categories:
            parser.error("All series must contain the same categories in the same order")
    data["position"] = data["category"].map(dict(zip(categories, range(len(categories)))))
    sns.set_theme(style="whitegrid", context="paper", rc={
        "font.family": "serif", "font.size": 8, "axes.labelsize": 8,
        "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8,
        "axes.linewidth": 0.6, "grid.linewidth": 0.45, "grid.color": "0.88",
        "pdf.fonttype": 42, "ps.fonttype": 42,
    })
    fig, ax = plt.subplots(figsize=(3.35, 2.25), layout="constrained")
    sns.lineplot(data=data, x="position", y="value", hue="series", style="series",
                 hue_order=series, style_order=series,
                 palette=["#4C78A8", "#E69F00", "#C44E52"][:len(series)],
                 markers=["o", "s", "^"][:len(series)],
                 dashes=[(1, 1), (4, 2), ""][:len(series)],
                 estimator=None, errorbar=None, sort=False, linewidth=1.4,
                 markersize=5, markerfacecolor="white", markeredgewidth=1, ax=ax)
    for index, line in enumerate(ax.lines[:len(series)]):
        line.set_markeredgecolor(line.get_color())
        line.set_markersize(7 - index * 1.5)
    ax.set_xticks(range(len(categories)), categories)
    ax.set(xlabel=args.xlabel, ylabel=args.ylabel)
    ax.xaxis.grid(False)
    ax.legend(title=None, frameon=False)
    sns.despine(ax=ax)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for extension in ("pdf", "png"):
        fig.savefig(str(args.output) + "." + extension, dpi=300, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


if __name__ == "__main__":
    main()
