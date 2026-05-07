#!/usr/bin/env python3
"""
Generate the required Week 1 figures for Labor II.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_isoquant_isocost() -> None:
    l_grid = np.linspace(1.0, 14.0, 400)
    alpha = 0.6
    qbar = 8.0
    k_isoquant = (qbar / (l_grid ** alpha)) ** (1 / (1 - alpha))

    w = 1.0
    r = 1.5
    l_star = alpha * qbar * (r / w) ** (1 - alpha)
    k_star = (1 - alpha) * qbar * (w / r) ** alpha
    total_cost = w * l_star + r * k_star
    k_isocost = (total_cost - w * l_grid) / r

    plt.figure(figsize=(7.2, 5.4))
    plt.plot(l_grid, k_isoquant, label="Isoquant: fixed output", linewidth=2.2)
    plt.plot(l_grid, k_isocost, label="Isocost", linewidth=2.2)
    plt.scatter([l_star], [k_star], color="black", zorder=4)
    plt.annotate("Optimum", (l_star, k_star), textcoords="offset points", xytext=(6, 8))
    plt.xlim(0.5, 14)
    plt.ylim(0.5, 16)
    plt.xlabel("Labor")
    plt.ylabel("Capital")
    plt.title("Week 1 cost minimization geometry")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "01-static-labor-demand-isoquant-isocost.png", dpi=220)
    plt.close()


def make_conditional_total_demand() -> None:
    wage = np.linspace(0.8, 2.0, 300)
    conditional = 145 * wage ** (-0.45)
    total = 155 * wage ** (-0.9)

    plt.figure(figsize=(7.2, 5.4))
    plt.plot(wage, conditional, linewidth=2.3, label="Conditional labor demand")
    plt.plot(wage, total, linewidth=2.3, label="Total labor demand")
    plt.xlabel("Labor cost")
    plt.ylabel("Labor input")
    plt.title("Conditional versus total labor demand")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "01-conditional-vs-unconditional-demand.png", dpi=220)
    plt.close()


def make_hicks_marshall() -> None:
    labels = [
        "Low substitution",
        "Higher substitution",
        "More elastic\nproduct demand",
        "Higher labor share",
        "Flexible other\ninputs",
    ]
    values = np.array([0.35, 0.62, 0.88, 1.02, 1.14])

    plt.figure(figsize=(8.0, 5.0))
    bars = plt.bar(labels, values, color=["#91b5d8", "#5d8cc1", "#f2b880", "#d97a56", "#7f9c66"])
    plt.ylabel("Absolute own-wage elasticity")
    plt.title("Hicks--Marshall laws as a schematic map")
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 0.02, f"{value:.2f}", ha="center")
    plt.ylim(0, 1.28)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "01-hicks-marshall-laws.png", dpi=220)
    plt.close()


def make_payroll_tax_incidence() -> None:
    labor = np.linspace(50, 150, 300)
    demand_pre = 210 - 0.9 * labor
    supply = 35 + 0.45 * labor
    tax = 14
    demand_post = demand_pre - tax

    eq_pre = (210 - 35) / (0.9 + 0.45)
    wage_pre = 35 + 0.45 * eq_pre
    eq_post = (210 - tax - 35) / (0.9 + 0.45)
    wage_post = 35 + 0.45 * eq_post
    employer_cost_post = wage_post + tax

    plt.figure(figsize=(7.4, 5.4))
    plt.plot(labor, demand_pre, linewidth=2.1, label="Labor demand (pre-tax)")
    plt.plot(labor, demand_post, linewidth=2.1, label="Labor demand (post-tax)")
    plt.plot(labor, supply, linewidth=2.1, label="Labor supply / wage-setting curve")
    plt.scatter([eq_pre, eq_post], [wage_pre, wage_post], color="black", zorder=4)
    plt.vlines(eq_post, wage_post, employer_cost_post, colors="black", linestyles="--")
    plt.annotate("Tax wedge", (eq_post + 2, 0.5 * (wage_post + employer_cost_post)))
    plt.xlabel("Employment")
    plt.ylabel("Wage or labor cost")
    plt.title("Static payroll-tax incidence")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "01-payroll-tax-incidence.png", dpi=220)
    plt.close()


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    make_isoquant_isocost()
    make_conditional_total_demand()
    make_hicks_marshall()
    make_payroll_tax_incidence()
    print(f"Saved Week 1 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
