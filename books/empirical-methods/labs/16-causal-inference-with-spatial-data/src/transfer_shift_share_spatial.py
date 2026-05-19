"""Transfer Week 16 spatial design logic to a synthetic shift-share exposure."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def slope(y: pd.Series, x: pd.Series) -> dict[str, float]:
    yv = y.to_numpy(dtype=float)
    xv = x.to_numpy(dtype=float)
    design = np.column_stack([np.ones(len(xv)), xv])
    beta = np.linalg.lstsq(design, yv, rcond=None)[0]
    resid = yv - design @ beta
    return {
        "intercept": float(beta[0]),
        "slope": float(beta[1]),
        "rmse": float(np.sqrt(np.mean(resid**2))),
        "n": float(len(yv)),
    }


def make_exposures(counties: pd.DataFrame, shares: pd.DataFrame, shocks: pd.DataFrame) -> pd.DataFrame:
    merged = shares.merge(shocks, on="sector", how="left")
    merged["contribution"] = merged["sector_share_1990"] * merged["shock"]
    merged["leave_one_out_shock"] = merged["shock"] - merged["feedback_penalty"] * merged["sector_share_1990"]
    merged["leave_one_out_contribution"] = merged["sector_share_1990"] * merged["leave_one_out_shock"]

    county_exposure = merged.groupby("county_id", as_index=False).agg(
        shift_share_exposure=("contribution", "sum"),
        leave_one_out_exposure=("leave_one_out_contribution", "sum"),
        max_abs_contribution=("contribution", lambda s: float(np.abs(s).max())),
        contribution_abs_sum=("contribution", lambda s: float(np.abs(s).sum())),
        sector_share_herfindahl=("sector_share_1990", lambda s: float(np.sum(np.square(s)))),
    )
    county_exposure["dominant_contribution_share"] = (
        county_exposure["max_abs_contribution"] / county_exposure["contribution_abs_sum"]
    )
    county_exposure["effective_sector_count"] = 1.0 / county_exposure["sector_share_herfindahl"]

    region_sector = merged.groupby(["region_id", "sector"], as_index=False).agg(
        sector_employment_1990=("sector_employment_1990", "sum"),
        baseline_employment_1990=("baseline_employment_1990", "sum"),
        shock=("shock", "first"),
    )
    region_totals = region_sector.groupby("region_id")["sector_employment_1990"].transform("sum")
    region_sector["region_sector_share"] = region_sector["sector_employment_1990"] / region_totals
    region_sector["region_contribution"] = region_sector["region_sector_share"] * region_sector["shock"]
    region_exposure = region_sector.groupby("region_id", as_index=False).agg(
        region_shift_share_exposure=("region_contribution", "sum")
    )

    exposure = counties.merge(county_exposure, on="county_id", how="left").merge(region_exposure, on="region_id", how="left")
    exposure["county_minus_region_exposure"] = exposure["shift_share_exposure"] - exposure["region_shift_share_exposure"]
    return exposure


def write_outputs(counties: pd.DataFrame, shares: pd.DataFrame, shocks: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    exposure = make_exposures(counties, shares, shocks)
    exposure.round(6).to_csv(outdir / "shift_share_exposure.csv", index=False)

    merged = shares.merge(shocks, on="sector", how="left")
    merged["contribution"] = merged["sector_share_1990"] * merged["shock"]
    dominant = (
        merged.assign(abs_contribution=lambda d: np.abs(d["contribution"]))
        .sort_values(["county_id", "abs_contribution"], ascending=[True, False])
        .groupby("county_id", as_index=False)
        .first()
    )
    dominant = dominant[
        [
            "county_id",
            "region_id",
            "sector",
            "sector_share_1990",
            "shock",
            "contribution",
            "abs_contribution",
        ]
    ]
    dominant.round(6).to_csv(outdir / "dominant_contributions.csv", index=False)

    diagnostics = exposure[
        [
            "county_id",
            "region_id",
            "shift_share_exposure",
            "leave_one_out_exposure",
            "region_shift_share_exposure",
            "dominant_contribution_share",
            "effective_sector_count",
            "county_minus_region_exposure",
        ]
    ].copy()
    diagnostics["highly_concentrated_shares"] = (diagnostics["effective_sector_count"] < 3.5).astype(int)
    diagnostics["dominant_contribution_warning"] = (diagnostics["dominant_contribution_share"] > 0.55).astype(int)
    diagnostics.round(6).to_csv(outdir / "share_diagnostics.csv", index=False)

    estimate_rows = []
    outcome = exposure["employment_growth_2000_2010"]
    for label, x_col in [
        ("baseline_shift_share", "shift_share_exposure"),
        ("leave_one_out_shift_share", "leave_one_out_exposure"),
        ("region_level_shift_share", "region_shift_share_exposure"),
    ]:
        stats = slope(outcome, exposure[x_col])
        stats["specification"] = label
        stats["exposure_variable"] = x_col
        estimate_rows.append(stats)
    pd.DataFrame(estimate_rows)[["specification", "exposure_variable", "n", "intercept", "slope", "rmse"]].round(6).to_csv(
        outdir / "transfer_estimates.csv",
        index=False,
    )

    prompts = pd.DataFrame(
        [
            {
                "prompt": "What are the shares?",
                "answer_guidance": "County baseline sector shares; they embed historical local economic structure.",
            },
            {
                "prompt": "What are the shocks?",
                "answer_guidance": "Common sector shocks; validity depends on whether they are exogenous to local residual shocks.",
            },
            {
                "prompt": "What does the dominant contribution diagnostic show?",
                "answer_guidance": "Whether a small number of sectors drive most exposure variation.",
            },
            {
                "prompt": "Why compare county and region exposure?",
                "answer_guidance": "Changing geography changes the exposure object and may change the estimand.",
            },
            {
                "prompt": "What is the first identification caveat?",
                "answer_guidance": "A shift-share exposure is not automatically an instrument; shares, shocks, and geography require defense.",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)
    print(f"Wrote shift-share transfer outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--counties", required=True, type=Path)
    parser.add_argument("--shares", required=True, type=Path)
    parser.add_argument("--shocks", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    counties = pd.read_csv(args.counties)
    shares = pd.read_csv(args.shares)
    shocks = pd.read_csv(args.shocks)
    write_outputs(counties, shares, shocks, args.outdir)


if __name__ == "__main__":
    main()
