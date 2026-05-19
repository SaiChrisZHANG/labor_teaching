"""Run the Week 11 source-to-target transportability exercise."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from policy_learning_utils import (
    NUMERIC_FEATURES,
    apply_policy,
    effective_sample_size,
    ensure_outdir,
    evaluate_policies,
    fairness_audit,
    fit_nuisance,
    make_policy_candidates,
    policy_by_name,
    predict_nuisance,
    select_policy,
    source_target_cell_weights,
    split_train_eval,
    true_policy_value,
)


def source_target_covariates(source: pd.DataFrame, target: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for column in NUMERIC_FEATURES:
        rows.append(
            {
                "variable": column,
                "source_mean": float(source[column].mean()),
                "target_mean": float(target[column].mean()),
                "target_minus_source": float(target[column].mean() - source[column].mean()),
            }
        )
    for region in sorted(set(source["region"]).union(set(target["region"]))):
        rows.append(
            {
                "variable": f"share_region_{region}",
                "source_mean": float((source["region"] == region).mean()),
                "target_mean": float((target["region"] == region).mean()),
                "target_minus_source": float((target["region"] == region).mean() - (source["region"] == region).mean()),
            }
        )
    for group in sorted(set(source["demographic_group"]).union(set(target["demographic_group"]))):
        rows.append(
            {
                "variable": f"share_demographic_{group}",
                "source_mean": float((source["demographic_group"] == group).mean()),
                "target_mean": float((target["demographic_group"] == group).mean()),
                "target_minus_source": float(
                    (target["demographic_group"] == group).mean() - (source["demographic_group"] == group).mean()
                ),
            }
        )
    return pd.DataFrame(rows)


def subgroup_shift(source: pd.DataFrame, target: pd.DataFrame) -> pd.DataFrame:
    cuts = np.quantile(source["baseline_risk"], [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    cuts[0] = -np.inf
    cuts[-1] = np.inf
    labels = ["low", "middle", "high"]
    source_tmp = source.copy()
    target_tmp = target.copy()
    source_tmp["risk_group"] = pd.cut(source_tmp["baseline_risk"], bins=cuts, labels=labels, include_lowest=True)
    target_tmp["risk_group"] = pd.cut(target_tmp["baseline_risk"], bins=cuts, labels=labels, include_lowest=True)
    rows: list[dict[str, object]] = []
    for group in labels:
        s = source_tmp[source_tmp["risk_group"] == group]
        t = target_tmp[target_tmp["risk_group"] == group]
        rows.append(
            {
                "risk_group": group,
                "source_share": float(len(s) / len(source_tmp)),
                "target_share": float(len(t) / len(target_tmp)),
                "source_mean_true_net_effect": float(s["true_net_effect"].mean()) if len(s) else float("nan"),
                "target_mean_true_net_effect": float(t["true_net_effect"].mean()) if len(t) else float("nan"),
            }
        )
    return pd.DataFrame(rows)


def run(source_input: Path, target_input: Path, outdir: Path, capacity: float = 0.35) -> None:
    ensure_outdir(outdir)
    source = split_train_eval(pd.read_csv(source_input))
    target = pd.read_csv(target_input)
    train = source[source["analysis_split"] == "train"].copy()
    source_eval = source[source["analysis_split"] == "eval"].copy()

    models = fit_nuisance(train)
    train_pred = predict_nuisance(train, models)
    source_pred = predict_nuisance(source_eval, models)
    target_pred = predict_nuisance(target, models)
    policies = make_policy_candidates(train, train_pred, capacity=capacity)

    training_values = evaluate_policies(train, train_pred, policies)
    selected_name = select_policy(training_values)
    selected_policy = policy_by_name(policies, selected_name)

    weights, weight_cells = source_target_cell_weights(source_eval, target)
    source_values = evaluate_policies(source_eval, source_pred, policies)
    weighted_source_values = evaluate_policies(source_eval, source_pred, policies, weights=weights)

    rows: list[dict[str, object]] = []
    for policy in policies:
        source_assignment = apply_policy(source_eval, source_pred, policy)
        target_assignment = apply_policy(target, target_pred, policy)
        source_value = float(source_values.loc[source_values["policy"] == policy.name, "dr_value"].iloc[0])
        weighted_value = float(weighted_source_values.loc[weighted_source_values["policy"] == policy.name, "dr_value"].iloc[0])
        target_value = true_policy_value(target, target_assignment)
        rows.append(
            {
                "policy": policy.name,
                "selected_by_source_training_value": policy.name == selected_name,
                "source_eval_dr_value": source_value,
                "source_eval_target_weighted_dr_value": weighted_value,
                "target_true_value_synthetic": target_value,
                "target_minus_weighted_source_value": target_value - weighted_value,
                "source_assignment_rate": float(source_assignment.mean()),
                "target_assignment_rate": float(target_assignment.mean()),
            }
        )
    pd.DataFrame(rows).to_csv(outdir / "policy_transfer_values.csv", index=False)

    source_target_covariates(source_eval, target).to_csv(outdir / "source_vs_target_covariates.csv", index=False)
    weight_cells.to_csv(outdir / "transport_weight_cells.csv", index=False)
    pd.DataFrame(
        [
            {
                "n_source_eval": int(len(source_eval)),
                "n_target": int(len(target)),
                "weight_min": float(weights.min()),
                "weight_p50": float(np.quantile(weights, 0.50)),
                "weight_p90": float(np.quantile(weights, 0.90)),
                "weight_max": float(weights.max()),
                "effective_source_sample_size": effective_sample_size(weights),
            }
        ]
    ).to_csv(outdir / "transport_weight_summary.csv", index=False)
    subgroup_shift(source_eval, target).to_csv(outdir / "subgroup_shift.csv", index=False)

    selected_source_assignment = apply_policy(source_eval, source_pred, selected_policy)
    selected_target_assignment = apply_policy(target, target_pred, selected_policy)
    source_fairness = fairness_audit(source_eval, source_pred, selected_source_assignment)
    source_fairness["sample"] = "source_eval"
    target_fairness = fairness_audit(target, target_pred, selected_target_assignment)
    target_fairness["sample"] = "target"
    pd.concat([source_fairness, target_fairness], ignore_index=True).to_csv(
        outdir / "fairness_transfer_audit.csv",
        index=False,
    )

    pd.DataFrame(
        [
            {
                "step": "covariate_shift",
                "prompt": "Use source_vs_target_covariates.csv and subgroup_shift.csv to describe how the target population differs from the source evaluation sample.",
            },
            {
                "step": "target_weighting",
                "prompt": "Use transport_weight_summary.csv to decide whether source-to-target reweighting leaves enough effective support.",
            },
            {
                "step": "policy_transfer",
                "prompt": "Compare source_eval_target_weighted_dr_value with target_true_value_synthetic for the selected rule.",
            },
            {
                "step": "fairness",
                "prompt": "Use fairness_transfer_audit.csv to ask whether the source-trained rule changes assignment disparities in the target population.",
            },
        ]
    ).to_csv(outdir / "transfer_design_prompts.csv", index=False)

    print(f"Selected source-trained policy: {selected_name}")
    print(f"Wrote transfer outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-input", type=Path, required=True)
    parser.add_argument("--target-input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--capacity", type=float, default=0.35)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.source_input, args.target_input, args.outdir, capacity=args.capacity)


if __name__ == "__main__":
    main()
