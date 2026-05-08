#!/usr/bin/env python3
"""Generate conceptual Week 6 figures for Labor I."""
from __future__ import annotations

import os
from pathlib import Path
import sys

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, apply_style, save_figure, style_axis


FIG_DIR = Path(__file__).resolve().parents[1] / "figures"


def household_time_allocation() -> None:
    states = ["Pre-child", "Post-child"]
    market = np.array([7.2, 4.9])
    home = np.array([2.4, 5.4])
    leisure = np.array([6.4, 5.7])
    x = np.arange(len(states))

    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    ax.bar(x, market, color=COLORS["navy"], width=0.56, label="Market work")
    ax.bar(x, home, bottom=market, color=COLORS["rust"], width=0.56, label="Home production and care")
    ax.bar(x, leisure, bottom=market + home, color=COLORS["teal"], width=0.56, label="Leisure")
    ax.text(-0.12, 13.6, "Childbirth raises the shadow value of care time", fontsize=9.5, color=COLORS["muted"])
    ax.text(0.82, 10.2, "Hours and leisure are reallocated,\nnot only preferences", fontsize=9.5, color=COLORS["muted"])
    ax.set_xticks(x, states)
    ax.set_ylabel("Hours in a stylized non-sleep day")
    ax.set_title("Household time allocation before and after childbirth")
    ax.set_ylim(0, 18)
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="y")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-household-time-allocation-schematic.png")
    plt.close(fig)


def child_penalty_event_study() -> None:
    event_time = np.arange(-5, 11)
    mothers = np.array([0.01, 0.01, 0.005, 0.0, 0.0, -0.08, -0.18, -0.24, -0.27, -0.29, -0.30, -0.31, -0.31, -0.30, -0.30, -0.29])
    fathers = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005, 0.01, 0.01, 0.012, 0.012, 0.013, 0.013, 0.014, 0.014, 0.015])

    fig, ax = plt.subplots(figsize=(9.0, 5.6))
    ax.plot(event_time, mothers, color=COLORS["rust"], linewidth=2.7, marker="o", markersize=3.8, label="Mothers")
    ax.plot(event_time, fathers, color=COLORS["navy"], linewidth=2.7, marker="o", markersize=3.8, label="Fathers")
    ax.axhline(0.0, color=COLORS["muted"], linewidth=1.0)
    ax.axvline(0.0, color=COLORS["muted"], linewidth=1.0, linestyle="--")
    ax.axvspan(-0.1, 0.9, color=COLORS["gold"], alpha=0.16)
    ax.text(0.18, 0.022, "First birth", fontsize=9.5, color=COLORS["muted"])
    ax.text(4.6, -0.27, "Persistent post-birth earnings penalty", fontsize=9.5, color=COLORS["muted"])
    ax.set_xlabel("Years relative to first birth")
    ax.set_ylabel("Log earnings relative to year -1")
    ax.set_title("Stylized event-study child penalty in earnings")
    ax.set_xlim(-5, 10)
    ax.set_ylim(-0.36, 0.05)
    ax.legend(loc="lower left")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-child-penalty-event-study.png")
    plt.close(fig)


def childcare_substitution() -> None:
    care_price = np.linspace(0.15, 1.05, 200)
    baseline = 0.26 + 0.36 * (1.05 - care_price)
    high_cost = baseline - 0.08 * np.exp(-((care_price - 0.82) / 0.17) ** 2)
    low_cost = baseline + 0.08 * np.exp(-((care_price - 0.42) / 0.19) ** 2)

    fig, ax = plt.subplots(figsize=(8.8, 5.6))
    ax.plot(care_price, high_cost, linewidth=2.7, color=COLORS["rust"], label="Without cheap substitutes")
    ax.plot(care_price, low_cost, linewidth=2.7, color=COLORS["navy"], label="With childcare / household-service access")
    ax.axvspan(0.18, 0.42, color=COLORS["navy"], alpha=0.10)
    ax.text(0.20, 0.57, "Lower effective care price", fontsize=9.5, color=COLORS["muted"])
    ax.text(0.62, 0.37, "Labor supply responds more when market substitutes exist", fontsize=9.5, color=COLORS["muted"])
    ax.set_xlabel("Price of childcare or home-production substitute")
    ax.set_ylabel("Market hours of high-opportunity-cost spouse")
    ax.set_title("Cheaper market substitutes relax the home-production constraint")
    ax.set_xlim(0.15, 1.05)
    ax.set_ylim(0.22, 0.68)
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "06-childcare-substitution-schematic.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    household_time_allocation()
    child_penalty_event_study()
    childcare_substitution()
    print(f"Wrote Week 6 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
