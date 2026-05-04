#!/usr/bin/env python3
"""Bounded Week 5 reproduction in the spirit of Oreopoulos (2006)."""
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
    parser.add_argument("--input", required=True, help="Path to the synthetic schooling CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for reproduction files.")
    return parser.parse_args()


def ols_with_controls(df: pd.DataFrame) -> float:
    x = np.column_stack(
        [
            np.ones(len(df)),
            df["schooling_years"].to_numpy(),
            df["experience"].to_numpy(),
            np.square(df["experience"].to_numpy()),
            df["urban"].to_numpy(),
            df["reform_region"].to_numpy(),
        ]
    )
    y = df["log_wage"].to_numpy()
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return float(beta[1])


def residualize(series: pd.Series, controls: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(controls, series.to_numpy(), rcond=None)
    return series.to_numpy() - controls @ coef


def iv_with_controls(df: pd.DataFrame) -> tuple[float, float]:
    controls = np.column_stack(
        [
            np.ones(len(df)),
            df["experience"].to_numpy(),
            np.square(df["experience"].to_numpy()),
            df["urban"].to_numpy(),
            df["reform_region"].to_numpy(),
        ]
    )
    y_tilde = residualize(df["log_wage"], controls)
    s_tilde = residualize(df["schooling_years"], controls)
    z_tilde = residualize(df["compulsory_schooling"], controls)
    first_stage = float(np.cov(s_tilde, z_tilde, bias=True)[0, 1] / np.var(z_tilde))
    iv_beta = float(np.cov(y_tilde, z_tilde, bias=True)[0, 1] / np.cov(s_tilde, z_tilde, bias=True)[0, 1])
    return iv_beta, first_stage


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {
        "compulsory_schooling",
        "schooling_years",
        "log_wage",
        "experience",
        "urban",
        "reform_region",
        "birth_cohort",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    summary = (
        df.groupby("compulsory_schooling", as_index=False)
        .agg(
            mean_schooling=("schooling_years", "mean"),
            mean_log_wage=("log_wage", "mean"),
            mean_experience=("experience", "mean"),
            people=("person_id", "size"),
        )
        .sort_values("compulsory_schooling")
    )
    summary["group_label"] = summary["compulsory_schooling"].map({0: "No reform exposure", 1: "Reform exposure"})
    summary.to_csv(outdir / "reproduction_summary.csv", index=False)

    ols_beta = ols_with_controls(df)
    iv_beta, first_stage = iv_with_controls(df)
    estimates = pd.DataFrame(
        {
            "estimate": ["ols_mincer_return", "iv_late_return", "first_stage_years"],
            "value": [ols_beta, iv_beta, first_stage],
        }
    )
    estimates.to_csv(outdir / "return_estimates.csv", index=False)

    subgroup = (
        df.assign(cohort_group=np.where(df["birth_cohort"] < 1946, "older_cohorts", "younger_cohorts"))
        .groupby(["cohort_group", "urban"], as_index=False)
        .agg(mean_schooling=("schooling_years", "mean"), mean_log_wage=("log_wage", "mean"))
    )
    subgroup["urban_label"] = subgroup["urban"].map({0: "Non-urban", 1: "Urban"})
    subgroup.to_csv(outdir / "subgroup_summary.csv", index=False)

    plt.figure(figsize=(8.8, 5.4))
    labels = ["OLS premium", "IV / LATE"]
    values = [ols_beta, iv_beta]
    colors = ["#c25b2a", "#1f5c99"]
    plt.bar(labels, values, color=colors, width=0.55)
    plt.axhline(0.0, color="#555555", linewidth=1)
    plt.text(0.04, max(values) + 0.006, f"First stage = {first_stage:.2f} years", fontsize=10, color="#374151")
    plt.ylabel("Estimated return to one year of schooling")
    plt.title("Bounded Week 5 comparison of OLS and IV returns")
    plt.ylim(0, max(values) + 0.02)
    plt.tight_layout()
    plt.savefig(outdir / "reproduction_returns_comparison.png", dpi=200)
    plt.close()

    note_lines = [
        "The OLS coefficient is a descriptive Mincer return conditional on the included controls.",
        "The IV coefficient is a local return for the schooling margin shifted by compulsory-schooling exposure.",
        "The gap between the two reminds us that changing the design changes the estimand, not only the precision.",
    ]
    (outdir / "reproduction_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
