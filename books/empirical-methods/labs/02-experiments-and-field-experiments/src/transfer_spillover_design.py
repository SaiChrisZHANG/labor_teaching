"""Run a bounded saturation and spillover teaching workflow."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def mean_difference(df: pd.DataFrame, outcome: str, assignment: str) -> float:
    return float(df[df[assignment] == 1][outcome].mean() - df[df[assignment] == 0][outcome].mean())


def ols_coef(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return beta


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    itt_employment = mean_difference(df, "employed_after", "assigned_assistance")
    first_stage = mean_difference(df, "took_assistance", "assigned_assistance")
    wald_late = itt_employment / first_stage if abs(first_stage) > 1e-9 else np.nan
    naive_receipt = mean_difference(df, "employed_after", "took_assistance")

    y = df["employed_after"].to_numpy(dtype=float)
    x = np.column_stack(
        [
            np.ones(len(df)),
            df["assigned_assistance"].to_numpy(dtype=float),
            df["market_saturation"].to_numpy(dtype=float),
            df["untreated_exposure_share"].to_numpy(dtype=float),
            df["baseline_skill"].to_numpy(dtype=float),
            df["prior_employed"].to_numpy(dtype=float),
        ]
    )
    beta = ols_coef(y, x)

    untreated = df[df["assigned_assistance"] == 0].copy()
    high_exposure = untreated[untreated["market_saturation"] >= 0.70]["employed_after"].mean()
    low_exposure = untreated[untreated["market_saturation"] <= 0.45]["employed_after"].mean()
    untreated_exposure_gap = float(high_exposure - low_exposure)

    estimates = pd.DataFrame(
        [
            {
                "estimand": "individual ITT",
                "method": "employment difference by individual assignment",
                "estimate": itt_employment,
                "interpretation": "direct effect of assistance assignment in the experimental markets",
            },
            {
                "estimand": "first stage",
                "method": "take-up difference by individual assignment",
                "estimate": first_stage,
                "interpretation": "how much assignment shifted assistance receipt",
            },
            {
                "estimand": "Wald/LATE-style ratio",
                "method": "ITT employment divided by first stage",
                "estimate": wald_late,
                "interpretation": "complier effect under additional assumptions",
            },
            {
                "estimand": "naive receipt contrast",
                "method": "employment difference by receipt",
                "estimate": naive_receipt,
                "interpretation": "not randomized after assignment",
            },
            {
                "estimand": "saturation association",
                "method": "OLS with market saturation and controls",
                "estimate": float(beta[2]),
                "interpretation": "market saturation contrast; useful for scale and spillover discussion",
            },
            {
                "estimand": "untreated exposure gap",
                "method": "untreated workers in high- vs low-saturation markets",
                "estimate": untreated_exposure_gap,
                "interpretation": "diagnostic for displacement or spillover exposure among controls",
            },
        ]
    )

    exposure = (
        df.groupby("market_id")
        .agg(
            market_size=("worker_id", "size"),
            market_saturation=("market_saturation", "first"),
            assignment_rate=("assigned_assistance", "mean"),
            takeup_rate=("took_assistance", "mean"),
            employment_rate=("employed_after", "mean"),
            untreated_employment_rate=(
                "employed_after",
                lambda x: float(x[df.loc[x.index, "assigned_assistance"] == 0].mean()),
            ),
        )
        .reset_index()
    )

    prompts = pd.DataFrame(
        [
            {
                "design_object": "assignment unit",
                "student_prompt": "Is assignment individual, clustered, saturated by market, or a mix?",
            },
            {
                "design_object": "main estimand",
                "student_prompt": "Would you lead with ITT, LATE, spillover, or market-level effect?",
            },
            {
                "design_object": "spillover channel",
                "student_prompt": "Name the likely referral, congestion, displacement, or information channel.",
            },
            {
                "design_object": "scale",
                "student_prompt": "Would a larger rollout change untreated workers' outcomes?",
            },
        ]
    )

    estimates.to_csv(outdir / "saturation_estimates.csv", index=False)
    exposure.to_csv(outdir / "market_exposure_summary.csv", index=False)
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)
    df.to_csv(outdir / "transfer_analysis_dataset.csv", index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    analyze(df, args.outdir)
    print(f"Wrote transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
