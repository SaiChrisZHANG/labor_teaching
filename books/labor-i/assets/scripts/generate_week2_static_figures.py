"""Generate conceptual figures for Labor I Week 2: Static labor supply.

These figures are intentionally schematic so they can be built locally without
external data. They support the Week 2 chapter without changing any teaching
content.
"""
from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, apply_style, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / "assets" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def budget_set_figure() -> None:
    leisure = np.linspace(0, 1, 300)
    total_time = 1.0
    wage = 30.0
    nonlabor_income = 10.0
    tax = 0.25
    fixed_cost = 6.0

    hours = total_time - leisure
    c_no_tax = nonlabor_income + wage * hours
    c_tax = nonlabor_income + (1 - tax) * wage * hours
    c_fixed = np.where(hours > 0, nonlabor_income + (1 - tax) * wage * hours - fixed_cost, nonlabor_income)

    fig, ax = plt.subplots(figsize=(8.0, 5.2))
    ax.plot(leisure, c_no_tax, color=COLORS["navy"], linewidth=2.5, label="No tax")
    ax.plot(leisure, c_tax, color=COLORS["teal"], linewidth=2.5, label="Proportional tax")
    ax.plot(leisure, c_fixed, color=COLORS["rust"], linewidth=2.5, label="Tax plus fixed work cost")
    ax.set_xlabel("Leisure share")
    ax.set_ylabel("Consumption")
    ax.set_title("Static labor-supply budget sets")
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "02-static-budget-sets.png")
    plt.close(fig)


def eitc_schematic() -> None:
    earnings = np.linspace(0, 60, 600)
    base = 5.0
    phase_in_rate = 0.4
    phase_out_rate = 0.21
    phase_in_end, phase_out_start = 12.0, 28.0

    credit = np.piecewise(
        earnings,
        [earnings <= phase_in_end, (earnings > phase_in_end) & (earnings <= phase_out_start), earnings > phase_out_start],
        [
            lambda x: phase_in_rate * x,
            lambda x: phase_in_rate * phase_in_end,
            lambda x: np.maximum(phase_in_rate * phase_in_end - phase_out_rate * (x - phase_out_start), 0),
        ],
    )
    baseline = base + earnings
    consumption = baseline + credit

    fig, ax = plt.subplots(figsize=(8.1, 5.2))
    ax.plot(earnings, consumption, color=COLORS["navy"], linewidth=2.6)
    ax.fill_between(earnings, baseline, consumption, color=COLORS["gold"], alpha=0.16)
    ax.axvline(phase_in_end, linestyle="--", linewidth=1.2, color=COLORS["muted"])
    ax.axvline(phase_out_start, linestyle="--", linewidth=1.2, color=COLORS["muted"])
    ax.text(phase_in_end + 0.9, 23.0, "Phase-in ends", rotation=90, color=COLORS["muted"], fontsize=9)
    ax.text(phase_out_start + 0.9, 23.0, "Phase-out begins", rotation=90, color=COLORS["muted"], fontsize=9)
    ax.set_xlabel("Pre-tax earnings")
    ax.set_ylabel("Consumption resources")
    ax.set_title("Stylized piecewise-linear tax-transfer schedule")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "02-eitc-schematic.png")
    plt.close(fig)


def main() -> None:
    apply_style()
    budget_set_figure()
    eitc_schematic()
    print(f"Saved figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
