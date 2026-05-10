from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ARM_ORDER = ["control", "cash_gift", "noncash_gift", "piece_rate", "employer_return"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)
    df["arm"] = pd.Categorical(df["arm"], categories=ARM_ORDER, ordered=True)

    summary = (
        df.groupby("arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            gift_value=("gift_value", "mean"),
            employer_effort=("employer_effort", "mean"),
            piece_rate=("piece_rate", "mean"),
            reciprocity_index=("reciprocity_index", "mean"),
            extra_work_minutes=("extra_work_minutes", "mean"),
            output_units=("output_units", "mean"),
            quality_score=("quality_score", "mean"),
            productivity_value=("productivity_value", "mean"),
            productivity_per_minute=("productivity_per_minute", "mean"),
        )
        .sort_values("arm")
    )
    summary.to_csv(outdir / "gift_exchange_summary.csv", index=False)

    control = summary.loc[summary["arm"] == "control"].iloc[0]
    effects = summary.copy()
    for col in ["extra_work_minutes", "output_units", "quality_score", "productivity_value", "productivity_per_minute"]:
        effects[f"{col}_vs_control"] = effects[col] - control[col]
    effects.to_csv(outdir / "gift_exchange_effects.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
    axes[0].bar(summary["arm"].astype(str), summary["extra_work_minutes"], color="#4C78A8")
    axes[0].set_ylabel("Extra work minutes")
    axes[0].tick_params(axis="x", rotation=22)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(summary["arm"].astype(str), summary["productivity_value"], color="#59A14F")
    axes[1].set_ylabel("Productivity value")
    axes[1].tick_params(axis="x", rotation=22)
    axes[1].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "gift_exchange_extra_work_vs_productivity.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic workplace data to compare "
        "gift treatments, employer-effort treatments, standard piece-rate "
        "incentives, extra work, output, quality, and productivity. It is not "
        "an official replication of DellaVigna, List, Malmendier, and Rao.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
