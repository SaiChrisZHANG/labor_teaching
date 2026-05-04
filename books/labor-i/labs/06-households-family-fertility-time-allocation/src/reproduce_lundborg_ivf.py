#!/usr/bin/env python3
"""Bounded Week 6 reproduction in the spirit of Lundborg, Plug, and Rasmussen (2017)."""
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
    parser.add_argument("--input", required=True, help="Path to the synthetic IVF CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for reproduction files.")
    return parser.parse_args()


def residualize(series: pd.Series, controls: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(controls, series.to_numpy(), rcond=None)
    return series.to_numpy() - controls @ coef


def iv_effect(df: pd.DataFrame, outcome: str) -> tuple[float, float, float]:
    controls = np.column_stack(
        [
            np.ones(len(df)),
            df["age_at_treatment"].to_numpy(),
            df["education_years"].to_numpy(),
            df["prior_children"].to_numpy(),
            df["baseline_hours"].to_numpy(),
            df["baseline_earnings_index"].to_numpy(),
            df["partner_income_index"].to_numpy(),
        ]
    )
    y_tilde = residualize(df[outcome], controls)
    d_tilde = residualize(df["birth_within_two_years"], controls)
    z_tilde = residualize(df["ivf_success"], controls)
    reduced_form = float(np.cov(y_tilde, z_tilde, bias=True)[0, 1] / np.var(z_tilde))
    first_stage = float(np.cov(d_tilde, z_tilde, bias=True)[0, 1] / np.var(z_tilde))
    wald = float(np.cov(y_tilde, z_tilde, bias=True)[0, 1] / np.cov(d_tilde, z_tilde, bias=True)[0, 1])
    return reduced_form, first_stage, wald


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {
        "ivf_success",
        "birth_within_two_years",
        "employment_after",
        "hours_after",
        "earnings_after_index",
        "age_at_treatment",
        "education_years",
        "prior_children",
        "baseline_hours",
        "baseline_earnings_index",
        "partner_income_index",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    summary = (
        df.groupby("ivf_success", as_index=False)
        .agg(
            birth_rate=("birth_within_two_years", "mean"),
            mean_employment=("employment_after", "mean"),
            mean_hours=("hours_after", "mean"),
            mean_earnings=("earnings_after_index", "mean"),
            people=("person_id", "size"),
        )
        .sort_values("ivf_success")
    )
    summary["group_label"] = summary["ivf_success"].map({0: "No IVF success", 1: "IVF success"})
    summary.to_csv(outdir / "reproduction_summary.csv", index=False)

    estimates = []
    for outcome, label in [
        ("employment_after", "employment_after"),
        ("hours_after", "hours_after"),
        ("earnings_after_index", "earnings_after_index"),
    ]:
        reduced_form, first_stage, wald = iv_effect(df, outcome)
        estimates.append(
            {
                "outcome": label,
                "reduced_form": reduced_form,
                "first_stage_births": first_stage,
                "wald_effect_of_birth": wald,
            }
        )
    estimate_df = pd.DataFrame(estimates)
    estimate_df.to_csv(outdir / "wald_estimates.csv", index=False)

    plt.figure(figsize=(9.0, 5.4))
    labels = ["Employment", "Hours", "Earnings index"]
    values = estimate_df["wald_effect_of_birth"].to_numpy()
    colors = ["#4c78a8", "#f58518", "#c44e52"]
    plt.bar(labels, values, color=colors, width=0.56)
    plt.axhline(0.0, color="#666666", linewidth=1)
    plt.ylabel("Local effect of an additional birth")
    plt.title("Bounded IVF-based fertility effects on labor outcomes")
    plt.tight_layout()
    plt.savefig(outdir / "reproduction_ivf_effects.png", dpi=200)
    plt.close()

    note_lines = [
        "The instrument is IVF treatment success, which shifts the probability of birth within the bounded window.",
        "The first stage is a fertility object, while the Wald ratio translates that induced fertility change into labor outcomes.",
        "The resulting estimate is local to the IVF-shifted fertility margin and should not be read as the universal effect of parenthood.",
    ]
    (outdir / "reproduction_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
