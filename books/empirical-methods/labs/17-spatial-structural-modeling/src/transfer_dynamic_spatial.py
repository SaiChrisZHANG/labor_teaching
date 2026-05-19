"""Transfer Week 17 logic to a small dynamic spatial adjustment exercise."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from spatial_model import solve_static_equilibrium


def transition_path(locations: pd.DataFrame, flows: pd.DataFrame, policy: pd.Series) -> pd.DataFrame:
    shock_location = str(policy["shock_location_id"])
    multiplier = float(policy["productivity_multiplier"])
    periods = int(policy["periods"])
    migration_speed = float(policy["migration_adjustment_speed"])
    housing_speed = float(policy["housing_adjustment_speed"])
    model_flows = flows.rename(columns={"baseline_commuters": "commuters"})

    baseline = solve_static_equilibrium(locations, model_flows)
    long_run = solve_static_equilibrium(
        locations,
        model_flows,
        productivity_multiplier={shock_location: multiplier},
    )

    rows: list[dict[str, object]] = []
    for period in range(periods + 1):
        migration_weight = 1.0 - np.exp(-migration_speed * period)
        housing_weight = 1.0 - np.exp(-housing_speed * period)
        for _, base_row in baseline.locations.iterrows():
            cf_row = long_run.locations.loc[long_run.locations["location_id"] == base_row["location_id"]].iloc[0]
            residents = float(base_row["equilibrium_residents"] + migration_weight * (cf_row["equilibrium_residents"] - base_row["equilibrium_residents"]))
            employment = float(base_row["equilibrium_employment"] + migration_weight * (cf_row["equilibrium_employment"] - base_row["equilibrium_employment"]))
            wage = float(base_row["equilibrium_wage"] + migration_weight * (cf_row["equilibrium_wage"] - base_row["equilibrium_wage"]))
            rent = float(base_row["equilibrium_rent"] + housing_weight * (cf_row["equilibrium_rent"] - base_row["equilibrium_rent"]))
            welfare_proxy = residents * (wage - rent + 2.4 * float(base_row["amenity"]))
            rows.append(
                {
                    "period": period,
                    "location_id": base_row["location_id"],
                    "location_name": base_row["location_name"],
                    "residents": residents,
                    "employment": employment,
                    "wage": wage,
                    "rent": rent,
                    "welfare_proxy": welfare_proxy,
                    "migration_adjustment_weight": migration_weight,
                    "housing_adjustment_weight": housing_weight,
                    "shock_location_id": shock_location,
                }
            )
    return pd.DataFrame(rows)


def transition_summary(path: pd.DataFrame) -> pd.DataFrame:
    rows = []
    baseline = path.loc[path["period"] == 0]
    base_welfare = float(baseline["welfare_proxy"].sum() / baseline["residents"].sum())
    base_rent = float(np.average(baseline["rent"], weights=baseline["residents"]))
    base_employment = float(baseline["employment"].sum())
    for label, period in [("impact", 1), ("medium_run", int(path["period"].max() // 2)), ("long_run", int(path["period"].max()))]:
        frame = path.loc[path["period"] == period]
        rows.append(
            {
                "horizon": label,
                "period": period,
                "aggregate_employment": float(frame["employment"].sum()),
                "employment_change_from_baseline": float(frame["employment"].sum() - base_employment),
                "resident_weighted_rent": float(np.average(frame["rent"], weights=frame["residents"])),
                "rent_change_from_baseline": float(np.average(frame["rent"], weights=frame["residents"]) - base_rent),
                "resident_weighted_welfare_proxy": float(frame["welfare_proxy"].sum() / frame["residents"].sum()),
                "welfare_change_from_baseline": float(frame["welfare_proxy"].sum() / frame["residents"].sum() - base_welfare),
            }
        )
    return pd.DataFrame(rows)


def frontier_prompts() -> pd.DataFrame:
    prompts = [
        "Which conclusion would differ if students only compared the baseline and long-run equilibria?",
        "Which workers bear transition costs when migration is slow?",
        "How does slower housing adjustment change rent incidence?",
        "Which objects would a full dynamic urban model need beyond this teaching path?",
        "What data would discipline forward-looking migration rather than a reduced adjustment rule?",
    ]
    return pd.DataFrame({"prompt_id": range(1, len(prompts) + 1), "transfer_prompt": prompts})


def write_outputs(locations: pd.DataFrame, flows: pd.DataFrame, policy: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    path = transition_path(locations, flows, policy.iloc[0])
    path.round(6).to_csv(outdir / "dynamic_transition_path.csv", index=False)
    transition_summary(path).round(6).to_csv(outdir / "transition_summary.csv", index=False)
    frontier_prompts().to_csv(outdir / "dynamic_frontier_prompts.csv", index=False)
    print(f"Wrote Week 17 dynamic transfer outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locations", required=True, type=Path)
    parser.add_argument("--flows", required=True, type=Path)
    parser.add_argument("--policy", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    locations = pd.read_csv(args.locations)
    flows = pd.read_csv(args.flows)
    policy = pd.read_csv(args.policy)
    write_outputs(locations, flows, policy, args.outdir)


if __name__ == "__main__":
    main()
