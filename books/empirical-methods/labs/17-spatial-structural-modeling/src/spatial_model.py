"""Small teaching spatial-equilibrium utilities for the Week 17 lab."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class SpatialSolution:
    locations: pd.DataFrame
    flows: pd.DataFrame
    probabilities: np.ndarray
    commute_costs: np.ndarray
    iterations: int


def _location_index(locations: pd.DataFrame) -> dict[str, int]:
    return {str(location_id): idx for idx, location_id in enumerate(locations["location_id"])}


def commute_cost_matrix(locations: pd.DataFrame, bilateral: pd.DataFrame) -> np.ndarray:
    ids = list(locations["location_id"].astype(str))
    index = _location_index(locations)
    costs = np.zeros((len(ids), len(ids)), dtype=float)
    for _, row in bilateral.iterrows():
        i = index[str(row["residence_id"])]
        j = index[str(row["workplace_id"])]
        costs[i, j] = float(row["commute_cost"])
    return costs


def productivity_vector(
    locations: pd.DataFrame,
    productivity_multiplier: dict[str, float] | None = None,
) -> np.ndarray:
    productivity = locations["productivity"].to_numpy(dtype=float).copy()
    if productivity_multiplier:
        index = _location_index(locations)
        for location_id, multiplier in productivity_multiplier.items():
            productivity[index[str(location_id)]] *= float(multiplier)
    return productivity


def solve_static_equilibrium(
    locations: pd.DataFrame,
    bilateral: pd.DataFrame,
    productivity_multiplier: dict[str, float] | None = None,
    commute_cost_scale: float = 1.0,
    housing_supply_scale: float = 1.0,
    utility_scale: float = 9.0,
    max_iter: int = 600,
    tolerance: float = 1e-8,
) -> SpatialSolution:
    df = locations.copy().reset_index(drop=True)
    ids = list(df["location_id"].astype(str))
    n_locations = len(ids)
    total_workers = float(df["population_seed"].sum())
    commute_cost = commute_cost_scale * commute_cost_matrix(df, bilateral)
    productivity = productivity_vector(df, productivity_multiplier)
    amenity = df["amenity"].to_numpy(dtype=float)
    housing_capacity = df["housing_capacity"].to_numpy(dtype=float)
    housing_elasticity = df["housing_supply_elasticity"].to_numpy(dtype=float) * housing_supply_scale
    job_capacity = df["job_capacity"].to_numpy(dtype=float)

    wage = 42.0 + 18.0 * np.log(productivity)
    rent = 12.0 + 1.4 * amenity
    probabilities = np.full((n_locations, n_locations), 1.0 / (n_locations * n_locations))

    for iteration in range(max_iter):
        utility = wage[None, :] - rent[:, None] - commute_cost + 2.4 * amenity[:, None]
        centered = (utility - utility.max()) / utility_scale
        exp_utility = np.exp(centered)
        next_probabilities = exp_utility / exp_utility.sum()
        residents = total_workers * next_probabilities.sum(axis=1)
        employment = total_workers * next_probabilities.sum(axis=0)

        density = np.maximum(residents / housing_capacity, 0.25)
        employment_load = np.maximum(employment / job_capacity, 0.25)
        next_rent = 12.0 + (7.5 / housing_elasticity) * np.log(density) + 1.4 * amenity
        next_wage = 42.0 + 18.0 * np.log(productivity) - 2.2 * np.log(employment_load)

        wage_update = 0.58 * wage + 0.42 * next_wage
        rent_update = 0.58 * rent + 0.42 * next_rent
        delta = max(
            float(np.max(np.abs(wage_update - wage))),
            float(np.max(np.abs(rent_update - rent))),
            float(np.max(np.abs(next_probabilities - probabilities))),
        )
        wage = wage_update
        rent = rent_update
        probabilities = next_probabilities
        if delta < tolerance:
            break

    residents = total_workers * probabilities.sum(axis=1)
    employment = total_workers * probabilities.sum(axis=0)
    utility_matrix = wage[None, :] - rent[:, None] - commute_cost + 2.4 * amenity[:, None]
    expected_utility = utility_scale * np.log(np.exp((utility_matrix - utility_matrix.max()) / utility_scale).sum())
    expected_utility += float(utility_matrix.max())
    output = productivity * employment * 100.0
    welfare = residents * (wage.mean() - rent + 2.4 * amenity)

    out_locations = df.copy()
    out_locations["equilibrium_residents"] = residents
    out_locations["equilibrium_employment"] = employment
    out_locations["equilibrium_wage"] = wage
    out_locations["equilibrium_rent"] = rent
    out_locations["equilibrium_output"] = output
    out_locations["resident_welfare_proxy"] = welfare
    out_locations["aggregate_expected_utility"] = expected_utility
    out_locations["solver_iterations"] = int(iteration + 1)

    flow_rows: list[dict[str, object]] = []
    names = dict(zip(df["location_id"].astype(str), df["location_name"].astype(str)))
    distances = {
        (str(row["residence_id"]), str(row["workplace_id"])): float(row["distance"])
        for _, row in bilateral.iterrows()
    }
    base_costs = {
        (str(row["residence_id"]), str(row["workplace_id"])): float(row["commute_cost"])
        for _, row in bilateral.iterrows()
    }
    for i, residence_id in enumerate(ids):
        for j, workplace_id in enumerate(ids):
            commuters = total_workers * probabilities[i, j]
            flow_rows.append(
                {
                    "residence_id": residence_id,
                    "residence_name": names[residence_id],
                    "workplace_id": workplace_id,
                    "workplace_name": names[workplace_id],
                    "distance": distances[(residence_id, workplace_id)],
                    "commute_cost": base_costs[(residence_id, workplace_id)] * commute_cost_scale,
                    "commuters": commuters,
                    "share_of_residents": commuters / residents[i] if residents[i] > 0 else np.nan,
                }
            )
    flows = pd.DataFrame(flow_rows)
    return SpatialSolution(out_locations, flows, probabilities, commute_cost, int(iteration + 1))


def aggregate_metrics(solution: SpatialSolution, scenario: str) -> dict[str, float | str]:
    loc = solution.locations
    total_residents = float(loc["equilibrium_residents"].sum())
    return {
        "scenario": scenario,
        "total_residents": total_residents,
        "aggregate_employment": float(loc["equilibrium_employment"].sum()),
        "aggregate_output": float(loc["equilibrium_output"].sum()),
        "resident_weighted_wage": float(np.average(loc["equilibrium_wage"], weights=loc["equilibrium_residents"])),
        "resident_weighted_rent": float(np.average(loc["equilibrium_rent"], weights=loc["equilibrium_residents"])),
        "resident_weighted_welfare_proxy": float(loc["resident_welfare_proxy"].sum() / total_residents),
        "aggregate_expected_utility": float(loc["aggregate_expected_utility"].iloc[0]),
        "max_solver_iterations": float(loc["solver_iterations"].max()),
    }


def ols(y: np.ndarray, x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    xtx_inv = np.linalg.pinv(x.T @ x)
    beta = xtx_inv @ x.T @ y
    residual = y - x @ beta
    n, k = x.shape
    sigma2 = float((residual @ residual) / max(n - k, 1))
    vcov = sigma2 * xtx_inv
    return beta, residual, vcov


def gravity_design(flows: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, list[str]]:
    df = flows.copy()
    df = df.loc[df["commuters"] > 0].reset_index(drop=True)
    origin_dummies = pd.get_dummies(df["residence_id"], prefix="origin", drop_first=True, dtype=float)
    destination_dummies = pd.get_dummies(df["workplace_id"], prefix="dest", drop_first=True, dtype=float)
    design = pd.concat(
        [
            pd.Series(1.0, index=df.index, name="intercept"),
            np.log(df["commute_cost"].astype(float)).rename("log_commute_cost"),
            origin_dummies,
            destination_dummies,
        ],
        axis=1,
    )
    y = np.log(df["commuters"].astype(float)).to_numpy(dtype=float)
    return y, design.to_numpy(dtype=float), list(design.columns)
