#!/usr/bin/env python3
"""
Generate the required Week 4 figures for Labor II.
"""
from __future__ import annotations

import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"

BLUE = "#3B6EA8"
TEAL = "#5DA5A4"
GOLD = "#C79A35"
RED = "#B55D4C"
GRAY = "#5B6470"
LIGHT = "#E9EEF4"


def clean_axis(ax) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def make_course_map() -> None:
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    clean_axis(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    boxes = [
        (0.7, 2.2, 2.2, 1.4, BLUE, "Week 3\nPersonnel\nEconomics"),
        (3.9, 2.0, 2.4, 1.8, TEAL, "Week 4\nSearch, Matching,\nTurnover, U"),
        (7.1, 2.2, 2.2, 1.4, GOLD, "Week 5\nWage-Setting\nand Bargaining"),
    ]
    for x, y, width, height, color, label in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                width,
                height,
                boxstyle="round,pad=0.04,rounding_size=0.15",
                facecolor=LIGHT,
                edgecolor=color,
                linewidth=2.5,
            )
        )
        ax.text(
            x + width / 2,
            y + height / 2,
            label,
            ha="center",
            va="center",
            fontsize=13,
            color=GRAY,
            weight="bold",
        )

    arrows = [
        ((2.95, 2.9), (3.85, 2.9), "retention, quits, hiring", 3.35),
        ((6.35, 2.9), (7.05, 2.9), "outside options, wages", 3.35),
    ]
    for start, end, label, ypos in arrows:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=18,
                linewidth=2.2,
                color=GRAY,
            )
        )
        ax.text((start[0] + end[0]) / 2, ypos, label, ha="center", va="bottom", fontsize=10, color=GRAY)

    ax.text(
        5,
        5.15,
        "Labor II pivots from the inside of the firm to market-wide labor allocation",
        ha="center",
        fontsize=14,
        color=GRAY,
    )
    fig.tight_layout()
    fig.savefig(FIG_DIR / "04-search-course-map.png", dpi=220)
    plt.close(fig)


def make_worker_flows() -> None:
    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    clean_axis(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    positions = {"U": (2.2, 3.0), "E": (5.2, 3.0), "V": (8.0, 4.3), "J": (8.0, 1.7)}
    labels = {
        "U": "Unemployment\nU",
        "E": "Employment\nE",
        "V": "Vacancies\nV",
        "J": "Other firms /\njob ladder",
    }
    for key, (x, y) in positions.items():
        edge = BLUE if key in {"U", "E"} else GOLD
        ax.add_patch(Circle((x, y), 0.72, facecolor=LIGHT, edgecolor=edge, linewidth=2.4))
        ax.text(x, y, labels[key], ha="center", va="center", fontsize=13, color=GRAY, weight="bold")

    ax.add_patch(
        FancyArrowPatch((2.95, 3.05), (4.45, 3.05), arrowstyle="-|>", mutation_scale=18, linewidth=2.3, color=TEAL)
    )
    ax.text(3.7, 3.35, "U -> E\njob-finding hazard  f", ha="center", fontsize=11, color=TEAL)

    ax.add_patch(
        FancyArrowPatch((4.45, 2.75), (2.95, 2.75), arrowstyle="-|>", mutation_scale=18, linewidth=2.3, color=RED)
    )
    ax.text(3.7, 2.18, "E -> U\nseparation hazard  s", ha="center", fontsize=11, color=RED)

    ax.add_patch(
        FancyArrowPatch(
            (5.95, 3.15),
            (7.15, 4.0),
            connectionstyle="arc3,rad=0.15",
            arrowstyle="-|>",
            mutation_scale=18,
            linewidth=2.1,
            color=GOLD,
        )
    )
    ax.text(6.85, 4.55, "vacancy-filling hazard  q", ha="center", fontsize=11, color=GOLD)

    ax.add_patch(
        FancyArrowPatch(
            (5.95, 2.85),
            (7.15, 2.0),
            connectionstyle="arc3,rad=-0.08",
            arrowstyle="-|>",
            mutation_scale=18,
            linewidth=2.1,
            color=BLUE,
        )
    )
    ax.text(6.85, 1.15, "E -> E job-to-job moves", ha="center", fontsize=11, color=BLUE)
    ax.text(5.1, 5.25, "Week 4 tracks three transition margins, not only unemployment exits", ha="center", fontsize=14, color=GRAY)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "04-worker-flows-and-hazards.png", dpi=220)
    plt.close(fig)


def make_beveridge() -> None:
    u = np.linspace(3, 10, 200)
    v1 = 11 / u + 0.35
    v2 = 13 / u + 0.55

    fig, ax = plt.subplots(figsize=(7.6, 5.2))
    ax.plot(u, v1, linewidth=2.6, color=BLUE, label="baseline Beveridge relation")
    ax.plot(u, v2, linewidth=2.6, color=RED, linestyle="--", label="outward shift")
    ax.scatter([3.8, 6.1, 8.8], [11 / 3.8 + 0.35, 11 / 6.1 + 0.35, 11 / 8.8 + 0.35], color=BLUE, s=36)
    ax.scatter([4.1, 6.4, 9.1], [13 / 4.1 + 0.55, 13 / 6.4 + 0.55, 13 / 9.1 + 0.55], color=RED, s=36)
    ax.annotate(
        "composition or mismatch shift",
        xy=(6.4, 2.58),
        xytext=(7.3, 3.65),
        arrowprops={"arrowstyle": "->", "color": RED, "linewidth": 1.8},
        fontsize=10,
        color=RED,
    )
    ax.annotate(
        "stronger matching / tighter market",
        xy=(4.1, 3.72),
        xytext=(3.1, 4.55),
        arrowprops={"arrowstyle": "->", "color": BLUE, "linewidth": 1.8},
        fontsize=10,
        color=BLUE,
    )
    ax.set_xlabel("Unemployment rate / job seekers")
    ax.set_ylabel("Vacancies")
    ax.set_title("Beveridge logic: the same vacancy-unemployment map can move for different reasons")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "04-beveridge-matching-efficiency.png", dpi=220)
    plt.close(fig)


def make_separation_churning_jobladder() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    for ax in axes:
        clean_axis(ax)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)

    ax = axes[0]
    ax.add_patch(
        FancyBboxPatch(
            (0.8, 2.1),
            2.3,
            1.5,
            boxstyle="round,pad=0.04,rounding_size=0.12",
            facecolor=LIGHT,
            edgecolor=BLUE,
            linewidth=2.2,
        )
    )
    ax.text(1.95, 2.85, "Stable headcount", ha="center", va="center", fontsize=13, color=GRAY, weight="bold")
    labels = [(4.7, "layoffs / job loss", RED), (3.8, "replacement hiring", TEAL), (1.4, "quits to other firms", GOLD)]
    for ypos, label, color in labels:
        ax.add_patch(
            FancyArrowPatch((3.15, 2.85), (5.6, ypos), arrowstyle="-|>", mutation_scale=18, linewidth=2.1, color=color)
        )
        ax.text(5.95, ypos, label, va="center", fontsize=11, color=color)
    ax.text(1.95, 5.3, "Gross worker flows can be large even when net employment is flat", ha="center", fontsize=12.5, color=GRAY)

    ax = axes[1]
    levels = [("low-wage firm", 1.1, 1.1, BLUE), ("middle-wage firm", 4.0, 2.4, TEAL), ("high-wage firm", 6.9, 3.7, GOLD)]
    for label, x, y, color in levels:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                2.0,
                0.95,
                boxstyle="round,pad=0.03,rounding_size=0.12",
                facecolor=LIGHT,
                edgecolor=color,
                linewidth=2.2,
            )
        )
        ax.text(x + 1.0, y + 0.47, label, ha="center", va="center", fontsize=11.5, color=GRAY, weight="bold")

    ax.add_patch(FancyArrowPatch((3.1, 1.6), (4.0, 2.65), arrowstyle="-|>", mutation_scale=18, linewidth=2.2, color=BLUE))
    ax.add_patch(FancyArrowPatch((6.0, 2.9), (6.9, 3.95), arrowstyle="-|>", mutation_scale=18, linewidth=2.2, color=TEAL))
    ax.add_patch(
        FancyArrowPatch((7.0, 3.55), (5.9, 2.55), arrowstyle="-|>", mutation_scale=16, linewidth=1.6, color=RED, linestyle="--")
    )
    ax.text(5.2, 5.1, "Job ladders: E -> E mobility sorts workers across firms", ha="center", fontsize=12.5, color=GRAY)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "04-separation-churning-jobladder.png", dpi=220)
    plt.close(fig)


def make_duration_scarring() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    months = np.arange(1, 8)
    obs_hazard = np.array([0.34, 0.29, 0.24, 0.20, 0.17, 0.15, 0.14])
    sel_only = np.array([0.34, 0.31, 0.28, 0.25, 0.23, 0.21, 0.20])

    axes[0].plot(months, obs_hazard, marker="o", linewidth=2.3, color=RED, label="observed exit hazard")
    axes[0].plot(months, sel_only, marker="s", linewidth=2.1, color=BLUE, linestyle="--", label="selection-only benchmark")
    axes[0].set_title("Observed duration dependence")
    axes[0].set_xlabel("Months unemployed")
    axes[0].set_ylabel("U-to-E hazard")
    axes[0].grid(alpha=0.2)
    axes[0].legend(fontsize=8)

    post = np.arange(0, 5)
    quality_fast = np.array([0.0, 0.05, 0.08, 0.10, 0.12])
    quality_scar = np.array([-0.12, -0.08, -0.05, -0.03, -0.01])
    axes[1].plot(post, quality_fast, marker="o", linewidth=2.3, color=TEAL, label="short spell / better reemployment")
    axes[1].plot(post, quality_scar, marker="o", linewidth=2.3, color=GOLD, label="long spell / scarring path")
    axes[1].axhline(0.0, color="gray", linewidth=0.8)
    axes[1].set_title("Post-reemployment job quality")
    axes[1].set_xlabel("Years after reemployment")
    axes[1].set_ylabel("Quality or wage gap")
    axes[1].grid(alpha=0.2)
    axes[1].legend(fontsize=8)

    fig.suptitle("Duration, selection, and scarring are distinct Week 4 objects")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "04-unemployment-duration-and-scarring.png", dpi=220)
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    make_course_map()
    make_worker_flows()
    make_beveridge()
    make_separation_churning_jobladder()
    make_duration_scarring()
    print(f"Saved Week 4 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
