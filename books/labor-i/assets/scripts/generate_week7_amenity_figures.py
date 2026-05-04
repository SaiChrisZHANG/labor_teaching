#!/usr/bin/env python3
"""Generate conceptual Week 7 figures for job amenities and compensating differentials."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "axes.titlesize": 14,
            "axes.labelsize": 11,
            "font.size": 10,
        }
    )


def make_hedonic_equilibrium() -> None:
    amenity = np.linspace(0.5, 9.5, 300)
    wage_schedule = 35.0 - 1.0 * amenity - 0.05 * (amenity - 5.0) ** 2

    fig, ax = plt.subplots(figsize=(8.4, 5.4))
    ax.plot(amenity, wage_schedule, color="#1f5c99", linewidth=2.8, label="Equilibrium wage schedule $w(a)$")

    tangencies = [
        {"a_star": 2.0, "theta": 0.70, "label": "Type L: lower amenity valuation", "color": "#c25b2a"},
        {"a_star": 8.0, "theta": 1.30, "label": "Type H: higher amenity valuation", "color": "#2a7f62"},
    ]

    for spec in tangencies:
        a_star = spec["a_star"]
        theta = spec["theta"]
        w_star = 35.0 - 1.0 * a_star - 0.05 * (a_star - 5.0) ** 2
        utility_line = w_star + theta * a_star - theta * amenity + 0.06 * (amenity - a_star) ** 2
        ax.plot(amenity, utility_line, linestyle="--", linewidth=2.0, color=spec["color"], label=spec["label"])
        ax.scatter([a_star], [w_star], color=spec["color"], s=55, zorder=5)
        ax.annotate(
            f"({a_star:.0f}, {w_star:.1f})",
            (a_star, w_star),
            xytext=(8, 8),
            textcoords="offset points",
            color=spec["color"],
        )

    ax.set_xlabel("Amenity level $a$ (better schedule, safety, flexibility, location)")
    ax.set_ylabel("Hourly wage $w(a)$")
    ax.set_title("Equalizing differentials in wage-amenity space")
    ax.set_xlim(0, 10)
    ax.set_ylim(20, 36.5)
    ax.legend(frameon=False, loc="lower left")
    ax.text(
        0.03,
        0.06,
        "Higher-valuation workers sort toward better amenities and accept lower wages along the schedule.",
        transform=ax.transAxes,
        fontsize=9,
        color="#374151",
    )
    fig.tight_layout()
    fig.savefig(FIG_DIR / "07-hedonic-wage-amenity-equilibrium.png", bbox_inches="tight")
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
    colors = ["#1f5c99", "#2a7f62", "#c25b2a", "#6b8e23", "#8c564b"]

    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    y_pos = np.arange(len(labels))
    ax.barh(y_pos, values, color=colors, height=0.6)
    ax.set_yticks(y_pos, labels)
    ax.set_xlabel("Illustrative willingness to pay (dollars per hour equivalent)")
    ax.set_title("Stylized willingness to pay for selected job amenities")
    ax.invert_yaxis()
    for idx, value in enumerate(values):
        ax.text(value + 0.08, idx, f"{value:.1f}", va="center", fontsize=9)
    ax.text(
        0.02,
        -0.18,
        "Conceptual magnitudes anchored to modern amenity valuation evidence rather than a single paper.",
        transform=ax.transAxes,
        fontsize=9,
        color="#374151",
    )
    fig.tight_layout()
    fig.savefig(FIG_DIR / "07-wtp-selected-amenities.png", bbox_inches="tight")
    plt.close(fig)


def make_inequality_bridge() -> None:
    jobs = np.array(list("ABCDEFGH"))
    wages = np.array([18, 20, 22, 24, 26, 29, 31, 34], dtype=float)
    amenity_value = np.array([4, 1, 6, 0, 3, -1, 2, -2], dtype=float)
    total_value = wages + amenity_value

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.8))

    axes[0].bar(jobs, wages, color="#d8a25b", width=0.65, label="Hourly wage")
    axes[0].plot(jobs, total_value, color="#1f5c99", marker="o", linewidth=2.2, label="Wage + amenity value")
    axes[0].set_title("Wage ranking can miss job value")
    axes[0].set_ylabel("Hourly dollars")
    axes[0].legend(frameon=False, loc="upper left")

    wage_rank = np.argsort(np.argsort(wages)) + 1
    value_rank = np.argsort(np.argsort(total_value)) + 1
    axes[1].scatter(wage_rank, value_rank, s=70, color="#2a7f62")
    axes[1].plot([1, len(jobs)], [1, len(jobs)], linestyle="--", linewidth=1.6, color="#555555")
    for idx, job in enumerate(jobs):
        axes[1].annotate(job, (wage_rank[idx], value_rank[idx]), xytext=(5, 5), textcoords="offset points")
    axes[1].set_title("Value-adjusted ranks can reorder jobs")
    axes[1].set_xlabel("Rank by wage only")
    axes[1].set_ylabel("Rank by total job value")
    axes[1].set_xlim(0.5, len(jobs) + 0.5)
    axes[1].set_ylim(0.5, len(jobs) + 0.5)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "07-wage-inequality-total-job-value.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    style()
    make_hedonic_equilibrium()
    make_wtp_plot()
    make_inequality_bridge()
    print(f"Wrote Week 7 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
