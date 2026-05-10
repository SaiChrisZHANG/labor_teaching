from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


GIFT_ORDER = ["control", "cash_gift", "noncash_gift", "piece_rate", "employer_return"]
KNOWLEDGE_ORDER = ["low_knowledge", "high_knowledge"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gift-input", required=True)
    parser.add_argument("--schedule-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    gift = pd.read_csv(args.gift_input)
    gift["arm"] = pd.Categorical(gift["arm"], categories=GIFT_ORDER, ordered=True)
    gift_summary = (
        gift.groupby("arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            gift_value=("gift_value", "mean"),
            piece_rate=("piece_rate", "mean"),
            employer_effort=("employer_effort", "mean"),
            reciprocity_index=("reciprocity_index", "mean"),
            effort_minutes=("effort_minutes", "mean"),
            output_units=("output_units", "mean"),
            quality_score=("quality_score", "mean"),
            value_created=("value_created", "mean"),
        )
        .sort_values("arm")
    )
    gift_summary.to_csv(outdir / "gift_exchange_method_summary.csv", index=False)

    control = gift_summary.loc[gift_summary["arm"] == "control"].iloc[0]
    moment_rows = []
    for _, row in gift_summary.iterrows():
        moment_rows.append(
            {
                "arm": row["arm"],
                "moment": "effort_response_vs_control",
                "data_moment": row["effort_minutes"] - control["effort_minutes"],
                "structural_use": "reciprocity or incentive response",
            }
        )
        moment_rows.append(
            {
                "arm": row["arm"],
                "moment": "value_response_vs_control",
                "data_moment": row["value_created"] - control["value_created"],
                "structural_use": "productivity value of effort response",
            }
        )
        moment_rows.append(
            {
                "arm": row["arm"],
                "moment": "quality_response_vs_control",
                "data_moment": row["quality_score"] - control["quality_score"],
                "structural_use": "quality-adjusted effort and task motivation",
            }
        )
    pd.DataFrame(moment_rows).to_csv(outdir / "gift_exchange_moment_targets.csv", index=False)

    schedule = pd.read_csv(args.schedule_input)
    schedule["knowledge_group"] = pd.Categorical(
        schedule["knowledge_group"], categories=KNOWLEDGE_ORDER, ordered=True
    )
    schedule["distance_bin"] = pd.cut(
        schedule["distance_to_kink"],
        bins=[-4000, -2000, -1000, -500, 500, 1000, 2000, 4000],
        include_lowest=True,
    )
    schedule_summary = (
        schedule.groupby(["knowledge_group", "distance_bin"], observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            mean_observed_earnings=("observed_earnings", "mean"),
            mean_schedule_knowledge=("schedule_knowledge", "mean"),
            mean_phaseout_rate=("phaseout_rate", "mean"),
        )
        .sort_values(["knowledge_group", "distance_bin"])
    )
    schedule_summary.to_csv(outdir / "schedule_bunching_summary.csv", index=False)

    elasticity_rows = []
    for group, group_df in schedule.groupby("knowledge_group", observed=False):
        near = group_df.loc[group_df["distance_to_kink"].abs() <= 500, "worker_id"].count()
        left = group_df.loc[
            (group_df["distance_to_kink"] < -500) & (group_df["distance_to_kink"] >= -1500),
            "worker_id",
        ].count()
        right = group_df.loc[
            (group_df["distance_to_kink"] > 500) & (group_df["distance_to_kink"] <= 1500),
            "worker_id",
        ].count()
        counterfactual = max(1.0, (left + right) / 2)
        excess_mass = near - counterfactual
        delta_b_over_b = excess_mass / counterfactual
        delta_net_of_tax = 0.21
        elasticity_rows.append(
            {
                "knowledge_group": group,
                "near_kink_count": near,
                "shoulder_counterfactual": counterfactual,
                "excess_mass": excess_mass,
                "delta_b_over_b": delta_b_over_b,
                "delta_net_of_tax": delta_net_of_tax,
                "local_elasticity_analog": delta_b_over_b / delta_net_of_tax,
                "interpretation_limit": "local response combines preferences, knowledge, salience, and adjustment costs",
            }
        )
    elasticity = pd.DataFrame(elasticity_rows)
    elasticity.to_csv(outdir / "schedule_local_elasticity.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    axes[0].bar(gift_summary["arm"].astype(str), gift_summary["value_created"], color="#4C78A8")
    axes[0].set_ylabel("Value created")
    axes[0].tick_params(axis="x", rotation=24)
    axes[0].spines[["top", "right"]].set_visible(False)

    for group in KNOWLEDGE_ORDER:
        group_bins = schedule_summary.loc[schedule_summary["knowledge_group"] == group]
        axes[1].plot(
            group_bins["distance_bin"].astype(str),
            group_bins["workers"],
            marker="o",
            label=group,
        )
    axes[1].set_ylabel("Workers by distance bin")
    axes[1].tick_params(axis="x", rotation=24)
    axes[1].legend(frameon=False, fontsize=8)
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "method_bridge_transfer.png", dpi=180)
    plt.close(fig)

    note = (
        "The transfer path links workplace gift-exchange moments to structural "
        "parameter-recovery logic and links nonlinear schedule data to a "
        "bunching/local-elasticity diagnostic. The files are synthetic teaching "
        "artifacts, not official replication data.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
