from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def belief_bin(value: float) -> str:
    if value < 0.20:
        return "low"
    if value < 0.32:
        return "middle"
    return "high"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    summary = (
        df.groupby("duration_week", as_index=False)
        .agg(
            observations=("seeker_id", "count"),
            subjective_prob=("subjective_job_find_prob_4wk", "mean"),
            model_predicted_prob=("model_predicted_prob_4wk", "mean"),
            realized_exit_rate=("realized_exit_next_4wk", "mean"),
            applications=("applications_last_week", "mean"),
            reservation_wage=("reservation_wage", "mean"),
        )
        .sort_values("duration_week")
    )
    summary["subjective_minus_realized"] = summary["subjective_prob"] - summary["realized_exit_rate"]
    summary.to_csv(outdir / "belief_duration_summary.csv", index=False)

    df["belief_bin"] = df["subjective_job_find_prob_4wk"].map(belief_bin)
    calibration = (
        df.groupby("belief_bin", as_index=False)
        .agg(
            observations=("seeker_id", "count"),
            subjective_prob=("subjective_job_find_prob_4wk", "mean"),
            realized_exit_rate=("realized_exit_next_4wk", "mean"),
            applications=("applications_last_week", "mean"),
        )
        .sort_values("subjective_prob")
    )
    calibration["subjective_minus_realized"] = calibration["subjective_prob"] - calibration["realized_exit_rate"]
    calibration.to_csv(outdir / "belief_calibration_by_bin.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2))
    axes[0].plot(summary["duration_week"], summary["subjective_prob"], marker="o", label="Subjective belief")
    axes[0].plot(summary["duration_week"], summary["realized_exit_rate"], marker="o", label="Realized exit")
    axes[0].plot(summary["duration_week"], summary["model_predicted_prob"], marker="o", label="Model prediction")
    axes[0].set_xlabel("Unemployment duration week")
    axes[0].set_ylabel("Four-week probability")
    axes[0].set_ylim(0, 0.40)
    axes[0].legend(frameon=False, fontsize=8)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(summary["duration_week"].astype(str), summary["applications"], color="#4C78A8")
    axes[1].set_xlabel("Unemployment duration week")
    axes[1].set_ylabel("Applications last week")
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "job_search_beliefs_duration.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic belief-panel data to compare "
        "subjective job-finding probabilities, model-predicted probabilities, "
        "realized exits, applications, and reservation wages by unemployment "
        "duration. It is not an official replication of Mueller, Spinnewijn, "
        "and Topa.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
