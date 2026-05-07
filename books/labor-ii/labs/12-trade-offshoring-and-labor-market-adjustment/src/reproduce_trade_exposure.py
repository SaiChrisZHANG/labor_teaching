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


def build_sector_shocks() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "sector": [
                "apparel",
                "electronics",
                "machinery",
                "autos",
                "business_services",
                "consumer_services",
            ],
            "import_shock": [1.32, 1.18, 0.92, 0.84, 0.28, 0.14],
            "export_shock": [0.18, 0.36, 0.42, 0.31, 0.21, 0.12],
            "offshoring_shock": [0.74, 0.82, 0.58, 0.41, 0.37, 0.09],
        }
    )


def build_panel(shocks: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(12)
    sectors = shocks["sector"].to_list()
    import_map = dict(zip(shocks["sector"], shocks["import_shock"]))
    export_map = dict(zip(shocks["sector"], shocks["export_shock"]))
    offshoring_map = dict(zip(shocks["sector"], shocks["offshoring_shock"]))
    years = np.arange(2000, 2008)

    rows: list[dict[str, float | str | int]] = []
    for cz_idx in range(1, 25):
        cz = f"cz-{cz_idx:02d}"
        shares = rng.dirichlet([2.6, 2.1, 2.2, 2.0, 1.6, 1.4])
        share_map = dict(zip(sectors, shares))
        import_exposure = float(sum(share_map[s] * import_map[s] for s in sectors))
        export_exposure = float(sum(share_map[s] * export_map[s] for s in sectors))
        offshoring_exposure = float(sum(share_map[s] * offshoring_map[s] for s in sectors))

        baseline_mfg_share = float(0.18 + 0.22 * sum(share_map[s] for s in sectors[:4]))
        baseline_service_share = float(0.42 + 0.18 * sum(share_map[s] for s in sectors[4:]))
        baseline_unemployment = float(rng.uniform(0.042, 0.078))
        baseline_nonparticipation = float(rng.uniform(0.155, 0.235))
        baseline_wage = float(rng.uniform(43.0, 63.0))

        for year in years:
            t = year - years[0]
            import_intensity = import_exposure * (0.45 + 0.11 * t)
            export_intensity = export_exposure * (0.30 + 0.08 * t)
            offshoring_intensity = offshoring_exposure * (0.28 + 0.07 * t)

            manufacturing_share = (
                baseline_mfg_share
                - 0.013 * import_intensity
                + 0.004 * export_intensity
                - 0.003 * offshoring_intensity
                - 0.002 * t
                + rng.normal(0.0, 0.004)
            )
            service_share = (
                baseline_service_share
                + 0.010 * import_intensity
                + 0.004 * export_intensity
                + 0.003 * offshoring_intensity
                + 0.0022 * t
                + rng.normal(0.0, 0.004)
            )
            unemployment_rate = (
                baseline_unemployment
                + 0.0075 * import_intensity
                - 0.0024 * export_intensity
                + 0.0007 * offshoring_intensity
                + rng.normal(0.0, 0.0022)
            )
            nonparticipation_rate = (
                baseline_nonparticipation
                + 0.0055 * import_intensity
                - 0.0012 * export_intensity
                + 0.0008 * offshoring_intensity
                + rng.normal(0.0, 0.0020)
            )
            wage_growth = (
                0.014
                - 0.0090 * import_intensity
                + 0.0048 * export_intensity
                + 0.0015 * offshoring_intensity
                + 0.0010 * t
                + rng.normal(0.0, 0.0032)
            )
            wage_index = baseline_wage * (1.0 + wage_growth)

            rows.append(
                {
                    "commuting_zone": cz,
                    "year": year,
                    "import_exposure": round(import_exposure, 4),
                    "export_exposure": round(export_exposure, 4),
                    "offshoring_exposure": round(offshoring_exposure, 4),
                    "manufacturing_share": round(float(np.clip(manufacturing_share, 0.05, 0.55)), 4),
                    "service_share": round(float(np.clip(service_share, 0.20, 0.82)), 4),
                    "unemployment_rate": round(float(np.clip(unemployment_rate, 0.02, 0.16)), 4),
                    "nonparticipation_rate": round(float(np.clip(nonparticipation_rate, 0.08, 0.34)), 4),
                    "wage_growth": round(wage_growth, 4),
                    "wage_index": round(wage_index, 2),
                    "baseline_mfg_share": round(baseline_mfg_share, 4),
                }
            )

    return pd.DataFrame(rows)


def build_summary(panel: pd.DataFrame) -> pd.DataFrame:
    latest = panel.loc[panel["year"] == panel["year"].max()].copy()
    latest["import_bucket"] = pd.qcut(
        latest["import_exposure"], q=3, labels=["low", "middle", "high"]
    )
    return (
        latest.groupby("import_bucket", as_index=False, observed=False)[
            [
                "import_exposure",
                "manufacturing_share",
                "service_share",
                "unemployment_rate",
                "nonparticipation_rate",
                "wage_growth",
            ]
        ]
        .mean()
        .round(4)
    )


def build_relationships(panel: pd.DataFrame) -> pd.DataFrame:
    latest = panel.loc[panel["year"] == panel["year"].max()].copy()
    latest["manufacturing_share_change"] = latest["manufacturing_share"] - latest["baseline_mfg_share"]
    out = latest[
        [
            "commuting_zone",
            "import_exposure",
            "export_exposure",
            "offshoring_exposure",
            "manufacturing_share_change",
            "service_share",
            "unemployment_rate",
            "nonparticipation_rate",
            "wage_growth",
        ]
    ].copy()
    return out.round(4)


def plot_outputs(latest: pd.DataFrame, outpath: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

    axes[0].scatter(
        latest["import_exposure"],
        latest["manufacturing_share"] - latest["baseline_mfg_share"],
        color="#b6483a",
        alpha=0.85,
    )
    axes[0].set_title("Import exposure and manufacturing-share change")
    axes[0].set_xlabel("Import exposure")
    axes[0].set_ylabel("Manufacturing-share change")
    axes[0].axhline(0.0, color="#333333", linewidth=1.0)

    axes[1].scatter(
        latest["import_exposure"],
        latest["unemployment_rate"],
        color="#3d6f8e",
        alpha=0.85,
        label="Unemployment",
    )
    axes[1].scatter(
        latest["import_exposure"],
        latest["nonparticipation_rate"],
        color="#7a9e48",
        alpha=0.75,
        label="Nonparticipation",
    )
    axes[1].set_title("Import exposure and extensive-margin outcomes")
    axes[1].set_xlabel("Import exposure")
    axes[1].set_ylabel("Rate")
    axes[1].legend(frameon=False, fontsize=8)

    fig.tight_layout()
    fig.savefig(outpath, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    shocks = build_sector_shocks()
    panel = build_panel(shocks)
    summary = build_summary(panel)
    relationships = build_relationships(panel)
    latest = panel.loc[panel["year"] == panel["year"].max()].copy()

    shocks.to_csv(args.outdir / "sector_trade_shocks.csv", index=False)
    panel.to_csv(args.outdir / "cz_trade_panel.csv", index=False)
    summary.to_csv(args.outdir / "trade_exposure_summary.csv", index=False)
    relationships.to_csv(args.outdir / "trade_exposure_relationships.csv", index=False)
    plot_outputs(latest, args.outdir / "trade_exposure_margins.png")


if __name__ == "__main__":
    main()
