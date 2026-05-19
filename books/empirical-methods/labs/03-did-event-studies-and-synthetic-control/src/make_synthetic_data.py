"""Create deterministic synthetic data for the Week 3 teaching lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def make_card_krueger_like_data() -> pd.DataFrame:
    rng = np.random.default_rng(3303)
    chains = np.array(["Burger Barn", "Chicken House", "Pizza Port", "Taco Tower"])
    chain_effects = {
        "Burger Barn": 1.2,
        "Chicken House": -0.4,
        "Pizza Port": 0.3,
        "Taco Tower": -0.8,
    }
    rows = []
    restaurant_id = 1

    for state, n_state in [("NJ", 92), ("PA", 74)]:
        treated_state = int(state == "NJ")
        for _ in range(n_state):
            chain = str(rng.choice(chains))
            highway = int(rng.binomial(1, 0.38 if state == "NJ" else 0.34))
            store_quality = rng.normal(0.0, 2.7)
            baseline_wage = rng.normal(4.42 if state == "NJ" else 4.36, 0.14)
            unit_base = 22.5 + chain_effects[chain] + 1.4 * highway + store_quality

            for post in [0, 1]:
                common_trend = -0.85 * post
                state_untreated_trend = -0.10 * post if state == "NJ" else -0.30 * post
                treatment_effect = 2.10 * treated_state * post
                noise = rng.normal(0.0, 1.35)
                fte = unit_base + common_trend + state_untreated_trend + treatment_effect + noise
                wage = baseline_wage + treated_state * post * 0.70 + (1 - treated_state) * post * 0.05

                rows.append(
                    {
                        "restaurant_id": restaurant_id,
                        "state": state,
                        "period": "post" if post else "pre",
                        "post": post,
                        "treated_state": treated_state,
                        "treated_post": treated_state * post,
                        "chain": chain,
                        "highway": highway,
                        "starting_wage": round(float(wage), 2),
                        "fte_employment": round(float(max(fte, 4.0)), 3),
                    }
                )
            restaurant_id += 1

    return pd.DataFrame(rows)


def make_staggered_panel() -> pd.DataFrame:
    rng = np.random.default_rng(4107)
    years = np.arange(2010, 2020)
    cohorts = np.array([2013, 2015, 2017, 9999])
    cohort_probs = np.array([0.22, 0.28, 0.25, 0.25])
    regions = np.array(["North", "South", "Central", "Coastal"])
    rows = []

    for county_id in range(1, 73):
        adoption_year = int(rng.choice(cohorts, p=cohort_probs))
        region = str(rng.choice(regions))
        county_fe = rng.normal(0.0, 3.2)
        baseline_trend = rng.normal(0.04, 0.05)
        region_shift = {"North": 0.35, "South": -0.20, "Central": 0.05, "Coastal": 0.18}[region]
        cohort_shift = {2013: -0.25, 2015: 0.10, 2017: 0.05, 9999: 0.0}[adoption_year]

        for year in years:
            year_index = year - years[0]
            treated = int(year >= adoption_year)
            event_time = year - adoption_year if adoption_year < 9999 else -999
            common_year = 0.45 * year_index + 0.18 * np.sin(year_index / 1.7)
            untreated = 58.0 + county_fe + region_shift + cohort_shift + common_year + baseline_trend * year_index

            if treated:
                dynamic = 0.45 + 0.32 * max(event_time, 0)
                cohort_heterogeneity = {2013: 1.15, 2015: 0.62, 2017: 0.25}[adoption_year]
                effect = dynamic + cohort_heterogeneity
            else:
                effect = 0.0

            outcome = untreated + effect + rng.normal(0.0, 0.75)
            rows.append(
                {
                    "county_id": county_id,
                    "region": region,
                    "year": int(year),
                    "adoption_year": adoption_year,
                    "ever_treated": int(adoption_year < 9999),
                    "treated": treated,
                    "event_time": int(event_time),
                    "employment_index": round(float(outcome), 3),
                }
            )

    return pd.DataFrame(rows)


def make_synthetic_control_data() -> pd.DataFrame:
    rng = np.random.default_rng(5179)
    years = np.arange(2010, 2020)
    donor_cities = ["River City", "Lake City", "Hill City", "Port City", "Prairie City"]
    donor_params = {
        "River City": (48.5, 0.70, 0.35),
        "Lake City": (46.8, 0.82, -0.12),
        "Hill City": (50.4, 0.55, 0.18),
        "Port City": (47.6, 0.76, 0.42),
        "Prairie City": (45.9, 0.92, -0.20),
    }
    donor_paths: dict[str, list[float]] = {}

    for city, (level, trend, cycle) in donor_params.items():
        values = []
        for year in years:
            t = year - years[0]
            values.append(level + trend * t + cycle * np.sin(t / 1.8) + rng.normal(0.0, 0.20))
        donor_paths[city] = values

    true_weights = {
        "River City": 0.42,
        "Lake City": 0.26,
        "Hill City": 0.18,
        "Port City": 0.10,
        "Prairie City": 0.04,
    }
    treated_path = []
    for idx, year in enumerate(years):
        untreated = sum(true_weights[city] * donor_paths[city][idx] for city in donor_cities)
        treatment_effect = 0.0 if year <= 2015 else 1.1 + 0.42 * (year - 2016)
        treated_path.append(untreated + treatment_effect + rng.normal(0.0, 0.18))

    rows = []
    for city in ["Bay City"] + donor_cities:
        for idx, year in enumerate(years):
            treated_city = int(city == "Bay City")
            value = treated_path[idx] if treated_city else donor_paths[city][idx]
            rows.append(
                {
                    "city": city,
                    "year": int(year),
                    "treated_city": treated_city,
                    "post": int(year >= 2016),
                    "placement_index": round(float(value), 3),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    card_path = ROOT / "original" / "reduced" / "card_krueger_synthetic.csv"
    staggered_path = ROOT / "original" / "reduced" / "staggered_minimum_wage_synthetic.csv"
    transfer_path = ROOT / "transfer" / "data" / "synthetic_control_city.csv"

    card_path.parent.mkdir(parents=True, exist_ok=True)
    staggered_path.parent.mkdir(parents=True, exist_ok=True)
    transfer_path.parent.mkdir(parents=True, exist_ok=True)

    make_card_krueger_like_data().to_csv(card_path, index=False)
    make_staggered_panel().to_csv(staggered_path, index=False)
    make_synthetic_control_data().to_csv(transfer_path, index=False)

    print(f"Wrote {card_path}")
    print(f"Wrote {staggered_path}")
    print(f"Wrote {transfer_path}")


if __name__ == "__main__":
    main()
