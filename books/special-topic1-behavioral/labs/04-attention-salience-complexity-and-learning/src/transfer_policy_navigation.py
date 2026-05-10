from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ARM_ORDER = ["control", "information", "reminder", "simplified", "info_simplified"]
CONTRACT_ORDER = ["simple", "opaque", "opaque_with_tutorial"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy-input", required=True)
    parser.add_argument("--workplace-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    policy = pd.read_csv(args.policy_input)
    policy["arm"] = pd.Categorical(policy["arm"], categories=ARM_ORDER, ordered=True)
    policy_summary = (
        policy.groupby("arm", observed=False, as_index=False)
        .agg(
            applicants=("applicant_id", "count"),
            eligible_rate=("eligible", "mean"),
            information_index=("information_index", "mean"),
            salience_index=("salience_index", "mean"),
            hassle_index=("hassle_index", "mean"),
            perceived_eligibility=("perceived_eligibility", "mean"),
            completed_claim=("completed_claim", "mean"),
            take_up=("take_up", "mean"),
        )
        .sort_values("arm")
    )
    policy_summary.to_csv(outdir / "policy_navigation_summary.csv", index=False)

    control = policy_summary.loc[policy_summary["arm"] == "control"].iloc[0]
    policy_effects = policy_summary.copy()
    for col in ["information_index", "salience_index", "hassle_index", "perceived_eligibility", "take_up"]:
        policy_effects[f"{col}_vs_control"] = policy_effects[col] - control[col]
    policy_effects.to_csv(outdir / "policy_navigation_effects.csv", index=False)

    workplace = pd.read_csv(args.workplace_input)
    workplace["contract"] = pd.Categorical(workplace["contract"], categories=CONTRACT_ORDER, ordered=True)
    workplace_summary = (
        workplace.groupby("contract", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            true_bonus_rate=("true_bonus_rate", "mean"),
            perceived_bonus_rate=("perceived_bonus_rate", "mean"),
            perception_gap=("perception_gap", "mean"),
            attention_minutes=("attention_minutes", "mean"),
            effort_units=("effort_units", "mean"),
            bonus_earned=("bonus_earned", "mean"),
        )
        .sort_values("contract")
    )
    workplace_summary.to_csv(outdir / "workplace_complexity_summary.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.2))
    axes[0].bar(policy_summary["arm"].astype(str), policy_summary["take_up"], color="#59A14F")
    axes[0].set_ylabel("Take-up rate")
    axes[0].set_ylim(0, 1)
    axes[0].tick_params(axis="x", rotation=25)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(workplace_summary["contract"].astype(str), workplace_summary["effort_units"], color="#4C78A8")
    axes[1].set_ylabel("Effort units")
    axes[1].tick_params(axis="x", rotation=20)
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "policy_navigation_and_complexity.png", dpi=180)
    plt.close(fig)

    note = (
        "The transfer path uses synthetic data to classify policy-navigation "
        "effects into information, salience, hassle, and perceived eligibility "
        "objects, then applies the same logic to workplace incentive opacity and "
        "effort. These are teaching analogs, not official replications.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
