"""Create deterministic synthetic data for the Week 10 DML and heterogeneity lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


REGIONS = ["Northeast", "Midwest", "South", "West"]
OCCUPATIONS = ["software", "design", "admin", "data", "operations", "writing"]
NEIGHBORHOODS = ["central", "inner_ring", "outer_ring", "suburban"]


def sigmoid(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-values))


def make_online_labor_data() -> pd.DataFrame:
    rng = np.random.default_rng(10101)
    n = 420
    rows: list[dict[str, object]] = []
    occupation_shift = {
        "software": 0.23,
        "design": 0.08,
        "admin": -0.16,
        "data": 0.18,
        "operations": -0.05,
        "writing": -0.03,
    }
    region_shift = {"Northeast": 0.05, "Midwest": -0.03, "South": -0.05, "West": 0.08}

    for worker_id in range(1, n + 1):
        region = str(rng.choice(REGIONS, p=[0.24, 0.22, 0.30, 0.24]))
        occupation = str(rng.choice(OCCUPATIONS, p=[0.18, 0.15, 0.18, 0.18, 0.16, 0.15]))
        experience_years = float(rng.gamma(shape=2.3, scale=2.0))
        completed_tasks = int(rng.poisson(18 + 2.5 * experience_years))
        rating = float(np.clip(rng.normal(4.45 + 0.03 * experience_years, 0.28), 3.0, 5.0))
        prior_log_wage = float(
            2.55
            + 0.045 * experience_years
            + 0.11 * rating
            + occupation_shift[occupation]
            + region_shift[region]
            + rng.normal(0.0, 0.18)
        )
        market_thickness = float(np.clip(rng.normal(0.55 + 0.06 * (occupation in ["software", "data"]), 0.18), 0.08, 0.96))
        local_unemployment = float(np.clip(rng.normal(0.06 + 0.025 * (region == "South"), 0.018), 0.025, 0.13))
        skill_score = float(np.clip(rng.normal(0.0, 1.0) + 0.18 * experience_years + occupation_shift[occupation], -2.2, 3.2))
        repeat_client_share = float(np.clip(rng.beta(2.2, 4.0) + 0.08 * (occupation in ["admin", "writing"]), 0.02, 0.92))
        logit_treat = (
            -0.15
            + 1.6 * repeat_client_share
            - 1.15 * market_thickness
            - 0.22 * skill_score
            + 2.4 * local_unemployment
            + 0.28 * (occupation == "admin")
            - 0.18 * (occupation == "software")
            + rng.normal(0.0, 0.40)
        )
        treatment_probability = float(sigmoid(np.array([logit_treat]))[0])
        high_client_concentration = int(rng.binomial(1, treatment_probability))
        true_effect = -0.095 - 0.025 * (market_thickness < 0.38) + 0.018 * (skill_score > 1.0)
        log_hourly_wage = float(
            2.70
            + true_effect * high_client_concentration
            + 0.54 * prior_log_wage
            + 0.035 * experience_years
            + 0.045 * np.log1p(completed_tasks)
            + 0.10 * rating
            + 0.16 * skill_score
            - 0.58 * local_unemployment
            + 0.10 * market_thickness
            + occupation_shift[occupation]
            + region_shift[region]
            + rng.normal(0.0, 0.18)
        )
        future_client_rating = float(
            np.clip(
                rating
                - 0.09 * high_client_concentration
                + 0.04 * (log_hourly_wage - prior_log_wage)
                + rng.normal(0.0, 0.08),
                2.8,
                5.0,
            )
        )
        rows.append(
            {
                "worker_id": worker_id,
                "region": region,
                "occupation": occupation,
                "experience_years": experience_years,
                "completed_tasks": completed_tasks,
                "rating": rating,
                "prior_log_wage": prior_log_wage,
                "market_thickness": market_thickness,
                "local_unemployment": local_unemployment,
                "skill_score": skill_score,
                "repeat_client_share": repeat_client_share,
                "high_client_concentration": high_client_concentration,
                "treatment_probability_true": treatment_probability,
                "true_effect": true_effect,
                "log_hourly_wage": log_hourly_wage,
                "future_client_rating": future_client_rating,
            }
        )

    return pd.DataFrame(rows)


def make_youth_program_data() -> pd.DataFrame:
    rng = np.random.default_rng(10117)
    n = 900
    rows: list[dict[str, object]] = []
    neighborhood_shift = {"central": 0.07, "inner_ring": 0.03, "outer_ring": -0.03, "suburban": -0.07}

    for applicant_id in range(1, n + 1):
        neighborhood = str(rng.choice(NEIGHBORHOODS, p=[0.25, 0.30, 0.25, 0.20]))
        age = int(rng.choice([16, 17, 18, 19, 20], p=[0.16, 0.23, 0.25, 0.22, 0.14]))
        prior_work_months = float(np.clip(rng.gamma(1.6, 2.0) - 0.5, 0.0, 14.0))
        school_enrolled = int(rng.binomial(1, 0.70 - 0.05 * (age >= 19)))
        neighborhood_unemployment = float(
            np.clip(rng.normal(0.12 + neighborhood_shift[neighborhood], 0.025), 0.045, 0.22)
        )
        baseline_risk = float(
            np.clip(
                0.42
                + 1.35 * neighborhood_unemployment
                - 0.035 * prior_work_months
                - 0.06 * school_enrolled
                + rng.normal(0.0, 0.16),
                0.02,
                0.96,
            )
        )
        offer_probability = float(
            sigmoid(
                np.array(
                    [
                        -0.15
                        + 0.95 * baseline_risk
                        - 0.18 * school_enrolled
                        + 0.07 * (neighborhood == "central")
                        + rng.normal(0.0, 0.22)
                    ]
                )
            )[0]
        )
        program_offer = int(rng.binomial(1, offer_probability))
        treatment_logit_effect = 0.80 + 1.20 * baseline_risk - 0.10 * (prior_work_months > 7)
        untreated_logit = (
            -0.55
            - 0.95 * baseline_risk
            + 0.10 * prior_work_months
            + 0.16 * school_enrolled
            - 0.80 * neighborhood_unemployment
            + rng.normal(0.0, 0.12)
        )
        untreated_probability = float(sigmoid(np.array([untreated_logit]))[0])
        treated_probability = float(sigmoid(np.array([untreated_logit + treatment_logit_effect]))[0])
        true_cate = treated_probability - untreated_probability
        employment_probability = treated_probability if program_offer else untreated_probability
        summer_employed = int(rng.binomial(1, employment_probability))
        rows.append(
            {
                "applicant_id": applicant_id,
                "neighborhood": neighborhood,
                "age": age,
                "prior_work_months": prior_work_months,
                "school_enrolled": school_enrolled,
                "neighborhood_unemployment": neighborhood_unemployment,
                "baseline_risk": baseline_risk,
                "program_offer": program_offer,
                "offer_probability_true": offer_probability,
                "treatment_logit_effect": treatment_logit_effect,
                "true_cate": true_cate,
                "summer_employed": summer_employed,
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    online_path = ROOT / "original" / "reduced" / "online_labor_synthetic.csv"
    youth_path = ROOT / "transfer" / "data" / "youth_program_synthetic.csv"
    online_path.parent.mkdir(parents=True, exist_ok=True)
    youth_path.parent.mkdir(parents=True, exist_ok=True)
    make_online_labor_data().to_csv(online_path, index=False)
    make_youth_program_data().to_csv(youth_path, index=False)
    print(f"Wrote {online_path}")
    print(f"Wrote {youth_path}")


if __name__ == "__main__":
    main()
