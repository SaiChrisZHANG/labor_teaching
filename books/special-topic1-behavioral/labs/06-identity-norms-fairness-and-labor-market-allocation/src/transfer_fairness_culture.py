from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


FAIRNESS_ORDER = ["equal_pay", "underpaid_hidden", "underpaid_informed", "manager_salary_info", "compressed_pay"]
MESSAGE_ORDER = ["neutral", "collaborative", "competitive", "flexible", "inclusive_growth"]
MANAGER_ORDER = ["supportive_growth", "traditional_gatekeeping", "high_pressure_merit"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fairness-input", required=True)
    parser.add_argument("--culture-input", required=True)
    parser.add_argument("--manager-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fairness = pd.read_csv(args.fairness_input)
    fairness["comparison_arm"] = pd.Categorical(fairness["comparison_arm"], categories=FAIRNESS_ORDER, ordered=True)
    fairness_summary = (
        fairness.groupby("comparison_arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            wage=("wage", "mean"),
            peer_ref_wage=("peer_ref_wage", "mean"),
            manager_ref_wage=("manager_ref_wage", "mean"),
            comparison_info=("comparison_info", "mean"),
            transparency_depth=("transparency_depth", "mean"),
            peer_gap=("peer_gap", "mean"),
            fairness_cost=("fairness_cost", "mean"),
            morale_index=("morale_index", "mean"),
            effort_units=("effort_units", "mean"),
            quit_intent=("quit_intent", "mean"),
        )
        .sort_values("comparison_arm")
    )
    fairness_summary.to_csv(outdir / "pay_comparison_summary.csv", index=False)

    equal_pay = fairness_summary.loc[fairness_summary["comparison_arm"] == "equal_pay"].iloc[0]
    fairness_effects = fairness_summary.copy()
    for col in ["fairness_cost", "morale_index", "effort_units", "quit_intent"]:
        fairness_effects[f"{col}_vs_equal_pay"] = fairness_effects[col] - equal_pay[col]
    fairness_effects.to_csv(outdir / "pay_comparison_effects.csv", index=False)

    culture = pd.read_csv(args.culture_input)
    culture["culture_message"] = pd.Categorical(culture["culture_message"], categories=MESSAGE_ORDER, ordered=True)
    culture_summary = (
        culture.groupby(["culture_message", "worker_type"], observed=False, as_index=False)
        .agg(
            applicants=("applicant_id", "count"),
            culture_fit=("culture_fit", "mean"),
            apply_score=("apply_score", "mean"),
            accept_score=("accept_score", "mean"),
            expected_retention=("expected_retention", "mean"),
        )
        .sort_values(["culture_message", "worker_type"])
    )
    culture_summary.to_csv(outdir / "culture_sorting_summary.csv", index=False)

    manager = pd.read_csv(args.manager_input)
    manager["manager_norm"] = pd.Categorical(manager["manager_norm"], categories=MANAGER_ORDER, ordered=True)
    manager_summary = (
        manager.groupby("manager_norm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            support_index=("support_index", "mean"),
            promotion_standard=("promotion_standard", "mean"),
            conformity_pressure=("conformity_pressure", "mean"),
            culture_alignment=("culture_alignment", "mean"),
            promotion_score=("promotion_score", "mean"),
            retention_index=("retention_index", "mean"),
            local_norm_shift=("local_norm_shift", "mean"),
        )
        .sort_values("manager_norm")
    )
    manager_summary.to_csv(outdir / "manager_transmission_summary.csv", index=False)

    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.0))
    axes[0].bar(fairness_summary["comparison_arm"].astype(str), fairness_summary["morale_index"], color="#4C78A8")
    axes[0].set_ylabel("Morale index")
    axes[0].tick_params(axis="x", rotation=24)
    axes[0].spines[["top", "right"]].set_visible(False)

    best_fit = culture_summary.groupby("culture_message", observed=False, as_index=False)["culture_fit"].max()
    axes[1].bar(best_fit["culture_message"].astype(str), best_fit["culture_fit"], color="#59A14F")
    axes[1].set_ylabel("Best applicant culture fit")
    axes[1].tick_params(axis="x", rotation=24)
    axes[1].spines[["top", "right"]].set_visible(False)

    axes[2].plot(
        manager_summary["manager_norm"].astype(str),
        manager_summary["promotion_score"],
        marker="o",
        color="#F28E2B",
        label="Promotion score",
    )
    axes[2].plot(
        manager_summary["manager_norm"].astype(str),
        manager_summary["retention_index"] * 100,
        marker="o",
        color="#B07AA1",
        label="Retention x 100",
    )
    axes[2].set_ylabel("Manager outcomes")
    axes[2].tick_params(axis="x", rotation=20)
    axes[2].legend(frameon=False, fontsize=8)
    axes[2].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "fairness_culture_transfer.png", dpi=180)
    plt.close(fig)

    note = (
        "The transfer path uses synthetic data to classify fairness, pay "
        "comparison, culture sorting, and manager-transmission designs. It "
        "distinguishes reference groups, labor margins, identifying variation, "
        "and treatment versus sorting versus transmission claims.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
