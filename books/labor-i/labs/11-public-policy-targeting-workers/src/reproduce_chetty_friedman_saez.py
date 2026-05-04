#!/usr/bin/env python3
"""Build a bounded Week 11 EITC-knowledge factbook from synthetic data."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def quartile_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["knowledge_quartile", "post"], as_index=False)
        .agg(
            mean_earnings_k=("mean_earnings_k", "mean"),
            employment_rate=("employment_rate", "mean"),
            takeup_rate=("takeup_rate", "mean"),
            effective_exposure=("effective_exposure", "mean"),
        )
        .sort_values(["knowledge_quartile", "post"])
        .reset_index(drop=True)
    )
    pivot = summary.pivot(index="knowledge_quartile", columns="post")
    pivot.columns = [f"{name}_{'post' if post == 1 else 'pre'}" for name, post in pivot.columns]
    pivot = pivot.reset_index()
    pivot["earnings_change_k"] = pivot["mean_earnings_k_post"] - pivot["mean_earnings_k_pre"]
    pivot["employment_change"] = pivot["employment_rate_post"] - pivot["employment_rate_pre"]
    pivot["takeup_change"] = pivot["takeup_rate_post"] - pivot["takeup_rate_pre"]
    return pivot


def estimate_exposure_gradient(df: pd.DataFrame) -> pd.DataFrame:
    design = df.copy()
    design["interaction"] = design["post"] * design["effective_exposure"]
    region_dummies = pd.get_dummies(design["region"], drop_first=True, dtype=float)
    year_dummies = pd.get_dummies(design["year"].astype(str), drop_first=True, dtype=float)
    neigh_dummies = pd.get_dummies(design["neighborhood"], drop_first=True, dtype=float)

    results: list[dict[str, float | str]] = []
    for outcome in ["mean_earnings_k", "employment_rate", "takeup_rate"]:
        X = np.column_stack(
            [
                np.ones(len(design)),
                design["interaction"].to_numpy(),
                design["post"].to_numpy(),
                design["effective_exposure"].to_numpy(),
                region_dummies.to_numpy(),
                year_dummies.to_numpy(),
                neigh_dummies.to_numpy(),
            ]
        )
        y = design[outcome].to_numpy()
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        resid = y - X @ coef
        dof = X.shape[0] - X.shape[1]
        sigma2 = float((resid @ resid) / dof)
        vcov = sigma2 * np.linalg.inv(X.T @ X)
        results.append(
            {
                "outcome": outcome,
                "beta_post_x_exposure": float(coef[1]),
                "se": float(np.sqrt(vcov[1, 1])),
            }
        )
    return pd.DataFrame(results)


def make_figure(quartile_df: pd.DataFrame, estimate_df: pd.DataFrame, outdir: Path) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))

    axes[0].plot(
        quartile_df["knowledge_quartile"],
        quartile_df["earnings_change_k"],
        marker="o",
        linewidth=2.0,
        color="#1f5c99",
        label="Earnings change",
    )
    axes[0].plot(
        quartile_df["knowledge_quartile"],
        100 * quartile_df["employment_change"],
        marker="o",
        linewidth=2.0,
        color="#c25b2a",
        label="Employment change x100",
    )
    axes[0].set_title("High-knowledge places respond more")
    axes[0].set_ylabel("Change from pre to post")
    axes[0].legend(frameon=False)

    axes[1].bar(
        estimate_df["outcome"],
        estimate_df["beta_post_x_exposure"],
        color=["#2a7f62", "#d8a25b", "#7d5ba6"],
    )
    axes[1].errorbar(
        estimate_df["outcome"],
        estimate_df["beta_post_x_exposure"],
        yerr=1.96 * estimate_df["se"],
        fmt="none",
        ecolor="#374151",
        elinewidth=1.2,
        capsize=4,
    )
    axes[1].set_title("Post x effective exposure coefficients")
    axes[1].tick_params(axis="x", rotation=18)

    fig.tight_layout()
    fig.savefig(outdir / "reproduction_eitc_knowledge.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    quartile_df = quartile_summary(df)
    estimate_df = estimate_exposure_gradient(df)

    quartile_df.to_csv(args.outdir / "knowledge_quartile_summary.csv", index=False)
    estimate_df.to_csv(args.outdir / "knowledge_gradient_estimates.csv", index=False)
    make_figure(quartile_df, estimate_df, args.outdir)

    note = (
        "This bounded reproduction estimates how earnings, employment, and take-up respond more strongly in "
        "higher-knowledge neighborhoods after an expansion. It teaches effective policy exposure rather than a "
        "pure statutory-schedule effect."
    )
    (args.outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote Week 11 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
