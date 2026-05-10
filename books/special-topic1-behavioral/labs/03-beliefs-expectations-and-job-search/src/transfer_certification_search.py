from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certification-input", required=True)
    parser.add_argument("--wage-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    cert = pd.read_csv(args.certification_input)
    summary = (
        cert.groupby("certified", as_index=False)
        .agg(
            workers=("worker_id", "count"),
            true_skill=("true_skill_score", "mean"),
            prior_self_belief=("prior_self_belief", "mean"),
            posterior_self_belief=("posterior_self_belief", "mean"),
            high_skill_targeting=("targets_high_skill_vacancies", "mean"),
            firm_signal=("firm_signal_score", "mean"),
            hire_rate=("hired", "mean"),
        )
        .sort_values("certified")
    )
    summary["group"] = summary["certified"].map({0: "uncertified", 1: "certified"})
    summary.to_csv(outdir / "certification_summary.csv", index=False)

    uncertified = summary.loc[summary["certified"] == 0].iloc[0]
    effects = summary.copy()
    for col in ["posterior_self_belief", "high_skill_targeting", "firm_signal", "hire_rate"]:
        effects[f"{col}_vs_uncertified"] = effects[col] - uncertified[col]
    effects.to_csv(outdir / "certification_effects.csv", index=False)

    wage = pd.read_csv(args.wage_input)
    wage_summary = (
        wage.groupby("posted_wage", as_index=False)
        .agg(
            seekers=("seeker_id", "count"),
            perceived_competition=("perceived_competition", "mean"),
            application_index=("application_index", "mean"),
            application_rate=("applied", "mean"),
        )
        .sort_values("posted_wage")
    )
    wage_summary.to_csv(outdir / "wage_signal_summary.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2))
    axes[0].bar(summary["group"], summary["high_skill_targeting"], color=["#4C78A8", "#59A14F"])
    axes[0].set_ylabel("Share targeting high-skill vacancies")
    axes[0].set_ylim(0, 1)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(summary["group"], summary["hire_rate"], color=["#4C78A8", "#59A14F"])
    axes[1].set_ylabel("Hire rate")
    axes[1].set_ylim(0, 1)
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "certification_search.png", dpi=180)
    plt.close(fig)

    note = (
        "The certification transfer uses synthetic data to separate worker "
        "self-beliefs, application targeting, firm-visible skill signals, and "
        "hiring. The wage-signal table is an optional perceived-competition "
        "exercise. These are teaching analogs, not official replications.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
