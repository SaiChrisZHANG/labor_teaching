"""Create deterministic synthetic data for the Week 11 policy-learning lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from policy_learning_utils import sigmoid


ROOT = Path(__file__).resolve().parents[1]

REGIONS = ["central_city", "suburban", "rural"]
GROUPS = ["group_a", "group_b"]


def make_population(n: int, seed: int, population: str) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    is_target = population == "target"
    region_prob = [0.46, 0.34, 0.20] if not is_target else [0.24, 0.28, 0.48]
    group_prob = [0.54, 0.46] if not is_target else [0.43, 0.57]
    rows: list[dict[str, object]] = []
    region_shift = {"central_city": 2400.0, "suburban": 900.0, "rural": -1600.0}
    unemployment_shift = {"central_city": 0.00, "suburban": -0.01, "rural": 0.025}

    for applicant_id in range(1, n + 1):
        region = str(rng.choice(REGIONS, p=region_prob))
        demographic_group = str(rng.choice(GROUPS, p=group_prob))
        age = int(np.clip(rng.normal(34 if not is_target else 37, 8), 19, 58))
        education_years = float(
            np.clip(
                rng.normal(13.8 if not is_target else 12.9, 1.8)
                - 0.25 * (demographic_group == "group_b")
                - 0.35 * (region == "rural"),
                9.0,
                18.5,
            )
        )
        months_unemployed = float(
            np.clip(
                rng.gamma(2.0 if not is_target else 2.4, 2.4)
                + 1.2 * (region == "rural")
                + 0.5 * (demographic_group == "group_b"),
                0.0,
                18.0,
            )
        )
        digital_skill = float(
            np.clip(
                rng.normal(0.12 if not is_target else -0.18, 0.85)
                + 0.20 * (education_years - 13.0)
                - 0.35 * (region == "rural"),
                -2.6,
                2.8,
            )
        )
        local_unemployment = float(
            np.clip(
                rng.normal(0.075 + unemployment_shift[region] + (0.018 if is_target else 0.0), 0.016),
                0.025,
                0.16,
            )
        )
        prior_earnings = float(
            np.clip(
                7000.0
                + 1750.0 * education_years
                + 2800.0 * digital_skill
                - 580.0 * months_unemployed
                + region_shift[region]
                - 650.0 * (demographic_group == "group_b")
                + rng.normal(0.0, 3600.0),
                6000.0,
                72000.0,
            )
        )
        risk_index = (
            -0.45
            + 0.135 * months_unemployed
            - 0.000035 * prior_earnings
            - 0.46 * digital_skill
            + 3.8 * local_unemployment
            + 0.18 * (demographic_group == "group_b")
            + 0.12 * (region == "rural")
        )
        baseline_risk = float(sigmoid(np.array([risk_index]))[0])
        treatment_cost = float(
            1450.0
            + 450.0 * (region == "rural")
            + 220.0 * (months_unemployed > 9.0)
            + rng.normal(0.0, 80.0)
        )
        implementation_quality = 1.0 if not is_target else 0.72 - 0.06 * (region == "rural")
        true_effect = float(
            implementation_quality
            * (
                950.0
                + 5200.0 * baseline_risk
                + 900.0 * (months_unemployed > 8.0)
                + 650.0 * (digital_skill < -0.35)
                - 950.0 * (digital_skill > 1.1)
                - 420.0 * (education_years > 15.5)
            )
        )
        true_y0 = float(
            10400.0
            + 1900.0 * education_years
            + 3100.0 * digital_skill
            - 720.0 * months_unemployed
            - 24000.0 * local_unemployment
            + region_shift[region]
            - 700.0 * (demographic_group == "group_b")
            + rng.normal(0.0, 4200.0)
        )
        true_y1 = true_y0 + true_effect
        prop_index = (
            -0.30
            + 1.15 * baseline_risk
            - 0.18 * digital_skill
            + 0.22 * (region == "central_city")
            + 0.14 * (demographic_group == "group_b")
            - 0.12 * is_target
        )
        propensity_true = float(np.clip(sigmoid(np.array([prop_index]))[0], 0.08, 0.92))
        training_offer = int(rng.binomial(1, propensity_true))
        earnings_12mo = true_y1 if training_offer else true_y0
        rows.append(
            {
                "applicant_id": applicant_id,
                "population": population,
                "region": region,
                "demographic_group": demographic_group,
                "age": age,
                "education_years": education_years,
                "months_unemployed": months_unemployed,
                "prior_earnings": prior_earnings,
                "digital_skill": digital_skill,
                "local_unemployment": local_unemployment,
                "baseline_risk": baseline_risk,
                "training_cost": treatment_cost,
                "propensity_true": propensity_true,
                "training_offer": training_offer,
                "true_y0": true_y0,
                "true_y1": true_y1,
                "true_effect": true_effect,
                "true_net_effect": true_effect - treatment_cost,
                "earnings_12mo": earnings_12mo,
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    source_path = ROOT / "original" / "reduced" / "job_training_policy_synthetic.csv"
    target_path = ROOT / "transfer" / "data" / "job_training_target_synthetic.csv"
    source_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    make_population(900, 11101, "source").to_csv(source_path, index=False)
    make_population(700, 11117, "target").to_csv(target_path, index=False)
    print(f"Wrote {source_path}")
    print(f"Wrote {target_path}")


if __name__ == "__main__":
    main()
