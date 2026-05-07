#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "output" / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / "output" / ".cache"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_structural_change(latest: pd.DataFrame) -> pd.DataFrame:
    out = latest[
        [
            "commuting_zone",
            "import_exposure",
            "export_exposure",
            "offshoring_exposure",
            "manufacturing_share",
            "service_share",
            "unemployment_rate",
            "nonparticipation_rate",
        ]
    ].copy()
    out["manufacturing_share_change"] = (
        latest["manufacturing_share"] - latest["baseline_mfg_share"]
    ).round(4)
    out["service_share_change"] = (
        0.009
        + 0.018 * latest["import_exposure"]
        + 0.006 * latest["export_exposure"]
        + 0.004 * latest["offshoring_exposure"]
    ).round(4)
    out["adjustment_type"] = np.where(
        out["service_share_change"] > out["unemployment_rate"] - 0.03,
        "reallocation-heavy",
        "distress-heavy",
    )
    return out.round(4)


def build_transfer_summary(structural: pd.DataFrame) -> pd.DataFrame:
    structural["exposure_bucket"] = pd.qcut(
        structural["import_exposure"], q=3, labels=["low", "middle", "high"]
    )
    return (
        structural.groupby("exposure_bucket", as_index=False, observed=False)[
            [
                "import_exposure",
                "manufacturing_share_change",
                "service_share_change",
                "unemployment_rate",
                "nonparticipation_rate",
            ]
        ]
        .mean()
        .round(4)
    )


def build_dynamic_panel(structural: pd.DataFrame) -> pd.DataFrame:
    years = np.arange(1991, 2003)
    rows: list[dict[str, float | str | int]] = []
    for idx, row in structural.reset_index(drop=True).iterrows():
        for year in years:
            h = year - 1994
            post = max(h, 0)
            manufacturing_share = (
                0.30
                + row["manufacturing_share_change"]
                - 0.0045 * row["import_exposure"] * post
                + 0.0012 * row["export_exposure"] * post
            )
            service_share = (
                0.45
                + 0.0038 * row["import_exposure"] * post
                + 0.0015 * row["offshoring_exposure"] * post
            )
            earnings_index = (
                100.0
                - 1.7 * row["import_exposure"] * post
                + 0.8 * row["export_exposure"] * post
                + 0.35 * min(post, 6)
            )
            unemployment_rate = (
                0.055
                + 0.0038 * row["import_exposure"] * np.exp(-0.08 * post) * max(post, 1)
                - 0.0009 * row["export_exposure"] * post
            )
            rows.append(
                {
                    "region": row["commuting_zone"].replace("cz", "region"),
                    "year": year,
                    "event_time": h,
                    "import_exposure": row["import_exposure"],
                    "export_exposure": row["export_exposure"],
                    "manufacturing_share": round(float(np.clip(manufacturing_share, 0.06, 0.48)), 4),
                    "service_share": round(float(np.clip(service_share, 0.30, 0.82)), 4),
                    "earnings_index": round(float(np.clip(earnings_index, 72.0, 118.0)), 2),
                    "unemployment_rate": round(float(np.clip(unemployment_rate, 0.025, 0.16)), 4),
                }
            )
    return pd.DataFrame(rows)


def build_dynamic_summary(panel: pd.DataFrame) -> pd.DataFrame:
    summary_rows = []
    for label, mask in {
        "pre": panel["event_time"] < 0,
        "short_run": panel["event_time"].between(0, 3),
        "long_run": panel["event_time"] >= 6,
    }.items():
        subset = panel.loc[mask]
        summary_rows.append(
            {
                "horizon": label,
                "manufacturing_share": round(subset["manufacturing_share"].mean(), 4),
                "service_share": round(subset["service_share"].mean(), 4),
                "earnings_index": round(subset["earnings_index"].mean(), 2),
                "unemployment_rate": round(subset["unemployment_rate"].mean(), 4),
            }
        )
    return pd.DataFrame(summary_rows)


def plot_outputs(structural: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

    axes[0].scatter(
        structural["import_exposure"],
        structural["service_share_change"],
        color="#4c8b5d",
        alpha=0.85,
        label="Service-share change",
    )
    axes[0].scatter(
        structural["import_exposure"],
        structural["manufacturing_share_change"],
        color="#b6483a",
        alpha=0.80,
        label="Manufacturing-share change",
    )
    axes[0].axhline(0.0, color="#333333", linewidth=1.0)
    axes[0].set_title("Transfer: exposure and structural change")
    axes[0].set_xlabel("Import exposure")
    axes[0].set_ylabel("Change")
    axes[0].legend(frameon=False, fontsize=8)

    axes[1].scatter(
        structural["service_share_change"],
        structural["unemployment_rate"],
        c=np.where(structural["adjustment_type"] == "reallocation-heavy", "#3d6f8e", "#d17c2f"),
        alpha=0.85,
    )
    axes[1].set_title("Service growth is not the same as worker recovery")
    axes[1].set_xlabel("Service-share change")
    axes[1].set_ylabel("Unemployment rate")

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
    latest = panel.loc[panel["year"] == panel["year"].max()].copy()

    structural = build_structural_change(latest)
    transfer_summary = build_transfer_summary(structural.copy())
    dynamic_panel = build_dynamic_panel(structural)
    dynamic_summary = build_dynamic_summary(dynamic_panel)

    structural.to_csv(args.outdir / "structural_change_transfer.csv", index=False)
    transfer_summary.to_csv(args.outdir / "transfer_adjustment_summary.csv", index=False)
    dynamic_panel.to_csv(args.outdir / "dynamic_region_panel.csv", index=False)
    dynamic_summary.to_csv(args.outdir / "dynamic_region_summary.csv", index=False)
    plot_outputs(structural, args.outdir / "trade_adjustment_transfer.png")


if __name__ == "__main__":
    main()
