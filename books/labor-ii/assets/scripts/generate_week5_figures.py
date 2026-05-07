#!/usr/bin/env python3
"""Generate the required Week 5 figures for Labor II."""
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


def clean_axis(ax) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def course_map() -> None:
    fig, ax = plt.subplots(figsize=(8.6, 4.9))
    clean_axis(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    boxes = [
        (0.7, 2.1, 2.35, 1.55, BLUE, "Week 4\nSearch, Matching,\nTurnover"),
        (3.8, 1.9, 2.45, 1.95, TEAL, "Week 5\nWage Posting,\nBargaining,\nWage Rules"),
        (6.95, 2.1, 2.35, 1.55, GOLD, "Week 6\nMonopsony,\nMarket Power"),
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
        ((3.05, 2.88), (3.75, 2.88), "outside options,\nE-E mobility", 4.15),
        ((6.28, 2.88), (6.9, 2.88), "pass-through,\nfirm conduct", 4.15),
    ]
    for start, end, label, ypos in arrows:
        ax.add_patch(
            FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18, linewidth=2.2, color=GRAY)
        )
        ax.text((start[0] + end[0]) / 2, ypos, label, ha="center", va="bottom", fontsize=10, color=GRAY)

    ax.text(5.0, 5.15, "Week 5 turns worker flows into wage-setting protocols and empirical wage objects", ha="center", fontsize=14, color=GRAY)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "05-wage-setting-course-map.png", dpi=220)
    plt.close(fig)


def posting_vs_bargaining() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.9))

    for ax in axes:
        clean_axis(ax)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)

    ax = axes[0]
    ax.set_title("Posted wages", fontsize=14, color=GRAY)
    ax.add_patch(
        FancyBboxPatch((1.0, 2.0), 2.5, 1.9, boxstyle="round,pad=0.05,rounding_size=0.12", facecolor=LIGHT, edgecolor=BLUE, linewidth=2.4)
    )
    ax.text(2.25, 2.95, "Firm chooses\nposted wage", ha="center", va="center", fontsize=13, color=GRAY, weight="bold")
    for ypos, label in [(4.7, "High posted wage"), (3.8, "Medium posted wage"), (2.9, "Low posted wage")]:
        ax.plot([5.0, 8.5], [ypos, ypos], linewidth=3, color=TEAL if ypos > 3.0 else GOLD)
        ax.text(8.75, ypos, label, va="center", fontsize=10, color=GRAY)
    ax.add_patch(FancyArrowPatch((3.55, 2.95), (4.85, 3.75), arrowstyle="-|>", mutation_scale=18, linewidth=2.2, color=GRAY))
    ax.text(5.9, 5.15, "Recruiting and retention respond\nto the posted schedule", ha="center", fontsize=11, color=GRAY)
    ax.text(5.9, 1.15, "Worker mobility sorts matches across the wage ladder", ha="center", fontsize=11, color=GRAY)

    ax = axes[1]
    ax.set_title("Individualized bargaining", fontsize=14, color=GRAY)
    ax.add_patch(
        FancyBboxPatch((1.2, 2.0), 2.2, 1.9, boxstyle="round,pad=0.05,rounding_size=0.12", facecolor=LIGHT, edgecolor=BLUE, linewidth=2.4)
    )
    ax.add_patch(
        FancyBboxPatch((6.4, 2.0), 2.2, 1.9, boxstyle="round,pad=0.05,rounding_size=0.12", facecolor=LIGHT, edgecolor=GOLD, linewidth=2.4)
    )
    ax.text(2.3, 2.95, "Worker", ha="center", va="center", fontsize=13, color=GRAY, weight="bold")
    ax.text(7.5, 2.95, "Firm", ha="center", va="center", fontsize=13, color=GRAY, weight="bold")
    ax.add_patch(FancyArrowPatch((3.55, 3.25), (6.25, 3.25), arrowstyle="<->", mutation_scale=18, linewidth=2.2, color=RED))
    ax.add_patch(FancyArrowPatch((3.55, 2.65), (6.25, 2.65), arrowstyle="<->", mutation_scale=18, linewidth=2.2, color=TEAL))
    ax.text(4.9, 3.55, "outside offers,\nnonemployment value", ha="center", fontsize=11, color=GRAY)
    ax.text(4.9, 2.05, "threat points and\nbargaining power", ha="center", fontsize=11, color=GRAY)
    ax.text(4.9, 5.05, "Wage depends on the protocol used to split surplus", ha="center", fontsize=11, color=GRAY)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "05-posting-vs-bargaining.png", dpi=220)
    plt.close(fig)


def outside_options() -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    clean_axis(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    nodes = [
        (1.0, 2.2, 2.0, 1.25, BLUE, "Value of\nnonemployment\n$V^U$"),
        (4.0, 3.85, 2.0, 1.2, TEAL, "Outside\noffer"),
        (4.0, 0.95, 2.0, 1.2, GOLD, "Reservation\nwage"),
        (7.0, 2.2, 2.0, 1.25, RED, "Threat point\nin bargaining"),
    ]
    for x, y, w, h, color, label in nodes:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.05,rounding_size=0.12",
                facecolor=LIGHT,
                edgecolor=color,
                linewidth=2.4,
            )
        )
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=12, color=GRAY, weight="bold")

    ax.add_patch(
        FancyBboxPatch((4.0, 2.2), 2.0, 1.25, boxstyle="round,pad=0.05,rounding_size=0.12", facecolor="#F7F4E8", edgecolor=GRAY, linewidth=2.2)
    )
    ax.text(5.0, 2.82, "Current wage", ha="center", va="center", fontsize=12, color=GRAY, weight="bold")

    connections = [
        ((3.05, 2.82), (3.95, 2.82), "fallback value", 2.25),
        ((5.0, 3.8), (5.0, 3.45), "realized offer", 4.75),
        ((5.0, 2.15), (5.0, 1.8), "acceptance cutoff", 1.55),
        ((6.05, 2.82), (6.95, 2.82), "protocol-specific link", 2.25),
    ]
    for start, end, label, ypos in connections:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17, linewidth=2.1, color=GRAY))
        ax.text((start[0] + end[0]) / 2, ypos, label, ha="center", fontsize=10, color=GRAY)

    ax.text(5.0, 5.4, "Week 5 separates fallback values, realized outside offers, and bargaining threat points", ha="center", fontsize=14, color=GRAY)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "05-outside-options-and-wage-setting.png", dpi=220)
    plt.close(fig)


def rent_sharing() -> None:
    shock = np.linspace(-0.12, 0.18, 200)
    high_pass = 0.06 + 0.48 * shock
    low_pass = 0.04 + 0.18 * shock
    outside_option = 0.05 + 0.32 * shock

    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    ax.plot(shock, high_pass, linewidth=3, color=RED, label="High pass-through from firm shock")
    ax.plot(shock, low_pass, linewidth=3, color=BLUE, label="Low pass-through from firm shock")
    ax.plot(shock, outside_option, linewidth=2.5, linestyle="--", color=TEAL, label="Outside-option shock pass-through")
    ax.axhline(0.05, color="#9AA4AF", linestyle=":", linewidth=1.2)
    ax.axvline(0.0, color="#9AA4AF", linestyle=":", linewidth=1.2)
    ax.annotate("same firm shock,\ndifferent wage response", xy=(0.12, 0.118), xytext=(0.065, 0.17), arrowprops={"arrowstyle": "->", "linewidth": 1.8, "color": RED}, fontsize=10, color=RED)
    ax.annotate("different object:\nfallback-value shock", xy=(0.1, 0.082), xytext=(0.135, 0.035), arrowprops={"arrowstyle": "->", "linewidth": 1.8, "color": TEAL}, fontsize=10, color=TEAL)
    ax.set_xlabel("Shock to firm surplus or outside option")
    ax.set_ylabel("Change in log wage")
    ax.set_title("Pass-through and rent-sharing depend on which shock moves the wage-setting problem")
    ax.grid(alpha=0.2)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "05-rent-sharing-pass-through.png", dpi=220)
    plt.close(fig)


def standardized_vs_discretionary() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.9))

    steps_x = np.arange(1, 7)
    steps_y = np.array([1.4, 1.4, 2.1, 2.1, 2.8, 2.8])
    axes[0].step(steps_x, steps_y, where="mid", linewidth=3, color=BLUE)
    axes[0].scatter(steps_x, steps_y, s=48, color=BLUE)
    axes[0].set_title("Standardized pay schedule")
    axes[0].set_xlabel("Grade / step")
    axes[0].set_ylabel("Wage")
    axes[0].grid(alpha=0.2)
    axes[0].text(1.2, 3.02, "Compression within grade,\ntransparent progression", fontsize=10, color=GRAY)

    rng = np.random.default_rng(20260505)
    tenure = np.linspace(1, 6, 70)
    wages = 1.05 + 0.28 * tenure + rng.normal(0.0, 0.23, size=tenure.size)
    axes[1].scatter(tenure, wages, s=34, alpha=0.75, color=RED, edgecolors="none")
    slope, intercept = np.polyfit(tenure, wages, deg=1)
    axes[1].plot(tenure, intercept + slope * tenure, linewidth=2.6, color=GRAY)
    axes[1].set_title("Discretionary pay setting")
    axes[1].set_xlabel("Role / tenure index")
    axes[1].set_ylabel("Wage")
    axes[1].grid(alpha=0.2)
    axes[1].text(1.15, wages.max() - 0.08, "Same broad role,\nmore within-cell spread", fontsize=10, color=GRAY)

    fig.suptitle("Standardization compresses pay; discretion leaves more room for bargaining and managerial choice")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "05-standardized-vs-discretionary-pay.png", dpi=220)
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    course_map()
    posting_vs_bargaining()
    outside_options()
    rent_sharing()
    standardized_vs_discretionary()
    print(f"Wrote Week 5 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
