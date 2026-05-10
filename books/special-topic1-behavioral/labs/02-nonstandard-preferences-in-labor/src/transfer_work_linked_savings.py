from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


REGIME_ORDER = ["active_choice", "auto_enrollment", "auto_enrollment_match"]
LABELS = ["Active\nchoice", "Auto\nenrollment", "Auto +\nmatch"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    summary = (
        df.groupby("regime", as_index=False)
        .agg(
            employees=("employee_id", "count"),
            participation=("participates", "mean"),
            contribution_rate=("contribution_rate", "mean"),
            contribution_rate_conditional=("contribution_rate", lambda x: x[x > 0].mean()),
        )
        .set_index("regime")
        .loc[REGIME_ORDER]
        .reset_index()
    )
    summary.to_csv(outdir / "savings_summary.csv", index=False)

    active = summary.loc[summary["regime"] == "active_choice"].iloc[0]
    effects = summary.copy()
    for col in ["participation", "contribution_rate", "contribution_rate_conditional"]:
        effects[f"{col}_vs_active_choice"] = effects[col] - active[col]
    effects.to_csv(outdir / "savings_effects.csv", index=False)

    fig, ax1 = plt.subplots(figsize=(8, 4.5))
    x = range(len(summary))
    ax1.bar(x, summary["participation"], color="#4C78A8", label="Participation")
    ax1.set_xticks(list(x), LABELS)
    ax1.set_ylim(0, 1)
    ax1.set_ylabel("Participation rate")
    ax1.spines[["top", "right"]].set_visible(False)

    ax2 = ax1.twinx()
    ax2.plot(x, summary["contribution_rate"], marker="o", color="#E15759", label="Contribution")
    ax2.set_ylim(0, 0.09)
    ax2.set_ylabel("Average contribution rate")
    ax2.spines["top"].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "work_linked_savings.png", dpi=180)
    plt.close(fig)

    note = (
        "The transfer exercise uses a synthetic work-linked savings default. The "
        "direct margin is participation and contribution behavior; the behavioral "
        "interpretation must distinguish self-control and inertia from transaction "
        "costs, information, and liquidity.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
