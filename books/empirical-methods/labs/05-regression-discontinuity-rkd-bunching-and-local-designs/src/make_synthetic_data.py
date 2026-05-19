"""Create deterministic synthetic data for the Week 5 local-design lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def make_close_election_data() -> pd.DataFrame:
    rng = np.random.default_rng(5505)
    n = 6000
    districts = np.array(["North", "South", "Central", "Coastal", "Mountain"])
    district_group = rng.choice(districts, size=n, p=[0.22, 0.23, 0.21, 0.20, 0.14])
    election_year = rng.choice(np.arange(1992, 2013, 2), size=n)

    raw_margin = rng.normal(0.0, 0.24, size=n)
    close_draw = rng.normal(0.0, 0.065, size=n)
    close_indicator = rng.binomial(1, 0.45, size=n)
    vote_margin = np.where(close_indicator == 1, close_draw, raw_margin)
    vote_margin = np.clip(vote_margin, -0.65, 0.65)
    won_seat = (vote_margin >= 0).astype(int)

    district_income = (
        58_000
        + 9_000 * (district_group == "Coastal")
        - 6_500 * (district_group == "South")
        + rng.normal(0.0, 7_500, size=n)
    )
    pre_turnout = np.clip(
        0.54
        + 0.035 * (district_group == "North")
        - 0.025 * (district_group == "South")
        + 0.04 * vote_margin
        + rng.normal(0.0, 0.045, size=n),
        0.30,
        0.83,
    )
    party_strength = np.clip(
        0.50
        + 0.28 * vote_margin
        + 0.06 * (district_group == "Coastal")
        - 0.04 * (district_group == "Mountain")
        + rng.normal(0.0, 0.07, size=n),
        0.15,
        0.86,
    )
    candidate_quality = rng.normal(0.0, 1.0, size=n) + 0.35 * vote_margin

    true_incumbency_effect = (
        0.055
        + 0.010 * (np.abs(vote_margin) <= 0.05)
        + 0.006 * (district_group == "South")
    )
    next_vote_share = (
        0.485
        + 0.22 * vote_margin
        - 0.10 * vote_margin**2
        + true_incumbency_effect * won_seat
        + 0.070 * (party_strength - 0.50)
        + 0.090 * (pre_turnout - 0.54)
        + 0.009 * candidate_quality
        + rng.normal(0.0, 0.055, size=n)
    )
    next_vote_share = np.clip(next_vote_share, 0.05, 0.95)

    return pd.DataFrame(
        {
            "race_id": np.arange(1, n + 1),
            "district_group": district_group,
            "election_year": election_year,
            "vote_margin": np.round(vote_margin, 5),
            "won_seat": won_seat,
            "next_vote_share": np.round(next_vote_share, 5),
            "pre_turnout": np.round(pre_turnout, 5),
            "party_strength": np.round(party_strength, 5),
            "district_income": np.round(district_income, 2),
            "synthetic_candidate_quality": np.round(candidate_quality, 5),
            "synthetic_true_effect": np.round(true_incumbency_effect, 5),
        }
    )


def make_tax_kink_data() -> pd.DataFrame:
    rng = np.random.default_rng(5515)
    n = 42000
    kink = 50_000.0
    lower_tax = 0.25
    upper_tax = 0.35

    ability = rng.normal(0.0, 1.0, size=n)
    counterfactual_earnings = np.exp(rng.normal(np.log(49_500), 0.27, size=n))
    counterfactual_earnings *= np.exp(0.055 * ability)
    counterfactual_earnings = np.clip(counterfactual_earnings, 20_000, 95_000)

    distance_above = counterfactual_earnings - kink
    response_zone = (distance_above > 0) & (distance_above < 8_500)
    response_probability = np.zeros(n)
    response_probability[response_zone] = np.clip(
        0.88 - distance_above[response_zone] / 10_000,
        0.08,
        0.88,
    )
    buncher = rng.binomial(1, response_probability).astype(bool)

    observed_earnings = counterfactual_earnings.copy()
    observed_earnings[buncher] = kink - np.abs(rng.normal(420, 360, size=buncher.sum()))
    observed_earnings += rng.normal(0.0, 160, size=n)
    observed_earnings = np.clip(observed_earnings, 20_000, 95_000)

    return pd.DataFrame(
        {
            "earner_id": np.arange(1, n + 1),
            "observed_earnings": np.round(observed_earnings, 2),
            "counterfactual_earnings_synthetic": np.round(counterfactual_earnings, 2),
            "tax_kink": kink,
            "lower_marginal_tax_rate": lower_tax,
            "upper_marginal_tax_rate": upper_tax,
            "synthetic_buncher": buncher.astype(int),
        }
    )


def main() -> None:
    close_path = ROOT / "original" / "reduced" / "close_election_synthetic.csv"
    bunching_path = ROOT / "transfer" / "data" / "tax_kink_bunching_synthetic.csv"

    close_path.parent.mkdir(parents=True, exist_ok=True)
    bunching_path.parent.mkdir(parents=True, exist_ok=True)

    make_close_election_data().to_csv(close_path, index=False)
    make_tax_kink_data().to_csv(bunching_path, index=False)

    print(f"Wrote {close_path}")
    print(f"Wrote {bunching_path}")


if __name__ == "__main__":
    main()
