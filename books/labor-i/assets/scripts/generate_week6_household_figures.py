#!/usr/bin/env python3
"""Generate conceptual Week 6 figures for Labor I."""
from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np


FIG_DIR = Path(__file__).resolve().parents[1] / "figures"


def household_time_allocation() -> None:
    states = ["Pre-child", "Post-child"]
    market = np.array([7.2, 4.9])
    home = np.array([2.4, 5.4])
    leisure = np.array([6.4, 5.7])
    x = np.arange(len(states))

    plt.figure(figsize=(8.8, 5.6))
    plt.bar(x, market, color="#4c78a8", width=0.58, label="Market work")
    plt.bar(x, home, bottom=market, color="#f58518", width=0.58, label="Home production and care")
    plt.bar(x, leisure, bottom=market + home, color="#54a24b", width=0.58, label="Leisure")
    plt.text(-0.18, 13.6, "Childbirth raises the shadow value of care time", fontsize=10, color="#374151")
    plt.text(0.84, 10.4, "Hours and leisure are reallocated,\nnot only preferences", fontsize=10, color="#374151")
    plt.xticks(x, states)
    plt.ylabel("Hours in a stylized non-sleep day")
    plt.title("Household time allocation before and after childbirth")
    plt.ylim(0, 18)
    plt.legend(frameon=False, loc="upper right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "06-household-time-allocation-schematic.png", dpi=220)
    plt.close()


def child_penalty_event_study() -> None:
    event_time = np.arange(-5, 11)
    mothers = np.array([0.01, 0.01, 0.005, 0.0, 0.0, -0.08, -0.18, -0.24, -0.27, -0.29, -0.30, -0.31, -0.31, -0.30, -0.30, -0.29])
    fathers = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005, 0.01, 0.01, 0.012, 0.012, 0.013, 0.013, 0.014, 0.014, 0.015])

    plt.figure(figsize=(9.2, 5.7))
    plt.plot(event_time, mothers, color="#c44e52", linewidth=3, marker="o", label="Mothers")
    plt.plot(event_time, fathers, color="#4c78a8", linewidth=3, marker="o", label="Fathers")
    plt.axhline(0.0, color="#7a7a7a", linewidth=1)
    plt.axvline(0.0, color="#7a7a7a", linewidth=1, linestyle="--")
    plt.axvspan(-0.1, 0.9, color="#efe6d8", alpha=0.7)
    plt.text(0.2, 0.022, "First birth", fontsize=10, color="#7a5a2b")
    plt.text(4.6, -0.27, "Persistent post-birth earnings penalty", fontsize=10, color="#7a2f33")
    plt.xlabel("Years relative to first birth")
    plt.ylabel("Log earnings relative to year -1")
    plt.title("Stylized event-study child penalty in earnings")
    plt.xlim(-5, 10)
    plt.ylim(-0.36, 0.05)
    plt.legend(frameon=False, loc="lower left")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "06-child-penalty-event-study.png", dpi=220)
    plt.close()


def childcare_substitution() -> None:
    care_price = np.linspace(0.15, 1.05, 200)
    baseline = 0.26 + 0.36 * (1.05 - care_price)
    high_cost = baseline - 0.08 * np.exp(-((care_price - 0.82) / 0.17) ** 2)
    low_cost = baseline + 0.08 * np.exp(-((care_price - 0.42) / 0.19) ** 2)

    plt.figure(figsize=(8.9, 5.7))
    plt.plot(care_price, high_cost, linewidth=3, color="#8c564b", label="Without cheap substitutes")
    plt.plot(care_price, low_cost, linewidth=3, color="#2a6f97", label="With childcare / household-service access")
    plt.axvspan(0.18, 0.42, color="#dbeafe", alpha=0.7)
    plt.text(0.2, 0.57, "Lower effective care price", fontsize=10, color="#1e4f7a")
    plt.text(0.62, 0.37, "Labor supply responds more when market substitutes exist", fontsize=10, color="#374151")
    plt.xlabel("Price of childcare or home-production substitute")
    plt.ylabel("Market hours of high-opportunity-cost spouse")
    plt.title("Cheaper market substitutes relax the home-production constraint")
    plt.xlim(0.15, 1.05)
    plt.ylim(0.22, 0.68)
    plt.legend(frameon=False, loc="upper right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "06-childcare-substitution-schematic.png", dpi=220)
    plt.close()


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    household_time_allocation()
    child_penalty_event_study()
    childcare_substitution()
    print(f"Wrote Week 6 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
