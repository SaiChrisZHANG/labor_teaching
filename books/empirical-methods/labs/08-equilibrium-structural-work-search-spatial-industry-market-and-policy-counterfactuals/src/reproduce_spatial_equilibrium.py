"""Run the Week 8 spatial-equilibrium reproduce and diagnose workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week8_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week8_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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

    for iteration in range(max_iter):
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
    else:
        iteration = max_iter

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
    out["solver_iterations"] = int(iteration + 1)
    return out


def aggregate_summary(baseline: pd.DataFrame, counterfactual: pd.DataFrame) -> pd.DataFrame:
    total_population = baseline["equilibrium_population"].sum()
    rows = []
    for label, frame in [("baseline", baseline), ("housing_relaxation", counterfactual)]:
        rows.append(
            {
                "scenario": label,
                "total_population": float(frame["equilibrium_population"].sum()),
                "aggregate_output": float(frame["equilibrium_output"].sum()),
                "population_weighted_wage": float(
                    np.average(frame["equilibrium_wage"], weights=frame["equilibrium_population"])
                ),
                "population_weighted_rent": float(
                    np.average(frame["equilibrium_rent"], weights=frame["equilibrium_population"])
                ),
                "population_weighted_utility": float(
                    frame["equilibrium_welfare"].sum() / total_population
                ),
                "total_welfare": float(frame["equilibrium_welfare"].sum()),
                "max_solver_iterations": int(frame["solver_iterations"].max()),
            }
        )
    summary = pd.DataFrame(rows)
    baseline_row = summary.loc[summary["scenario"] == "baseline"].iloc[0]
    for column in [
        "aggregate_output",
        "population_weighted_wage",
        "population_weighted_rent",
        "population_weighted_utility",
        "total_welfare",
    ]:
        summary[f"{column}_change_from_baseline"] = summary[column] - float(baseline_row[column])
        summary[f"{column}_pct_change_from_baseline"] = (
            100.0 * summary[f"{column}_change_from_baseline"] / abs(float(baseline_row[column]))
        )
    return summary


def write_outputs(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    baseline = solve_spatial_equilibrium(df, housing_relaxation=0.0)
    counterfactual = solve_spatial_equilibrium(df, housing_relaxation=0.55)

    baseline_cols = [
        "city_id",
        "city",
        "region",
        "productivity",
        "housing_supply_elasticity",
        "housing_constraint_index",
        "equilibrium_population",
        "equilibrium_wage",
        "equilibrium_rent",
        "equilibrium_utility",
        "equilibrium_output",
    ]
    baseline[baseline_cols].round(6).to_csv(outdir / "baseline_equilibrium.csv", index=False)

    comparison = baseline[["city_id", "city", "region", "productivity", "housing_constraint_index"]].copy()
    for column in [
        "equilibrium_population",
        "equilibrium_wage",
        "equilibrium_rent",
        "equilibrium_utility",
        "equilibrium_output",
    ]:
        comparison[f"baseline_{column}"] = baseline[column]
        comparison[f"counterfactual_{column}"] = counterfactual[column]
        comparison[f"change_{column}"] = counterfactual[column] - baseline[column]
        comparison[f"pct_change_{column}"] = 100.0 * comparison[f"change_{column}"] / baseline[column].abs()
    comparison.round(6).to_csv(outdir / "housing_counterfactual.csv", index=False)

    aggregate_summary(baseline, counterfactual).round(6).to_csv(
        outdir / "aggregate_counterfactual_summary.csv",
        index=False,
    )

    fit = pd.DataFrame(
        {
            "city_id": df["city_id"],
            "city": df["city"],
            "observed_baseline_population": df["baseline_population"],
            "model_baseline_population": baseline["equilibrium_population"],
            "observed_baseline_wage": df["baseline_wage"],
            "model_baseline_wage": baseline["equilibrium_wage"],
            "observed_baseline_rent": df["baseline_rent"],
            "model_baseline_rent": baseline["equilibrium_rent"],
            "fit_note": "Baseline moments are generated by the teaching model; publishable work would need external validation.",
        }
    )
    fit.round(6).to_csv(outdir / "equilibrium_moment_fit.csv", index=False)

    assumption_map = pd.DataFrame(
        [
            {
                "object": "city productivity",
                "role": "primitive",
                "status": "observed in synthetic teaching data",
                "diagnostic": "In frontier work this would be inferred from wages, output, or productivity measures.",
            },
            {
                "object": "housing-supply elasticity",
                "role": "equilibrium closure",
                "status": "calibrated in teaching data",
                "diagnostic": "Sensitivity is required because the counterfactual depends on rent incidence.",
            },
            {
                "object": "mobility scale",
                "role": "location-choice friction",
                "status": "chosen by the teaching model",
                "diagnostic": "Migration or commuting flows would be needed to discipline this object.",
            },
            {
                "object": "amenity value",
                "role": "latent utility component",
                "status": "observed in synthetic teaching data",
                "diagnostic": "Real papers need restrictions separating amenities from productivity and rents.",
            },
            {
                "object": "housing relaxation",
                "role": "policy counterfactual",
                "status": "imposed counterfactual shock",
                "diagnostic": "Interpret as a local policy experiment, not a forecast of actual zoning reform.",
            },
        ]
    )
    assumption_map.to_csv(outdir / "assumption_map.csv", index=False)

    sensitivity_rows = []
    for relaxation in [0.20, 0.35, 0.55, 0.75]:
        for mobility_scale in [8.0, 11.0, 15.0]:
            base_s = solve_spatial_equilibrium(df, housing_relaxation=0.0, mobility_scale=mobility_scale)
            cf_s = solve_spatial_equilibrium(df, housing_relaxation=relaxation, mobility_scale=mobility_scale)
            base_agg = aggregate_summary(base_s, cf_s).iloc[0]
            cf_agg = aggregate_summary(base_s, cf_s).iloc[1]
            sensitivity_rows.append(
                {
                    "housing_relaxation": relaxation,
                    "mobility_scale": mobility_scale,
                    "aggregate_output_pct_change": cf_agg["aggregate_output_pct_change_from_baseline"],
                    "weighted_rent_change": cf_agg["population_weighted_rent_change_from_baseline"],
                    "weighted_utility_change": cf_agg["population_weighted_utility_change_from_baseline"],
                    "max_solver_iterations": cf_agg["max_solver_iterations"],
                    "diagnostic_note": "Smaller mobility_scale means workers are more responsive to utility differences.",
                }
            )
    pd.DataFrame(sensitivity_rows).round(6).to_csv(outdir / "spatial_sensitivity.csv", index=False)

    plt.figure(figsize=(7.6, 4.6))
    colors = np.where(comparison["housing_constraint_index"] > 0.30, "#D55E00", "#0072B2")
    plt.scatter(
        comparison["productivity"],
        comparison["change_equilibrium_population"],
        s=46 + 95 * comparison["housing_constraint_index"],
        c=colors,
        alpha=0.82,
        edgecolor="white",
        linewidth=0.6,
    )
    for _, row in comparison.nlargest(4, "housing_constraint_index").iterrows():
        plt.text(row["productivity"], row["change_equilibrium_population"], row["city"], fontsize=7)
    plt.axhline(0.0, color="#333333", linewidth=0.8)
    plt.xlabel("Productivity")
    plt.ylabel("Population change after housing relaxation")
    plt.tight_layout()
    plt.savefig(outdir / "spatial_incidence.png", dpi=160)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    write_outputs(df, args.outdir)
    print(f"Wrote spatial-equilibrium outputs to {args.outdir}")


if __name__ == "__main__":
    main()
