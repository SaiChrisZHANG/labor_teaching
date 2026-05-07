#!/usr/bin/env python3
"""Generate the required Week 6 figures for Labor II."""
from __future__ import annotations

import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"

BLUE = "#3B6EA8"
TEAL = "#4E9A8E"
GOLD = "#C79A35"
RED = "#B55D4C"
GRAY = "#4F5B66"
LIGHT = "#E9EEF4"
PALE = "#F7F4E8"


def clean_axis(ax) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def course_map() -> None:
    fig, ax = plt.subplots(figsize=(8.8, 5.0))
    clean_axis(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    boxes = [
        (0.7, 2.0, 2.35, 1.7, BLUE, "Week 5\nWage posting,\nbargaining,\npay rules"),
        (3.85, 1.8, 2.35, 2.1, TEAL, "Week 6\nMonopsony,\nmeasurement,\nsources of power"),
        (6.95, 2.0, 2.35, 1.7, GOLD, "Week 7\nMinimum wages,\npolicy incidence"),
    ]
    for x, y, w, h, color, label in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.05,rounding_size=0.16",
                facecolor=LIGHT,
                edgecolor=color,
                linewidth=2.6,
            )
        )
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=13, color=GRAY, weight="bold")

    arrows = [
        ((3.05, 2.85), (3.8, 2.85), "protocols -> power", 4.2),
        ((6.25, 2.85), (6.9, 2.85), "power -> policy", 4.2),
    ]
    for start, end, label, ypos in arrows:
        ax.add_patch(
            FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18, linewidth=2.2, color=GRAY)
        )
        ax.text((start[0] + end[0]) / 2, ypos, label, ha="center", va="bottom", fontsize=10, color=GRAY)

    ax.text(
        5.0,
        5.2,
        "Week 6 turns wage-setting protocols into measurable employer power",
        ha="center",
        fontsize=14,
        color=GRAY,
    )
    ax.text(
        5.0,
        0.9,
        "Core objects: labor supply to the firm, markdowns, concentration, mergers, pass-through",
        ha="center",
        fontsize=10.5,
        color=GRAY,
    )
    fig.tight_layout()
    fig.savefig(FIG_DIR / "06-monopsony-course-map.png", dpi=220)
    plt.close(fig)


def classic_vs_modern() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.0))
    for ax in axes:
        clean_axis(ax)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)

    ax = axes[0]
    ax.set_title("Classic monopsony", fontsize=14, color=GRAY)
    ax.add_patch(
        FancyBboxPatch((3.0, 2.15), 3.0, 1.7, boxstyle="round,pad=0.05,rounding_size=0.14", facecolor=LIGHT, edgecolor=BLUE, linewidth=2.6)
    )
    ax.text(4.5, 3.0, "One dominant\nemployer", ha="center", va="center", fontsize=14, color=GRAY, weight="bold")
    for worker_x in [1.5, 1.7, 2.0, 2.2, 7.0, 7.3, 7.6, 7.9]:
        ax.scatter(worker_x, 4.6 if worker_x < 3.0 else 1.4, s=60, color=GOLD, edgecolors="white", linewidth=0.8)
        ax.add_patch(FancyArrowPatch((worker_x, 4.25 if worker_x < 3.0 else 1.75), (4.2 if worker_x < 3.0 else 4.8, 3.75 if worker_x < 3.0 else 2.25), arrowstyle="-|>", mutation_scale=13, linewidth=1.5, color=GRAY, alpha=0.85))
    ax.text(4.5, 5.2, "Employer directly internalizes the wage-employment tradeoff", ha="center", fontsize=11, color=GRAY)
    ax.text(4.5, 0.7, "Useful benchmark for thin markets,\nnot the whole modern field", ha="center", fontsize=10.5, color=GRAY)

    ax = axes[1]
    ax.set_title("Modern dynamic/search monopsony", fontsize=14, color=GRAY)
    firms = [
        (1.0, 3.9, 2.0, 1.2, BLUE, "Firm A"),
        (4.0, 2.2, 2.0, 1.2, TEAL, "Firm B"),
        (7.0, 3.9, 2.0, 1.2, GOLD, "Firm C"),
    ]
    for x, y, w, h, color, label in firms:
        ax.add_patch(
            FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.14", facecolor=LIGHT, edgecolor=color, linewidth=2.4)
        )
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=13, color=GRAY, weight="bold")

    worker_points = [(2.2, 1.0), (3.6, 4.8), (5.0, 0.95), (6.5, 4.8)]
    for x, y in worker_points:
        ax.scatter(x, y, s=70, color=RED, edgecolors="white", linewidth=0.8)
    links = [
        ((2.2, 1.0), (2.0, 3.85)),
        ((2.2, 1.0), (5.0, 2.2)),
        ((3.6, 4.8), (5.0, 3.4)),
        ((3.6, 4.8), (8.0, 4.0)),
        ((5.0, 0.95), (5.0, 2.2)),
        ((6.5, 4.8), (8.0, 4.0)),
    ]
    for start, end in links:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=12, linewidth=1.6, color=GRAY, alpha=0.8))
    ax.text(5.0, 5.45, "Power comes from imperfect mobility,\nnot only from a single employer", ha="center", fontsize=11, color=GRAY)
    ax.text(5.0, 0.35, "Many firms can still face finite labor-supply elasticities", ha="center", fontsize=10.5, color=GRAY)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "06-classic-vs-modern-monopsony.png", dpi=220)
    plt.close(fig)


def labor_supply_to_firm() -> None:
    n = np.linspace(0.5, 10.0, 300)
    wage = 0.65 + 0.12 * n + 0.008 * n**2
    mcl = wage + n * (0.12 + 0.016 * n)
    market_supply = 0.85 + 0.04 * n

    fig, ax = plt.subplots(figsize=(8.8, 5.3))
    ax.plot(n, wage, linewidth=3, color=BLUE, label="Labor supply to the firm")
    ax.plot(n, mcl, linewidth=3, color=RED, label="Marginal cost of labor")
    ax.plot(n, market_supply, linewidth=2.4, linestyle="--", color=TEAL, label="Illustrative market labor supply")
    chosen_n = 5.8
    chosen_w = 0.65 + 0.12 * chosen_n + 0.008 * chosen_n**2
    chosen_mcl = chosen_w + chosen_n * (0.12 + 0.016 * chosen_n)
    ax.vlines(chosen_n, 0.6, chosen_mcl, colors="#9AA4AF", linestyles=":", linewidth=1.4)
    ax.hlines(chosen_w, 0.5, chosen_n, colors=BLUE, linestyles=":", linewidth=1.4)
    ax.hlines(chosen_mcl, 0.5, chosen_n, colors=RED, linestyles=":", linewidth=1.4)
    ax.annotate("wage paid", xy=(chosen_n, chosen_w), xytext=(7.0, 1.95), arrowprops={"arrowstyle": "->", "linewidth": 1.7, "color": BLUE}, fontsize=10.5, color=BLUE)
    ax.annotate("marginal labor cost", xy=(chosen_n, chosen_mcl), xytext=(7.05, 3.15), arrowprops={"arrowstyle": "->", "linewidth": 1.7, "color": RED}, fontsize=10.5, color=RED)
    ax.text(1.15, 3.75, "The firm's elasticity is about\nmovement across firms", fontsize=10.5, color=GRAY)
    ax.set_xlabel("Employment at the firm")
    ax.set_ylabel("Wage or cost index")
    ax.set_title("Labor supply to the firm differs from market labor supply")
    ax.grid(alpha=0.2)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "06-labor-supply-to-the-firm.png", dpi=220)
    plt.close(fig)


def markdown_measurement_map() -> None:
    fig, ax = plt.subplots(figsize=(10.5, 5.4))
    clean_axis(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)

    left_boxes = [
        (0.7, 4.2, 2.25, 1.05, BLUE, "Wage variation\nand applications"),
        (0.7, 2.6, 2.25, 1.05, TEAL, "Quit / retention\nvariation"),
        (0.7, 1.0, 2.25, 1.05, GOLD, "Production-side\nmoments"),
    ]
    middle_boxes = [
        (4.2, 4.2, 2.6, 1.05, BLUE, "Labor supply /\nrecruiting elasticity"),
        (4.2, 2.6, 2.6, 1.05, TEAL, "Dynamic monopsony\nthrough mobility"),
        (4.2, 1.0, 2.6, 1.05, GOLD, "Markdown:\nMRPL / wage"),
    ]
    right_boxes = [
        (8.3, 4.2, 2.95, 1.05, RED, "Concentration and\nmerger evidence"),
        (8.3, 2.6, 2.95, 1.05, "#7C6CA8", "Firm shocks and\npass-through"),
        (8.3, 1.0, 2.95, 1.05, "#5C7C57", "Partial views of\nlabor market power"),
    ]

    for group in (left_boxes, middle_boxes, right_boxes):
        for x, y, w, h, color, label in group:
            ax.add_patch(
                FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.12", facecolor=LIGHT, edgecolor=color, linewidth=2.2)
            )
            ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=11.5, color=GRAY, weight="bold")

    for y in [4.72, 3.12, 1.52]:
        ax.add_patch(FancyArrowPatch((2.98, y), (4.1, y), arrowstyle="-|>", mutation_scale=15, linewidth=1.9, color=GRAY))
    for start, end in [((6.85, 4.72), (8.2, 4.72)), ((6.85, 3.12), (8.2, 3.12)), ((6.85, 1.52), (8.2, 1.52))]:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15, linewidth=1.9, color=GRAY))

    ax.text(6.0, 5.55, "Different data and designs recover different monopsony objects", ha="center", fontsize=14, color=GRAY)
    ax.text(6.0, 0.4, "Conceptual agreement does not require numerical identity across measures", ha="center", fontsize=10.5, color=GRAY)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "06-markdown-measurement-map.png", dpi=220)
    plt.close(fig)


def sources_of_power() -> None:
    fig, ax = plt.subplots(figsize=(9.4, 5.5))
    clean_axis(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    ax.add_patch(
        FancyBboxPatch((3.5, 2.2), 3.0, 1.55, boxstyle="round,pad=0.05,rounding_size=0.16", facecolor=PALE, edgecolor=RED, linewidth=2.6)
    )
    ax.text(5.0, 2.98, "Employer\nwage-setting\npower", ha="center", va="center", fontsize=14, color=GRAY, weight="bold")

    nodes = [
        (1.0, 4.5, 2.0, 0.95, BLUE, "Search and\nmobility frictions"),
        (4.0, 4.95, 2.0, 0.95, TEAL, "Amenities and\njob differentiation"),
        (7.0, 4.5, 2.0, 0.95, GOLD, "Information\nfrictions"),
        (0.8, 0.95, 2.2, 0.95, "#7C6CA8", "Geographic or\noccupational thinness"),
        (3.9, 0.45, 2.2, 0.95, "#5C7C57", "Concentration and\nlarge employers"),
        (7.0, 0.95, 2.0, 0.95, RED, "Contracts and\ninstitutional barriers"),
    ]
    for x, y, w, h, color, label in nodes:
        ax.add_patch(
            FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.14", facecolor=LIGHT, edgecolor=color, linewidth=2.2)
        )
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=11.2, color=GRAY, weight="bold")
        center = (x + w / 2, y + h / 2)
        ax.add_patch(FancyArrowPatch(center, (5.0, 2.98), arrowstyle="-|>", mutation_scale=14, linewidth=1.7, color=GRAY, alpha=0.85))

    ax.text(5.0, 5.75, "Modern monopsony is usually multi-source", ha="center", fontsize=14, color=GRAY)
    ax.text(5.0, 0.1, "Concentration matters, but it is only one branch of the causal tree", ha="center", fontsize=10.3, color=GRAY)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "06-sources-of-monopsony-power.png", dpi=220)
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    course_map()
    classic_vs_modern()
    labor_supply_to_firm()
    markdown_measurement_map()
    sources_of_power()
    print(f"Wrote Week 6 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
