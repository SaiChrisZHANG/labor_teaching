#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for the Week 11 worker-policy lab."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"


def logistic(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-values))


def build_knowledge_panel(rng: np.random.Generator) -> pd.DataFrame:
    years = list(range(1998, 2005))
    expansion_year = 2001
    neighborhoods = [f"tract_{idx:02d}" for idx in range(1, 37)]
    rows: list[dict[str, float | int | str]] = []

    knowledge_index = rng.uniform(0.18, 0.92, len(neighborhoods))
    baseline_single_parent_share = rng.uniform(0.10, 0.42, len(neighborhoods))
    filing_support_rate = rng.uniform(0.08, 0.58, len(neighborhoods))
    labor_demand_trend = rng.normal(0.0, 0.06, len(neighborhoods))
    region = rng.choice(["North", "Midwest", "South", "West"], len(neighborhoods))

    for idx, neighborhood in enumerate(neighborhoods):
        for year in years:
            post = int(year >= expansion_year)
            year_offset = year - years[0]
            trend = 0.011 * year_offset
            effective_exposure = knowledge_index[idx] * filing_support_rate[idx] * baseline_single_parent_share[idx]

            employment_rate = (
                0.56
                + 0.012 * year_offset
                + 0.045 * post * effective_exposure
                + 0.020 * filing_support_rate[idx]
                + 0.5 * labor_demand_trend[idx]
                + rng.normal(0.0, 0.012)
            )
            mean_earnings = (
                16.5
                + 0.55 * year_offset
                + 5.8 * post * effective_exposure
                + 1.3 * filing_support_rate[idx]
                + 2.2 * labor_demand_trend[idx]
                + rng.normal(0.0, 0.35)
            )
            takeup_rate = logistic(
                np.array(
                    [
                        -0.75
                        + 1.55 * knowledge_index[idx]
                        + 0.90 * filing_support_rate[idx]
                        + 0.70 * post
                        + 0.55 * baseline_single_parent_share[idx]
                    ]
                )
            )[0]
            rows.append(
                {
                    "neighborhood": neighborhood,
                    "region": region[idx],
                    "year": year,
                    "post": post,
                    "knowledge_index": knowledge_index[idx],
                    "single_parent_share": baseline_single_parent_share[idx],
                    "filing_support_rate": filing_support_rate[idx],
                    "effective_exposure": effective_exposure,
                    "employment_rate": employment_rate,
                    "mean_earnings_k": mean_earnings,
                    "takeup_rate": takeup_rate,
                }
            )

    df = pd.DataFrame(rows)
    df["knowledge_quartile"] = pd.qcut(
        df["knowledge_index"],
        4,
        labels=["Q1 low", "Q2", "Q3", "Q4 high"],
    )
    return df


def build_takeup_experiment(rng: np.random.Generator) -> pd.DataFrame:
    n = 2400
    treatment = rng.choice(
        ["control", "reminder_letter", "simplified_notice"],
        size=n,
        p=[0.34, 0.33, 0.33],
    )
    burden = rng.choice(["low", "medium", "high"], size=n, p=[0.28, 0.40, 0.32])
    prior_filer = rng.binomial(1, 0.57, n)
    eligible_credit_k = np.clip(rng.normal(2.1, 0.75, n), 0.4, None)
    wage_income_k = np.clip(rng.normal(17.5, 5.0, n), 2.0, None)

    burden_effect = {"low": 0.20, "medium": 0.00, "high": -0.26}
    treatment_effect = {
        "control": 0.00,
        "reminder_letter": 0.16,
        "simplified_notice": 0.30,
    }
    interaction_effect = {
        "control": 0.00,
        "reminder_letter": 0.06,
        "simplified_notice": 0.13,
    }

    burden_component = np.array([burden_effect[item] for item in burden])
    treat_component = np.array([treatment_effect[item] for item in treatment])
    interact_component = np.array([interaction_effect[item] for item in treatment])
    high_burden = (burden == "high").astype(int)

    latent = (
        -0.82
        + 0.32 * prior_filer
        + 0.22 * eligible_credit_k
        - 0.025 * wage_income_k
        + burden_component
        + treat_component
        + high_burden * interact_component
    )
    take_up = (rng.random(n) < logistic(latent)).astype(int)
    completed_filing = (
        rng.random(n)
        < logistic(
            latent
            + 0.12 * prior_filer
            + 0.18 * (treatment == "simplified_notice").astype(int)
        )
    ).astype(int)

    benefit_received_k = take_up * np.clip(eligible_credit_k + rng.normal(0.0, 0.18, n), 0.0, None)

    df = pd.DataFrame(
        {
            "claimant_id": np.arange(1, n + 1),
            "treatment_arm": treatment,
            "burden_group": burden,
            "prior_filer": prior_filer,
            "eligible_credit_k": eligible_credit_k,
            "wage_income_k": wage_income_k,
            "take_up": take_up,
            "completed_filing": completed_filing,
            "benefit_received_k": benefit_received_k,
        }
    )
    return df


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(20260511)
    knowledge_df = build_knowledge_panel(rng)
    takeup_df = build_takeup_experiment(rng)

    knowledge_df.to_csv(
        ORIGINAL_DIR / "chetty_friedman_saez_knowledge_synthetic.csv",
        index=False,
    )
    takeup_df.to_csv(
        TRANSFER_DIR / "linos_eitc_nudge_synthetic.csv",
        index=False,
    )

    print(f"Wrote Week 11 knowledge panel to {ORIGINAL_DIR}")
    print(f"Wrote Week 11 nudge experiment to {TRANSFER_DIR}")


if __name__ == "__main__":
    main()
