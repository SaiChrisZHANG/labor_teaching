#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_panel() -> pd.DataFrame:
    dates = pd.date_range("2006-01-01", "2014-12-01", freq="MS")
    alpha = 0.60
    labor_force = 1_000_000
    periods = np.arange(len(dates))

    slump = np.exp(-0.5 * ((periods - 44) / 10.0) ** 2)
    recovery = np.clip((periods - 56) / 28.0, 0.0, 1.0)

    theta_path = 0.72 - 0.46 * slump + 0.06 * np.sin(periods / 11.0)
    theta_path = np.clip(theta_path, 0.18, None)
    mu_base = 0.43 + 0.01 * np.sin(periods / 8.0)
    composition_index = 0.98 - 0.16 * slump + 0.05 * recovery
    composition_index = np.clip(composition_index, 0.74, 1.05)
    separation_rate = 0.016 + 0.010 * slump + 0.0015 * np.cos(periods / 7.0)
    separation_rate = np.clip(separation_rate, 0.010, None)

    unemployment = np.zeros(len(dates))
    unemployment[0] = 0.055

    rows: list[dict[str, float | str]] = []
    for idx, date in enumerate(dates):
        u_rate = unemployment[idx]
        theta = theta_path[idx]
        vacancies_rate = theta * u_rate
        effective_searchers = u_rate * composition_index[idx]
        match_rate = mu_base[idx] * (effective_searchers**alpha) * (
            vacancies_rate ** (1.0 - alpha)
        )
        finding_rate = match_rate / u_rate
        filling_rate = match_rate / vacancies_rate
        matching_residual = match_rate / (
            (u_rate**alpha) * (vacancies_rate ** (1.0 - alpha))
        )

        phase = "pre-downturn"
        if 30 <= idx <= 57:
            phase = "downturn"
        elif 58 <= idx <= 83:
            phase = "recovery"
        elif idx > 83:
            phase = "late-cycle"

        rows.append(
            {
                "date": date.strftime("%Y-%m"),
                "phase": phase,
                "u_rate": u_rate,
                "v_rate": vacancies_rate,
                "theta": theta,
                "s_rate": separation_rate[idx],
                "f_rate": finding_rate,
                "q_rate": filling_rate,
                "mu_base": mu_base[idx],
                "composition_index": composition_index[idx],
                "mu_observed": matching_residual,
                "matches": match_rate * labor_force,
                "unemployed": u_rate * labor_force,
                "vacancies": vacancies_rate * labor_force,
            }
        )

        if idx < len(dates) - 1:
            next_u = u_rate + separation_rate[idx] * (1.0 - u_rate) - finding_rate * u_rate
            unemployment[idx + 1] = float(np.clip(next_u, 0.03, 0.16))

    return pd.DataFrame(rows)


def build_summary(panel: pd.DataFrame) -> pd.DataFrame:
    summary = (
        panel.groupby("phase", sort=False)[
            [
                "u_rate",
                "v_rate",
                "theta",
                "s_rate",
                "f_rate",
                "mu_observed",
                "composition_index",
            ]
        ]
        .mean()
        .reset_index()
    )
    return summary.round(4)


def build_counterfactual(panel: pd.DataFrame) -> pd.DataFrame:
    alpha = 0.60
    labor_force = 1_000_000
    pre_comp = float(panel.loc[panel["phase"] == "pre-downturn", "composition_index"].mean())
    counterfactual_matches = (
        panel["mu_base"]
        * ((panel["u_rate"] * pre_comp) ** alpha)
        * (panel["v_rate"] ** (1.0 - alpha))
        * labor_force
    )
    frame = panel[["date", "phase", "matches"]].copy()
    frame["matches_fixed_composition"] = counterfactual_matches
    frame["gap_from_fixed_composition"] = frame["matches"] - frame["matches_fixed_composition"]
    return frame.round(2)


def plot_outputs(panel: pd.DataFrame, outpath: Path) -> None:
    date_index = pd.to_datetime(panel["date"])
    colors = {
        "pre-downturn": "#4c78a8",
        "downturn": "#e45756",
        "recovery": "#72b7b2",
        "late-cycle": "#54a24b",
    }

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

    for phase, group in panel.groupby("phase", sort=False):
        axes[0].plot(
            group["v_rate"],
            group["u_rate"],
            marker="o",
            linewidth=1.8,
            markersize=3.5,
            color=colors[phase],
            label=phase,
        )
    axes[0].set_title("Beveridge curve path")
    axes[0].set_xlabel("Vacancy rate")
    axes[0].set_ylabel("Unemployment rate")
    axes[0].legend(frameon=False, fontsize=8)

    axes[1].plot(date_index, panel["mu_observed"], color="#e45756", linewidth=2.0, label="Observed residual")
    axes[1].plot(date_index, panel["mu_base"], color="#4c78a8", linewidth=1.8, linestyle="--", label="Base efficiency")
    axes[1].plot(
        date_index,
        panel["composition_index"],
        color="#54a24b",
        linewidth=1.8,
        linestyle=":",
        label="Composition index",
    )
    axes[1].set_title("Residual versus composition")
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Index / residual")
    axes[1].legend(frameon=False, fontsize=8)

    fig.tight_layout()
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    panel = build_panel()
    summary = build_summary(panel)
    counterfactual = build_counterfactual(panel)

    panel.to_csv(args.outdir / "aggregate_matching_panel.csv", index=False)
    summary.to_csv(args.outdir / "aggregate_matching_summary.csv", index=False)
    counterfactual.to_csv(args.outdir / "aggregate_matching_counterfactual.csv", index=False)
    plot_outputs(panel, args.outdir / "aggregate_matching_beveridge.png")


if __name__ == "__main__":
    main()
