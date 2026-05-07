#!/usr/bin/env python3
"""
Transfer exercise for Week 4 job ladders and E-to-E mobility.
"""
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
    work["ee_rate"] = work["ee_moves"] / work["employed"]
    work["upgrade_share"] = work["upward_moves"] / work["ee_moves"].where(work["ee_moves"] > 0, 1)

    summary = work[
        ["market_state", "origin_tier", "employed", "ee_moves", "upward_moves", "ee_rate", "upgrade_share"]
    ].copy()
    summary.to_csv(outdir / "job_ladder_transition_summary.csv", index=False)

    aggregate = (
        work.groupby("market_state", as_index=False)
        .agg({"employed": "sum", "ee_moves": "sum", "upward_moves": "sum"})
    )
    aggregate["ee_rate"] = aggregate["ee_moves"] / aggregate["employed"]
    aggregate["upgrade_share"] = aggregate["upward_moves"] / aggregate["ee_moves"]
    aggregate.to_csv(outdir / "job_ladder_market_summary.csv", index=False)

    order = ["low-wage", "middle-wage", "high-wage"]
    states = ["tight", "loose"]
    xpos = range(len(order))
    width = 0.35

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    for offset, state in zip([-width / 2, width / 2], states):
        subset = work[work["market_state"] == state].set_index("origin_tier").reindex(order)
        positions = [x + offset for x in xpos]
        axes[0].bar(positions, subset["ee_rate"], width=width, label=state.title())
        axes[1].bar(positions, subset["upgrade_share"], width=width, label=state.title())

    axes[0].set_title("E-to-E mobility by origin firm tier")
    axes[0].set_ylabel("E-to-E rate")
    axes[0].set_xticks(list(xpos))
    axes[0].set_xticklabels(order, rotation=15)
    axes[0].legend(fontsize=8)

    axes[1].set_title("Upward job-ladder share")
    axes[1].set_ylabel("Share of E-to-E moves that upgrade")
    axes[1].set_xticks(list(xpos))
    axes[1].set_xticklabels(order, rotation=15)
    axes[1].legend(fontsize=8)

    fig.suptitle("Synthetic job ladders in tight versus loose markets")
    fig.tight_layout()
    fig.savefig(outdir / "job_ladder_transfer.png", dpi=220)
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
    print(f"Saved Week 4 job-ladder transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
