#!/usr/bin/env python3
"""
Reduced pedagogical local-demand pipeline for Labor II, Week 1.

Required input columns:
- city
- industry
- year
- local_demand_index
- employment
- wage_index
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REQUIRED_COLUMNS = {
    "city",
    "industry",
    "year",
    "local_demand_index",
    "employment",
    "wage_index",
}


def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    numeric_cols = ["local_demand_index", "employment", "wage_index"]
    for col in numeric_cols:
        if (df[col] <= 0).any():
            raise ValueError(f"Column {col} must be strictly positive for log changes.")


def prepare_deltas(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    temp = df.copy().sort_values(["city", "industry", "year"])
    group_cols = ["city", "industry"]
    temp["log_demand"] = np.log(temp["local_demand_index"])
    temp["log_employment"] = np.log(temp["employment"])
    temp["log_wage"] = np.log(temp["wage_index"])
    temp["dlog_demand"] = temp.groupby(group_cols)["log_demand"].diff()
    temp["dlog_employment"] = temp.groupby(group_cols)["log_employment"].diff()
    temp["dlog_wage"] = temp.groupby(group_cols)["log_wage"].diff()
    temp["baseline_employment"] = temp.groupby(group_cols)["employment"].shift()
    temp = temp.dropna(
        subset=["dlog_demand", "dlog_employment", "dlog_wage", "baseline_employment"]
    ).copy()
    temp["cell"] = temp["city"] + " - " + temp["industry"]
    return temp


def ols_slope(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    design = np.column_stack([np.ones(len(x)), x])
    beta, *_ = np.linalg.lstsq(design, y, rcond=None)
    return float(beta[0]), float(beta[1])


def make_summary(deltas: pd.DataFrame) -> pd.DataFrame:
    x = deltas["dlog_demand"].to_numpy()
    summaries = []
    for outcome in ["dlog_employment", "dlog_wage"]:
        intercept, slope = ols_slope(x, deltas[outcome].to_numpy())
        summaries.append(
            {
                "outcome": outcome,
                "intercept": intercept,
                "slope": slope,
                "mean_outcome": float(deltas[outcome].mean()),
                "observations": int(len(deltas)),
            }
        )
    return pd.DataFrame(summaries)


def make_plot(deltas: pd.DataFrame, summary: pd.DataFrame, outdir: Path) -> None:
    fig_path = outdir / "beaudry_city_industry_scatter.png"
    x = deltas["dlog_demand"].to_numpy()
    y = deltas["dlog_employment"].to_numpy()
    _, slope = ols_slope(x, y)
    intercept = float(summary.loc[summary["outcome"] == "dlog_employment", "intercept"].iloc[0])

    plt.figure(figsize=(8.5, 5.5))
    scatter_sizes = 0.45 * deltas["baseline_employment"].to_numpy()
    for industry, g in deltas.groupby("industry"):
        plt.scatter(
            g["dlog_demand"],
            g["dlog_employment"],
            s=0.45 * g["baseline_employment"],
            alpha=0.75,
            label=industry,
        )

    xline = np.linspace(x.min() - 0.005, x.max() + 0.005, 100)
    yline = intercept + slope * xline
    plt.plot(xline, yline, color="black", linewidth=2, label="Fitted slope")
    plt.axhline(0.0, color="gray", linewidth=0.8, linestyle="--")
    plt.axvline(0.0, color="gray", linewidth=0.8, linestyle="--")
    plt.title("Week 1 reduced local-demand relationship")
    plt.xlabel("Change in log local demand index")
    plt.ylabel("Change in log employment")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=220)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic city-industry CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for outputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    deltas = prepare_deltas(df)
    summary = make_summary(deltas)
    outdir.mkdir(parents=True, exist_ok=True)
    deltas.to_csv(outdir / "beaudry_city_industry_deltas.csv", index=False)
    summary.to_csv(outdir / "beaudry_city_industry_summary.csv", index=False)
    make_plot(deltas, summary, outdir)
    print(f"Saved reduced Week 1 outputs to {outdir}")


if __name__ == "__main__":
    main()
