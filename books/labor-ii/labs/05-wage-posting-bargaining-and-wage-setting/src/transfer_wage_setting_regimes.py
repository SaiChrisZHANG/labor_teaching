#!/usr/bin/env python3
"""Transfer exercise for Week 5 wage-setting regimes."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd


def build_outputs(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    work = df.copy()
    work["compression_ratio"] = work["within_cell_sd"] / work["mean_wage"]
    work["offer_response_rate"] = work["offer_responses"] / work["outside_offer_cases"]
    work["retention_rate"] = 1 - (work["separations"] / work["workers"])

    summary = (
        work.groupby("regime", as_index=False)
        .agg(
            mean_wage=("mean_wage", "mean"),
            mean_within_cell_sd=("within_cell_sd", "mean"),
            compression_ratio=("compression_ratio", "mean"),
            offer_response_rate=("offer_response_rate", "mean"),
            retention_rate=("retention_rate", "mean"),
        )
    )
    summary.to_csv(outdir / "wage_setting_regimes_summary.csv", index=False)

    order = ["standardized", "discretionary"]
    plot_df = summary.set_index("regime").reindex(order).reset_index()
    xpos = range(len(plot_df))

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    axes[0].bar(xpos, plot_df["compression_ratio"], color=["#3B6EA8", "#B55D4C"])
    axes[0].set_title("Within-cell wage compression")
    axes[0].set_ylabel("Within-cell SD / mean wage")
    axes[0].set_xticks(list(xpos))
    axes[0].set_xticklabels(order)

    axes[1].bar(xpos, plot_df["offer_response_rate"], color=["#3B6EA8", "#B55D4C"])
    axes[1].set_title("Response to outside offers")
    axes[1].set_ylabel("Share of offer cases with wage response")
    axes[1].set_xticks(list(xpos))
    axes[1].set_xticklabels(order)

    fig.suptitle("Synthetic Week 5 transfer: standardized versus discretionary wage-setting")
    fig.tight_layout()
    fig.savefig(outdir / "wage_setting_regimes_comparison.png", dpi=220)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    build_outputs(df, args.outdir)
    print(f"Saved Week 5 wage-setting transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
