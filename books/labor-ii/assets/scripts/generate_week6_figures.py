#!/usr/bin/env python3
"""Generate the required Week 6 figures for Labor II."""
from __future__ import annotations

import os
from pathlib import Path
import sys
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, add_arrow, add_box, apply_style, clean_axis, rgba, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def course_map() -> None:
    fig, ax = plt.subplots(figsize=(8.9, 5.1))
    clean_axis(ax, xlim=(0, 10), ylim=(0, 6))

    add_box(ax, 0.7, 2.0, 2.35, 1.7, "Week 5\nWage posting,\nbargaining,\npay rules", edge=COLORS["navy"], fontsize=12.2)
    add_box(ax, 3.85, 1.75, 2.35, 2.1, "Week 6\nMonopsony,\nmeasurement,\nsources of power", edge=COLORS["teal"], fontsize=12.1)
    add_box(ax, 6.95, 2.0, 2.35, 1.7, "Week 7\nMinimum wages,\npolicy incidence", edge=COLORS["gold"], fontsize=12.2)

    add_arrow(ax, (3.05, 2.85), (3.85, 2.85), text="protocols -> power", text_xy=(3.44, 4.1))
    add_arrow(ax, (6.20, 2.85), (6.95, 2.85), text="power -> policy", text_xy=(6.58, 4.1))
    ax.text(5.0, 5.18, "Week 6 turns wage-setting protocols into measurable employer power.", ha="center", fontsize=13.5, color=COLORS["ink"], weight="semibold")
    ax.text(5.0, 0.82, "Core objects: labor supply to the firm, markdowns, concentration, mergers, pass-through.", ha="center", fontsize=10, color=COLORS["muted"])

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-monopsony-course-map.png")
    plt.close(fig)


def classic_vs_modern() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.1))

    clean_axis(axes[0], xlim=(0, 10), ylim=(0, 6))
    axes[0].set_title("Classic monopsony", fontsize=13.5, color=COLORS["ink"])
    add_box(axes[0], 3.0, 2.1, 3.0, 1.7, "One dominant\nemployer", edge=COLORS["navy"], fontsize=13)
    for worker_x in [1.45, 1.75, 2.05, 2.35]:
        axes[0].scatter(worker_x, 4.6, s=34, color=COLORS["gold"], edgecolors="white", linewidth=0.7)
        add_arrow(axes[0], (worker_x, 4.25), (4.1, 3.7), color=COLORS["muted"], linewidth=1.4, shrink_a=4, shrink_b=8)
    for worker_x in [7.0, 7.3, 7.6, 7.9]:
        axes[0].scatter(worker_x, 1.4, s=34, color=COLORS["gold"], edgecolors="white", linewidth=0.7)
        add_arrow(axes[0], (worker_x, 1.75), (5.0, 2.25), color=COLORS["muted"], linewidth=1.4, shrink_a=4, shrink_b=8)
    axes[0].text(4.5, 5.18, "Employer directly internalizes the wage-employment tradeoff.", ha="center", fontsize=10.2, color=COLORS["muted"])
    axes[0].text(4.5, 0.58, "Useful benchmark for thin markets, not the whole modern field.", ha="center", fontsize=10.0, color=COLORS["muted"])

    clean_axis(axes[1], xlim=(0, 10), ylim=(0, 6))
    axes[1].set_title("Modern dynamic/search monopsony", fontsize=13.5, color=COLORS["ink"])
    firms = [(1.0, 3.9, 2.0, 1.15, "Firm A", COLORS["navy"]), (4.0, 2.2, 2.0, 1.15, "Firm B", COLORS["teal"]), (7.0, 3.9, 2.0, 1.15, "Firm C", COLORS["gold"])]
    for x, y, w, h, label, edge in firms:
        add_box(axes[1], x, y, w, h, label, edge=edge, fontsize=12)
    worker_points = [(2.2, 1.0), (3.6, 4.8), (5.0, 0.95), (6.5, 4.8)]
    for x, y in worker_points:
        axes[1].scatter(x, y, s=40, color=COLORS["rust"], edgecolors="white", linewidth=0.7, zorder=4)
    for start, end in [((2.2, 1.0), (2.0, 3.9)), ((2.2, 1.0), (5.0, 2.2)), ((3.6, 4.8), (5.0, 3.35)), ((3.6, 4.8), (8.0, 3.95)), ((5.0, 0.95), (5.0, 2.2)), ((6.5, 4.8), (8.0, 3.95))]:
        add_arrow(axes[1], start, end, color=COLORS["muted"], linewidth=1.4, alpha=0.85, shrink_a=4, shrink_b=8)
    axes[1].text(5.0, 5.18, "Power comes from imperfect mobility, not only from a single employer.", ha="center", fontsize=10.2, color=COLORS["muted"])
    axes[1].text(5.0, 0.46, "Many firms can still face finite labor-supply elasticities.", ha="center", fontsize=10.0, color=COLORS["muted"])

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-classic-vs-modern-monopsony.png")
    plt.close(fig)


def labor_supply_to_firm() -> None:
    employment = np.linspace(0.5, 10.0, 300)
    wage = 0.65 + 0.12 * employment + 0.008 * employment**2
    marginal_cost = wage + employment * (0.12 + 0.016 * employment)
    market_supply = 0.85 + 0.04 * employment

    chosen_n = 5.8
    chosen_w = 0.65 + 0.12 * chosen_n + 0.008 * chosen_n**2
    chosen_mcl = chosen_w + chosen_n * (0.12 + 0.016 * chosen_n)

    fig, ax = plt.subplots(figsize=(8.8, 5.3))
    ax.plot(employment, wage, linewidth=2.8, color=COLORS["navy"], label="Labor supply to the firm")
    ax.plot(employment, marginal_cost, linewidth=2.8, color=COLORS["rust"], label="Marginal cost of labor")
    ax.plot(employment, market_supply, linewidth=2.2, linestyle="--", color=COLORS["teal"], label="Illustrative market labor supply")
    ax.vlines(chosen_n, 0.6, chosen_mcl, colors=COLORS["muted"], linestyles=":", linewidth=1.1)
    ax.hlines(chosen_w, 0.5, chosen_n, colors=COLORS["navy"], linestyles=":", linewidth=1.1)
    ax.hlines(chosen_mcl, 0.5, chosen_n, colors=COLORS["rust"], linestyles=":", linewidth=1.1)
    ax.annotate("Wage paid", xy=(chosen_n, chosen_w), xytext=(7.0, 1.95), arrowprops={"arrowstyle": "->", "linewidth": 1.4, "color": COLORS["navy"]}, fontsize=9, color=COLORS["navy"])
    ax.annotate("Marginal labor cost", xy=(chosen_n, chosen_mcl), xytext=(6.9, 3.15), arrowprops={"arrowstyle": "->", "linewidth": 1.4, "color": COLORS["rust"]}, fontsize=9, color=COLORS["rust"])
    ax.text(1.15, 3.78, "The firm's elasticity is about\nmovement across firms.", fontsize=9.5, color=COLORS["muted"])
    ax.set_xlabel("Employment at the firm")
    ax.set_ylabel("Wage or cost index")
    ax.set_title("Labor supply to the firm differs from market labor supply")
    ax.legend(loc="upper left", fontsize=8.5)
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-labor-supply-to-the-firm.png")
    plt.close(fig)


def markdown_measurement_map() -> None:
    fig, ax = plt.subplots(figsize=(10.9, 5.5))
    clean_axis(ax, xlim=(0, 12), ylim=(0, 6))

    left_boxes = [(0.65, 4.18, 2.3, 1.0, "Wage variation\nand applications", COLORS["navy"]), (0.65, 2.58, 2.3, 1.0, "Quit / retention\nvariation", COLORS["teal"]), (0.65, 0.98, 2.3, 1.0, "Production-side\nmoments", COLORS["gold"])]
    middle_boxes = [(4.15, 4.18, 2.65, 1.0, "Labor supply /\nrecruiting elasticity", COLORS["navy"]), (4.15, 2.58, 2.65, 1.0, "Dynamic monopsony\nthrough mobility", COLORS["teal"]), (4.15, 0.98, 2.65, 1.0, "Markdown:\nMRPL / wage", COLORS["gold"])]
    right_boxes = [(8.35, 4.18, 2.95, 1.0, "Concentration and\nmerger evidence", COLORS["rust"]), (8.35, 2.58, 2.95, 1.0, "Firm shocks and\npass-through", COLORS["slate"]), (8.35, 0.98, 2.95, 1.0, "Partial views of\nlabor market power", COLORS["teal"])]

    for x, y, w, h, text, edge in left_boxes + middle_boxes + right_boxes:
        add_box(ax, x, y, w, h, text, edge=edge, fontsize=10.6)

    for y in [4.68, 3.08, 1.48]:
        add_arrow(ax, (2.95, y), (4.15, y), color=COLORS["muted"], linewidth=1.7)
        add_arrow(ax, (6.8, y), (8.35, y), color=COLORS["muted"], linewidth=1.7)

    ax.text(6.0, 5.55, "Different data and designs recover different monopsony objects.", ha="center", fontsize=13.5, color=COLORS["ink"], weight="semibold")
    ax.text(6.0, 0.28, "Conceptual agreement does not require numerical identity across measures.", ha="center", fontsize=10, color=COLORS["muted"])

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-markdown-measurement-map.png")
    plt.close(fig)


def sources_of_power() -> None:
    fig, ax = plt.subplots(figsize=(9.7, 5.7))
    clean_axis(ax, xlim=(0, 10), ylim=(0, 6))

    add_box(ax, 3.55, 2.2, 2.9, 1.55, "Employer\nwage-setting\npower", edge=COLORS["rust"], face=rgba(COLORS["rust"], 0.10), fontsize=13.2)
    nodes = [
        (0.9, 4.52, 2.0, 0.9, "Search and\nmobility frictions", COLORS["navy"]),
        (4.0, 4.95, 2.0, 0.9, "Amenities and\njob differentiation", COLORS["teal"]),
        (7.05, 4.52, 2.0, 0.9, "Information\nfrictions", COLORS["gold"]),
        (0.75, 0.95, 2.25, 0.9, "Geographic or\noccupational thinness", COLORS["slate"]),
        (3.88, 0.45, 2.25, 0.9, "Concentration and\nlarge employers", COLORS["teal"]),
        (7.0, 0.95, 2.05, 0.9, "Contracts and\ninstitutional barriers", COLORS["rust"]),
    ]
    for x, y, w, h, text, edge in nodes:
        add_box(ax, x, y, w, h, text, edge=edge, fontsize=10.4)
        add_arrow(ax, (x + w / 2, y + h / 2), (5.0, 2.98), color=COLORS["muted"], linewidth=1.5, alpha=0.9)

    ax.text(5.0, 5.76, "Modern monopsony is usually multi-source.", ha="center", fontsize=13.5, color=COLORS["ink"], weight="semibold")
    ax.text(5.0, 0.08, "Concentration matters, but it is only one branch of the causal tree.", ha="center", fontsize=10, color=COLORS["muted"])

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-sources-of-monopsony-power.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    course_map()
    classic_vs_modern()
    labor_supply_to_firm()
    markdown_measurement_map()
    sources_of_power()
    print(f"Wrote Week 6 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
