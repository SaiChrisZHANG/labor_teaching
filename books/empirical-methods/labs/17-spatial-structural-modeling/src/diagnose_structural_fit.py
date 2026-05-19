"""Diagnose fit, calibration, and counterfactual sensitivity for Week 17."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from reproduce_spatial_flows import estimate_gravity
from spatial_model import aggregate_metrics, solve_static_equilibrium


def flow_fit_diagnostics(flows: pd.DataFrame) -> pd.DataFrame:
    _, fitted = estimate_gravity(flows)
    actual = np.exp(fitted["log_commuters"].to_numpy(dtype=float))
    predicted = np.exp(fitted["log_commuters_fitted"].to_numpy(dtype=float))
    residual = fitted["gravity_residual"].to_numpy(dtype=float)
    long_commute = fitted["distance"].to_numpy(dtype=float) >= np.quantile(fitted["distance"], 0.75)
    cross_commute = fitted["residence_id"] != fitted["workplace_id"]
    rows = [
        {
            "diagnostic": "log_flow_rmse",
            "value": float(np.sqrt(np.mean(residual**2))),
            "interpretation": "Targeted gravity fit in log commuting flows.",
        },
        {
            "diagnostic": "flow_correlation",
            "value": float(np.corrcoef(actual, predicted)[0, 1]),
            "interpretation": "Correlation between observed synthetic and fitted bilateral flows.",
        },
        {
            "diagnostic": "actual_cross_commute_share",
            "value": float(actual[cross_commute].sum() / actual.sum()),
            "interpretation": "Share of commuters working outside their residence location.",
        },
        {
            "diagnostic": "fitted_cross_commute_share",
            "value": float(predicted[cross_commute].sum() / predicted.sum()),
            "interpretation": "Gravity-implied outside-residence commuting share.",
        },
        {
            "diagnostic": "actual_long_commute_share",
            "value": float(actual[long_commute].sum() / actual.sum()),
            "interpretation": "Untargeted check on the upper-distance tail.",
        },
        {
            "diagnostic": "fitted_long_commute_share",
            "value": float(predicted[long_commute].sum() / predicted.sum()),
            "interpretation": "Gravity-implied upper-distance tail.",
        },
    ]
    return pd.DataFrame(rows)


def parameter_audit() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "object": "flow-cost elasticity",
                "status": "estimated in synthetic gravity regression",
                "evidence": "bilateral residence-workplace flows",
                "diagnostic": "gravity residuals and long-commute fit",
            },
            {
                "object": "local productivity",
                "status": "observed synthetic primitive",
                "evidence": "location productivity index",
                "diagnostic": "real papers infer this from wages, output, or firms",
            },
            {
                "object": "amenity value",
                "status": "observed synthetic primitive",
                "evidence": "location amenity index",
                "diagnostic": "real papers need external amenities or restrictions",
            },
            {
                "object": "housing supply elasticity",
                "status": "calibrated synthetic primitive",
                "evidence": "location-specific elasticity in teaching data",
                "diagnostic": "counterfactual rent incidence sensitivity",
            },
            {
                "object": "utility scale",
                "status": "chosen model closure",
                "evidence": "normalizes responsiveness to utility gaps",
                "diagnostic": "flow and population sensitivity",
            },
            {
                "object": "productivity shock",
                "status": "imposed counterfactual",
                "evidence": "teaching policy scenario",
                "diagnostic": "distance from observed support and affected margins",
            },
        ]
    )


def sensitivity(locations: pd.DataFrame, flows: pd.DataFrame) -> pd.DataFrame:
    model_flows = flows.rename(columns={"baseline_commuters": "commuters"})
    shock_location = str(locations.loc[locations["productivity"].idxmax(), "location_id"])
    rows = []
    for commute_scale in [0.85, 1.0, 1.15]:
        for housing_scale in [0.75, 1.0, 1.25]:
            baseline = solve_static_equilibrium(
                locations,
                model_flows,
                commute_cost_scale=commute_scale,
                housing_supply_scale=housing_scale,
            )
            counterfactual = solve_static_equilibrium(
                locations,
                model_flows,
                productivity_multiplier={shock_location: 1.08},
                commute_cost_scale=commute_scale,
                housing_supply_scale=housing_scale,
            )
            base_metrics = aggregate_metrics(baseline, "baseline")
            cf_metrics = aggregate_metrics(counterfactual, "counterfactual")
            target_base = baseline.locations.loc[baseline.locations["location_id"] == shock_location].iloc[0]
            target_cf = counterfactual.locations.loc[counterfactual.locations["location_id"] == shock_location].iloc[0]
            rows.append(
                {
                    "commute_cost_scale": commute_scale,
                    "housing_supply_scale": housing_scale,
                    "aggregate_output_change": float(cf_metrics["aggregate_output"] - base_metrics["aggregate_output"]),
                    "expected_utility_change": float(cf_metrics["aggregate_expected_utility"] - base_metrics["aggregate_expected_utility"]),
                    "resident_weighted_rent_change": float(cf_metrics["resident_weighted_rent"] - base_metrics["resident_weighted_rent"]),
                    "target_employment_change": float(target_cf["equilibrium_employment"] - target_base["equilibrium_employment"]),
                    "target_resident_change": float(target_cf["equilibrium_residents"] - target_base["equilibrium_residents"]),
                }
            )
    return pd.DataFrame(rows)


def diagnostic_prompts() -> pd.DataFrame:
    prompts = [
        "Which parameters are directly disciplined by bilateral flows?",
        "Which headline changes depend on housing supply elasticity?",
        "Does the model fit long-distance commuting as well as short-distance commuting?",
        "What would a reduced-form design identify before the structural model begins?",
        "Which welfare claim would be most sensitive to amenities being mismeasured?",
        "Is the productivity shock close to observed support or a large extrapolation?",
    ]
    return pd.DataFrame({"prompt_id": range(1, len(prompts) + 1), "diagnostic_prompt": prompts})


def write_outputs(locations: pd.DataFrame, flows: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    flow_fit_diagnostics(flows).round(6).to_csv(outdir / "flow_fit_diagnostics.csv", index=False)
    parameter_audit().to_csv(outdir / "parameter_audit.csv", index=False)
    sensitivity(locations, flows).round(6).to_csv(outdir / "counterfactual_sensitivity.csv", index=False)
    diagnostic_prompts().to_csv(outdir / "diagnostic_prompts.csv", index=False)
    print(f"Wrote Week 17 diagnose outputs to {outdir}")


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
