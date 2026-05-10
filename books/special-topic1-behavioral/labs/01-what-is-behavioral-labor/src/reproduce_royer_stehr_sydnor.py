from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ORDER = ["control", "incentive", "commitment", "incentive_commitment"]
LABELS = ["Control", "Incentive", "Commitment", "Incentive +\ncommitment"]


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
            workers=("worker_id", "count"),
            baseline_participation=("baseline_participation", "mean"),
            program_participation=("program_participation", "mean"),
            post_participation=("post_participation", "mean"),
            commitment_takeup=("commitment_takeup", "mean"),
        )
        .set_index("arm")
        .loc[ORDER]
        .reset_index()
    )
    summary.to_csv(outdir / "arm_summary.csv", index=False)

    control = summary.loc[summary["arm"] == "control"].iloc[0]
    effects = summary.copy()
    for col in ["program_participation", "post_participation", "commitment_takeup"]:
        effects[f"{col}_vs_control"] = effects[col] - control[col]
    effects.to_csv(outdir / "program_effects.csv", index=False)

    fig, ax = plt.subplots(figsize=(8, 4.8))
    x = range(len(summary))
    ax.bar([i - 0.18 for i in x], summary["program_participation"], width=0.35, label="Program")
    ax.bar([i + 0.18 for i in x], summary["post_participation"], width=0.35, label="Post")
    ax.set_xticks(list(x), LABELS)
    ax.set_ylim(0, 0.7)
    ax.set_ylabel("Participation rate")
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(outdir / "reproduction_worker_wellness.png", dpi=180)
    plt.close(fig)

    note = (
        "The bounded reproduction separates the short-run incentive margin from "
        "commitment take-up and post-program persistence. It is a teaching analog, "
        "not an official replication with employer microdata.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()

