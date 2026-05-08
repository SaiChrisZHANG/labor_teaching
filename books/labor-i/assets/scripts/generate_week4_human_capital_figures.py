#!/usr/bin/env python3
"""Generate conceptual Week 4 figures for Labor I."""
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

from shared.figure_style import COLORS, SEQUENTIAL_CMAP, apply_style, save_figure, style_axis


FIG_DIR = Path(__file__).resolve().parents[1] / "figures"


def lifecycle_human_capital_earnings() -> None:
    age = np.linspace(16, 65, 300)
    human_capital = 0.42 + 0.62 * (1 - np.exp(-(age - 16) / 12)) - 0.0022 * np.maximum(age - 48, 0) ** 1.4
    human_capital = np.clip(human_capital, 0.25, None)
    earnings = 0.28 + 0.018 * (age - 16) + 0.48 * (1 - np.exp(-(age - 16) / 18)) - 0.0042 * np.maximum(age - 52, 0) ** 1.25
    earnings = np.clip(earnings, 0.18, None)

    fig, ax = plt.subplots(figsize=(9.4, 5.5))
    ax.plot(age, human_capital, linewidth=2.8, color=COLORS["navy"], label="Latent human capital")
    ax.plot(age, earnings, linewidth=2.8, color=COLORS["rust"], label="Observed earnings / wages")
    ax.axvspan(16, 24, color=COLORS["navy"], alpha=0.12)
    ax.axvspan(24, 35, color=COLORS["gold"], alpha=0.15)
    ax.text(18, 1.11, "Schooling-intensive phase", fontsize=9.5, color=COLORS["navy"])
    ax.text(26, 1.11, "Training and career build-up", fontsize=9.5, color=COLORS["rust"])
    ax.set_xlabel("Age")
    ax.set_ylabel("Relative level")
    ax.set_title("Conceptual lifecycle profiles of human capital and earnings")
    ax.set_ylim(0.15, 1.18)
    ax.set_xlim(16, 65)
    ax.legend(loc="lower right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-lifecycle-human-capital-earnings.png")
    plt.close(fig)


def investment_intensity() -> None:
    age = np.linspace(16, 65, 300)
    schooling = 0.95 * np.exp(-((age - 20) / 4.8) ** 2)
    employer_training = 0.6 * np.exp(-((age - 29) / 8.0) ** 2)
    learning_by_doing = 0.18 + 0.22 * np.exp(-((age - 35) / 18.0) ** 2)

    fig, ax = plt.subplots(figsize=(9.4, 5.5))
    ax.plot(age, schooling, linewidth=2.8, color=COLORS["navy"], label="Formal schooling")
    ax.plot(age, employer_training, linewidth=2.8, color=COLORS["rust"], label="Employer training")
    ax.plot(age, learning_by_doing, linewidth=2.8, color=COLORS["teal"], label="Learning-by-doing")
    ax.axvline(22, linestyle="--", color=COLORS["muted"], linewidth=1.0)
    ax.axvline(35, linestyle="--", color=COLORS["muted"], linewidth=1.0)
    ax.text(16.7, 1.02, "Schooling intensive", fontsize=9.5, color=COLORS["muted"])
    ax.text(23.2, 1.02, "Early-career training", fontsize=9.5, color=COLORS["muted"])
    ax.text(40.0, 1.02, "Later-career low investment", fontsize=9.5, color=COLORS["muted"])
    ax.set_xlabel("Age")
    ax.set_ylabel("Investment intensity")
    ax.set_title("Human-capital investment intensity over the lifecycle")
    ax.set_ylim(0, 1.08)
    ax.set_xlim(16, 65)
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-investment-intensity-lifecycle.png")
    plt.close(fig)


def dynamic_complementarity() -> None:
    baseline = np.linspace(0.1, 1.0, 160)
    later_investment = np.linspace(0.1, 1.0, 160)
    b_grid, i_grid = np.meshgrid(baseline, later_investment)
    next_skill = 0.55 + 0.55 * b_grid + 0.35 * i_grid + 0.65 * b_grid * i_grid

    fig, ax = plt.subplots(figsize=(8.4, 6.0))
    contour = ax.contourf(b_grid, i_grid, next_skill, levels=16, cmap=SEQUENTIAL_CMAP)
    ax.contour(b_grid, i_grid, next_skill, levels=8, colors="white", linewidths=0.7, alpha=0.8)
    cbar = fig.colorbar(contour, ax=ax, shrink=0.9)
    cbar.set_label("Next-period skill")
    ax.set_xlabel("Baseline skill")
    ax.set_ylabel("Later investment")
    ax.set_title("Dynamic complementarity in skill formation")
    style_axis(ax, grid_axis="none")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "04-dynamic-complementarity.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    lifecycle_human_capital_earnings()
    investment_intensity()
    dynamic_complementarity()
    print(f"Wrote Week 4 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
