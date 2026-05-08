#!/usr/bin/env python3
"""Generate conceptual Week 5 figures for Labor I."""
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


def mincer_profiles() -> None:
    experience = np.linspace(0, 40, 300)
    groups = [
        ("High school", 2.12, 0.028, COLORS["slate"]),
        ("Some college", 2.28, 0.033, COLORS["gold"]),
        ("College", 2.48, 0.039, COLORS["teal"]),
    ]

    fig, ax = plt.subplots(figsize=(9.4, 5.5))
    for label, intercept, slope, color in groups:
        profile = intercept + slope * experience - 0.00055 * experience**2
        ax.plot(experience, profile, linewidth=2.8, color=color, label=label)

    ax.axvspan(0, 8, color=COLORS["navy"], alpha=0.10)
    ax.text(1.2, 3.26, "Early-career slope differences", fontsize=9.5, color=COLORS["navy"])
    ax.text(22.8, 3.11, "Concavity from lifecycle experience returns", fontsize=9.5, color=COLORS["muted"])
    ax.set_xlabel("Potential experience")
    ax.set_ylabel("Log wage")
    ax.set_title("Stylized Mincer wage profiles by schooling group")
    ax.set_xlim(0, 40)
    ax.set_ylim(2.0, 3.34)
    ax.legend(loc="lower right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-mincer-wage-profiles.png")
    plt.close(fig)


def ols_iv_objects() -> None:
    quantile = np.linspace(0.05, 0.95, 200)
    causal_gain = 0.055 + 0.07 * quantile
    ols_level = np.full_like(quantile, 0.094)
    iv_level = np.full_like(quantile, 0.073)
    marginal_policy = 0.062 + 0.024 * np.exp(-((quantile - 0.42) / 0.18) ** 2)

    fig, ax = plt.subplots(figsize=(9.6, 5.6))
    ax.plot(quantile, causal_gain, linewidth=2.8, color=COLORS["navy"], label="Heterogeneous causal return schedule")
    ax.plot(quantile, ols_level, linewidth=2.2, linestyle="--", color=COLORS["rust"], label="Descriptive OLS premium")
    ax.plot(quantile, iv_level, linewidth=2.2, linestyle="-.", color=COLORS["slate"], label="IV / LATE for compliers")
    ax.plot(quantile, marginal_policy, linewidth=2.2, color=COLORS["teal"], label="Policy-induced marginal return")
    ax.axvspan(0.28, 0.55, color=COLORS["gold"], alpha=0.14)
    ax.text(0.31, 0.109, "Complier margin", fontsize=9.5, color=COLORS["muted"])
    ax.set_xlabel("Latent schooling margin / complier ranking")
    ax.set_ylabel("Return to schooling")
    ax.set_title("OLS, IV, and policy returns are different empirical objects")
    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.045, 0.122)
    ax.legend(loc="upper left")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-ols-iv-late-objects.png")
    plt.close(fig)


def worker_firm_sorting() -> None:
    rng = np.random.default_rng(202605)
    worker_skill = np.linspace(-1.2, 1.2, 130)
    firm_premium = 0.18 + 0.34 * worker_skill + 0.08 * np.sin(worker_skill * 3.2) + rng.normal(0.0, 0.08, size=worker_skill.size)

    fig, ax = plt.subplots(figsize=(8.6, 5.8))
    ax.scatter(worker_skill, firm_premium, s=28, alpha=0.7, color=COLORS["navy"], edgecolors="none")
    slope, intercept = np.polyfit(worker_skill, firm_premium, deg=1)
    fit = intercept + slope * worker_skill
    ax.plot(worker_skill, fit, linewidth=2.8, color=COLORS["rust"])
    ax.axvline(0.0, linestyle="--", color=COLORS["muted"], linewidth=1.0)
    ax.axhline(0.18, linestyle="--", color=COLORS["muted"], linewidth=1.0)
    ax.text(-1.14, 0.58, "Higher-skill workers sort toward higher-premium firms", fontsize=9.5, color=COLORS["muted"])
    ax.set_xlabel("Worker skill or schooling index")
    ax.set_ylabel("Firm wage premium")
    ax.set_title("Worker-firm sorting schematic")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "05-worker-firm-sorting-schematic.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    mincer_profiles()
    ols_iv_objects()
    worker_firm_sorting()
    print(f"Wrote Week 5 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
