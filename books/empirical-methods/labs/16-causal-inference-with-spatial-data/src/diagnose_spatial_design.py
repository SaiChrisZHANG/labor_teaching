"""Diagnose spatial identification risks in the synthetic Week 16 border design."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


BALANCE_VARS = [
    "baseline_log_wage",
    "baseline_employment_rate",
    "unemployment_rate_1990",
    "manufacturing_share_1990",
    "pretrend_1980_1990",
]


def standardized_difference(df: pd.DataFrame, variable: str) -> dict[str, float | str]:
    treated = df.loc[df["treated_policy_side"] == 1, variable].to_numpy(dtype=float)
    control = df.loc[df["treated_policy_side"] == 0, variable].to_numpy(dtype=float)
    pooled = np.sqrt((treated.var(ddof=1) + control.var(ddof=1)) / 2.0)
    diff = float(treated.mean() - control.mean())
    return {
        "variable": variable,
        "treated_mean": float(treated.mean()),
        "control_mean": float(control.mean()),
        "difference": diff,
        "standardized_difference": diff / pooled if pooled > 0 else np.nan,
    }


def paired_effect(df: pd.DataFrame) -> float:
    diffs = []
    for _, group in df.groupby("pair_id"):
        treated = group.loc[group["treated_policy_side"] == 1, "employment_growth_2000_2010"]
        control = group.loc[group["treated_policy_side"] == 0, "employment_growth_2000_2010"]
        if len(treated) == 1 and len(control) == 1:
            diffs.append(float(treated.iloc[0] - control.iloc[0]))
    return float(np.mean(diffs)) if diffs else np.nan


def make_pair_balance(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for pair_id, group in df.groupby("pair_id"):
        row: dict[str, object] = {"pair_id": pair_id}
        max_abs = 0.0
        for variable in BALANCE_VARS:
            treated = float(group.loc[group["treated_policy_side"] == 1, variable].iloc[0])
            control = float(group.loc[group["treated_policy_side"] == 0, variable].iloc[0])
            diff = treated - control
            row[f"{variable}_treated_minus_control"] = round(diff, 6)
            max_abs = max(max_abs, abs(diff))
        row["max_absolute_difference"] = round(max_abs, 6)
        row["fragile_pair_input"] = int(group["fragile_pair"].max())
        row["flag_large_balance_gap"] = int(max_abs > 0.075)
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["flag_large_balance_gap", "max_absolute_difference"], ascending=[False, False])


def make_spillover_audit(df: pd.DataFrame, links: pd.DataFrame, cutoff: float = 45.0) -> pd.DataFrame:
    weights = links.copy()
    weights["kernel_weight"] = np.maximum(0.0, 1.0 - weights["distance_miles"] / cutoff)
    weights.loc[weights["distance_miles"] > cutoff, "kernel_weight"] = 0.0
    weights["treated_neighbor_weight"] = weights["kernel_weight"] * weights["neighbor_treated_policy_side"]
    exposure = weights.groupby("county_id", as_index=False).agg(
        treated_neighbor_exposure=("treated_neighbor_weight", "sum"),
        nearby_counties_within_cutoff=("kernel_weight", lambda s: int((s > 0).sum())),
        same_pair_neighbor=("same_pair", "max"),
    )
    exposure = exposure.merge(df[["county_id", "pair_id", "treated_policy_side"]], on="county_id", how="left")
    exposure["control_with_treated_neighbor_exposure"] = (
        (exposure["treated_policy_side"] == 0) & (exposure["treated_neighbor_exposure"] > 0)
    ).astype(int)
    return exposure.sort_values(["control_with_treated_neighbor_exposure", "treated_neighbor_exposure"], ascending=False)


def write_outputs(counties: pd.DataFrame, links: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    balance = pd.DataFrame([standardized_difference(counties, variable) for variable in BALANCE_VARS])
    balance.round(6).to_csv(outdir / "border_balance.csv", index=False)

    pair_balance = make_pair_balance(counties)
    pair_balance.to_csv(outdir / "pair_balance_audit.csv", index=False)

    spillovers = make_spillover_audit(counties, links)
    spillovers.round(6).to_csv(outdir / "spillover_exposure_audit.csv", index=False)

    flagged_pairs = set(pair_balance.loc[pair_balance["flag_large_balance_gap"] == 1, "pair_id"])
    high_spillover_controls = set(
        spillovers.loc[
            (spillovers["treated_policy_side"] == 0) & (spillovers["treated_neighbor_exposure"] > 1.25),
            "pair_id",
        ]
    )
    sensitivity_rows = []
    samples = {
        "all_pairs": counties,
        "drop_large_balance_gaps": counties.loc[~counties["pair_id"].isin(flagged_pairs)],
        "drop_high_control_exposure_pairs": counties.loc[~counties["pair_id"].isin(high_spillover_controls)],
        "drop_both_flags": counties.loc[~counties["pair_id"].isin(flagged_pairs | high_spillover_controls)],
    }
    for label, sample in samples.items():
        sensitivity_rows.append(
            {
                "sample": label,
                "border_pairs": int(sample["pair_id"].nunique()),
                "paired_treated_minus_control_growth": paired_effect(sample),
                "main_design_risk": "comparison changes when fragile or contaminated pairs are removed",
            }
        )
    pd.DataFrame(sensitivity_rows).round(6).to_csv(outdir / "comparison_set_sensitivity.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "diagnostic": "geography_role",
                "student_prompt": "Is the border the source of identification, a threat to inference, or the mechanism?",
                "teaching_point": "In this lab, the border is the source; proximity also creates inference and spillover threats.",
            },
            {
                "diagnostic": "spatial_inference",
                "student_prompt": "Does a larger Conley standard error change the identifying assumption?",
                "teaching_point": "No. It changes uncertainty, not bias from sorting or spillovers.",
            },
            {
                "diagnostic": "spillover_exposure",
                "student_prompt": "Are untreated counties close enough to treated counties to be partly exposed?",
                "teaching_point": "Contaminated controls are an estimand and bias issue, not only a standard-error issue.",
            },
            {
                "diagnostic": "balance",
                "student_prompt": "Which predetermined differences would make the border comparison less credible?",
                "teaching_point": "Border-pair fixed effects help only if local continuity is plausible.",
            },
        ]
    )
    prompts.to_csv(outdir / "diagnostic_prompts.csv", index=False)
    print(f"Wrote spatial-design diagnostics to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--counties", required=True, type=Path)
    parser.add_argument("--links", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    counties = pd.read_csv(args.counties)
    links = pd.read_csv(args.links)
    write_outputs(counties, links, args.outdir)


if __name__ == "__main__":
    main()
