#!/usr/bin/env python3
"""Generate conceptual Week 7 figures for job amenities and compensating differentials."""
from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, apply_style, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_hedonic_equilibrium() -> None:
    amenity = np.linspace(0.5, 9.5, 300)
    wage_schedule = 35.0 - 1.0 * amenity - 0.05 * (amenity - 5.0) ** 2

    fig, ax = plt.subplots(figsize=(8.4, 5.4))
    ax.plot(amenity, wage_schedule, color=COLORS["navy"], linewidth=2.8, label="Equilibrium wage schedule $w(a)$")

    tangencies = [
        {"a_star": 2.0, "theta": 0.70, "label": "Type L: lower amenity valuation", "color": COLORS["rust"]},
        {"a_star": 8.0, "theta": 1.30, "label": "Type H: higher amenity valuation", "color": COLORS["teal"]},
    ]

    for spec in tangencies:
        a_star = spec["a_star"]
        theta = spec["theta"]
        w_star = 35.0 - 1.0 * a_star - 0.05 * (a_star - 5.0) ** 2
        utility_line = w_star + theta * a_star - theta * amenity + 0.06 * (amenity - a_star) ** 2
        ax.plot(amenity, utility_line, linestyle="--", linewidth=2.0, color=spec["color"], label=spec["label"])
        ax.scatter([a_star], [w_star], color=spec["color"], s=40, zorder=5)
        ax.annotate(
            f"({a_star:.0f}, {w_star:.1f})",
            (a_star, w_star),
            xytext=(8, 8),
            textcoords="offset points",
            color=spec["color"],
            fontsize=9,
        )

    ax.set_xlabel("Amenity level $a$ (better schedule, safety, flexibility, location)")
    ax.set_ylabel("Hourly wage $w(a)$")
    ax.set_title("Equalizing differentials in wage-amenity space")
    ax.set_xlim(0, 10)
    ax.set_ylim(20, 36.5)
    ax.legend(loc="lower left")
    ax.text(
        0.03,
        0.06,
        "Higher-valuation workers sort toward better amenities and accept lower wages along the schedule.",
        transform=ax.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "07-hedonic-wage-amenity-equilibrium.png")
    plt.close(fig)


def make_wtp_plot() -> None:
    labels = [
        "Worker-controlled flexibility",
        "Lower injury risk",
        "Predictable schedule",
        "Remote option",
        "Shorter commute",
    ]
    values = np.array([3.2, 2.6, 1.9, 1.4, 1.1])
    colors = [COLORS["navy"], COLORS["teal"], COLORS["rust"], COLORS["gold"], COLORS["slate"]]

    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    y_pos = np.arange(len(labels))
    ax.barh(y_pos, values, color=colors, height=0.6)
    ax.set_yticks(y_pos, labels)
    ax.set_xlabel("Illustrative willingness to pay (dollars per hour equivalent)")
    ax.set_title("Stylized willingness to pay for selected job amenities")
    ax.invert_yaxis()
    for idx, value in enumerate(values):
        ax.text(value + 0.08, idx, f"{value:.1f}", va="center", fontsize=9, color=COLORS["muted"])
    ax.text(
        0.02,
        -0.18,
        "Conceptual magnitudes anchored to modern amenity valuation evidence rather than a single paper.",
        transform=ax.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    style_axis(ax, grid_axis="x")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "07-wtp-selected-amenities.png")
    plt.close(fig)


def make_inequality_bridge() -> None:
    jobs = np.array(list("ABCDEFGH"))
    wages = np.array([18, 20, 22, 24, 26, 29, 31, 34], dtype=float)
    amenity_value = np.array([4, 1, 6, 0, 3, -1, 2, -2], dtype=float)
    total_value = wages + amenity_value

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))

    axes[0].bar(jobs, wages, color=COLORS["gold"], width=0.65, label="Hourly wage")
    axes[0].plot(jobs, total_value, color=COLORS["navy"], marker="o", linewidth=2.2, label="Wage plus amenity value")
    axes[0].set_title("Wage ranking can miss total job value")
    axes[0].set_ylabel("Hourly dollars")
    axes[0].legend(loc="upper left")
    style_axis(axes[0], grid_axis="y")

    wage_rank = np.argsort(np.argsort(wages)) + 1
    value_rank = np.argsort(np.argsort(total_value)) + 1
    axes[1].scatter(wage_rank, value_rank, s=52, color=COLORS["teal"])
    axes[1].plot([1, len(jobs)], [1, len(jobs)], linestyle="--", linewidth=1.5, color=COLORS["muted"])
    for idx, job in enumerate(jobs):
        axes[1].annotate(job, (wage_rank[idx], value_rank[idx]), xytext=(5, 5), textcoords="offset points", fontsize=8.5)
    axes[1].set_title("Value-adjusted ranks can reorder jobs")
    axes[1].set_xlabel("Rank by wage only")
    axes[1].set_ylabel("Rank by total job value")
    axes[1].set_xlim(0.5, len(jobs) + 0.5)
    axes[1].set_ylim(0.5, len(jobs) + 0.5)
    style_axis(axes[1], grid_axis="both")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "07-wage-inequality-total-job-value.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    make_hedonic_equilibrium()
    make_wtp_plot()
    make_inequality_bridge()
    print(f"Wrote Week 7 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
