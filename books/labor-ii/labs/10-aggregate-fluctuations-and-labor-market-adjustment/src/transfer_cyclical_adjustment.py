#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_stock_flow(panel: pd.DataFrame) -> pd.DataFrame:
    frame = panel.copy()
    frame["next_u_rate"] = frame["u_rate"].shift(-1)
    frame["delta_u_next"] = frame["next_u_rate"] - frame["u_rate"]
    frame["inflow_component"] = frame["s_rate"] * (1.0 - frame["u_rate"])
    frame["outflow_component"] = -frame["f_rate"] * frame["u_rate"]
    frame["net_component"] = frame["inflow_component"] + frame["outflow_component"]
    return frame.dropna().round(6)


def build_job_to_job(panel: pd.DataFrame) -> pd.DataFrame:
    frame = panel[["date", "phase", "u_rate", "theta"]].copy()
    tightness_gap = (frame["theta"] - frame["theta"].mean()) / frame["theta"].std()
    unemployment_gap = frame["u_rate"] - frame["u_rate"].mean()

    frame["ee_rate"] = 0.022 + 0.006 * tightness_gap
    frame["incumbent_wage_growth"] = 0.006 + 0.0012 * tightness_gap
    frame["mover_wage_growth"] = 0.012 + 0.0045 * tightness_gap
    frame["composition_term"] = 0.004 * unemployment_gap
    frame["sorting_term"] = 0.0015 * unemployment_gap - 0.0008 * tightness_gap
    frame["aggregate_wage_growth"] = (
        frame["incumbent_wage_growth"]
        + frame["ee_rate"] * frame["mover_wage_growth"]
        + frame["composition_term"]
        + frame["sorting_term"]
    )
    return frame.round(6)


def build_summary(stock_flow: pd.DataFrame, job_to_job: pd.DataFrame) -> pd.DataFrame:
    merged = stock_flow.merge(
        job_to_job[
            [
                "date",
                "ee_rate",
                "incumbent_wage_growth",
                "mover_wage_growth",
                "aggregate_wage_growth",
            ]
        ],
        on="date",
        how="left",
    )
    summary = (
        merged.groupby("phase", sort=False)[
            [
                "u_rate",
                "s_rate",
                "f_rate",
                "inflow_component",
                "outflow_component",
                "delta_u_next",
                "ee_rate",
                "incumbent_wage_growth",
                "mover_wage_growth",
                "aggregate_wage_growth",
            ]
        ]
        .mean()
        .reset_index()
    )
    return summary.round(5)


def plot_outputs(stock_flow: pd.DataFrame, job_to_job: pd.DataFrame, outpath: Path) -> None:
    dates = pd.to_datetime(stock_flow["date"])
    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

    axes[0].plot(dates, stock_flow["inflow_component"], color="#e45756", linewidth=2.0, label="Inflow component")
    axes[0].plot(dates, -stock_flow["outflow_component"], color="#4c78a8", linewidth=2.0, label="Outflow component")
    axes[0].plot(dates, stock_flow["delta_u_next"], color="#2f2f2f", linewidth=1.8, linestyle="--", label="Next-period du")
    axes[0].set_title("Unemployment stock-flow decomposition")
    axes[0].set_ylabel("Rate contribution")
    axes[0].legend(frameon=False, fontsize=8)

    job_dates = pd.to_datetime(job_to_job["date"])
    axes[1].plot(job_dates, job_to_job["ee_rate"], color="#54a24b", linewidth=2.0, label="E-to-E rate")
    axes[1].plot(
        job_dates,
        job_to_job["incumbent_wage_growth"],
        color="#4c78a8",
        linewidth=1.8,
        label="Incumbent wage growth",
    )
    axes[1].plot(
        job_dates,
        job_to_job["mover_wage_growth"],
        color="#f58518",
        linewidth=1.8,
        label="Mover wage growth",
    )
    axes[1].plot(
        job_dates,
        job_to_job["aggregate_wage_growth"],
        color="#e45756",
        linewidth=1.8,
        linestyle="--",
        label="Aggregate wage growth",
    )
    axes[1].set_title("Job-to-job mobility and wage cyclicality")
    axes[1].set_ylabel("Rate")
    axes[1].set_xlabel("Date")
    axes[1].legend(frameon=False, fontsize=8, ncol=2)

    fig.tight_layout()
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reproduced", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    panel = pd.read_csv(args.reproduced)
    stock_flow = build_stock_flow(panel)
    job_to_job = build_job_to_job(panel)
    summary = build_summary(stock_flow, job_to_job)

    stock_flow.to_csv(args.outdir / "stock_flow_decomposition.csv", index=False)
    job_to_job.to_csv(args.outdir / "job_to_job_wage_panel.csv", index=False)
    summary.to_csv(args.outdir / "transfer_summary.csv", index=False)
    plot_outputs(stock_flow, job_to_job, args.outdir / "cyclical_adjustment_transfer.png")


if __name__ == "__main__":
    main()
