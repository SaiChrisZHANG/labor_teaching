#!/usr/bin/env python3
"""Transfer Week 7 valuation logic to broader working-conditions bundles."""
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


def add_value_objects(df: pd.DataFrame) -> pd.DataFrame:
    value = (
        1.6 * df["predictable_schedule"]
        + 1.2 * df["remote_option"]
        + 2.0 * df["low_injury_risk"]
        + 2.4 * df["autonomy_score"]
        - 0.05 * df["commute_minutes"]
    )
    out = df.copy()
    out["amenity_value"] = value
    out["total_job_value"] = out["hourly_wage"] + out["amenity_value"]
    out["wage_rank"] = out["hourly_wage"].rank(method="first", ascending=True).astype(int)
    out["total_value_rank"] = out["total_job_value"].rank(method="first", ascending=True).astype(int)
    out["rank_change"] = out["wage_rank"] - out["total_value_rank"]
    return out


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {
        "worker_group",
        "hourly_wage",
        "predictable_schedule",
        "remote_option",
        "low_injury_risk",
        "autonomy_score",
        "commute_minutes",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    valued = add_value_objects(df)

    summary = (
        valued.groupby("worker_group", as_index=False)
        .agg(
            mean_hourly_wage=("hourly_wage", "mean"),
            mean_amenity_value=("amenity_value", "mean"),
            mean_total_job_value=("total_job_value", "mean"),
            mean_commute_minutes=("commute_minutes", "mean"),
        )
    )
    summary.to_csv(outdir / "group_value_summary.csv", index=False)

    top_rank_changes = (
        valued.loc[:, ["worker_id", "worker_group", "hourly_wage", "amenity_value", "total_job_value", "wage_rank", "total_value_rank", "rank_change"]]
        .reindex(valued["rank_change"].abs().sort_values(ascending=False).index)
        .head(80)
    )
    top_rank_changes.to_csv(outdir / "rank_change_summary.csv", index=False)

    quantile_summary = (
        valued.assign(wage_quartile=pd.qcut(valued["hourly_wage"], 4, labels=["Q1", "Q2", "Q3", "Q4"]))
        .groupby("wage_quartile", as_index=False, observed=False)
        .agg(
            mean_hourly_wage=("hourly_wage", "mean"),
            mean_total_job_value=("total_job_value", "mean"),
        )
    )
    quantile_summary.to_csv(outdir / "quartile_value_summary.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.8))

    plot_summary = summary.set_index("worker_group").reindex(["frontline_track", "professional_track"])
    x = np.arange(len(plot_summary))
    axes[0].bar(x - 0.18, plot_summary["mean_hourly_wage"], width=0.36, label="Wage", color="#d8a25b")
    axes[0].bar(x + 0.18, plot_summary["mean_total_job_value"], width=0.36, label="Total job value", color="#1f5c99")
    axes[0].set_xticks(x, ["Frontline", "Professional"])
    axes[0].set_ylabel("Hourly dollars")
    axes[0].set_title("Working conditions change group gaps")
    axes[0].legend(frameon=False)

    sample = valued.sample(n=min(220, len(valued)), random_state=7)
    colors = sample["worker_group"].map({"frontline_track": "#c25b2a", "professional_track": "#2a7f62"})
    axes[1].scatter(sample["hourly_wage"], sample["total_job_value"], c=colors, alpha=0.72, s=30)
    min_wage = float(sample["hourly_wage"].min())
    max_wage = float(sample["hourly_wage"].max())
    axes[1].plot([min_wage, max_wage], [min_wage, max_wage], linestyle="--", color="#555555", linewidth=1.4)
    axes[1].set_title("Value-adjusted rankings differ from wage-only rankings")
    axes[1].set_xlabel("Hourly wage")
    axes[1].set_ylabel("Total job value")

    plt.tight_layout()
    plt.savefig(outdir / "transfer_working_conditions_value.png", dpi=200)
    plt.close(fig)

    note_lines = [
        "The transfer step adds a money-metric value for broader working conditions to observed wages.",
        "Value-adjusted rankings differ from wage-only rankings when commute burden, predictability, safety, and autonomy covary with wages.",
        "The resulting object is closer to total compensation than to wage inequality alone.",
    ]
    (outdir / "transfer_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
