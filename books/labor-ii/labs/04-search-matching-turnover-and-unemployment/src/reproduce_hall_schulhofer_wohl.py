#!/usr/bin/env python3
"""
Bounded Week 4 reproduction path inspired by Hall and Schulhofer-Wohl (2018).
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

    grouped = (
        df.groupby("month", as_index=False)
        .agg({"unemployed": "sum", "matches": "sum", "vacancies": "first"})
        .sort_values("month")
    )
    grouped["job_finding_rate"] = grouped["matches"] / grouped["unemployed"]
    grouped["tightness"] = grouped["vacancies"] / grouped["unemployed"]

    type_rates = df.copy()
    type_rates["type_rate"] = type_rates["matches"] / type_rates["unemployed"]
    baseline = type_rates[type_rates["month"] == type_rates["month"].min()].copy()
    baseline["base_share"] = baseline["unemployed"] / baseline["unemployed"].sum()
    share_map = baseline.set_index("seeker_type")["base_share"]

    type_rates["base_share"] = type_rates["seeker_type"].map(share_map)
    type_rates["weighted_type_rate"] = type_rates["base_share"] * type_rates["type_rate"]
    fixed_comp = (
        type_rates.groupby("month", as_index=False)["weighted_type_rate"]
        .sum()
        .rename(columns={"weighted_type_rate": "fixed_composition_rate"})
    )

    seeker_shares = df.copy()
    seeker_shares["share"] = seeker_shares["unemployed"] / seeker_shares.groupby("month")["unemployed"].transform("sum")
    share_wide = (
        seeker_shares.pivot(index="month", columns="seeker_type", values="share")
        .reset_index()
        .rename_axis(None, axis=1)
    )

    decomposition = grouped.merge(fixed_comp, on="month")
    decomposition["composition_component"] = decomposition["job_finding_rate"] - decomposition["fixed_composition_rate"]
    decomposition["matching_gap_proxy"] = decomposition["job_finding_rate"] / decomposition["tightness"]

    summary = pd.DataFrame(
        [
            {
                "metric": "average_job_finding_rate",
                "value": decomposition["job_finding_rate"].mean(),
            },
            {
                "metric": "start_to_end_change_job_finding_rate",
                "value": decomposition["job_finding_rate"].iloc[-1] - decomposition["job_finding_rate"].iloc[0],
            },
            {
                "metric": "start_to_end_change_fixed_composition_rate",
                "value": decomposition["fixed_composition_rate"].iloc[-1] - decomposition["fixed_composition_rate"].iloc[0],
            },
            {
                "metric": "end_period_composition_component",
                "value": decomposition["composition_component"].iloc[-1],
            },
        ]
    )

    decomposition.to_csv(outdir / "hall_schulhofer_wohl_decomposition.csv", index=False)
    share_wide.to_csv(outdir / "hall_schulhofer_wohl_seeker_shares.csv", index=False)
    summary.to_csv(outdir / "hall_schulhofer_wohl_summary.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    axes[0].plot(decomposition["month"], decomposition["job_finding_rate"], marker="o", linewidth=2.2, label="Observed aggregate rate")
    axes[0].plot(
        decomposition["month"],
        decomposition["fixed_composition_rate"],
        marker="s",
        linewidth=2.2,
        label="Fixed-composition counterfactual",
    )
    axes[0].set_title("U-to-E job-finding rate")
    axes[0].set_ylabel("Hazard")
    axes[0].tick_params(axis="x", rotation=45)
    axes[0].legend(fontsize=8)

    share_columns = [col for col in share_wide.columns if col != "month"]
    axes[1].stackplot(
        share_wide["month"],
        [share_wide[col] for col in share_columns],
        labels=share_columns,
        alpha=0.85,
    )
    axes[1].set_title("Composition of unemployed job seekers")
    axes[1].set_ylabel("Share")
    axes[1].tick_params(axis="x", rotation=45)
    axes[1].legend(fontsize=8, loc="upper right")

    fig.suptitle("Composition and job-finding rates in the bounded Week 4 path")
    fig.tight_layout()
    fig.savefig(outdir / "hall_schulhofer_wohl_matching.png", dpi=220)
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
    print(f"Saved bounded Hall-Schulhofer-Wohl outputs to {args.outdir}")


if __name__ == "__main__":
    main()
