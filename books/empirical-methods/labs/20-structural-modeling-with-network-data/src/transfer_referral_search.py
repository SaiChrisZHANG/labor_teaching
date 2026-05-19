"""Transfer the structural network workflow to referral-search counterfactuals."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from network_structural_utils import fit_ols, model_rows, predict_ols


CALLBACK_COLS = [
    "tie_strength",
    "signal_quality",
    "same_group",
    "applicant_skill",
    "referrer_access",
    "applicant_group_b",
]


def prepare(data: pd.DataFrame) -> pd.DataFrame:
    out = data.copy()
    out["applicant_group_b"] = (out["applicant_group"] == "B").astype(int)
    return out


def summarize_policy(scenario: str, data: pd.DataFrame, callback_result) -> dict[str, float | str | int]:
    active = prepare(data.loc[data["observed_referral"] == 1].copy())
    active["predicted_callback"] = np.clip(
        predict_ols(active, callback_result, CALLBACK_COLS),
        0.01,
        0.99,
    )
    group_means = active.groupby("applicant_group")["predicted_callback"].mean().to_dict()
    return {
        "scenario": scenario,
        "referral_count": int(len(active)),
        "cross_group_share": float(active["cross_group"].mean()),
        "mean_tie_strength": float(active["tie_strength"].mean()),
        "mean_signal_quality": float(active["signal_quality"].mean()),
        "mean_predicted_callback": float(active["predicted_callback"].mean()),
        "group_a_predicted_callback": float(group_means.get("A", np.nan)),
        "group_b_predicted_callback": float(group_means.get("B", np.nan)),
        "a_minus_b_callback_gap": float(group_means.get("A", np.nan) - group_means.get("B", np.nan)),
    }


def build_cross_group_policy(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    policy = data.copy()
    candidates = policy.loc[(policy["observed_referral"] == 0) & (policy["cross_group"] == 1)].copy()
    candidates["policy_score"] = (
        candidates["observed_referral_probability"]
        + 0.35 * candidates["referrer_access"]
        + 0.20 * candidates["applicant_skill"]
        + 0.10 * candidates["signal_quality"]
    )
    additions = candidates.nlargest(80, "policy_score").copy()
    addition_ids = set(additions["opportunity_id"])
    policy["policy_added_referral"] = policy["opportunity_id"].isin(addition_ids).astype(int)
    policy.loc[policy["policy_added_referral"] == 1, "observed_referral"] = 1
    policy.loc[policy["policy_added_referral"] == 1, "tie_strength"] = np.clip(
        policy.loc[policy["policy_added_referral"] == 1, "tie_strength"] + 0.16,
        0.0,
        0.98,
    )
    policy.loc[policy["policy_added_referral"] == 1, "signal_quality"] = np.clip(
        policy.loc[policy["policy_added_referral"] == 1, "signal_quality"] + 0.10,
        0.0,
        0.98,
    )
    return policy, additions[
        [
            "opportunity_id",
            "referrer_id",
            "applicant_id",
            "referrer_group",
            "applicant_group",
            "tie_strength",
            "signal_quality",
            "policy_score",
        ]
    ]


def prompts() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "stage": "transfer",
                "prompt": "What is the economic meaning of an added cross-group referral opportunity?",
            },
            {
                "stage": "transfer",
                "prompt": "Which part of the exercise is behavior on observed links and which part is link formation?",
            },
            {
                "stage": "transfer",
                "prompt": "How does the applicant-group callback gap change under the cross-group subsidy?",
            },
            {
                "stage": "transfer",
                "prompt": "What real-world evidence would be needed before treating the simulated policy as credible?",
            },
        ]
    )


def run(referrals_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    referrals = pd.read_csv(referrals_path)
    observed = prepare(referrals.loc[referrals["observed_referral"] == 1].copy())
    callback_result = fit_ols(observed, "callback", CALLBACK_COLS)
    pd.DataFrame(model_rows(callback_result, "observed_referral_callback_lpm")).to_csv(
        outdir / "callback_model_estimates.csv",
        index=False,
    )

    baseline = referrals.copy()
    fixed_info = referrals.copy()
    fixed_info.loc[fixed_info["observed_referral"] == 1, "signal_quality"] = np.clip(
        fixed_info.loc[fixed_info["observed_referral"] == 1, "signal_quality"] + 0.08,
        0.0,
        0.98,
    )
    cross_group_policy, additions = build_cross_group_policy(referrals)

    scenario_rows = [
        summarize_policy("baseline_observed_referrals", baseline, callback_result),
        summarize_policy("fixed_referral_better_information", fixed_info, callback_result),
        summarize_policy("endogenous_cross_group_referral_policy", cross_group_policy, callback_result),
    ]
    pd.DataFrame(scenario_rows).to_csv(outdir / "referral_policy_counterfactuals.csv", index=False)
    additions.to_csv(outdir / "added_cross_group_referrals.csv", index=False)

    access_summary = (
        observed.groupby("applicant_group", as_index=False)
        .agg(
            observed_referrals=("opportunity_id", "count"),
            callback_rate=("callback", "mean"),
            mean_tie_strength=("tie_strength", "mean"),
            mean_signal_quality=("signal_quality", "mean"),
            cross_group_share=("cross_group", "mean"),
        )
    )
    access_summary.to_csv(outdir / "referral_access_summary.csv", index=False)
    prompts().to_csv(outdir / "transfer_prompts.csv", index=False)

    print(f"Wrote transfer outputs to {outdir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--referrals", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()
    run(args.referrals, args.outdir)


if __name__ == "__main__":
    main()
