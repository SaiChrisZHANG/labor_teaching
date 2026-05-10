from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


MONITORING_ORDER = ["control", "pay_only", "monitoring_only", "pay_monitoring", "digital_dashboard"]
EVALUATION_ORDER = ["objective_metric", "subjective_low_discretion", "subjective_high_discretion"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--monitoring-input", required=True)
    parser.add_argument("--evaluation-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    monitoring = pd.read_csv(args.monitoring_input)
    monitoring["arm"] = pd.Categorical(monitoring["arm"], categories=MONITORING_ORDER, ordered=True)
    monitoring_summary = (
        monitoring.groupby("arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            bonus_rate=("bonus_rate", "mean"),
            monitoring_intensity=("monitoring_intensity", "mean"),
            feedback_score=("feedback_score", "mean"),
            relational_motivation=("relational_motivation", "mean"),
            visible_effort=("visible_effort", "mean"),
            productive_output=("productive_output", "mean"),
            compliance_actions=("compliance_actions", "mean"),
            gaming_score=("gaming_score", "mean"),
        )
        .sort_values("arm")
    )
    monitoring_summary.to_csv(outdir / "monitoring_summary.csv", index=False)

    control = monitoring_summary.loc[monitoring_summary["arm"] == "control"].iloc[0]
    monitoring_effects = monitoring_summary.copy()
    for col in ["visible_effort", "productive_output", "compliance_actions", "gaming_score", "relational_motivation"]:
        monitoring_effects[f"{col}_vs_control"] = monitoring_effects[col] - control[col]
    monitoring_effects.to_csv(outdir / "monitoring_effects.csv", index=False)

    evaluation = pd.read_csv(args.evaluation_input)
    evaluation["regime"] = pd.Categorical(evaluation["regime"], categories=EVALUATION_ORDER, ordered=True)
    evaluation_summary = (
        evaluation.groupby("regime", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            evaluation_weight=("evaluation_weight", "mean"),
            discretion=("discretion", "mean"),
            influence_activity=("influence_activity", "mean"),
            productive_effort=("productive_effort", "mean"),
            objective_output=("objective_output", "mean"),
            subjective_rating=("subjective_rating", "mean"),
            pay_index=("pay_index", "mean"),
        )
        .sort_values("regime")
    )
    evaluation_summary.to_csv(outdir / "subjective_evaluation_summary.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2))
    axes[0].plot(
        monitoring_summary["arm"].astype(str),
        monitoring_summary["productive_output"],
        marker="o",
        label="Productive output",
    )
    axes[0].plot(
        monitoring_summary["arm"].astype(str),
        monitoring_summary["gaming_score"] * 100,
        marker="o",
        label="Gaming score x 100",
    )
    axes[0].set_ylabel("Monitoring outcomes")
    axes[0].tick_params(axis="x", rotation=22)
    axes[0].legend(frameon=False, fontsize=8)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(
        evaluation_summary["regime"].astype(str),
        evaluation_summary["influence_activity"],
        color="#F28E2B",
        label="Influence activity",
    )
    axes[1].plot(
        evaluation_summary["regime"].astype(str),
        evaluation_summary["objective_output"] / 10,
        marker="o",
        color="#4C78A8",
        label="Objective output / 10",
    )
    axes[1].set_ylabel("Subjective evaluation outcomes")
    axes[1].tick_params(axis="x", rotation=20)
    axes[1].legend(frameon=False, fontsize=8)
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "monitoring_and_evaluation.png", dpi=180)
    plt.close(fig)

    note = (
        "The transfer path uses synthetic data to classify monitoring and "
        "subjective-evaluation effects. It distinguishes pay, observation, "
        "feedback, productive output, compliance, gaming, subjective ratings, "
        "and influence activity. These are teaching analogs, not official "
        "replications.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
