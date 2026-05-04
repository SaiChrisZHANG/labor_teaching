#!/usr/bin/env python3
"""Transfer the Week 4 workflow to center-quality heterogeneity."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mpl-cache"))

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic transfer CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for transfer files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {"center_quality", "treatment", "classroom_input", "endline_skill", "language_score"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    grouped = (
        df.groupby(["center_quality", "treatment"], as_index=False)
        .agg(
            mean_classroom_input=("classroom_input", "mean"),
            mean_endline_skill=("endline_skill", "mean"),
            mean_language_score=("language_score", "mean"),
            children=("child_id", "size"),
        )
        .sort_values(["center_quality", "treatment"])
    )
    grouped.to_csv(outdir / "transfer_quality_summary.csv", index=False)

    pivot = grouped.pivot(index="center_quality", columns="treatment", values="mean_endline_skill").reset_index()
    pivot.columns = ["center_quality", "control_endline_skill", "treatment_endline_skill"]
    pivot["treatment_gap"] = pivot["treatment_endline_skill"] - pivot["control_endline_skill"]
    pivot.to_csv(outdir / "transfer_quality_gaps.csv", index=False)

    plt.figure(figsize=(9.2, 5.2))
    for quality_name, quality_df in grouped.groupby("center_quality"):
        ordered = quality_df.sort_values("treatment")
        plt.plot(
            ordered["treatment"],
            ordered["mean_endline_skill"],
            marker="o",
            linewidth=2.4,
            label=quality_name.replace("_", " "),
        )
    plt.xticks([0, 1], ["Control", "Treatment"])
    plt.ylabel("Mean endline skill")
    plt.title("Treatment gains by center-quality environment")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "transfer_quality_response.png", dpi=200)
    plt.close()

    print(f"Saved transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
