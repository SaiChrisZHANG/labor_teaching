#!/usr/bin/env python3
"""Transfer the Week 5 workflow to trend-sensitive compulsory-schooling designs."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic transfer CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for transfer files.")
    return parser.parse_args()


def iv_from_arrays(y: np.ndarray, s: np.ndarray, z: np.ndarray) -> tuple[float, float]:
    first_stage = float(np.cov(s, z, bias=True)[0, 1] / np.var(z))
    iv_beta = float(np.cov(y, z, bias=True)[0, 1] / np.cov(s, z, bias=True)[0, 1])
    return iv_beta, first_stage


def residualize_by_group_trend(df: pd.DataFrame, value_col: str) -> np.ndarray:
    residuals = np.zeros(len(df))
    for trend_group, group_df in df.groupby("trend_group"):
        idx = group_df.index.to_numpy()
        design = np.column_stack([np.ones(len(group_df)), group_df["birth_cohort"].to_numpy()])
        coef, *_ = np.linalg.lstsq(design, group_df[value_col].to_numpy(), rcond=None)
        residuals[idx] = group_df[value_col].to_numpy() - design @ coef
    return residuals


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {"birth_cohort", "trend_group", "reform", "schooling_years", "log_wage"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    naive_iv, naive_first_stage = iv_from_arrays(
        df["log_wage"].to_numpy(),
        df["schooling_years"].to_numpy(),
        df["reform"].to_numpy(),
    )

    y_resid = residualize_by_group_trend(df, "log_wage")
    s_resid = residualize_by_group_trend(df, "schooling_years")
    z_resid = residualize_by_group_trend(df, "reform")
    adjusted_iv, adjusted_first_stage = iv_from_arrays(y_resid, s_resid, z_resid)

    summary = pd.DataFrame(
        {
            "specification": ["naive_pooled_iv", "group_trend_adjusted_iv"],
            "iv_return": [naive_iv, adjusted_iv],
            "first_stage_years": [naive_first_stage, adjusted_first_stage],
        }
    )
    summary.to_csv(outdir / "transfer_specification_summary.csv", index=False)

    cohort_profiles = (
        df.groupby(["trend_group", "birth_cohort"], as_index=False)
        .agg(mean_schooling=("schooling_years", "mean"), mean_log_wage=("log_wage", "mean"), reform=("reform", "mean"))
        .sort_values(["trend_group", "birth_cohort"])
    )
    cohort_profiles.to_csv(outdir / "transfer_cohort_profiles.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.8))

    for trend_group, group_df in cohort_profiles.groupby("trend_group"):
        axes[0].plot(
            group_df["birth_cohort"],
            group_df["mean_log_wage"],
            marker="o",
            linewidth=2.1,
            label=trend_group.replace("_", " "),
        )
    axes[0].set_title("Cohort wage profiles by trend environment")
    axes[0].set_xlabel("Birth cohort")
    axes[0].set_ylabel("Mean log wage")
    axes[0].legend(frameon=False, fontsize=8)

    axes[1].bar(
        ["Naive IV", "Trend-adjusted IV"],
        [naive_iv, adjusted_iv],
        color=["#c25b2a", "#1f5c99"],
        width=0.58,
    )
    axes[1].set_title("Estimated return is specification-sensitive")
    axes[1].set_ylabel("IV return to schooling")
    axes[1].set_ylim(0, max(naive_iv, adjusted_iv) + 0.03)

    plt.tight_layout()
    plt.savefig(outdir / "transfer_trend_sensitivity.png", dpi=200)
    plt.close(fig)

    note_lines = [
        "A familiar instrument is not enough if cohort trends differ across reform environments.",
        "The pooled IV estimate mixes reform variation with secular trend differences.",
        "Trend-adjusted designs move the object closer to a credible policy margin but may still target a local return.",
    ]
    (outdir / "transfer_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
