"""Reproduce a compact commuting-flow and spatial-incidence object."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from spatial_model import aggregate_metrics, gravity_design, ols, solve_static_equilibrium


def estimate_gravity(flows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = flows.rename(columns={"baseline_commuters": "commuters"}).copy()
    y, x, names = gravity_design(df)
    beta, residual, vcov = ols(y, x)
    rows = []
    for name, value, se in zip(names, beta, np.sqrt(np.maximum(np.diag(vcov), 0.0))):
        if name in {"intercept", "log_commute_cost"}:
            rows.append(
                {
                    "term": name,
                    "estimate": float(value),
                    "std_error": float(se),
                    "interpretation": "negative flow-cost elasticity" if name == "log_commute_cost" else "normalization",
                }
            )
    fitted = df.loc[df["commuters"] > 0].reset_index(drop=True).copy()
    fitted["log_commuters"] = y
    fitted["log_commuters_fitted"] = x @ beta
    fitted["gravity_residual"] = residual
    return pd.DataFrame(rows), fitted


def commuting_openness(flows: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for residence_id, group in flows.groupby("residence_id"):
        total = float(group["baseline_commuters"].sum())
        home = float(group.loc[group["residence_id"] == group["workplace_id"], "baseline_commuters"].sum())
        weighted_cost = float(np.average(group["commute_cost"], weights=group["baseline_commuters"]))
        top_destination = group.sort_values("baseline_commuters", ascending=False).iloc[0]
        rows.append(
            {
                "residence_id": residence_id,
                "residence_name": top_destination["residence_name"],
                "resident_workers": total,
                "share_working_outside_residence": 1.0 - home / total,
                "commuter_weighted_cost": weighted_cost,
                "largest_workplace_id": top_destination["workplace_id"],
                "largest_workplace_share": float(top_destination["baseline_commuters"] / total),
            }
        )
    return pd.DataFrame(rows)


def fixed_flow_metrics(locations: pd.DataFrame, flows: pd.DataFrame, shock_location: str, multiplier: float) -> dict[str, float | str]:
    loc = locations.copy()
    ids = list(loc["location_id"].astype(str))
    productivity = loc["productivity"].to_numpy(dtype=float)
    target_index = int(loc.index[loc["location_id"] == shock_location][0])
    productivity[target_index] *= multiplier
    employment = loc["baseline_employment"].to_numpy(dtype=float)
    residents = loc["baseline_residents"].to_numpy(dtype=float)
    wage = loc["baseline_wage"].to_numpy(dtype=float)
    rent = loc["baseline_rent"].to_numpy(dtype=float)
    wage[target_index] += 18.0 * np.log(multiplier)
    output = productivity * employment * 100.0
    welfare_proxy = residents * (wage.mean() - rent + 2.4 * loc["amenity"].to_numpy(dtype=float))
    cost_lookup = {
        (str(row["residence_id"]), str(row["workplace_id"])): float(row["commute_cost"])
        for _, row in flows.iterrows()
    }
    commute_cost = np.array([[cost_lookup[(i, j)] for j in ids] for i in ids], dtype=float)
    utility = wage[None, :] - rent[:, None] - commute_cost + 2.4 * loc["amenity"].to_numpy(dtype=float)[:, None]
    utility_scale = 9.0
    expected_utility = utility_scale * np.log(np.exp((utility - utility.max()) / utility_scale).sum())
    expected_utility += float(utility.max())
    return {
        "scenario": "fixed_flow_productivity_shock",
        "total_residents": float(residents.sum()),
        "aggregate_employment": float(employment.sum()),
        "aggregate_output": float(output.sum()),
        "resident_weighted_wage": float(np.average(wage, weights=residents)),
        "resident_weighted_rent": float(np.average(rent, weights=residents)),
        "resident_weighted_welfare_proxy": float(welfare_proxy.sum() / residents.sum()),
        "aggregate_expected_utility": float(expected_utility),
        "max_solver_iterations": 0.0,
        "note": "Productivity and wages change at the shocked workplace, but residence and commuting flows are held fixed.",
    }


def write_outputs(locations: pd.DataFrame, flows: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    gravity, fitted_flows = estimate_gravity(flows)
    gravity.round(6).to_csv(outdir / "commuting_gravity_estimates.csv", index=False)
    fitted_flows.round(6).to_csv(outdir / "gravity_fitted_flows.csv", index=False)
    commuting_openness(flows).round(6).to_csv(outdir / "commuting_openness.csv", index=False)

    model_flows = flows.rename(columns={"baseline_commuters": "commuters"})
    baseline = solve_static_equilibrium(locations, model_flows)
    shock_location = str(locations.loc[locations["productivity"].idxmax(), "location_id"])
    multiplier = 1.08
    counterfactual = solve_static_equilibrium(
        locations,
        model_flows,
        productivity_multiplier={shock_location: multiplier},
    )

    baseline.locations.round(6).to_csv(outdir / "baseline_equilibrium.csv", index=False)
    comparison = baseline.locations[
        ["location_id", "location_name", "region", "productivity", "housing_supply_elasticity"]
    ].copy()
    for column in [
        "equilibrium_residents",
        "equilibrium_employment",
        "equilibrium_wage",
        "equilibrium_rent",
        "equilibrium_output",
        "resident_welfare_proxy",
    ]:
        comparison[f"baseline_{column}"] = baseline.locations[column]
        comparison[f"counterfactual_{column}"] = counterfactual.locations[column]
        comparison[f"change_{column}"] = counterfactual.locations[column] - baseline.locations[column]
    comparison.round(6).to_csv(outdir / "productivity_counterfactual.csv", index=False)

    summary_rows = [
        aggregate_metrics(baseline, "baseline"),
        fixed_flow_metrics(locations, flows, shock_location, multiplier),
        aggregate_metrics(counterfactual, "equilibrium_productivity_shock"),
    ]
    summary = pd.DataFrame(summary_rows)
    baseline_row = summary.loc[summary["scenario"] == "baseline"].iloc[0]
    for column in [
        "aggregate_output",
        "resident_weighted_wage",
        "resident_weighted_rent",
        "resident_weighted_welfare_proxy",
        "aggregate_expected_utility",
    ]:
        summary[f"{column}_change_from_baseline"] = summary[column] - float(baseline_row[column])
    summary.round(6).to_csv(outdir / "incidence_summary.csv", index=False)

    counterfactual.flows.round(6).to_csv(outdir / "counterfactual_commuting_flows.csv", index=False)
    manifest = {
        "task": "Week 17 synthetic commuting-flow and spatial-incidence exercise",
        "primary_anchor": "Monte, Redding, and Rossi-Hansberg commuting/migration spatial equilibrium logic",
        "not_official_replication": True,
        "locations": int(len(locations)),
        "bilateral_flows": int(len(flows)),
        "shock_location_id": shock_location,
        "productivity_multiplier": multiplier,
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote Week 17 reproduce outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locations", required=True, type=Path)
    parser.add_argument("--flows", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    locations = pd.read_csv(args.locations)
    flows = pd.read_csv(args.flows)
    write_outputs(locations, flows, args.outdir)


if __name__ == "__main__":
    main()
