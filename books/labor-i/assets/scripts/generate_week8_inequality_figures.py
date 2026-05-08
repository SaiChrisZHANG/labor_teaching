#!/usr/bin/env python3
"""Generate conceptual Week 8 figures for inequality and wage dispersion."""
from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, save_figure, apply_style, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_percentile_gap_series() -> None:
    years = np.array([1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2019])
    p90_p10 = np.array([1.05, 1.12, 1.22, 1.30, 1.37, 1.42, 1.47, 1.51, 1.55])
    p90_p50 = np.array([0.49, 0.55, 0.62, 0.69, 0.74, 0.78, 0.82, 0.86, 0.89])
    p50_p10 = np.array([0.56, 0.57, 0.60, 0.61, 0.63, 0.64, 0.65, 0.65, 0.66])

    fig, ax = plt.subplots(figsize=(8.6, 5.3))
    ax.plot(years, p90_p10, color=COLORS["navy"], linewidth=2.8, marker="o", markersize=4, label=r"$p90-p10$")
    ax.plot(years, p90_p50, color=COLORS["teal"], linewidth=2.5, marker="o", markersize=4, label=r"$p90-p50$")
    ax.plot(years, p50_p10, color=COLORS["rust"], linewidth=2.5, marker="o", markersize=4, label=r"$p50-p10$")
    ax.set_title("Stylized upper-tail and lower-tail inequality series")
    ax.set_xlabel("Year")
    ax.set_ylabel("Log wage gap")
    ax.set_xlim(1979, 2020)
    ax.legend(loc="upper left")
    ax.text(
        0.03,
        0.05,
        "The upper half of the distribution widens more persistently than the lower half.",
        transform=ax.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "08-percentile-gap-series.png")
    plt.close(fig)


def make_component_decomposition() -> None:
    years = ["1980", "2000", "2019"]
    between = np.array([0.07, 0.09, 0.10])
    within = np.array([0.15, 0.18, 0.20])
    firm = np.array([0.03, 0.05, 0.08])
    sorting = np.array([0.01, 0.03, 0.05])

    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    ax.bar(years, between, color=COLORS["gold"], label="Between observed groups")
    ax.bar(years, within, bottom=between, color="#8FA0C4", label="Within-group residual")
    ax.bar(years, firm, bottom=between + within, color=COLORS["teal"], label="Firm premia")
    ax.bar(years, sorting, bottom=between + within + firm, color=COLORS["slate"], label="Sorting covariance")
    ax.set_title("Conceptual partition of log-wage variance")
    ax.set_ylabel("Variance contribution")
    ax.legend(loc="upper left")
    ax.text(
        0.03,
        0.92,
        "Interpret as an accounting map, not a universal empirical ranking.",
        transform=ax.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    style_axis(ax, grid_axis="y")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "08-inequality-component-decomposition.png")
    plt.close(fig)


def make_polarization_schematic() -> None:
    categories = ["Low-wage service", "Middle routine", "High-skill abstract"]
    changes = np.array([3.5, -7.0, 5.2])
    colors = [COLORS["teal"], COLORS["rust"], COLORS["navy"]]

    fig, ax = plt.subplots(figsize=(8.4, 5.0))
    bars = ax.bar(categories, changes, color=colors, width=0.65)
    ax.axhline(0, color=COLORS["muted"], linewidth=1.2)
    ax.set_title("Stylized employment-share changes under polarization")
    ax.set_ylabel("Change in employment share (percentage points)")
    for bar, value in zip(bars, changes):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + (0.35 if value >= 0 else -0.75),
            f"{value:.1f}",
            ha="center",
            va="bottom" if value >= 0 else "top",
            fontsize=9,
            color=COLORS["muted"],
        )
    ax.text(
        0.04,
        0.08,
        "Polarization is about relative hollowing out in the middle, not a uniform shift in all skill prices.",
        transform=ax.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    style_axis(ax, grid_axis="y")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "08-polarization-schematic.png")
    plt.close(fig)


def make_wage_value_bridge() -> None:
    workers = np.array(list("ABCDEFGH"))
    wage = np.array([16, 18, 21, 23, 25, 28, 31, 35], dtype=float)
    amenity = np.array([4, 3, 1, 5, 0, -1, 2, -3], dtype=float)
    total_value = wage + amenity

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))

    axes[0].bar(workers, wage, color=COLORS["gold"], width=0.65, label="Wage")
    axes[0].plot(workers, total_value, color=COLORS["navy"], marker="o", linewidth=2.3, label="Wage plus amenity value")
    axes[0].set_title("Wage inequality and total job value need not match")
    axes[0].set_ylabel("Hourly dollars")
    axes[0].legend(loc="upper left")
    style_axis(axes[0], grid_axis="y")

    wage_rank = np.argsort(np.argsort(wage)) + 1
    value_rank = np.argsort(np.argsort(total_value)) + 1
    axes[1].scatter(wage_rank, value_rank, s=52, color=COLORS["teal"])
    axes[1].plot([1, len(workers)], [1, len(workers)], linestyle="--", linewidth=1.5, color=COLORS["muted"])
    for idx, worker in enumerate(workers):
        axes[1].annotate(worker, (wage_rank[idx], value_rank[idx]), xytext=(5, 5), textcoords="offset points", fontsize=8.5)
    axes[1].set_title("Ranks can change once job quality is valued")
    axes[1].set_xlabel("Rank by wage only")
    axes[1].set_ylabel("Rank by total job value")
    axes[1].set_xlim(0.5, len(workers) + 0.5)
    axes[1].set_ylim(0.5, len(workers) + 0.5)
    style_axis(axes[1], grid_axis="both")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "08-wage-vs-total-job-value.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    make_percentile_gap_series()
    make_component_decomposition()
    make_polarization_schematic()
    make_wage_value_bridge()
    print(f"Wrote Week 8 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
