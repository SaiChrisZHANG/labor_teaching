#!/usr/bin/env python3
"""Bounded Week 4 reproduction in the spirit of Attanasio et al. (2020)."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mpl-cache"))

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic child-level CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for reproduction files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {"treatment", "parental_investment", "endline_skill", "followup_language", "baseline_group"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    summary = (
        df.groupby("treatment", as_index=False)
        .agg(
            mean_parental_investment=("parental_investment", "mean"),
            mean_endline_skill=("endline_skill", "mean"),
            mean_followup_language=("followup_language", "mean"),
            children=("child_id", "size"),
        )
        .sort_values("treatment")
    )
    summary["group_label"] = summary["treatment"].map({0: "Control", 1: "Treatment"})
    summary.to_csv(outdir / "reproduction_summary.csv", index=False)

    effects = pd.DataFrame(
        {
            "metric": ["parental_investment", "endline_skill", "followup_language"],
            "treatment_minus_control": [
                summary.loc[summary["treatment"] == 1, "mean_parental_investment"].iloc[0]
                - summary.loc[summary["treatment"] == 0, "mean_parental_investment"].iloc[0],
                summary.loc[summary["treatment"] == 1, "mean_endline_skill"].iloc[0]
                - summary.loc[summary["treatment"] == 0, "mean_endline_skill"].iloc[0],
                summary.loc[summary["treatment"] == 1, "mean_followup_language"].iloc[0]
                - summary.loc[summary["treatment"] == 0, "mean_followup_language"].iloc[0],
            ],
        }
    )
    effects.to_csv(outdir / "treatment_effects.csv", index=False)

    heterogeneity = (
        df.groupby(["baseline_group", "treatment"], as_index=False)
        .agg(mean_endline_skill=("endline_skill", "mean"))
        .sort_values(["baseline_group", "treatment"])
    )
    heterogeneity.to_csv(outdir / "baseline_group_summary.csv", index=False)

    plt.figure(figsize=(9, 5.2))
    positions = range(len(summary))
    width = 0.34
    plt.bar([p - width / 2 for p in positions], summary["mean_parental_investment"], width=width, label="Parental investment")
    plt.bar([p + width / 2 for p in positions], summary["mean_endline_skill"], width=width, label="Endline skill")
    plt.xticks(list(positions), summary["group_label"])
    plt.ylabel("Mean level")
    plt.title("Bounded Week 4 treatment contrast")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "reproduction_treatment_contrast.png", dpi=200)
    plt.close()

    note_lines = [
        "This bounded output is a reduced-form treatment effect, not a full production-function estimate.",
        "Treatment shifts parental investments and endline skill, but dynamic complementarity still requires stronger structure to estimate.",
        "Baseline-skill heterogeneity helps motivate why the same intervention can generate different later returns.",
    ]
    (outdir / "reproduction_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
