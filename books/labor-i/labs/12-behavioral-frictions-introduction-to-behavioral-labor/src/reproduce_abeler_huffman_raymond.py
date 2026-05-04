#!/usr/bin/env python3
"""Reproduce a bounded Week 12 incentive-opacity factbook from synthetic data."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def contract_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["contract_arm", "cognitive_group"], as_index=False)
        .agg(
            observed_effort=("observed_effort", "mean"),
            rational_effort=("rational_effort", "mean"),
            perceived_piece_rate=("perceived_piece_rate", "mean"),
            true_piece_rate=("true_piece_rate", "mean"),
            mean_effort_gap=("effort_gap", "mean"),
            n=("worker_id", "count"),
        )
        .sort_values(["contract_arm", "cognitive_group"])
        .reset_index(drop=True)
    )
    return summary


def opacity_regression(df: pd.DataFrame) -> pd.DataFrame:
    design = df.copy()
    design["complex_bonus"] = (design["contract_arm"] == "complex_bonus").astype(float)
    design["opacity_gap"] = design["true_piece_rate"] - design["perceived_piece_rate"]
    cognitive_dummies = pd.get_dummies(design["cognitive_group"], drop_first=True, dtype=float)

    X = np.column_stack(
        [
            np.ones(len(design)),
            design["complex_bonus"].to_numpy(),
            design["opacity_gap"].to_numpy(),
            design["baseline_skill"].to_numpy(),
            design["cognitive_score"].to_numpy(),
            cognitive_dummies.to_numpy(),
        ]
    )
    y = design["observed_effort"].to_numpy()
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ coef
    dof = X.shape[0] - X.shape[1]
    sigma2 = float((resid @ resid) / dof)
    vcov = sigma2 * np.linalg.inv(X.T @ X)

    rows = [
        ("complex_bonus", 1),
        ("opacity_gap", 2),
        ("baseline_skill", 3),
        ("cognitive_score", 4),
    ]
    return pd.DataFrame(
        {
            "term": [name for name, _ in rows],
            "estimate": [float(coef[idx]) for _, idx in rows],
            "se": [float(np.sqrt(vcov[idx, idx])) for _, idx in rows],
        }
    )


def make_figure(summary_df: pd.DataFrame, regression_df: pd.DataFrame, outdir: Path) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.7))

    plot_df = summary_df.pivot(index="cognitive_group", columns="contract_arm", values="observed_effort")
    plot_df = plot_df.reindex(["low", "middle", "high"])
    axes[0].plot(
        plot_df.index,
        plot_df["simple_piece_rate"],
        marker="o",
        linewidth=2.0,
        color="#1f5c99",
        label="Simple contract",
    )
    axes[0].plot(
        plot_df.index,
        plot_df["complex_bonus"],
        marker="o",
        linewidth=2.0,
        color="#c25b2a",
        label="Complex contract",
    )
    axes[0].set_title("Complexity matters most at low cognition")
    axes[0].set_ylabel("Average observed effort")
    axes[0].legend(frameon=False)

    axes[1].bar(
        regression_df["term"],
        regression_df["estimate"],
        color=["#c25b2a", "#7d5ba6", "#2a7f62", "#d8a25b"],
    )
    axes[1].errorbar(
        regression_df["term"],
        regression_df["estimate"],
        yerr=1.96 * regression_df["se"],
        fmt="none",
        ecolor="#374151",
        elinewidth=1.2,
        capsize=4,
    )
    axes[1].axhline(0.0, color="#555555", linewidth=1.1)
    axes[1].set_title("Opacity shifts effort beyond true incentives")
    axes[1].tick_params(axis="x", rotation=18)

    fig.tight_layout()
    fig.savefig(outdir / "reproduction_incentive_opacity.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    summary_df = contract_summary(df)
    regression_df = opacity_regression(df)

    summary_df.to_csv(args.outdir / "contract_summary.csv", index=False)
    regression_df.to_csv(args.outdir / "opacity_regression.csv", index=False)
    make_figure(summary_df, regression_df, args.outdir)

    note = (
        "This bounded reproduction compares simple and complex incentive contracts with the same true piece rate. "
        "The key teaching object is the gap between true and perceived incentives, not a generic weak labor response."
    )
    (args.outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Wrote Week 12 reproduction outputs to {args.outdir}")


if __name__ == "__main__":
    main()
