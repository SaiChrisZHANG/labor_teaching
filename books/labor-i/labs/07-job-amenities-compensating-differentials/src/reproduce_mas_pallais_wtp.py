#!/usr/bin/env python3
"""Bounded Week 7 reproduction in the spirit of Mas and Pallais (2017)."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ATTRS = ["predictable", "remote", "flexibility"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic job-choice CSV.")
    parser.add_argument("--outdir", required=True, help="Output directory for reproduction files.")
    return parser.parse_args()


def prepare_design(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    x = np.column_stack(
        [
            np.ones(len(df)),
            df["wage_a"].to_numpy() - df["wage_b"].to_numpy(),
            df["predictable_a"].to_numpy() - df["predictable_b"].to_numpy(),
            df["remote_a"].to_numpy() - df["remote_b"].to_numpy(),
            df["flexibility_a"].to_numpy() - df["flexibility_b"].to_numpy(),
        ]
    )
    y = df["chosen_offer_a"].to_numpy()
    return x, y


def estimate_choice_model(df: pd.DataFrame) -> dict[str, float]:
    x, y = prepare_design(df)
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return {
        "wage_coef": float(beta[1]),
        "predictable_coef": float(beta[2]),
        "remote_coef": float(beta[3]),
        "flexibility_coef": float(beta[4]),
    }


def wtp_from_coefs(coefs: dict[str, float]) -> dict[str, float]:
    wage_coef = coefs["wage_coef"]
    return {
        "predictable_schedule": float(coefs["predictable_coef"] / wage_coef),
        "remote_option": float(coefs["remote_coef"] / wage_coef),
        "worker_controlled_flexibility": float(coefs["flexibility_coef"] / wage_coef),
    }


def subgroup_wtp(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    groups = [
        ("all_workers", df),
        ("non_caregivers", df.loc[df["caregiver"] == 0]),
        ("caregivers", df.loc[df["caregiver"] == 1]),
        ("shorter_commute_workers", df.loc[df["long_commute"] == 0]),
        ("long_commute_workers", df.loc[df["long_commute"] == 1]),
    ]
    for group_name, group_df in groups:
        coefs = estimate_choice_model(group_df)
        wtp = wtp_from_coefs(coefs)
        for amenity, value in wtp.items():
            rows.append({"group": group_name, "amenity": amenity, "wtp_hourly_dollars": round(value, 4)})
    return pd.DataFrame(rows)


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    required = {
        "chosen_offer_a",
        "wage_a",
        "wage_b",
        "predictable_a",
        "predictable_b",
        "remote_a",
        "remote_b",
        "flexibility_a",
        "flexibility_b",
        "caregiver",
        "long_commute",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    overall_coefs = estimate_choice_model(df)
    coef_table = pd.DataFrame(
        {
            "term": ["wage_coef", "predictable_coef", "remote_coef", "flexibility_coef"],
            "value": [
                overall_coefs["wage_coef"],
                overall_coefs["predictable_coef"],
                overall_coefs["remote_coef"],
                overall_coefs["flexibility_coef"],
            ],
        }
    )
    coef_table.to_csv(outdir / "choice_model_coefficients.csv", index=False)

    overall_wtp = wtp_from_coefs(overall_coefs)
    wtp_table = pd.DataFrame(
        {
            "amenity": list(overall_wtp.keys()),
            "wtp_hourly_dollars": list(overall_wtp.values()),
        }
    )
    wtp_table.to_csv(outdir / "wtp_estimates.csv", index=False)

    subgroup_table = subgroup_wtp(df)
    subgroup_table.to_csv(outdir / "subgroup_wtp_estimates.csv", index=False)

    choice_summary = pd.DataFrame(
        {
            "statistic": [
                "share_choose_offer_a",
                "share_caregivers",
                "share_long_commute_workers",
                "mean_wage_diff_a_minus_b",
            ],
            "value": [
                df["chosen_offer_a"].mean(),
                df["caregiver"].mean(),
                df["long_commute"].mean(),
                (df["wage_a"] - df["wage_b"]).mean(),
            ],
        }
    )
    choice_summary.to_csv(outdir / "choice_summary.csv", index=False)

    plot_data = subgroup_table.loc[subgroup_table["group"].isin(["non_caregivers", "caregivers"])]
    plot_order = [
        "predictable_schedule",
        "remote_option",
        "worker_controlled_flexibility",
    ]
    x = np.arange(len(plot_order))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    for offset, group_name, color in [
        (-width / 2, "non_caregivers", "#c25b2a"),
        (width / 2, "caregivers", "#1f5c99"),
    ]:
        group_vals = (
            plot_data.loc[plot_data["group"] == group_name]
            .set_index("amenity")
            .reindex(plot_order)["wtp_hourly_dollars"]
            .to_numpy()
        )
        ax.bar(x + offset, group_vals, width=width, label=group_name.replace("_", " "), color=color)

    ax.set_xticks(x, ["Predictable\nschedule", "Remote\noption", "Worker control\nflexibility"])
    ax.set_ylabel("Estimated willingness to pay (dollars per hour)")
    ax.set_title("Bounded Week 7 willingness to pay for explicit amenities")
    ax.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(outdir / "reproduction_wtp_comparison.png", dpi=200)
    plt.close(fig)

    note_lines = [
        "The bounded design estimates how workers trade wages against explicitly described job attributes.",
        "The wage coefficient converts amenity effects into money-metric willingness to pay.",
        "Differences across caregiver and commute groups illustrate heterogeneous amenity valuation rather than a single universal schedule.",
    ]
    (outdir / "reproduction_note.txt").write_text("\n".join(note_lines) + "\n", encoding="utf-8")
    print(f"Saved reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
