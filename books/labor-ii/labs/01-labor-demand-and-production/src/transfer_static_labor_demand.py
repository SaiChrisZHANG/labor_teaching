#!/usr/bin/env python3
"""
Apply Week 1 conditional-versus-total labor-demand formulas to a scenario file.

Required input columns:
- scenario
- labor_share
- substitution_elasticity
- product_demand_elasticity
- labor_cost_change
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REQUIRED_COLUMNS = {
    "scenario",
    "labor_share",
    "substitution_elasticity",
    "product_demand_elasticity",
    "labor_cost_change",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def compute_summary(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    out = df.copy()
    out["conditional_elasticity"] = -(1 - out["labor_share"]) * out["substitution_elasticity"]
    out["scale_component"] = -out["labor_share"] * out["product_demand_elasticity"]
    out["total_elasticity"] = out["conditional_elasticity"] + out["scale_component"]
    out["conditional_response_pct"] = 100 * out["conditional_elasticity"] * out["labor_cost_change"]
    out["scale_response_pct"] = 100 * out["scale_component"] * out["labor_cost_change"]
    out["total_response_pct"] = 100 * out["total_elasticity"] * out["labor_cost_change"]
    return out


def make_plot(summary: pd.DataFrame, outdir: Path) -> None:
    fig_path = outdir / "static_labor_demand_transfer.png"
    x = np.arange(len(summary))
    width = 0.35

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))

    axes[0].bar(x - width / 2, summary["conditional_elasticity"], width, label="Conditional")
    axes[0].bar(x + width / 2, summary["total_elasticity"], width, label="Total")
    axes[0].axhline(0.0, color="gray", linewidth=0.8)
    axes[0].set_title("Elasticity comparison")
    axes[0].set_ylabel("Elasticity")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(summary["scenario"], rotation=20, ha="right")
    axes[0].legend()

    axes[1].bar(x, summary["conditional_response_pct"], width, label="Substitution response")
    axes[1].bar(
        x,
        summary["scale_response_pct"],
        width,
        bottom=summary["conditional_response_pct"],
        label="Scale response",
    )
    axes[1].axhline(0.0, color="gray", linewidth=0.8)
    axes[1].set_title("Predicted employment response (pct)")
    axes[1].set_ylabel("Percent")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(summary["scenario"], rotation=20, ha="right")
    axes[1].legend()

    plt.tight_layout()
    plt.savefig(fig_path, dpi=220)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the scenario CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for outputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    summary = compute_summary(df)
    outdir.mkdir(parents=True, exist_ok=True)
    summary.to_csv(outdir / "static_labor_demand_transfer_summary.csv", index=False)
    make_plot(summary, outdir)
    print(f"Saved transfer outputs to {outdir}")


if __name__ == "__main__":
    main()
