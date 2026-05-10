from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    by_exposure = (
        df.groupby("exposure_count", as_index=False)
        .agg(
            observations=("worker_id", "count"),
            true_net_return=("true_net_return", "mean"),
            perceived_net_return=("perceived_net_return", "mean"),
            knowledge_gap=("knowledge_gap", "mean"),
            annual_hours=("annual_hours", "mean"),
            annual_earnings=("annual_earnings", "mean"),
        )
        .sort_values("exposure_count")
    )
    by_exposure.to_csv(outdir / "schedule_learning_by_exposure.csv", index=False)

    letter_effects = (
        df.groupby(["year", "schedule_letter"], as_index=False)
        .agg(
            workers=("worker_id", "count"),
            perceived_net_return=("perceived_net_return", "mean"),
            knowledge_gap=("knowledge_gap", "mean"),
            annual_hours=("annual_hours", "mean"),
        )
        .sort_values(["year", "schedule_letter"])
    )
    controls = letter_effects.loc[letter_effects["schedule_letter"] == 0, ["year", "annual_hours", "knowledge_gap"]]
    controls = controls.rename(
        columns={
            "annual_hours": "control_hours",
            "knowledge_gap": "control_knowledge_gap",
        }
    )
    letter_effects = letter_effects.merge(controls, on="year", how="left")
    letter_effects["hours_vs_control"] = letter_effects["annual_hours"] - letter_effects["control_hours"]
    letter_effects["gap_vs_control"] = letter_effects["knowledge_gap"] - letter_effects["control_knowledge_gap"]
    letter_effects.to_csv(outdir / "schedule_learning_letter_effects.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2))
    axes[0].plot(by_exposure["exposure_count"], by_exposure["true_net_return"], marker="o", label="True net return")
    axes[0].plot(
        by_exposure["exposure_count"],
        by_exposure["perceived_net_return"],
        marker="o",
        label="Perceived net return",
    )
    axes[0].set_xlabel("Exposure count")
    axes[0].set_ylabel("Net return to extra earnings")
    axes[0].set_ylim(0.45, 0.85)
    axes[0].legend(frameon=False, fontsize=8)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(by_exposure["exposure_count"].astype(str), by_exposure["annual_hours"], color="#4C78A8")
    axes[1].set_xlabel("Exposure count")
    axes[1].set_ylabel("Annual hours")
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "schedule_learning_response.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic panel data to compare true "
        "tax-benefit net returns, perceived net returns, exposure to the schedule, "
        "information letters, and annual hours. It is not an official replication "
        "of Kostol and Myhre.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
