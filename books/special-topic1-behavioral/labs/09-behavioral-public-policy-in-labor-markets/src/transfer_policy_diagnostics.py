from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


KNOWLEDGE_ORDER = ["low_knowledge", "high_knowledge"]
DEFAULT_ORDER = ["opt_in", "auto_enroll_3", "auto_enroll_6", "active_choice", "commitment_escalation"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--eitc-input", required=True)
    parser.add_argument("--default-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    eitc = pd.read_csv(args.eitc_input)
    eitc["knowledge_group"] = pd.Categorical(
        eitc["knowledge_group"], categories=KNOWLEDGE_ORDER, ordered=True
    )
    eitc_summary = (
        eitc.groupby(["knowledge_group", "segment"], observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            mean_observed_earnings=("observed_earnings", "mean"),
            mean_local_knowledge=("local_knowledge", "mean"),
            mean_perceived_subsidy=("perceived_subsidy", "mean"),
            mean_adjustment_cost=("adjustment_cost", "mean"),
        )
        .sort_values(["knowledge_group", "segment"])
    )
    eitc_summary.to_csv(outdir / "eitc_knowledge_summary.csv", index=False)

    local_rows = []
    for group, group_df in eitc.groupby("knowledge_group", observed=False):
        near = group_df.loc[group_df["distance_to_phasein_end"].abs() <= 500, "worker_id"].count()
        left = group_df.loc[
            (group_df["distance_to_phasein_end"] < -500)
            & (group_df["distance_to_phasein_end"] >= -1500),
            "worker_id",
        ].count()
        right = group_df.loc[
            (group_df["distance_to_phasein_end"] > 500)
            & (group_df["distance_to_phasein_end"] <= 1500),
            "worker_id",
        ].count()
        counterfactual = max(1.0, (left + right) / 2)
        excess_mass = near - counterfactual
        local_rows.append(
            {
                "knowledge_group": group,
                "near_phasein_end_count": near,
                "shoulder_counterfactual": counterfactual,
                "excess_mass": excess_mass,
                "excess_mass_ratio": excess_mass / counterfactual,
                "interpretation_limit": "local response combines knowledge, salience, preferences, and adjustment costs",
            }
        )
    local_response = pd.DataFrame(local_rows)
    local_response.to_csv(outdir / "eitc_local_response_diagnostic.csv", index=False)

    defaults = pd.read_csv(args.default_input)
    defaults["arm"] = pd.Categorical(defaults["arm"], categories=DEFAULT_ORDER, ordered=True)
    default_summary = (
        defaults.groupby("arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            default_rate=("default_rate", "mean"),
            active_prompt=("active_prompt", "mean"),
            commitment=("commitment", "mean"),
            participation=("participation", "mean"),
            chosen_rate=("chosen_rate", "mean"),
            benchmark_rate=("benchmark_rate", "mean"),
            welfare_gap=("welfare_gap", "mean"),
            welfare_score=("welfare_score", "mean"),
        )
        .sort_values("arm")
    )
    default_summary.to_csv(outdir / "default_welfare_summary.csv", index=False)

    diagnostic_rows = [
        {
            "setting": "benefit_take_up",
            "policy_tool": "salience, simplification, assistance",
            "friction_role": "implementation friction and possible correction",
            "main_method": "randomized field experiment with ANCOVA and take-up hazard summaries",
            "welfare_benchmark": "claiming under clear eligibility and lower procedural cost",
        },
        {
            "setting": "eitc_knowledge",
            "policy_tool": "local information and schedule knowledge",
            "friction_role": "dynamic learning and perceived incentive modifier",
            "main_method": "local response by knowledge group and schedule-segment diagnostics",
            "welfare_benchmark": "earnings choice under accurate schedule perception",
        },
        {
            "setting": "retirement_defaults",
            "policy_tool": "default, active choice, commitment",
            "friction_role": "lever to harness and welfare complication",
            "main_method": "treatment comparisons with calibrated benchmark-choice gap",
            "welfare_benchmark": "contribution rate under stable long-run saving objective",
        },
    ]
    pd.DataFrame(diagnostic_rows).to_csv(outdir / "policy_diagnostic_map.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.2))
    for group in KNOWLEDGE_ORDER:
        group_df = eitc_summary.loc[eitc_summary["knowledge_group"] == group]
        axes[0].plot(
            group_df["segment"],
            group_df["mean_observed_earnings"],
            marker="o",
            linewidth=1.3,
            label=group,
        )
    axes[0].set_ylabel("Mean observed earnings")
    axes[0].legend(frameon=False, fontsize=8)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(default_summary["arm"].astype(str), default_summary["welfare_gap"], color="#E15759")
    axes[1].set_ylabel("Mean benchmark-choice gap")
    axes[1].tick_params(axis="x", rotation=24)
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "policy_transfer_diagnostics.png", dpi=180)
    plt.close(fig)

    note = (
        "The transfer path moves from take-up to EITC local knowledge and "
        "retirement default welfare diagnostics. The files are synthetic "
        "teaching artifacts, not official replication data.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
