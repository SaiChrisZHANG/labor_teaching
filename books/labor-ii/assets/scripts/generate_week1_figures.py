#!/usr/bin/env python3
"""Generate the required Week 1 figures for Labor II."""
from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, apply_style, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_isoquant_isocost() -> None:
    labor_grid = np.linspace(1.0, 14.0, 400)
    alpha = 0.6
    output = 8.0
    isoquant = (output / (labor_grid**alpha)) ** (1 / (1 - alpha))

    wage = 1.0
    rental_rate = 1.5
    labor_star = alpha * output * (rental_rate / wage) ** (1 - alpha)
    capital_star = (1 - alpha) * output * (wage / rental_rate) ** alpha
    total_cost = wage * labor_star + rental_rate * capital_star
    isocost = (total_cost - wage * labor_grid) / rental_rate

    fig, ax = plt.subplots(figsize=(7.3, 5.4))
    ax.plot(labor_grid, isoquant, color=COLORS["navy"], linewidth=2.5, label="Isoquant: fixed output")
    ax.plot(labor_grid, isocost, color=COLORS["rust"], linewidth=2.5, label="Isocost")
    ax.scatter([labor_star], [capital_star], color=COLORS["ink"], s=24, zorder=4)
    ax.annotate("Optimum", (labor_star, capital_star), textcoords="offset points", xytext=(6, 8), fontsize=9, color=COLORS["muted"])
    ax.set_xlim(0.5, 14)
    ax.set_ylim(0.5, 16)
    ax.set_xlabel("Labor")
    ax.set_ylabel("Capital")
    ax.set_title("Week 1 cost-minimization geometry")
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "01-static-labor-demand-isoquant-isocost.png")
    plt.close(fig)


def make_conditional_total_demand() -> None:
    wage = np.linspace(0.8, 2.0, 300)
    conditional = 145 * wage ** (-0.45)
    total = 155 * wage ** (-0.9)

    fig, ax = plt.subplots(figsize=(7.3, 5.4))
    ax.plot(wage, conditional, linewidth=2.5, color=COLORS["navy"], label="Conditional labor demand")
    ax.plot(wage, total, linewidth=2.5, color=COLORS["rust"], label="Total labor demand")
    ax.set_xlabel("Labor cost")
    ax.set_ylabel("Labor input")
    ax.set_title("Conditional versus total labor demand")
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "01-conditional-vs-unconditional-demand.png")
    plt.close(fig)


def make_hicks_marshall() -> None:
    labels = ["Low substitution", "Higher substitution", "More elastic\nproduct demand", "Higher labor share", "Flexible other\ninputs"]
    values = np.array([0.35, 0.62, 0.88, 1.02, 1.14])
    colors = ["#B5C7D9", "#87A8C8", "#D7B07A", "#C98362", "#7C9582"]

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    bars = ax.bar(labels, values, color=colors)
    ax.set_ylabel("Absolute own-wage elasticity")
    ax.set_title("Hicks-Marshall laws as a schematic map")
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.02, f"{value:.2f}", ha="center", fontsize=9, color=COLORS["muted"])
    ax.set_ylim(0, 1.28)
    style_axis(ax, grid_axis="y")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "01-hicks-marshall-laws.png")
    plt.close(fig)


def make_payroll_tax_incidence() -> None:
    labor = np.linspace(50, 150, 300)
    demand_pre = 210 - 0.9 * labor
    supply = 35 + 0.45 * labor
    tax = 14
    demand_post = demand_pre - tax

    employment_pre = (210 - 35) / (0.9 + 0.45)
    wage_pre = 35 + 0.45 * employment_pre
    employment_post = (210 - tax - 35) / (0.9 + 0.45)
    wage_post = 35 + 0.45 * employment_post
    employer_cost_post = wage_post + tax

    fig, ax = plt.subplots(figsize=(7.5, 5.4))
    ax.plot(labor, demand_pre, linewidth=2.2, color=COLORS["navy"], label="Labor demand (pre-tax)")
    ax.plot(labor, demand_post, linewidth=2.2, color=COLORS["rust"], label="Labor demand (post-tax)")
    ax.plot(labor, supply, linewidth=2.2, color=COLORS["teal"], label="Labor supply / wage-setting curve")
    ax.scatter([employment_pre, employment_post], [wage_pre, wage_post], color=COLORS["ink"], s=20, zorder=4)
    ax.vlines(employment_post, wage_post, employer_cost_post, colors=COLORS["muted"], linestyles="--", linewidth=1.1)
    ax.annotate("Tax wedge", (employment_post + 2, 0.5 * (wage_post + employer_cost_post)), fontsize=9, color=COLORS["muted"])
    ax.set_xlabel("Employment")
    ax.set_ylabel("Wage or labor cost")
    ax.set_title("Static payroll-tax incidence")
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "01-payroll-tax-incidence.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    make_isoquant_isocost()
    make_conditional_total_demand()
    make_hicks_marshall()
    make_payroll_tax_incidence()
    print(f"Saved Week 1 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
