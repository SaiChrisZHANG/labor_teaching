"""Create deterministic synthetic data for the Week 4 IV teaching lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def make_compulsory_schooling_data() -> pd.DataFrame:
    rng = np.random.default_rng(4404)
    n = 8000
    states = np.array(["North", "South", "Central", "Coastal"])
    state = rng.choice(states, size=n, p=[0.26, 0.25, 0.27, 0.22])
    birth_year = rng.integers(1930, 1948, size=n)
    birth_quarter = rng.integers(1, 5, size=n)
    female = rng.binomial(1, 0.49, size=n)
    parent_education = np.clip(rng.normal(11.6, 2.1, size=n), 6.0, 18.0)
    family_income = np.clip(rng.normal(42_000, 13_000, size=n), 12_000, 95_000)

    state_effect = {
        "North": 0.04,
        "South": -0.03,
        "Central": 0.00,
        "Coastal": 0.06,
    }
    state_schooling_effect = {
        "North": 0.03,
        "South": -0.04,
        "Central": 0.00,
        "Coastal": 0.05,
    }

    ability = (
        rng.normal(0.0, 1.0, size=n)
        + 0.13 * (parent_education - parent_education.mean())
        + 0.000006 * (family_income - family_income.mean())
    )
    complier_score = (
        0.50 * ability
        + 0.10 * (parent_education - 12.0)
        + 0.000010 * (family_income - 42_000)
        + rng.normal(0.0, 1.0, size=n)
    )
    compliance_type = np.where(
        complier_score > 0.80,
        "always_taker",
        np.where(complier_score < -0.70, "never_taker", "complier"),
    )

    # Synthetic rule exposure: students born late in the school-entry cycle face
    # a binding compulsory-schooling margin in the stylized data.
    compulsory_exposure = (birth_quarter >= 3).astype(int)
    d0 = (compliance_type == "always_taker").astype(int)
    d1 = np.isin(compliance_type, ["always_taker", "complier"]).astype(int)
    stayed_in_school = np.where(compulsory_exposure == 1, d1, d0)

    years_schooling = (
        10.4
        + 1.35 * stayed_in_school
        + 0.22 * (compliance_type == "always_taker")
        + 0.28 * ability
        + 0.06 * (parent_education - 12.0)
        + np.vectorize(state_schooling_effect.get)(state)
        + rng.normal(0.0, 0.38, size=n)
    )

    true_treatment_effect = (
        0.062
        + 0.026 * (compliance_type == "complier")
        + 0.010 * (parent_education < 11.0)
        - 0.006 * female
    )
    untreated_log_earnings = (
        2.00
        + 0.170 * ability
        + 0.024 * parent_education
        + 0.0000035 * family_income
        + 0.004 * (birth_year - 1930)
        - 0.035 * female
        + np.vectorize(state_effect.get)(state)
        + rng.normal(0.0, 0.105, size=n)
    )
    log_earnings = untreated_log_earnings + true_treatment_effect * stayed_in_school

    return pd.DataFrame(
        {
            "person_id": np.arange(1, n + 1),
            "state": state,
            "birth_year": birth_year,
            "birth_quarter": birth_quarter,
            "female": female,
            "parent_education": np.round(parent_education, 3),
            "family_income": np.round(family_income, 2),
            "compulsory_exposure": compulsory_exposure,
            "stayed_in_school": stayed_in_school,
            "years_schooling": np.round(years_schooling, 3),
            "log_earnings": np.round(log_earnings, 4),
            "synthetic_ability": np.round(ability, 4),
            "synthetic_compliance_type": compliance_type,
            "synthetic_true_effect": np.round(true_treatment_effect, 4),
        }
    )


def make_shift_share_places() -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(5528)
    sectors = ["manufacturing", "health", "logistics", "education", "energy", "services"]
    shocks = pd.DataFrame(
        {
            "sector": sectors,
            "shock": [0.085, 0.032, 0.064, 0.018, -0.041, 0.027],
            "shock_note": [
                "tradable-sector demand shock",
                "health demand growth",
                "transport automation shock",
                "public-sector enrollment shock",
                "energy price reversal",
                "local-services demand shock",
            ],
        }
    )

    regions = ["North", "South", "Central", "Coastal"]
    rows = []
    alpha_by_region = {
        "North": np.array([3.6, 1.4, 1.6, 1.1, 0.9, 2.0]),
        "South": np.array([1.4, 1.3, 2.5, 1.0, 2.0, 1.8]),
        "Central": np.array([2.5, 1.5, 1.7, 1.4, 1.2, 2.2]),
        "Coastal": np.array([1.2, 2.1, 1.8, 1.6, 0.7, 2.7]),
    }

    shock_vector = shocks["shock"].to_numpy(dtype=float)
    for place_id in range(1, 73):
        region = regions[(place_id - 1) % len(regions)]
        shares = rng.dirichlet(alpha_by_region[region])
        shift_share = float(shares @ shock_vector)
        manufacturing_share = float(shares[0])
        energy_share = float(shares[4])
        baseline_growth = (
            0.012
            + 0.055 * manufacturing_share
            - 0.030 * energy_share
            + rng.normal(0.0, 0.010)
        )
        treatment_intensity = (
            0.22
            + 2.85 * shift_share
            + 0.70 * baseline_growth
            + rng.normal(0.0, 0.030)
        )
        direct_shock_channel = 0.30 * energy_share * shocks.loc[shocks["sector"] == "energy", "shock"].iloc[0]
        outcome_growth = (
            0.018
            - 0.42 * treatment_intensity
            + 0.82 * baseline_growth
            + direct_shock_channel
            + rng.normal(0.0, 0.025)
        )
        row = {
            "place_id": place_id,
            "region": region,
            "baseline_growth": round(float(baseline_growth), 5),
            "treatment_intensity": round(float(treatment_intensity), 5),
            "outcome_growth": round(float(outcome_growth), 5),
        }
        for sector, share in zip(sectors, shares):
            row[f"share_{sector}"] = round(float(share), 6)
        rows.append(row)

    return pd.DataFrame(rows), shocks


def main() -> None:
    schooling_path = ROOT / "original" / "reduced" / "compulsory_schooling_synthetic.csv"
    places_path = ROOT / "transfer" / "data" / "shift_share_places.csv"
    shocks_path = ROOT / "transfer" / "data" / "sector_shocks.csv"

    schooling_path.parent.mkdir(parents=True, exist_ok=True)
    places_path.parent.mkdir(parents=True, exist_ok=True)
    shocks_path.parent.mkdir(parents=True, exist_ok=True)

    make_compulsory_schooling_data().to_csv(schooling_path, index=False)
    places, shocks = make_shift_share_places()
    places.to_csv(places_path, index=False)
    shocks.to_csv(shocks_path, index=False)

    print(f"Wrote {schooling_path}")
    print(f"Wrote {places_path}")
    print(f"Wrote {shocks_path}")


if __name__ == "__main__":
    main()
