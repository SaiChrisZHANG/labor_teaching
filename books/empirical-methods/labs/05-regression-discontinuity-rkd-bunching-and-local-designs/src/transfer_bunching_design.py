"""Run the Week 5 bunching transfer workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week5_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week5_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_bins(
    df: pd.DataFrame,
    bin_width: int,
    lower: int = 30_000,
    upper: int = 72_000,
) -> pd.DataFrame:
    edges = np.arange(lower, upper + bin_width, bin_width)
    counts, edges = np.histogram(df["observed_earnings"], bins=edges)
    centers = (edges[:-1] + edges[1:]) / 2
    return pd.DataFrame(
        {
            "bin_left": edges[:-1],
            "bin_right": edges[1:],
            "bin_center": centers,
            "count": counts,
        }
    )


def fit_counterfactual_density(
    bins: pd.DataFrame,
    kink: float,
    excluded_left: float,
    excluded_right: float,
    degree: int,
) -> tuple[pd.DataFrame, np.ndarray]:
    work = bins.copy()
    work["centered"] = (work["bin_center"] - kink) / 10_000
    fit_sample = (work["bin_center"] < kink - excluded_left) | (
        work["bin_center"] > kink + excluded_right
    )
    fit_sample &= (work["bin_center"] >= kink - 16_000) & (work["bin_center"] <= kink + 18_000)
    x = np.column_stack([work.loc[fit_sample, "centered"] ** p for p in range(degree + 1)])
    y = work.loc[fit_sample, "count"].to_numpy(dtype=float)
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    pred_x = np.column_stack([work["centered"] ** p for p in range(degree + 1)])
    work["counterfactual_count"] = np.maximum(pred_x @ beta, 1.0)
    work["fit_sample"] = fit_sample
    return work, beta


def bunching_estimate(
    df: pd.DataFrame,
    bin_width: int = 500,
    excluded_left: float = 1_500,
    excluded_right: float = 4_500,
    bunch_left: float = 1_500,
    bunch_right: float = 1_000,
    degree: int = 4,
) -> tuple[pd.DataFrame, dict[str, float | str]]:
    kink = float(df["tax_kink"].iloc[0])
    lower_tax = float(df["lower_marginal_tax_rate"].iloc[0])
    upper_tax = float(df["upper_marginal_tax_rate"].iloc[0])
    bins = build_bins(df, bin_width)
    bins, _ = fit_counterfactual_density(bins, kink, excluded_left, excluded_right, degree)
    bunch_window = (bins["bin_center"] >= kink - bunch_left) & (
        bins["bin_center"] <= kink + bunch_right
    )
    missing_window = (bins["bin_center"] > kink + bunch_right) & (
        bins["bin_center"] <= kink + excluded_right
    )
    excess_mass = float((bins.loc[bunch_window, "count"] - bins.loc[bunch_window, "counterfactual_count"]).sum())
    missing_mass = float((bins.loc[missing_window, "counterfactual_count"] - bins.loc[missing_window, "count"]).sum())
    counterfactual_height = float(
        bins.iloc[(bins["bin_center"] - kink).abs().argsort()[:1]]["counterfactual_count"].iloc[0]
    )
    normalized_bunching_bins = excess_mass / max(counterfactual_height, 1.0)
    normalized_bunching_dollars = normalized_bunching_bins * bin_width
    delta_log_net_of_tax = float(np.log(1 - lower_tax) - np.log(1 - upper_tax))
    elasticity = (normalized_bunching_dollars / kink) / max(delta_log_net_of_tax, 1e-8)
    bins["bunching_window"] = bunch_window
    bins["missing_window"] = missing_window
    bins["excess_count"] = bins["count"] - bins["counterfactual_count"]

    estimate = {
        "bin_width": float(bin_width),
        "counterfactual_degree": float(degree),
        "excluded_left": float(excluded_left),
        "excluded_right": float(excluded_right),
        "bunch_left": float(bunch_left),
        "bunch_right": float(bunch_right),
        "excess_mass": excess_mass,
        "missing_mass_above_kink": missing_mass,
        "counterfactual_height_at_kink": counterfactual_height,
        "normalized_bunching_bins": normalized_bunching_bins,
        "normalized_bunching_dollars": normalized_bunching_dollars,
        "delta_log_net_of_tax": delta_log_net_of_tax,
        "stylized_elasticity": elasticity,
        "interpretation": "Excess mass mapped to elasticity using a simple kink model; not model-free.",
    }
    return bins, estimate


def make_plot(bins: pd.DataFrame, outdir: Path, kink: float) -> None:
    plt.figure(figsize=(7.4, 4.4))
    colors = np.where(bins["bunching_window"], "#F58518", "#4C78A8")
    plt.bar(
        bins["bin_center"],
        bins["count"],
        width=(bins["bin_right"] - bins["bin_left"]) * 0.92,
        color=colors,
        alpha=0.72,
        label="observed",
    )
    plt.plot(
        bins["bin_center"],
        bins["counterfactual_count"],
        color="black",
        linewidth=2.0,
        label="counterfactual density",
    )
    plt.axvline(kink, color="#D62728", linewidth=1.6)
    plt.xlabel("Observed earnings")
    plt.ylabel("Count")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(outdir / "tax_kink_bunching_plot.png", dpi=160)
    plt.close()


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    bins, estimate = bunching_estimate(df)
    bins.to_csv(outdir / "bunching_bins.csv", index=False)
    pd.DataFrame([estimate]).to_csv(outdir / "bunching_estimates.csv", index=False)

    sensitivity_rows = []
    for bin_width in [250, 500, 1000]:
        _, est = bunching_estimate(df, bin_width=bin_width)
        sensitivity_rows.append(est)
    for degree in [3, 4, 5]:
        _, est = bunching_estimate(df, bin_width=500, degree=degree)
        est["sensitivity_type"] = f"polynomial_degree_{degree}"
        sensitivity_rows.append(est)
    pd.DataFrame(sensitivity_rows).to_csv(outdir / "bunching_sensitivity.csv", index=False)

    kink = float(df["tax_kink"].iloc[0])
    make_plot(bins, outdir, kink)

    prompts = pd.DataFrame(
        [
            {
                "prompt": "What is the kink, and how does the marginal tax rate change?",
                "student_note": "Use lower_marginal_tax_rate and upper_marginal_tax_rate in the synthetic data.",
            },
            {
                "prompt": "Which observations are excluded to fit the counterfactual density?",
                "student_note": "Use bunching_bins.csv and the fit_sample column.",
            },
            {
                "prompt": "How sensitive is excess mass to bin width and polynomial degree?",
                "student_note": "Use bunching_sensitivity.csv.",
            },
            {
                "prompt": "Why is the elasticity estimate not model-free?",
                "student_note": "Name the optimization model, salience, frictions, and reporting response assumptions.",
            },
            {
                "prompt": "What would a notch change relative to a kink?",
                "student_note": "A notch creates a level payoff discontinuity and often a dominated region.",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)
    print(f"Wrote bunching diagnostics to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    analyze(df, args.outdir)


if __name__ == "__main__":
    main()
