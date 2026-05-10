from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ARM_ORDER = ["low_peer_visible", "average_peer_visible", "high_peer_hidden", "high_peer_visible"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)
    df["exposure_arm"] = pd.Categorical(df["exposure_arm"], categories=ARM_ORDER, ordered=True)

    summary = (
        df.groupby("exposure_arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            peer_effort_norm=("peer_effort_norm", "mean"),
            peer_visibility=("peer_visibility", "mean"),
            learning_signal=("learning_signal", "mean"),
            social_pressure=("social_pressure", "mean"),
            effort_units=("effort_units", "mean"),
            deviation_from_norm=("deviation_from_norm", "mean"),
            social_penalty_index=("social_penalty_index", "mean"),
            productivity_value=("productivity_value", "mean"),
            attendance_index=("attendance_index", "mean"),
        )
        .sort_values("exposure_arm")
    )
    summary.to_csv(outdir / "peer_pressure_summary.csv", index=False)

    control = summary.loc[summary["exposure_arm"] == "average_peer_visible"].iloc[0]
    effects = summary.copy()
    for col in ["effort_units", "deviation_from_norm", "social_penalty_index", "productivity_value", "attendance_index"]:
        effects[f"{col}_vs_average_visible"] = effects[col] - control[col]
    effects.to_csv(outdir / "peer_pressure_effects.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2))
    axes[0].bar(summary["exposure_arm"].astype(str), summary["productivity_value"], color="#4C78A8")
    axes[0].set_ylabel("Productivity value")
    axes[0].tick_params(axis="x", rotation=22)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].plot(
        summary["exposure_arm"].astype(str),
        summary["effort_units"],
        marker="o",
        label="Effort units",
        color="#59A14F",
    )
    axes[1].plot(
        summary["exposure_arm"].astype(str),
        summary["peer_effort_norm"],
        marker="o",
        label="Peer norm",
        color="#F28E2B",
    )
    axes[1].set_ylabel("Effort and peer norm")
    axes[1].tick_params(axis="x", rotation=22)
    axes[1].legend(frameon=False, fontsize=8)
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "peer_pressure_productivity.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic peer-at-work data to compare "
        "peer effort, visibility, learning signals, social pressure, effort, "
        "deviation from group norms, productivity, and attendance. It is not "
        "an official replication of Mas and Moretti.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
