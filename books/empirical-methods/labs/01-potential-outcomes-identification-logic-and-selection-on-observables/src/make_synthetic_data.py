"""Create deterministic synthetic data for the Week 1 teaching lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def make_training_data() -> pd.DataFrame:
    rng = np.random.default_rng(1401)
    n = 160

    age = rng.integers(19, 56, n)
    education = rng.integers(8, 17, n)
    black = rng.binomial(1, 0.38, n)
    hispanic = rng.binomial(1, 0.12, n)
    married_prob = sigmoid(-0.7 + 0.05 * (age - 30) + 0.10 * (education - 12))
    married = rng.binomial(1, married_prob)
    nodegree = (education < 12).astype(int)

    earnings_1974 = (
        2500
        + 520 * education
        + 85 * age
        - 1500 * nodegree
        - 800 * black
        - 500 * hispanic
        + 900 * married
        + rng.normal(0, 2200, n)
    )
    earnings_1974 = np.maximum(0, earnings_1974)

    earnings_1975 = (
        0.62 * earnings_1974
        + 2100
        + 270 * education
        - 900 * nodegree
        + 550 * married
        + rng.normal(0, 1800, n)
    )
    earnings_1975 = np.maximum(0, earnings_1975)

    latent = (
        -0.95
        - 0.08 * (education - 12)
        + 0.35 * nodegree
        - 0.00008 * earnings_1975
        + 0.28 * black
        + 0.18 * hispanic
        - 0.20 * married
        + rng.normal(0, 0.50, n)
    )
    treatment_prob = np.clip(sigmoid(latent), 0.08, 0.78)
    treatment = rng.binomial(1, treatment_prob)

    earnings_1978 = (
        2800
        + 0.52 * earnings_1975
        + 390 * education
        + 55 * age
        - 1050 * nodegree
        - 620 * black
        - 280 * hispanic
        + 520 * married
        + 1750 * treatment
        + rng.normal(0, 2300, n)
    )
    earnings_1978 = np.maximum(0, earnings_1978)

    return pd.DataFrame(
        {
            "unit_id": np.arange(1, n + 1),
            "treat": treatment,
            "age": age,
            "education": education,
            "black": black,
            "hispanic": hispanic,
            "married": married,
            "nodegree": nodegree,
            "earnings_1974": earnings_1974.round(2),
            "earnings_1975": earnings_1975.round(2),
            "earnings_1978": earnings_1978.round(2),
        }
    )


def make_transfer_data() -> pd.DataFrame:
    rng = np.random.default_rng(2209)
    n = 120

    tenure = rng.uniform(0.2, 9.5, n)
    prior_wage = rng.normal(22.0 + 0.85 * tenure, 4.0, n)
    baseline_perf = np.clip(rng.normal(0.0, 1.0, n), -2.5, 2.5)
    high_skill = rng.binomial(1, sigmoid(-0.2 + 0.12 * (prior_wage - 24) + 0.45 * baseline_perf))
    supervisor_referral = rng.binomial(1, sigmoid(-0.35 + 0.65 * baseline_perf + 0.30 * high_skill))
    schedule_flex = rng.binomial(1, sigmoid(-0.10 + 0.25 * tenure - 0.20 * high_skill))
    distance_training = np.maximum(1.0, rng.normal(14.0 - 3.0 * schedule_flex, 5.0, n))

    latent = (
        -1.0
        + 0.42 * supervisor_referral
        + 0.35 * baseline_perf
        + 0.28 * high_skill
        + 0.12 * tenure
        - 0.035 * distance_training
        + rng.normal(0, 0.45, n)
    )
    training_prob = np.clip(sigmoid(latent), 0.07, 0.86)
    training = rng.binomial(1, training_prob)

    next_wage = (
        prior_wage
        + 0.34 * tenure
        + 1.15 * baseline_perf
        + 1.30 * high_skill
        + 0.55 * supervisor_referral
        + 1.75 * training
        + rng.normal(0, 2.1, n)
    )

    return pd.DataFrame(
        {
            "worker_id": np.arange(1, n + 1),
            "training": training,
            "prior_wage": prior_wage.round(2),
            "tenure": tenure.round(2),
            "baseline_perf": baseline_perf.round(3),
            "high_skill": high_skill,
            "supervisor_referral": supervisor_referral,
            "schedule_flex": schedule_flex,
            "distance_training": distance_training.round(2),
            "next_wage": next_wage.round(2),
        }
    )


def main() -> None:
    training_path = ROOT / "original" / "reduced" / "training_synthetic.csv"
    transfer_path = ROOT / "transfer" / "data" / "workplace_training_synthetic.csv"
    training_path.parent.mkdir(parents=True, exist_ok=True)
    transfer_path.parent.mkdir(parents=True, exist_ok=True)

    make_training_data().to_csv(training_path, index=False)
    make_transfer_data().to_csv(transfer_path, index=False)

    print(f"Wrote {training_path}")
    print(f"Wrote {transfer_path}")


if __name__ == "__main__":
    main()
