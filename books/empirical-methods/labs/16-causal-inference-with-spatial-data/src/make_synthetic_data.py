"""Create deterministic synthetic data for the Week 16 spatial causal inference lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SECTORS = ["manufacturing", "logistics", "health", "retail", "construction", "business"]


def make_border_counties() -> pd.DataFrame:
    rng = np.random.default_rng(1616)
    rows: list[dict[str, object]] = []
    pair_centers = [(18 + 18 * (i % 6), 18 + 18 * (i // 6)) for i in range(18)]

    for pair_index, (center_x, center_y) in enumerate(pair_centers, start=1):
        pair_id = f"P{pair_index:02d}"
        region_id = f"R{1 + (pair_index - 1) // 6}"
        pair_shock = rng.normal(0.0, 0.012)
        treated_on_east = pair_index % 2 == 0
        fragile_pair = pair_index in {4, 11, 16}
        for side in [-1, 1]:
            side_name = "east" if side > 0 else "west"
            treated = int((side > 0) == treated_on_east)
            x_coord = center_x + side * rng.uniform(2.0, 4.2) + rng.normal(0.0, 0.7)
            y_coord = center_y + rng.normal(0.0, 2.0)
            manufacturing_share = float(
                np.clip(0.24 + 0.05 * (pair_index % 3 == 0) + rng.normal(0.0, 0.035), 0.08, 0.48)
            )
            baseline_log_wage = float(
                10.05
                + 0.05 * (region_id == "R3")
                + 0.025 * side
                + 0.075 * fragile_pair * treated
                + rng.normal(0.0, 0.035)
            )
            baseline_employment_rate = float(
                np.clip(
                    0.69
                    - 0.08 * manufacturing_share
                    + 0.018 * side
                    - 0.035 * fragile_pair * treated
                    + rng.normal(0.0, 0.018),
                    0.50,
                    0.84,
                )
            )
            unemployment_rate_1990 = float(
                np.clip(
                    0.055
                    + 0.09 * (1.0 - baseline_employment_rate)
                    + 0.035 * manufacturing_share
                    + rng.normal(0.0, 0.01),
                    0.025,
                    0.18,
                )
            )
            pretrend_1980_1990 = float(
                0.012
                - 0.030 * manufacturing_share
                - 0.010 * fragile_pair * treated
                + rng.normal(0.0, 0.012)
            )
            local_shock_index = float(
                0.45 * np.sin(center_x / 18.0) + 0.35 * np.cos(center_y / 22.0) + rng.normal(0.0, 0.18)
            )
            true_effect = -0.018
            employment_growth = float(
                0.035
                + true_effect * treated
                - 0.042 * manufacturing_share
                + 0.030 * baseline_employment_rate
                + pair_shock
                + 0.010 * local_shock_index
                + rng.normal(0.0, 0.012)
            )
            population_1990 = int(rng.integers(22000, 165000))
            rows.append(
                {
                    "county_id": f"C{pair_index:02d}{side_name[0].upper()}",
                    "pair_id": pair_id,
                    "region_id": region_id,
                    "side": side_name,
                    "treated_policy_side": treated,
                    "x_coord": round(float(x_coord), 4),
                    "y_coord": round(float(y_coord), 4),
                    "population_1990": population_1990,
                    "baseline_log_wage": round(baseline_log_wage, 5),
                    "baseline_employment_rate": round(baseline_employment_rate, 5),
                    "unemployment_rate_1990": round(unemployment_rate_1990, 5),
                    "manufacturing_share_1990": round(manufacturing_share, 5),
                    "pretrend_1980_1990": round(pretrend_1980_1990, 5),
                    "local_shock_index": round(local_shock_index, 5),
                    "fragile_pair": int(fragile_pair),
                    "employment_growth_2000_2010": round(employment_growth, 5),
                }
            )
    return pd.DataFrame(rows)


def make_neighbor_links(counties: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    coords = counties.set_index("county_id")[["x_coord", "y_coord"]]
    pair_map = counties.set_index("county_id")["pair_id"].to_dict()
    treated_map = counties.set_index("county_id")["treated_policy_side"].to_dict()
    ids = list(coords.index)
    for origin in ids:
        for neighbor in ids:
            if origin == neighbor:
                continue
            dx = float(coords.loc[origin, "x_coord"] - coords.loc[neighbor, "x_coord"])
            dy = float(coords.loc[origin, "y_coord"] - coords.loc[neighbor, "y_coord"])
            distance = float(np.sqrt(dx * dx + dy * dy))
            rows.append(
                {
                    "county_id": origin,
                    "neighbor_county_id": neighbor,
                    "distance_miles": round(distance, 4),
                    "same_pair": int(pair_map[origin] == pair_map[neighbor]),
                    "neighbor_treated_policy_side": int(treated_map[neighbor]),
                }
            )
    return pd.DataFrame(rows)


def make_sector_shocks() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"sector": "manufacturing", "shock": 0.190, "feedback_penalty": 0.030},
            {"sector": "logistics", "shock": 0.072, "feedback_penalty": 0.012},
            {"sector": "health", "shock": -0.020, "feedback_penalty": 0.006},
            {"sector": "retail", "shock": 0.038, "feedback_penalty": 0.009},
            {"sector": "construction", "shock": 0.094, "feedback_penalty": 0.016},
            {"sector": "business", "shock": 0.018, "feedback_penalty": 0.010},
        ]
    )


def make_sector_shares(counties: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(1620)
    profiles = {
        "R1": np.array([4.2, 1.4, 1.0, 1.4, 1.5, 1.2]),
        "R2": np.array([1.6, 3.6, 1.2, 1.5, 1.8, 1.4]),
        "R3": np.array([1.1, 1.3, 3.4, 1.5, 1.6, 2.4]),
    }
    rows: list[dict[str, object]] = []
    for _, county in counties.iterrows():
        alpha = profiles[str(county["region_id"])].copy()
        if int(county["treated_policy_side"]) == 1:
            alpha[0] += 0.45
            alpha[4] += 0.25
        shares = rng.dirichlet(alpha)
        baseline_employment = int(round(float(county["population_1990"]) * float(county["baseline_employment_rate"])))
        for sector, share in zip(SECTORS, shares):
            rows.append(
                {
                    "county_id": county["county_id"],
                    "region_id": county["region_id"],
                    "sector": sector,
                    "baseline_employment_1990": baseline_employment,
                    "sector_share_1990": round(float(share), 6),
                    "sector_employment_1990": int(round(float(share) * baseline_employment)),
                }
            )
    return pd.DataFrame(rows)


def write_outputs() -> None:
    original_dir = ROOT / "original" / "reduced"
    transfer_dir = ROOT / "transfer" / "data"
    original_dir.mkdir(parents=True, exist_ok=True)
    transfer_dir.mkdir(parents=True, exist_ok=True)

    counties = make_border_counties()
    links = make_neighbor_links(counties)
    shares = make_sector_shares(counties)
    shocks = make_sector_shocks()

    counties.to_csv(original_dir / "border_counties_synthetic.csv", index=False)
    links.to_csv(original_dir / "neighbor_links_synthetic.csv", index=False)
    shares.to_csv(original_dir / "sector_shares_synthetic.csv", index=False)
    shocks.to_csv(original_dir / "sector_shocks_synthetic.csv", index=False)

    transfer_counties = counties[
        [
            "county_id",
            "pair_id",
            "region_id",
            "x_coord",
            "y_coord",
            "population_1990",
            "baseline_employment_rate",
            "manufacturing_share_1990",
            "employment_growth_2000_2010",
        ]
    ].copy()
    transfer_counties.to_csv(transfer_dir / "shift_share_counties_synthetic.csv", index=False)
    print(f"Wrote synthetic Week 16 data to {original_dir} and {transfer_dir}")


if __name__ == "__main__":
    write_outputs()
