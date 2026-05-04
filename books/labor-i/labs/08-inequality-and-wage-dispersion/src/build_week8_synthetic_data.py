#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for the Week 8 inequality lab."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def build_repeated_cross_section(rng: np.random.Generator) -> pd.DataFrame:
    years = [1980, 1990, 2000, 2010, 2019]
    n_per_year = 1800
    year_scale = {1980: 0.0, 1990: 0.4, 2000: 0.8, 2010: 1.1, 2019: 1.3}
    college_share = {1980: 0.28, 1990: 0.32, 2000: 0.37, 2010: 0.41, 2019: 0.44}
    occ_probs = {
        1980: [0.27, 0.48, 0.25],
        1990: [0.28, 0.43, 0.29],
        2000: [0.29, 0.38, 0.33],
        2010: [0.31, 0.33, 0.36],
        2019: [0.32, 0.29, 0.39],
    }
    region_effect = {"Northeast": 0.04, "Midwest": 0.01, "South": -0.04, "West": 0.03}
    occ_effect = {"low_service": -0.11, "middle_routine": 0.01, "high_abstract": 0.15}

    rows: list[pd.DataFrame] = []
    worker_start = 1

    for year in years:
        scale = year_scale[year]
        worker_id = np.arange(worker_start, worker_start + n_per_year)
        worker_start += n_per_year

        college = rng.binomial(1, college_share[year], n_per_year)
        female = rng.binomial(1, 0.47, n_per_year)
        experience = rng.integers(1, 41, n_per_year)
        region = rng.choice(["Northeast", "Midwest", "South", "West"], size=n_per_year, p=[0.19, 0.25, 0.35, 0.21])
        occupation = rng.choice(
            ["low_service", "middle_routine", "high_abstract"],
            size=n_per_year,
            p=occ_probs[year],
        )
        latent_skill = rng.normal(0.0, 1.0, n_per_year)
        college_premium = 0.20 + 0.17 * scale
        female_gap = -0.10 + 0.02 * scale
        routine_penalty = np.where(occupation == "middle_routine", -0.05 * scale, 0.0)
        high_task_premium = np.where(occupation == "high_abstract", 0.03 * scale, 0.0)
        residual_sigma = 0.18 + 0.04 * scale

        log_hourly_wage = (
            2.10
            + 0.05 * scale
            + college_premium * college
            + 0.020 * experience
            - 0.00028 * np.square(experience)
            + female_gap * female
            + np.array([region_effect[item] for item in region])
            + np.array([occ_effect[item] for item in occupation])
            + routine_penalty
            + high_task_premium
            + residual_sigma * latent_skill
        )
        hourly_wage = np.exp(log_hourly_wage)
        annual_hours = np.clip(
            rng.normal(
                1985
                - 22 * female
                - 40 * (occupation == "low_service").astype(float)
                - 20 * scale
                + 24 * college,
                170,
                n_per_year,
            ),
            950,
            2750,
        )
        annual_earnings = hourly_wage * annual_hours
        weight = rng.uniform(0.55, 2.1, n_per_year)

        rows.append(
            pd.DataFrame(
                {
                    "worker_id": worker_id,
                    "year": year,
                    "weight": weight,
                    "college": college,
                    "female": female,
                    "experience": experience,
                    "region": region,
                    "occupation_group": occupation,
                    "hourly_wage": hourly_wage,
                    "annual_hours": annual_hours,
                    "annual_earnings": annual_earnings,
                }
            )
        )

    df = pd.concat(rows, ignore_index=True)
    df["log_hourly_wage"] = np.log(df["hourly_wage"])
    df["log_annual_earnings"] = np.log(df["annual_earnings"])
    return df


def assign_firm(score: float, firm_scores: np.ndarray, rng: np.random.Generator) -> int:
    noise = rng.normal(0.0, 0.45, len(firm_scores))
    return int(np.argmax(-np.abs(firm_scores - score) + noise))


def build_worker_firm_panel(rng: np.random.Generator) -> pd.DataFrame:
    years = [2016, 2017, 2018, 2019]
    n_workers = 360
    n_firms = 18

    worker_effect = rng.normal(0.0, 0.22, n_workers)
    college = rng.binomial(1, 0.46, n_workers)
    female = rng.binomial(1, 0.46, n_workers)
    base_experience = rng.integers(3, 24, n_workers)

    firm_scores = np.linspace(-0.30, 0.30, n_firms) + rng.normal(0.0, 0.03, n_firms)
    amenity_value = 0.06 + 0.45 * firm_scores + rng.normal(0.0, 0.025, n_firms)

    current_firm = np.array(
        [assign_firm(worker_effect[i] + 0.08 * college[i], firm_scores, rng) for i in range(n_workers)]
    )

    rows: list[dict[str, float | int]] = []
    for year_idx, year in enumerate(years):
        if year_idx > 0:
            move_prob = 0.16 + 0.04 * (current_firm < np.median(current_firm))
            move_draw = rng.random(n_workers) < move_prob
            for i in np.where(move_draw)[0]:
                current_firm[i] = assign_firm(worker_effect[i] + 0.06 * college[i], firm_scores, rng)

        for i in range(n_workers):
            firm_id = int(current_firm[i])
            experience = base_experience[i] + year_idx
            firm_premium = firm_scores[firm_id]
            epsilon = rng.normal(0.0, 0.06)
            log_wage = (
                2.35
                + worker_effect[i]
                + firm_premium
                + 0.045 * college[i]
                - 0.055 * female[i]
                + 0.012 * experience
                + epsilon
            )
            total_job_value = log_wage + amenity_value[firm_id]
            rows.append(
                {
                    "worker_id": i + 1,
                    "year": year,
                    "firm_id": firm_id + 1,
                    "college": int(college[i]),
                    "female": int(female[i]),
                    "experience": int(experience),
                    "worker_effect_true": float(worker_effect[i]),
                    "firm_premium_true": float(firm_premium),
                    "amenity_value": float(amenity_value[firm_id]),
                    "log_wage": float(log_wage),
                    "total_job_value": float(total_job_value),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(20260503)
    repeated_cross_section = build_repeated_cross_section(rng)
    worker_firm_panel = build_worker_firm_panel(rng)

    repeated_cross_section.to_csv(
        ORIGINAL_DIR / "autor_katz_kearney_inequality_synthetic.csv",
        index=False,
    )
    worker_firm_panel.to_csv(
        TRANSFER_DIR / "worker_firm_inequality_synthetic.csv",
        index=False,
    )

    print(f"Wrote repeated-cross-section file to {ORIGINAL_DIR}")
    print(f"Wrote worker-firm panel file to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
