#!/usr/bin/env python3
"""Synthetic Week 7 transfer comparing border and bite-based minimum-wage designs."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def build_border_panel(seed: int = 20260508) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    pairs = [
        {"pair_id": "North-1", "treated": 1, "control_name": "North B", "treated_name": "North A", "median_wage": 15.8, "new_floor": 13.5},
        {"pair_id": "River-2", "treated": 1, "control_name": "River B", "treated_name": "River A", "median_wage": 16.4, "new_floor": 13.5},
        {"pair_id": "Lake-3", "treated": 1, "control_name": "Lake B", "treated_name": "Lake A", "median_wage": 17.1, "new_floor": 14.0},
        {"pair_id": "Valley-4", "treated": 1, "control_name": "Valley B", "treated_name": "Valley A", "median_wage": 15.2, "new_floor": 13.0},
    ]
    rows = []
    for pair in pairs:
        bite = pair["new_floor"] / pair["median_wage"]
        for rel_time in range(-3, 4):
            for side, treated in [(pair["treated_name"], 1), (pair["control_name"], 0)]:
                post = int(rel_time >= 0)
                base_emp = 118 + 4 * rel_time + rng.normal(0.0, 2.2)
                base_hours = 34.5 + 0.15 * rel_time + rng.normal(0.0, 0.25)
                emp_effect = (1.8 - 1.2 * (bite - 0.8) + rng.normal(0.0, 0.8)) if treated and post else 0.0
                hours_effect = (-0.45 - 0.65 * (bite - 0.8) + rng.normal(0.0, 0.08)) if treated and post else 0.0
                wage_effect = (0.95 + 2.6 * (bite - 0.8) + rng.normal(0.0, 0.07)) if treated and post else 0.0
                rows.append(
                    {
                        "pair_id": pair["pair_id"],
                        "county": side,
                        "treated": treated,
                        "relative_time": rel_time,
                        "post": post,
                        "median_wage": pair["median_wage"],
                        "new_floor": pair["new_floor"],
                        "bite": bite,
                        "restaurant_employment": base_emp + emp_effect,
                        "average_hours": base_hours + hours_effect,
                        "average_wage": 11.9 + 0.12 * rel_time + wage_effect,
                    }
                )
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    treated_post = df[(df["treated"] == 1) & (df["post"] == 1)]
    treated_pre = df[(df["treated"] == 1) & (df["post"] == 0)]
    control_post = df[(df["treated"] == 0) & (df["post"] == 1)]
    control_pre = df[(df["treated"] == 0) & (df["post"] == 0)]

    did_emp = treated_post["restaurant_employment"].mean() - treated_pre["restaurant_employment"].mean() - (
        control_post["restaurant_employment"].mean() - control_pre["restaurant_employment"].mean()
    )
    did_hours = treated_post["average_hours"].mean() - treated_pre["average_hours"].mean() - (
        control_post["average_hours"].mean() - control_pre["average_hours"].mean()
    )
    did_wage = treated_post["average_wage"].mean() - treated_pre["average_wage"].mean() - (
        control_post["average_wage"].mean() - control_pre["average_wage"].mean()
    )

    summary = pd.DataFrame(
        [
            {"metric": "num_rows", "value": len(df)},
            {"metric": "mean_bite", "value": df["bite"].mean()},
            {"metric": "border_did_employment", "value": did_emp},
            {"metric": "border_did_hours", "value": did_hours},
            {"metric": "border_did_wage", "value": did_wage},
        ]
    )
    return summary


def make_figure(df: pd.DataFrame, outpath: Path) -> None:
    grouped = df.groupby(["treated", "relative_time"], as_index=False).agg(
        restaurant_employment=("restaurant_employment", "mean"),
        average_hours=("average_hours", "mean"),
    )

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.8))
    for treated, label, color in [(1, "Treated border counties", "#B55D4C"), (0, "Control border counties", "#3B6EA8")]:
        sub = grouped[grouped["treated"] == treated]
        axes[0].plot(sub["relative_time"], sub["restaurant_employment"], marker="o", linewidth=2.3, color=color, label=label)
        axes[1].plot(sub["relative_time"], sub["average_hours"], marker="o", linewidth=2.3, color=color, label=label)

    for ax in axes:
        ax.axvline(0, color="#9AA4AF", linestyle=":", linewidth=1.1)
        ax.grid(alpha=0.2)
        ax.legend(fontsize=8.8)

    axes[0].set_title("Restaurant employment")
    axes[0].set_xlabel("Time relative to policy")
    axes[0].set_ylabel("Mean jobs")

    axes[1].set_title("Average hours")
    axes[1].set_xlabel("Time relative to policy")
    axes[1].set_ylabel("Hours")

    fig.suptitle("Synthetic border-county panel: wage gains with modest employment and hours adjustment")
    fig.tight_layout()
    fig.savefig(outpath, dpi=220)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    df = build_border_panel()
    summary = summarize(df)

    df.to_csv(args.outdir / "minimum_wage_border_panel.csv", index=False)
    summary.to_csv(args.outdir / "minimum_wage_border_summary.csv", index=False)
    make_figure(df, args.outdir / "minimum_wage_border_event.png")

    print(f"Wrote Week 7 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
