"""Generate conceptual figures for Labor I Week 2: Static labor supply.

These figures are intentionally schematic so they can be built locally without
external data. They are meant to support the Week 2 chapter and slides while the
empirical figure/lab path is being finalized.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / "assets" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def budget_set_figure() -> None:
    leisure = np.linspace(0, 1, 300)
    total_time = 1.0
    w = 30.0
    y = 10.0
    tax = 0.25
    fixed_cost = 6.0

    hours = total_time - leisure
    c_no_tax = y + w * hours
    c_tax = y + (1 - tax) * w * hours
    c_fixed = np.where(hours > 0, y + (1 - tax) * w * hours - fixed_cost, y)

    plt.figure(figsize=(8, 5))
    plt.plot(leisure, c_no_tax, label="No tax")
    plt.plot(leisure, c_tax, label="Proportional tax")
    plt.plot(leisure, c_fixed, label="Tax + fixed work cost")
    plt.xlabel("Leisure share")
    plt.ylabel("Consumption")
    plt.title("Static labor-supply budget sets")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02-static-budget-sets.png", dpi=200)
    plt.close()


def eitc_schematic() -> None:
    earnings = np.linspace(0, 60, 600)
    base = 5.0
    phase_in_rate = 0.4
    phase_out_rate = 0.21
    p1, p2, p3 = 12.0, 28.0, 52.0

    credit = np.piecewise(
        earnings,
        [earnings <= p1, (earnings > p1) & (earnings <= p2), earnings > p2],
        [lambda x: phase_in_rate * x,
         lambda x: phase_in_rate * p1,
         lambda x: np.maximum(phase_in_rate * p1 - phase_out_rate * (x - p2), 0)],
    )
    consumption = base + earnings + credit

    plt.figure(figsize=(8, 5))
    plt.plot(earnings, consumption)
    plt.axvline(p1, linestyle="--")
    plt.axvline(p2, linestyle="--")
    plt.text(p1 + 0.5, consumption.max() * 0.35, "Phase-in ends", rotation=90)
    plt.text(p2 + 0.5, consumption.max() * 0.35, "Phase-out begins", rotation=90)
    plt.xlabel("Pre-tax earnings")
    plt.ylabel("Consumption resources")
    plt.title("Stylized piecewise-linear tax-transfer schedule")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02-eitc-schematic.png", dpi=200)
    plt.close()


def main() -> None:
    budget_set_figure()
    eitc_schematic()
    print(f"Saved figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
