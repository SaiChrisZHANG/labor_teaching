from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


CONTRACT_ORDER = ["standard", "commitment"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)

    worker_level = (
        df.groupby(["worker_id", "contract"], as_index=False)
        .agg(
            chose_commitment=("chose_commitment", "max"),
            average_output=("output_units", "mean"),
            target_rate=("met_target", "mean"),
            close_payday_output=("output_units", lambda x: x[df.loc[x.index, "close_to_payday"] == 1].mean()),
            far_payday_output=("output_units", lambda x: x[df.loc[x.index, "payday_distance"] >= 7].mean()),
        )
    )

    contract_summary = (
        worker_level.groupby("contract", as_index=False)
        .agg(
            workers=("worker_id", "count"),
            commitment_takeup=("chose_commitment", "mean"),
            average_output=("average_output", "mean"),
            target_rate=("target_rate", "mean"),
            close_payday_output=("close_payday_output", "mean"),
            far_payday_output=("far_payday_output", "mean"),
        )
        .set_index("contract")
        .loc[CONTRACT_ORDER]
        .reset_index()
    )
    contract_summary["close_minus_far_payday_output"] = (
        contract_summary["close_payday_output"] - contract_summary["far_payday_output"]
    )
    contract_summary.to_csv(outdir / "contract_summary.csv", index=False)

    payday_gradient = (
        df.groupby("payday_distance", as_index=False)
        .agg(average_output=("output_units", "mean"), target_rate=("met_target", "mean"))
        .sort_values("payday_distance")
    )
    payday_gradient.to_csv(outdir / "payday_gradient.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))
    axes[0].bar(contract_summary["contract"], contract_summary["average_output"], color=["#4C78A8", "#59A14F"])
    axes[0].set_ylabel("Average daily output")
    axes[0].set_xlabel("Chosen contract")
    axes[0].set_ylim(48, 62)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].plot(payday_gradient["payday_distance"], payday_gradient["average_output"], marker="o", color="#F28E2B")
    axes[1].invert_xaxis()
    axes[1].set_xlabel("Days from payday")
    axes[1].set_ylabel("Average daily output")
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "workplace_self_control.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic workplace data to separate "
        "commitment-contract take-up, output under the chosen contract, and effort "
        "near paydays. It is not an official replication of Kaur, Kremer, and "
        "Mullainathan.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
