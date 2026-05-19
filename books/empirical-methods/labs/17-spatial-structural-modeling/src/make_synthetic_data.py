"""Create deterministic synthetic data for the Week 17 spatial structural lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from spatial_model import solve_static_equilibrium


ROOT = Path(__file__).resolve().parents[1]


def make_locations() -> pd.DataFrame:
    rng = np.random.default_rng(1717)
    names = [
        "Harbor Core",
        "North Rail",
        "River Plant",
        "Mesa Tech",
        "South Port",
        "Lake Junction",
        "Cedar Loop",
        "East University",
        "Prairie Works",
        "West Gateway",
        "Hill Market",
        "Old Mill",
    ]
    coords = np.array(
        [
            [8.0, 8.0],
            [18.0, 14.0],
            [30.0, 9.0],
            [44.0, 16.0],
            [10.0, 30.0],
            [24.0, 30.0],
            [38.0, 32.0],
            [52.0, 32.0],
            [14.0, 48.0],
            [30.0, 50.0],
            [46.0, 50.0],
            [58.0, 47.0],
        ]
    )
    productivity = np.exp(np.linspace(-0.22, 0.26, len(names)) + rng.normal(0.0, 0.045, len(names)))
    amenity = rng.normal(0.0, 0.55, len(names)) + np.array([0.5, 0.1, -0.2, 0.4, 0.2, 0.0, -0.1, 0.45, -0.15, 0.1, 0.2, -0.25])
    high_productivity = productivity > np.quantile(productivity, 0.68)
    housing_supply_elasticity = np.clip(2.7 - 0.9 * high_productivity + rng.normal(0.0, 0.12, len(names)), 0.85, 3.1)
    housing_capacity = rng.uniform(70.0, 135.0, len(names)) * (1.0 - 0.15 * high_productivity)
    job_capacity = rng.uniform(68.0, 140.0, len(names)) * (0.9 + 0.25 * high_productivity)
    population_seed = rng.uniform(62.0, 122.0, len(names))
    region = np.where(coords[:, 0] < 22.0, "west", np.where(coords[:, 0] < 42.0, "central", "east"))
    return pd.DataFrame(
        {
            "location_id": [f"L{i:02d}" for i in range(1, len(names) + 1)],
            "location_name": names,
            "region": region,
            "x_coord": coords[:, 0],
            "y_coord": coords[:, 1],
            "productivity": productivity,
            "amenity": amenity,
            "housing_supply_elasticity": housing_supply_elasticity,
            "housing_capacity": housing_capacity,
            "job_capacity": job_capacity,
            "population_seed": population_seed,
            "housing_constraint_index": np.clip((productivity - productivity.mean()) * (2.9 - housing_supply_elasticity), 0.0, None),
        }
    ).round(6)


def make_bilateral(locations: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, residence in locations.iterrows():
        for _, workplace in locations.iterrows():
            dx = float(residence["x_coord"] - workplace["x_coord"])
            dy = float(residence["y_coord"] - workplace["y_coord"])
            distance = float(np.sqrt(dx * dx + dy * dy))
            same_region = str(residence["region"]) == str(workplace["region"])
            river_crossing_penalty = 4.5 if (float(residence["y_coord"]) < 28.0) != (float(workplace["y_coord"]) < 28.0) else 0.0
            commute_cost = 2.0 + 0.42 * distance + river_crossing_penalty - (1.4 if same_region else 0.0)
            if residence["location_id"] == workplace["location_id"]:
                commute_cost = 1.6
            rows.append(
                {
                    "residence_id": residence["location_id"],
                    "workplace_id": workplace["location_id"],
                    "distance": round(distance, 4),
                    "same_region": int(same_region),
                    "commute_cost": round(max(commute_cost, 1.0), 4),
                }
            )
    return pd.DataFrame(rows)


def write_outputs() -> None:
    original_dir = ROOT / "original" / "reduced"
    transfer_dir = ROOT / "transfer" / "data"
    original_dir.mkdir(parents=True, exist_ok=True)
    transfer_dir.mkdir(parents=True, exist_ok=True)

    locations = make_locations()
    bilateral = make_bilateral(locations)
    baseline = solve_static_equilibrium(locations, bilateral)

    enriched_locations = locations.copy()
    for column in [
        "equilibrium_residents",
        "equilibrium_employment",
        "equilibrium_wage",
        "equilibrium_rent",
        "equilibrium_output",
        "resident_welfare_proxy",
    ]:
        enriched_locations[f"baseline_{column.replace('equilibrium_', '')}"] = baseline.locations[column]

    enriched_locations.round(6).to_csv(original_dir / "locations_synthetic.csv", index=False)
    baseline.flows.rename(columns={"commuters": "baseline_commuters"}).round(6).to_csv(
        original_dir / "bilateral_commuting_synthetic.csv",
        index=False,
    )
    pd.DataFrame(
        [
            {
                "shock_location_id": enriched_locations.loc[enriched_locations["productivity"].idxmax(), "location_id"],
                "productivity_multiplier": 1.08,
                "periods": 12,
                "migration_adjustment_speed": 0.23,
                "housing_adjustment_speed": 0.13,
                "teaching_note": "Synthetic transition path for static-versus-dynamic comparison.",
            }
        ]
    ).to_csv(transfer_dir / "dynamic_policy_synthetic.csv", index=False)
    print(f"Wrote Week 17 synthetic data to {original_dir} and {transfer_dir}")


if __name__ == "__main__":
    write_outputs()
