"""Run a bounded synthetic-control transfer workflow."""

from __future__ import annotations

import argparse
import itertools
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week3_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week3_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def simplex_grid(n_weights: int, steps: int = 20) -> np.ndarray:
    rows = []
    for counts in itertools.product(range(steps + 1), repeat=n_weights):
        if sum(counts) == steps:
            rows.append([count / steps for count in counts])
    return np.asarray(rows, dtype=float)


def fit_weights(target: np.ndarray, donors: np.ndarray) -> tuple[np.ndarray, float]:
    grid = simplex_grid(donors.shape[1], steps=20)
    predictions = donors @ grid.T
    losses = ((predictions - target[:, None]) ** 2).mean(axis=0)
    best_idx = int(np.argmin(losses))
    weights = grid[best_idx, :]
    rmspe = float(np.sqrt(losses[best_idx]))
    return weights, rmspe


def wide_outcomes(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot(index="year", columns="city", values="placement_index").sort_index()


def estimate_for_target(wide: pd.DataFrame, target_city: str, donor_cities: list[str], treatment_year: int) -> dict[str, object]:
    pre = wide.index < treatment_year
    target_pre = wide.loc[pre, target_city].to_numpy(dtype=float)
    donor_pre = wide.loc[pre, donor_cities].to_numpy(dtype=float)
    weights, pre_rmspe = fit_weights(target_pre, donor_pre)
    synthetic = wide[donor_cities].to_numpy(dtype=float) @ weights
    actual = wide[target_city].to_numpy(dtype=float)
    gaps = actual - synthetic
    post = wide.index >= treatment_year
    post_rmspe = float(np.sqrt(np.mean(gaps[post] ** 2)))
    return {
        "weights": weights,
        "pre_rmspe": pre_rmspe,
        "post_rmspe": post_rmspe,
        "synthetic": synthetic,
        "actual": actual,
        "gaps": gaps,
    }


def run_synthetic_control(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    treatment_year = 2016
    treated_city = "Bay City"
    wide = wide_outcomes(df)
    donor_cities = [city for city in wide.columns if city != treated_city]

    fit = estimate_for_target(wide, treated_city, donor_cities, treatment_year)
    weights = pd.DataFrame(
        {
            "donor_city": donor_cities,
            "weight": fit["weights"],
        }
    ).sort_values("weight", ascending=False)
    weights.to_csv(outdir / "synthetic_control_weights.csv", index=False)

    gaps = pd.DataFrame(
        {
            "year": wide.index,
            "actual": fit["actual"],
            "synthetic": fit["synthetic"],
            "gap": fit["gaps"],
            "post": (wide.index >= treatment_year).astype(int),
        }
    )
    gaps.to_csv(outdir / "synthetic_control_gaps.csv", index=False)

    fit_stats = pd.DataFrame(
        [
            {
                "target_city": treated_city,
                "pre_rmspe": fit["pre_rmspe"],
                "post_rmspe": fit["post_rmspe"],
                "rmspe_ratio": fit["post_rmspe"] / fit["pre_rmspe"] if fit["pre_rmspe"] > 0 else np.nan,
                "interpretation": "large post/pre ratio is more persuasive when pre-fit is good",
            }
        ]
    )
    fit_stats.to_csv(outdir / "synthetic_control_fit.csv", index=False)

    placebo_rows = []
    for placebo_city in donor_cities:
        placebo_donors = [city for city in donor_cities if city != placebo_city]
        placebo_fit = estimate_for_target(wide, placebo_city, placebo_donors, treatment_year)
        placebo_rows.append(
            {
                "placebo_city": placebo_city,
                "pre_rmspe": placebo_fit["pre_rmspe"],
                "post_rmspe": placebo_fit["post_rmspe"],
                "rmspe_ratio": placebo_fit["post_rmspe"] / placebo_fit["pre_rmspe"]
                if placebo_fit["pre_rmspe"] > 0
                else np.nan,
                "mean_post_gap": float(np.mean(placebo_fit["gaps"][wide.index >= treatment_year])),
            }
        )
    placebo = pd.DataFrame(placebo_rows).sort_values("rmspe_ratio", ascending=False)
    placebo.to_csv(outdir / "placebo_summary.csv", index=False)

    plt.figure(figsize=(7.4, 4.4))
    plt.plot(gaps["year"], gaps["actual"], marker="o", linewidth=2, label="Bay City")
    plt.plot(gaps["year"], gaps["synthetic"], marker="s", linewidth=2, label="Synthetic Bay City")
    plt.axvline(treatment_year - 0.5, color="black", linestyle="--", linewidth=1)
    plt.ylabel("Placement index")
    plt.xlabel("Year")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "synthetic_control_paths.png", dpi=160)
    plt.close()

    plt.figure(figsize=(7.4, 4.2))
    plt.plot(gaps["year"], gaps["gap"], marker="o", linewidth=2, label="Bay City gap")
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(treatment_year - 0.5, color="black", linestyle="--", linewidth=1)
    plt.ylabel("Actual minus synthetic")
    plt.xlabel("Year")
    plt.tight_layout()
    plt.savefig(outdir / "synthetic_control_gaps.png", dpi=160)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    run_synthetic_control(df, Path(args.outdir))
    print(f"Wrote synthetic-control outputs to {args.outdir}")


if __name__ == "__main__":
    main()
