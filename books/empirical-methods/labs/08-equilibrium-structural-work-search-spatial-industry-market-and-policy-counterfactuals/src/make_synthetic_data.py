"""Create deterministic synthetic data for the Week 8 equilibrium lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def solve_spatial_equilibrium(
    city_inputs: pd.DataFrame,
    housing_relaxation: float = 0.0,
    mobility_scale: float = 11.0,
    max_iter: int = 800,
    tolerance: float = 1e-9,
) -> pd.DataFrame:
    df = city_inputs.copy()
    total_population = float(df["population_seed"].sum())
    relaxation_target = df["housing_constraint_index"].to_numpy(dtype=float)
    capacity = df["housing_capacity"].to_numpy(dtype=float) * (1.0 + housing_relaxation * relaxation_target)
    elasticity = df["housing_supply_elasticity"].to_numpy(dtype=float)
    productivity = df["productivity"].to_numpy(dtype=float)
    amenity = df["amenity"].to_numpy(dtype=float)
    population = df["population_seed"].to_numpy(dtype=float).copy()

    for _ in range(max_iter):
        density = np.maximum(population / capacity, 0.20)
        wage = 42.0 + 24.0 * np.log(productivity) - 1.25 * np.log(density)
        rent = 13.0 + (8.5 / elasticity) * np.log(density) + 1.4 * df["coastal"].to_numpy(dtype=float)
        utility = wage - rent + 2.8 * amenity
        centered = (utility - utility.max()) / mobility_scale
        shares = np.exp(centered)
        shares = shares / shares.sum()
        next_population = total_population * shares
        updated = 0.60 * population + 0.40 * next_population
        if np.max(np.abs(updated - population)) < tolerance:
            population = updated
            break
        population = updated

    density = np.maximum(population / capacity, 0.20)
    wage = 42.0 + 24.0 * np.log(productivity) - 1.25 * np.log(density)
    rent = 13.0 + (8.5 / elasticity) * np.log(density) + 1.4 * df["coastal"].to_numpy(dtype=float)
    utility = wage - rent + 2.8 * amenity
    output = productivity * population * 100.0
    welfare = population * utility
    out = df.copy()
    out["equilibrium_population"] = population
    out["equilibrium_wage"] = wage
    out["equilibrium_rent"] = rent
    out["equilibrium_utility"] = utility
    out["equilibrium_output"] = output
    out["equilibrium_welfare"] = welfare
    out["housing_capacity_effective"] = capacity
    return out


def make_spatial_data() -> pd.DataFrame:
    rng = np.random.default_rng(6808)
    n_cities = 18
    city_names = [
        "Harbor City",
        "Mesa Works",
        "North Junction",
        "Lakeport",
        "Cedar Valley",
        "Bay Ridge",
        "Prairie Hub",
        "South Forge",
        "Riverbend",
        "Pine Metro",
        "Capital Flats",
        "Stone Coast",
        "Summit Tech",
        "East Market",
        "Milltown",
        "West Anchor",
        "Desert Gate",
        "Old Port",
    ]
    productivity = np.exp(np.linspace(-0.20, 0.28, n_cities) + rng.normal(0.0, 0.07, n_cities))
    productivity_rank = pd.Series(productivity).rank(pct=True).to_numpy()
    coastal = (productivity_rank > 0.70).astype(float)
    housing_elasticity = 2.85 - 1.10 * coastal + rng.normal(0.0, 0.16, n_cities)
    housing_elasticity = np.clip(housing_elasticity, 0.85, 3.30)
    housing_capacity = rng.uniform(72.0, 132.0, n_cities) * (1.0 - 0.20 * coastal)
    amenity = rng.normal(0.0, 0.72, n_cities) + 0.35 * coastal
    population_seed = rng.uniform(55.0, 125.0, n_cities)
    constraint = np.clip((productivity_rank - 0.45) * (3.30 - housing_elasticity) / 1.85, 0.0, 1.0)

    base = pd.DataFrame(
        {
            "city_id": np.arange(1, n_cities + 1),
            "city": city_names,
            "region": np.where(coastal > 0.0, "high-productivity coast", "interior"),
            "productivity": productivity,
            "housing_supply_elasticity": housing_elasticity,
            "housing_capacity": housing_capacity,
            "amenity": amenity,
            "population_seed": population_seed,
            "coastal": coastal,
            "housing_constraint_index": constraint,
        }
    )
    solved = solve_spatial_equilibrium(base)
    for source, target in [
        ("equilibrium_population", "baseline_population"),
        ("equilibrium_wage", "baseline_wage"),
        ("equilibrium_rent", "baseline_rent"),
        ("equilibrium_utility", "baseline_utility"),
        ("equilibrium_output", "baseline_output"),
        ("equilibrium_welfare", "baseline_welfare"),
    ]:
        base[target] = solved[source]
    return base.round(6)


def make_market_data() -> pd.DataFrame:
    rng = np.random.default_rng(6818)
    rows: list[dict[str, float | int | str]] = []
    alpha = -1.15
    beta_quality = 0.78
    beta_auto = 0.20
    for market_id in range(1, 13):
        market_size = float(rng.integers(72_000, 155_000))
        market_income = float(rng.normal(0.0, 1.0))
        utilities = []
        product_rows = []
        for product_id in range(1, 6):
            quality = float(rng.normal(0.0, 1.0) + 0.22 * product_id)
            automation_exposure = float(np.clip(rng.normal(0.45, 0.22), 0.05, 0.95))
            labor_intensity = float(np.clip(rng.normal(0.65, 0.12) - 0.16 * automation_exposure, 0.20, 0.95))
            cost_shifter = float(rng.normal(0.0, 1.0))
            marginal_cost = 1.45 + 0.32 * cost_shifter + 0.55 * labor_intensity + 0.08 * market_income
            price = marginal_cost + 0.95 + 0.18 * quality + rng.normal(0.0, 0.06)
            utility = alpha * price + beta_quality * quality + beta_auto * automation_exposure + 0.08 * market_income
            product_rows.append(
                {
                    "market_id": market_id,
                    "product_id": product_id,
                    "product": f"M{market_id:02d}-P{product_id}",
                    "market_size": market_size,
                    "market_income_index": market_income,
                    "quality": quality,
                    "automation_exposure": automation_exposure,
                    "labor_intensity": labor_intensity,
                    "cost_shifter": cost_shifter,
                    "marginal_cost_truth": marginal_cost,
                    "price": price,
                }
            )
            utilities.append(utility)
        expu = np.exp(np.asarray(utilities))
        denominator = 1.0 + expu.sum()
        shares = expu / denominator
        outside_share = 1.0 / denominator
        for row, share in zip(product_rows, shares):
            row["share"] = float(share)
            row["outside_share"] = float(outside_share)
            row["quantity"] = float(share * market_size)
            row["employment"] = float(share * market_size * row["labor_intensity"] / 100.0)
            rows.append(row)
    return pd.DataFrame(rows).round(6)


def main() -> None:
    spatial_path = ROOT / "original" / "reduced" / "spatial_equilibrium_synthetic.csv"
    market_path = ROOT / "transfer" / "data" / "market_equilibrium_synthetic.csv"
    spatial_path.parent.mkdir(parents=True, exist_ok=True)
    market_path.parent.mkdir(parents=True, exist_ok=True)
    make_spatial_data().to_csv(spatial_path, index=False)
    make_market_data().to_csv(market_path, index=False)
    print(f"Wrote {spatial_path}")
    print(f"Wrote {market_path}")


if __name__ == "__main__":
    main()
