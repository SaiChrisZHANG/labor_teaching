#!/usr/bin/env python3
"""Generate conceptual Week 4 figures for Labor I."""
from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np


FIG_DIR = Path(__file__).resolve().parents[1] / "figures"


def lifecycle_human_capital_earnings() -> None:
    age = np.linspace(16, 65, 300)
    human_capital = 0.42 + 0.62 * (1 - np.exp(-(age - 16) / 12)) - 0.0022 * np.maximum(age - 48, 0) ** 1.4
    human_capital = np.clip(human_capital, 0.25, None)
    earnings = 0.28 + 0.018 * (age - 16) + 0.48 * (1 - np.exp(-(age - 16) / 18)) - 0.0042 * np.maximum(age - 52, 0) ** 1.25
    earnings = np.clip(earnings, 0.18, None)

    plt.figure(figsize=(9.5, 5.5))
    plt.plot(age, human_capital, linewidth=3, color="#1f5c99", label="Latent human capital")
    plt.plot(age, earnings, linewidth=3, color="#c25b2a", label="Observed earnings / wages")
    plt.axvspan(16, 24, color="#cfdceb", alpha=0.4)
    plt.axvspan(24, 35, color="#f1dccf", alpha=0.35)
    plt.text(18, 1.12, "Schooling-intensive phase", fontsize=10, color="#1f5c99")
    plt.text(26, 1.12, "Training and career build-up", fontsize=10, color="#8f431f")
    plt.xlabel("Age")
    plt.ylabel("Relative level")
    plt.title("Conceptual lifecycle profiles of human capital and earnings")
    plt.legend(frameon=False, loc="lower right")
    plt.ylim(0.15, 1.18)
    plt.xlim(16, 65)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "04-lifecycle-human-capital-earnings.png", dpi=220)
    plt.close()


def investment_intensity() -> None:
    age = np.linspace(16, 65, 300)
    schooling = 0.95 * np.exp(-((age - 20) / 4.8) ** 2)
    employer_training = 0.6 * np.exp(-((age - 29) / 8.0) ** 2)
    learning_by_doing = 0.18 + 0.22 * np.exp(-((age - 35) / 18.0) ** 2)

    plt.figure(figsize=(9.5, 5.5))
    plt.plot(age, schooling, linewidth=3, color="#1f5c99", label="Formal schooling")
    plt.plot(age, employer_training, linewidth=3, color="#c25b2a", label="Employer training")
    plt.plot(age, learning_by_doing, linewidth=3, color="#4f7f39", label="Learning-by-doing")
    plt.axvline(22, linestyle="--", color="#666666", linewidth=1)
    plt.axvline(35, linestyle="--", color="#666666", linewidth=1)
    plt.text(16.7, 1.02, "Schooling intensive", fontsize=10)
    plt.text(23.2, 1.02, "Early-career training", fontsize=10)
    plt.text(40.0, 1.02, "Later-career low investment", fontsize=10)
    plt.xlabel("Age")
    plt.ylabel("Investment intensity")
    plt.title("Human-capital investment intensity over the lifecycle")
    plt.ylim(0, 1.08)
    plt.xlim(16, 65)
    plt.legend(frameon=False, loc="upper right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "04-investment-intensity-lifecycle.png", dpi=220)
    plt.close()


def dynamic_complementarity() -> None:
    baseline = np.linspace(0.1, 1.0, 160)
    later_investment = np.linspace(0.1, 1.0, 160)
    b_grid, i_grid = np.meshgrid(baseline, later_investment)
    next_skill = 0.55 + 0.55 * b_grid + 0.35 * i_grid + 0.65 * b_grid * i_grid

    plt.figure(figsize=(8.6, 6.2))
    contour = plt.contourf(b_grid, i_grid, next_skill, levels=16, cmap="YlGnBu")
    plt.colorbar(contour, label="Next-period skill")
    plt.contour(b_grid, i_grid, next_skill, levels=8, colors="white", linewidths=0.7, alpha=0.7)
    plt.xlabel("Baseline skill")
    plt.ylabel("Later investment")
    plt.title("Dynamic complementarity: later inputs pay more when baseline skill is higher")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "04-dynamic-complementarity.png", dpi=220)
    plt.close()


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    lifecycle_human_capital_earnings()
    investment_intensity()
    dynamic_complementarity()
    print(f"Wrote Week 4 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
