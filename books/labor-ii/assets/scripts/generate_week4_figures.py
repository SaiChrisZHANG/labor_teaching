#!/usr/bin/env python3
"""Generate the required Week 4 figures for Labor II."""
from __future__ import annotations

import os
from pathlib import Path
import sys
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, add_arrow, add_box, apply_style, clean_axis, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_course_map() -> None:
    fig, ax = plt.subplots(figsize=(8.5, 5.0))
    clean_axis(ax, xlim=(0, 10), ylim=(0, 6))

    add_box(ax, 0.7, 2.15, 2.15, 1.45, "Week 3\nPersonnel\nEconomics", edge=COLORS["navy"], fontsize=12.5)
    add_box(ax, 3.75, 1.9, 2.5, 1.95, "Week 4\nSearch, matching,\nturnover,\nunemployment", edge=COLORS["teal"], fontsize=12.3)
    add_box(ax, 7.1, 2.15, 2.15, 1.45, "Week 5\nWage-setting\nand bargaining", edge=COLORS["gold"], fontsize=12.5)

    add_arrow(ax, (2.85, 2.9), (3.75, 2.9), text="retention, quits, hiring", text_xy=(3.3, 3.45))
    add_arrow(ax, (6.25, 2.9), (7.1, 2.9), text="outside options, wages", text_xy=(6.7, 3.45))
    ax.text(5.0, 5.2, "Labor II pivots from the inside of the firm to market-wide labor allocation.", ha="center", fontsize=13.5, color=COLORS["ink"], weight="semibold")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-search-course-map.png")
    plt.close(fig)


def make_worker_flows() -> None:
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    clean_axis(ax, xlim=(0, 10), ylim=(0, 6))

    positions = {"U": (2.1, 3.0), "E": (5.0, 3.0), "V": (7.95, 4.35), "J": (7.95, 1.65)}
    labels = {"U": "Unemployment\nU", "E": "Employment\nE", "V": "Vacancies\nV", "J": "Other firms /\njob ladder"}
    for key, (x, y) in positions.items():
        edge = COLORS["navy"] if key in {"U", "E"} else COLORS["gold"]
        ax.add_patch(Circle((x, y), 0.72, facecolor=(1, 1, 1, 1), edgecolor=edge, linewidth=1.8))
        ax.text(x, y, labels[key], ha="center", va="center", fontsize=12, color=COLORS["ink"], weight="semibold")

    add_arrow(ax, (2.82, 3.05), (4.28, 3.05), color=COLORS["teal"], text="U -> E\njob-finding hazard $f$", text_xy=(3.55, 3.55), linewidth=2.0)
    add_arrow(ax, (4.28, 2.75), (2.82, 2.75), color=COLORS["rust"], text="E -> U\nseparation hazard $s$", text_xy=(3.55, 2.15), linewidth=2.0)
    add_arrow(ax, (5.7, 3.18), (7.15, 4.02), color=COLORS["gold"], text="vacancy-filling hazard $q$", text_xy=(6.9, 4.75), linewidth=1.9, connectionstyle="arc3,rad=0.12")
    add_arrow(ax, (5.7, 2.82), (7.15, 1.98), color=COLORS["navy"], text="E -> E job-to-job moves", text_xy=(6.9, 1.05), linewidth=1.9, connectionstyle="arc3,rad=-0.08")
    ax.text(5.0, 5.25, "Week 4 tracks three transition margins, not only unemployment exits.", ha="center", fontsize=13.5, color=COLORS["ink"], weight="semibold")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-worker-flows-and-hazards.png")
    plt.close(fig)


def make_beveridge() -> None:
    unemployment = np.linspace(3, 10, 200)
    baseline = 11 / unemployment + 0.35
    outward_shift = 13 / unemployment + 0.55

    fig, ax = plt.subplots(figsize=(7.6, 5.2))
    ax.plot(unemployment, baseline, linewidth=2.6, color=COLORS["navy"], label="Baseline Beveridge relation")
    ax.plot(unemployment, outward_shift, linewidth=2.4, color=COLORS["rust"], linestyle="--", label="Outward shift")
    ax.scatter([3.8, 6.1, 8.8], [11 / 3.8 + 0.35, 11 / 6.1 + 0.35, 11 / 8.8 + 0.35], color=COLORS["navy"], s=26)
    ax.scatter([4.1, 6.4, 9.1], [13 / 4.1 + 0.55, 13 / 6.4 + 0.55, 13 / 9.1 + 0.55], color=COLORS["rust"], s=26)
    ax.annotate(
        "Composition or mismatch shift",
        xy=(6.4, 2.58),
        xytext=(7.25, 3.65),
        arrowprops={"arrowstyle": "->", "color": COLORS["rust"], "linewidth": 1.5},
        fontsize=9,
        color=COLORS["rust"],
    )
    ax.annotate(
        "Stronger matching / tighter market",
        xy=(4.1, 3.72),
        xytext=(3.1, 4.55),
        arrowprops={"arrowstyle": "->", "color": COLORS["navy"], "linewidth": 1.5},
        fontsize=9,
        color=COLORS["navy"],
    )
    ax.set_xlabel("Unemployment rate / job seekers")
    ax.set_ylabel("Vacancies")
    ax.set_title("Beveridge logic: one curve can move for different reasons")
    ax.legend(loc="upper right", fontsize=8)
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-beveridge-matching-efficiency.png")
    plt.close(fig)


def make_separation_churning_jobladder() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.9))

    clean_axis(axes[0], xlim=(0, 10), ylim=(0, 6))
    add_box(axes[0], 0.9, 2.15, 2.2, 1.35, "Stable headcount", edge=COLORS["navy"], fontsize=12.5)
    add_arrow(axes[0], (3.0, 2.85), (5.35, 4.55), color=COLORS["rust"], text="Layoffs / job loss", text_xy=(6.5, 4.55), linewidth=1.9)
    add_arrow(axes[0], (3.0, 2.85), (5.35, 3.2), color=COLORS["teal"], text="Replacement hiring", text_xy=(6.5, 3.2), linewidth=1.9)
    add_arrow(axes[0], (3.0, 2.85), (5.35, 1.45), color=COLORS["gold"], text="Quits to other firms", text_xy=(6.55, 1.45), linewidth=1.9)
    axes[0].text(5.0, 5.2, "Gross worker flows can be large even when net employment is flat.", ha="center", fontsize=12.8, color=COLORS["ink"], weight="semibold")

    clean_axis(axes[1], xlim=(0, 10), ylim=(0, 6))
    add_box(axes[1], 1.0, 1.0, 2.2, 0.95, "Low-wage firm", edge=COLORS["navy"], fontsize=11)
    add_box(axes[1], 4.05, 2.35, 2.2, 0.95, "Middle-wage firm", edge=COLORS["teal"], fontsize=11)
    add_box(axes[1], 7.1, 3.7, 2.0, 0.95, "High-wage firm", edge=COLORS["gold"], fontsize=11)
    add_arrow(axes[1], (3.2, 1.45), (4.05, 2.8), color=COLORS["navy"], linewidth=2.0)
    add_arrow(axes[1], (6.25, 2.8), (7.1, 4.15), color=COLORS["teal"], linewidth=2.0)
    add_arrow(axes[1], (7.8, 4.05), (6.1, 2.85), color=COLORS["rust"], linewidth=1.5, linestyle="--")
    axes[1].text(5.2, 5.2, "Job ladders: E-to-E mobility sorts workers across firms.", ha="center", fontsize=12.8, color=COLORS["ink"], weight="semibold")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-separation-churning-jobladder.png")
    plt.close(fig)


def make_duration_scarring() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    months = np.arange(1, 8)
    observed_hazard = np.array([0.34, 0.29, 0.24, 0.20, 0.17, 0.15, 0.14])
    selection_only = np.array([0.34, 0.31, 0.28, 0.25, 0.23, 0.21, 0.20])

    axes[0].plot(months, observed_hazard, marker="o", linewidth=2.3, color=COLORS["rust"], label="Observed exit hazard")
    axes[0].plot(months, selection_only, marker="s", linewidth=2.0, color=COLORS["navy"], linestyle="--", label="Selection-only benchmark")
    axes[0].set_title("Observed duration dependence")
    axes[0].set_xlabel("Months unemployed")
    axes[0].set_ylabel("U-to-E hazard")
    axes[0].legend(loc="upper right", fontsize=8)
    style_axis(axes[0], grid_axis="both")

    post = np.arange(0, 5)
    quality_fast = np.array([0.0, 0.05, 0.08, 0.10, 0.12])
    quality_scar = np.array([-0.12, -0.08, -0.05, -0.03, -0.01])
    axes[1].plot(post, quality_fast, marker="o", linewidth=2.3, color=COLORS["teal"], label="Short spell / better reemployment")
    axes[1].plot(post, quality_scar, marker="o", linewidth=2.3, color=COLORS["gold"], label="Long spell / scarring path")
    axes[1].axhline(0.0, color=COLORS["muted"], linewidth=0.8)
    axes[1].set_title("Post-reemployment job quality")
    axes[1].set_xlabel("Years after reemployment")
    axes[1].set_ylabel("Quality or wage gap")
    axes[1].legend(loc="upper left", fontsize=8)
    style_axis(axes[1], grid_axis="both")

    fig.suptitle("Duration, selection, and scarring are distinct Week 4 objects", fontsize=13.5, color=COLORS["ink"], weight="semibold")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-unemployment-duration-and-scarring.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    make_course_map()
    make_worker_flows()
    make_beveridge()
    make_separation_churning_jobladder()
    make_duration_scarring()
    print(f"Saved Week 4 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
