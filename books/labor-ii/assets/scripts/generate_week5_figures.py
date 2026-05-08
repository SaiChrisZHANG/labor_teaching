#!/usr/bin/env python3
"""Generate the required Week 5 figures for Labor II."""
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

from shared.figure_style import COLORS, add_arrow, add_box, apply_style, clean_axis, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def course_map() -> None:
    fig, ax = plt.subplots(figsize=(8.8, 5.1))
    clean_axis(ax, xlim=(0, 10), ylim=(0, 6))

    add_box(ax, 0.7, 2.1, 2.3, 1.55, "Week 4\nSearch, matching,\nturnover", edge=COLORS["navy"], fontsize=12.4)
    add_box(ax, 3.75, 1.85, 2.5, 2.0, "Week 5\nWage posting,\nbargaining,\nwage rules", edge=COLORS["teal"], fontsize=12.2)
    add_box(ax, 6.95, 2.1, 2.3, 1.55, "Week 6\nMonopsony,\nmarket power", edge=COLORS["gold"], fontsize=12.4)

    add_arrow(ax, (3.0, 2.88), (3.75, 2.88), text="outside options,\nE-to-E mobility", text_xy=(3.38, 4.02))
    add_arrow(ax, (6.25, 2.88), (6.95, 2.88), text="pass-through,\nfirm conduct", text_xy=(6.6, 4.02))
    ax.text(5.0, 5.22, "Week 5 turns worker flows into wage-setting protocols and empirical wage objects.", ha="center", fontsize=13.5, color=COLORS["ink"], weight="semibold")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-wage-setting-course-map.png")
    plt.close(fig)


def posting_vs_bargaining() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.0))

    clean_axis(axes[0], xlim=(0, 10), ylim=(0, 6))
    axes[0].set_title("Posted wages", fontsize=13.5, color=COLORS["ink"])
    add_box(axes[0], 1.0, 2.0, 2.5, 1.9, "Firm chooses\nposted wage", edge=COLORS["navy"], fontsize=12.6)
    for ypos, label, color in [(4.65, "High posted wage", COLORS["teal"]), (3.75, "Medium posted wage", COLORS["navy"]), (2.85, "Low posted wage", COLORS["gold"])]:
        axes[0].plot([5.1, 8.15], [ypos, ypos], linewidth=2.6, color=color)
        axes[0].text(8.45, ypos, label, va="center", fontsize=9.5, color=COLORS["muted"])
    add_arrow(axes[0], (3.5, 2.95), (5.0, 3.75), color=COLORS["muted"], linewidth=1.8)
    axes[0].text(5.95, 5.15, "Recruiting and retention respond\nto the posted schedule.", ha="center", fontsize=10.2, color=COLORS["muted"])
    axes[0].text(5.95, 1.02, "Worker mobility sorts matches across the wage ladder.", ha="center", fontsize=10.2, color=COLORS["muted"])

    clean_axis(axes[1], xlim=(0, 10), ylim=(0, 6))
    axes[1].set_title("Individualized bargaining", fontsize=13.5, color=COLORS["ink"])
    add_box(axes[1], 1.1, 2.0, 2.15, 1.9, "Worker", edge=COLORS["navy"], fontsize=13)
    add_box(axes[1], 6.75, 2.0, 2.15, 1.9, "Firm", edge=COLORS["gold"], fontsize=13)
    add_arrow(axes[1], (3.3, 3.28), (6.72, 3.28), color=COLORS["rust"], linewidth=2.0, bidirectional=True)
    add_arrow(axes[1], (3.3, 2.64), (6.72, 2.64), color=COLORS["teal"], linewidth=2.0, bidirectional=True)
    axes[1].text(5.0, 3.88, "Outside offers,\nnonemployment value", ha="center", fontsize=10.2, color=COLORS["muted"])
    axes[1].text(5.0, 1.75, "Threat points and\nbargaining power", ha="center", fontsize=10.2, color=COLORS["muted"])
    axes[1].text(5.0, 5.15, "Wage depends on the protocol used to split surplus.", ha="center", fontsize=10.2, color=COLORS["muted"])

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-posting-vs-bargaining.png")
    plt.close(fig)


def outside_options() -> None:
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    clean_axis(ax, xlim=(0, 10), ylim=(0, 6))
    label_box = {"facecolor": "white", "edgecolor": "none", "pad": 0.12}

    add_box(ax, 0.9, 2.25, 2.0, 1.2, "Value of\nnonemployment\n$V^U$", edge=COLORS["navy"], fontsize=11.5)
    add_box(ax, 4.0, 4.0, 2.0, 1.0, "Outside\noffer", edge=COLORS["teal"], fontsize=11.5)
    add_box(ax, 4.0, 0.95, 2.0, 1.0, "Reservation\nwage", edge=COLORS["gold"], fontsize=11.5)
    add_box(ax, 7.1, 2.25, 2.0, 1.2, "Threat point\nin bargaining", edge=COLORS["rust"], fontsize=11.5)
    add_box(ax, 4.0, 2.3, 2.0, 1.1, "Current wage", edge=COLORS["slate"], fontsize=11.8, face=(0.95, 0.96, 0.97, 1.0))

    add_arrow(ax, (2.9, 2.85), (4.0, 2.85), color=COLORS["muted"])
    add_arrow(ax, (5.0, 4.0), (5.0, 3.4), color=COLORS["muted"])
    add_arrow(ax, (5.0, 2.3), (5.0, 1.95), color=COLORS["muted"])
    add_arrow(ax, (6.0, 2.85), (7.1, 2.85), color=COLORS["muted"])

    ax.text(2.55, 3.42, "Fallback value", ha="left", va="bottom", fontsize=9.2, color=COLORS["muted"], bbox=label_box)
    ax.text(6.2, 3.95, "Realized offer", ha="left", va="bottom", fontsize=9.2, color=COLORS["muted"], bbox=label_box)
    ax.text(6.2, 1.62, "Acceptance cutoff", ha="left", va="top", fontsize=9.2, color=COLORS["muted"], bbox=label_box)
    ax.text(7.1, 3.42, "Protocol-specific link", ha="center", va="bottom", fontsize=9.0, color=COLORS["muted"], bbox=label_box)

    ax.text(5.0, 5.38, "Week 5 separates fallback values, realized outside offers, and bargaining threat points.", ha="center", fontsize=13.2, color=COLORS["ink"], weight="semibold")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-outside-options-and-wage-setting.png")
    plt.close(fig)


def rent_sharing() -> None:
    shock = np.linspace(-0.12, 0.18, 200)
    high_pass = 0.06 + 0.48 * shock
    low_pass = 0.04 + 0.18 * shock
    outside_option = 0.05 + 0.32 * shock

    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    ax.plot(shock, high_pass, linewidth=2.8, color=COLORS["rust"], label="High pass-through from firm shock")
    ax.plot(shock, low_pass, linewidth=2.8, color=COLORS["navy"], label="Low pass-through from firm shock")
    ax.plot(shock, outside_option, linewidth=2.3, linestyle="--", color=COLORS["teal"], label="Outside-option shock pass-through")
    ax.axhline(0.05, color=COLORS["muted"], linestyle=":", linewidth=1.0)
    ax.axvline(0.0, color=COLORS["muted"], linestyle=":", linewidth=1.0)
    ax.annotate(
        "Same firm shock,\ndifferent wage response",
        xy=(0.12, 0.118),
        xytext=(0.06, 0.165),
        arrowprops={"arrowstyle": "->", "linewidth": 1.5, "color": COLORS["rust"]},
        fontsize=9,
        color=COLORS["rust"],
    )
    ax.annotate(
        "Different object:\nfallback-value shock",
        xy=(0.1, 0.082),
        xytext=(0.128, 0.033),
        arrowprops={"arrowstyle": "->", "linewidth": 1.5, "color": COLORS["teal"]},
        fontsize=9,
        color=COLORS["teal"],
    )
    ax.set_xlabel("Shock to firm surplus or outside option")
    ax.set_ylabel("Change in log wage")
    ax.set_title("Pass-through and rent-sharing depend on the wage-setting object")
    ax.legend(loc="upper left", fontsize=8.5)
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-rent-sharing-pass-through.png")
    plt.close(fig)


def standardized_vs_discretionary() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0))

    steps_x = np.arange(1, 7)
    steps_y = np.array([1.4, 1.4, 2.1, 2.1, 2.8, 2.8])
    axes[0].step(steps_x, steps_y, where="mid", linewidth=2.8, color=COLORS["navy"])
    axes[0].scatter(steps_x, steps_y, s=34, color=COLORS["navy"])
    axes[0].set_title("Standardized pay schedule")
    axes[0].set_xlabel("Grade / step")
    axes[0].set_ylabel("Wage")
    axes[0].text(1.2, 3.0, "Compression within grade,\ntransparent progression", fontsize=9.5, color=COLORS["muted"])
    style_axis(axes[0], grid_axis="both")

    rng = np.random.default_rng(20260505)
    tenure = np.linspace(1, 6, 70)
    wages = 1.05 + 0.28 * tenure + rng.normal(0.0, 0.23, size=tenure.size)
    axes[1].scatter(tenure, wages, s=20, alpha=0.72, color=COLORS["rust"], edgecolors="none")
    slope, intercept = np.polyfit(tenure, wages, deg=1)
    axes[1].plot(tenure, intercept + slope * tenure, linewidth=2.4, color=COLORS["muted"])
    axes[1].set_title("Discretionary pay setting")
    axes[1].set_xlabel("Role / tenure index")
    axes[1].set_ylabel("Wage")
    axes[1].text(1.15, wages.max() - 0.08, "Same broad role,\nmore within-cell spread", fontsize=9.5, color=COLORS["muted"])
    style_axis(axes[1], grid_axis="both")

    fig.suptitle("Standardization compresses pay; discretion leaves more room for bargaining and managerial choice.", fontsize=13.2, color=COLORS["ink"], weight="semibold")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-standardized-vs-discretionary-pay.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    course_map()
    posting_vs_bargaining()
    outside_options()
    rent_sharing()
    standardized_vs_discretionary()
    print(f"Wrote Week 5 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
