from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ORDER = ["control", "information", "information_planning"]
LABELS = ["Control", "Information", "Information +\nplanning"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    summary = (
        df.groupby("arm", as_index=False)
        .agg(
            seekers=("seeker_id", "count"),
            weekly_applications=("weekly_applications", "mean"),
            subjective_job_finding_prob=("subjective_job_finding_prob", "mean"),
            employed_within_8_weeks=("employed_within_8_weeks", "mean"),
        )
        .set_index("arm")
        .loc[ORDER]
        .reset_index()
    )
    summary.to_csv(outdir / "search_arm_summary.csv", index=False)

    control = summary.loc[summary["arm"] == "control"].iloc[0]
    effects = summary.copy()
    for col in ["weekly_applications", "subjective_job_finding_prob", "employed_within_8_weeks"]:
        effects[f"{col}_vs_control"] = effects[col] - control[col]
    effects.to_csv(outdir / "search_effects.csv", index=False)

    fig, ax1 = plt.subplots(figsize=(8, 4.8))
    x = range(len(summary))
    ax1.bar(x, summary["weekly_applications"], color="#4C78A8", label="Applications")
    ax1.set_ylabel("Weekly applications")
    ax1.set_xticks(list(x), LABELS)
    ax1.spines[["top", "right"]].set_visible(False)
    ax2 = ax1.twinx()
    ax2.plot(x, summary["subjective_job_finding_prob"], color="#F28E2B", marker="o", label="Belief")
    ax2.set_ylabel("Subjective job-finding probability")
    ax2.set_ylim(0, 0.55)
    ax2.spines["top"].set_visible(False)
    fig.tight_layout()
    fig.savefig(outdir / "transfer_job_search.png", dpi=180)
    plt.close(fig)

    note = (
        "The transfer exercise classifies the intervention as an information and "
        "planning design. The direct margin is search effort; the inferred object "
        "may include beliefs, attention, and motivation.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
