#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for the Week 10 mobility lab."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def logistic(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-values))


def build_credit_lottery_data(rng: np.random.Generator) -> pd.DataFrame:
    regions = ["North", "Midwest", "South", "West"]
    n = 2200

    lottery_win = rng.binomial(1, 0.50, n)
    region = rng.choice(regions, size=n, p=[0.21, 0.27, 0.31, 0.21])
    baseline_rank = rng.uniform(10.0, 90.0, n)
    skill_index = rng.normal(0.0, 1.0, n)
    credit_score = rng.normal(0.0, 1.0, n)
    family_constraint = rng.uniform(0.0, 1.0, n)
    local_gap = rng.uniform(0.0, 1.0, n)

    region_effect = {"North": 0.10, "Midwest": 0.00, "South": -0.08, "West": 0.14}
    region_component = np.array([region_effect[item] for item in region])

    move_latent = (
        -1.35
        + 0.52 * lottery_win
        + 0.72 * local_gap
        - 0.78 * family_constraint
        + 0.15 * credit_score
        + 0.10 * skill_index
        + region_component
        + 0.28 * lottery_win * local_gap
    )
    move_any = (rng.random(n) < logistic(move_latent)).astype(int)

    far_move_latent = (
        -2.05
        + 0.66 * lottery_win
        + 0.95 * local_gap
        - 0.60 * family_constraint
        + 0.10 * skill_index
        + 0.18 * region_component
    )
    move_far = ((rng.random(n) < logistic(far_move_latent)) & (move_any == 1)).astype(int)

    employer_switch_latent = (
        -0.95
        + 0.38 * lottery_win
        + 0.82 * move_any
        + 0.18 * local_gap
        + 0.16 * skill_index
        - 0.12 * family_constraint
    )
    employer_switch = (rng.random(n) < logistic(employer_switch_latent)).astype(int)

    occupation_upgrade_latent = (
        -1.18
        + 0.26 * lottery_win
        + 0.46 * move_any
        + 0.38 * employer_switch
        + 0.12 * skill_index
        + 0.10 * credit_score
    )
    occupation_upgrade = (rng.random(n) < logistic(occupation_upgrade_latent)).astype(int)

    move_distance_km = np.where(
        move_any == 1,
        np.clip(rng.normal(140 + 95 * move_far + 30 * lottery_win + 25 * local_gap, 45, n), 15, None),
        0.0,
    )

    unemployment_days = np.clip(
        rng.normal(
            26
            - 3.5 * lottery_win
            - 4.0 * employer_switch
            - 2.5 * move_any
            + 5.0 * family_constraint,
            6.5,
            n,
        ),
        0,
        None,
    )

    wage_growth = (
        0.014
        + 0.010 * lottery_win
        + 0.019 * move_any
        + 0.016 * employer_switch
        + 0.012 * occupation_upgrade
        + 0.006 * local_gap
        + 0.003 * skill_index
        + rng.normal(0.0, 0.018, n)
    )

    df = pd.DataFrame(
        {
            "worker_id": np.arange(1, n + 1),
            "lottery_win": lottery_win,
            "region": region,
            "baseline_rank": baseline_rank,
            "skill_index": skill_index,
            "credit_score": credit_score,
            "family_constraint": family_constraint,
            "local_opportunity_gap": local_gap,
            "move_any": move_any,
            "move_far": move_far,
            "employer_switch": employer_switch,
            "occupation_upgrade": occupation_upgrade,
            "move_distance_km": move_distance_km,
            "unemployment_days": unemployment_days,
            "wage_growth": wage_growth,
        }
    )
    df["lottery_label"] = np.where(df["lottery_win"] == 1, "winner", "control")
    df["gap_quartile"] = pd.qcut(df["local_opportunity_gap"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
    return df


def build_exposure_panel(rng: np.random.Generator) -> pd.DataFrame:
    years = list(range(2014, 2023))
    n_regions = 20
    reform_year = 2018

    exposures = np.linspace(0.08, 0.62, n_regions) + rng.normal(0.0, 0.02, n_regions)
    manufacturing_share = np.linspace(0.18, 0.44, n_regions) + rng.normal(0.0, 0.015, n_regions)
    region_fe = rng.normal(0.0, 0.06, n_regions)
    names = [f"market_{idx:02d}" for idx in range(1, n_regions + 1)]

    rows: list[dict[str, float | int | str]] = []
    for idx, region_name in enumerate(names):
        for year in years:
            post = int(year >= reform_year)
            year_idx = year - years[0]
            common_trend = 0.010 * year_idx
            reform_effect = exposures[idx] * post
            ee_reallocation_rate = (
                0.095
                + 0.006 * year_idx
                + 0.040 * reform_effect
                - 0.018 * manufacturing_share[idx]
                + region_fe[idx]
                + rng.normal(0.0, 0.008)
            )
            log_firm_employment = (
                4.48
                + common_trend
                + 0.090 * reform_effect
                - 0.040 * manufacturing_share[idx]
                + 0.70 * region_fe[idx]
                + rng.normal(0.0, 0.020)
            )
            native_wage_growth = (
                0.010
                + 0.0015 * year_idx
                + 0.012 * reform_effect
                - 0.004 * manufacturing_share[idx]
                + 0.08 * region_fe[idx]
                + rng.normal(0.0, 0.005)
            )
            rows.append(
                {
                    "region_id": idx + 1,
                    "region_name": region_name,
                    "year": year,
                    "post": post,
                    "exposure_share": exposures[idx],
                    "manufacturing_share": manufacturing_share[idx],
                    "ee_reallocation_rate": ee_reallocation_rate,
                    "log_firm_employment": log_firm_employment,
                    "native_wage_growth": native_wage_growth,
                }
            )

    df = pd.DataFrame(rows)
    median_exposure = float(df[["region_id", "exposure_share"]].drop_duplicates()["exposure_share"].median())
    df["exposure_group"] = np.where(df["exposure_share"] >= median_exposure, "high_exposure", "low_exposure")
    return df


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(20260510)
    lottery_df = build_credit_lottery_data(rng)
    exposure_df = build_exposure_panel(rng)

    lottery_df.to_csv(
        ORIGINAL_DIR / "van_doornik_credit_lottery_synthetic.csv",
        index=False,
    )
    exposure_df.to_csv(
        TRANSFER_DIR / "beerli_open_border_synthetic.csv",
        index=False,
    )

    print(f"Wrote credit-lottery dataset to {ORIGINAL_DIR}")
    print(f"Wrote exposure panel to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
