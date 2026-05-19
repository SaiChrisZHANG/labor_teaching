"""Run the Week 11 policy-learning reproduction path."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from policy_learning_utils import (
    apply_policy,
    cate_by_risk_group,
    ensure_outdir,
    evaluate_policies,
    fairness_audit,
    fit_nuisance,
    make_policy_candidates,
    overlap_diagnostics,
    policy_by_name,
    predict_nuisance,
    select_policy,
    split_train_eval,
    add_regret,
)


def run(input_path: Path, outdir: Path, capacity: float = 0.35) -> None:
    ensure_outdir(outdir)
    df = split_train_eval(pd.read_csv(input_path))
    train = df[df["analysis_split"] == "train"].copy()
    eval_df = df[df["analysis_split"] == "eval"].copy()

    models = fit_nuisance(train)
    train_pred = predict_nuisance(train, models)
    eval_pred = predict_nuisance(eval_df, models)
    policies = make_policy_candidates(train, train_pred, capacity=capacity)

    training_values = evaluate_policies(train, train_pred, policies)
    selected_name = select_policy(training_values)
    selected_policy = policy_by_name(policies, selected_name)
    eval_values = add_regret(evaluate_policies(eval_df, eval_pred, policies))
    eval_values["selected_by_training_value"] = eval_values["policy"] == selected_name

    selected_assignment_eval = apply_policy(eval_df, eval_pred, selected_policy)
    selected_assignment_train = apply_policy(train, train_pred, selected_policy)

    training_values.to_csv(outdir / "policy_training_values.csv", index=False)
    eval_values.to_csv(outdir / "policy_value_comparison.csv", index=False)
    cate_by_risk_group(eval_df, eval_pred).to_csv(outdir / "cate_by_subgroup.csv", index=False)
    overlap_diagnostics(eval_df, eval_pred, selected_assignment_eval).to_csv(outdir / "overlap_diagnostics.csv", index=False)
    fairness_audit(eval_df, eval_pred, selected_assignment_eval).to_csv(outdir / "fairness_audit.csv", index=False)

    pd.DataFrame(
        [
            {
                "selected_policy": selected_policy.name,
                "description": selected_policy.description,
                "policy_kind": selected_policy.kind,
                "feature": selected_policy.feature,
                "direction": selected_policy.direction,
                "threshold": selected_policy.threshold,
                "capacity": capacity,
                "train_assignment_rate": float(selected_assignment_train.mean()),
                "eval_assignment_rate": float(selected_assignment_eval.mean()),
            }
        ]
    ).to_csv(outdir / "learned_policy_rule.csv", index=False)

    pd.DataFrame(
        [
            {
                "step": "reproduce",
                "prompt": "Define the policy class and explain why the selected rule is a welfare object rather than a prediction score.",
            },
            {
                "step": "diagnose",
                "prompt": "Use policy_value_comparison.csv to compare held-out value and regret across rules.",
            },
            {
                "step": "overlap",
                "prompt": "Use overlap_diagnostics.csv to decide whether the targeted group has treated and untreated support.",
            },
            {
                "step": "fairness",
                "prompt": "Use fairness_audit.csv to report assignment-rate differences across demographic groups.",
            },
        ]
    ).to_csv(outdir / "diagnostic_prompts.csv", index=False)

    print(f"Selected policy: {selected_name}")
    print(f"Wrote policy-learning outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--capacity", type=float, default=0.35)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.input, args.outdir, capacity=args.capacity)


if __name__ == "__main__":
    main()
