#!/usr/bin/env python3
"""Generate conceptual Week 5 figures for Labor I."""
from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np


FIG_DIR = Path(__file__).resolve().parents[1] / "figures"


def mincer_profiles() -> None:
    experience = np.linspace(0, 40, 300)
    groups = [
        ("High school", 2.12, 0.028, "#6c8ebf"),
        ("Some college", 2.28, 0.033, "#d79b00"),
        ("College", 2.48, 0.039, "#82b366"),
    ]

    plt.figure(figsize=(9.6, 5.6))
    for label, intercept, slope, color in groups:
        profile = intercept + slope * experience - 0.00055 * experience**2
        plt.plot(experience, profile, linewidth=3, color=color, label=label)

    plt.axvspan(0, 8, color="#eef3f8", alpha=0.8)
    plt.text(1.2, 3.27, "Early-career slope differences", fontsize=10, color="#355070")
    plt.text(23.0, 3.12, "Concavity from lifecycle experience returns", fontsize=10, color="#4a4a4a")
    plt.xlabel("Potential experience")
    plt.ylabel("Log wage")
    plt.title("Stylized Mincer wage profiles by schooling group")
    plt.xlim(0, 40)
    plt.ylim(2.0, 3.34)
    plt.legend(frameon=False, loc="lower right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "05-mincer-wage-profiles.png", dpi=220)
    plt.close()


def ols_iv_objects() -> None:
    quantile = np.linspace(0.05, 0.95, 200)
    causal_gain = 0.055 + 0.07 * quantile
    ols_level = np.full_like(quantile, 0.094)
    iv_level = np.full_like(quantile, 0.073)
    marginal_policy = 0.062 + 0.024 * np.exp(-((quantile - 0.42) / 0.18) ** 2)

    plt.figure(figsize=(9.8, 5.8))
    plt.plot(quantile, causal_gain, linewidth=3, color="#1f5c99", label="Heterogeneous causal return schedule")
    plt.plot(quantile, ols_level, linewidth=2.4, linestyle="--", color="#c25b2a", label="Descriptive OLS premium")
    plt.plot(quantile, iv_level, linewidth=2.4, linestyle="-.", color="#7b5ea7", label="IV / LATE for compliers")
    plt.plot(quantile, marginal_policy, linewidth=2.4, color="#4f7f39", label="Policy-induced marginal return")
    plt.axvspan(0.28, 0.55, color="#e8ddf3", alpha=0.45)
    plt.text(0.31, 0.109, "Complier margin", fontsize=10, color="#5d3c85")
    plt.xlabel("Latent schooling margin / complier ranking")
    plt.ylabel("Return to schooling")
    plt.title("OLS, IV, and policy returns are different empirical objects")
    plt.xlim(0.05, 0.95)
    plt.ylim(0.045, 0.122)
    plt.legend(frameon=False, loc="upper left")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "05-ols-iv-late-objects.png", dpi=220)
    plt.close()


def worker_firm_sorting() -> None:
    rng = np.random.default_rng(202605)
    worker_skill = np.linspace(-1.2, 1.2, 130)
    firm_premium = 0.18 + 0.34 * worker_skill + 0.08 * np.sin(worker_skill * 3.2) + rng.normal(0.0, 0.08, size=worker_skill.size)

    plt.figure(figsize=(8.8, 5.9))
    plt.scatter(worker_skill, firm_premium, s=34, alpha=0.72, color="#1f5c99", edgecolors="none")
    slope, intercept = np.polyfit(worker_skill, firm_premium, deg=1)
    fit = intercept + slope * worker_skill
    plt.plot(worker_skill, fit, linewidth=3, color="#c25b2a")
    plt.axvline(0.0, linestyle="--", color="#8c8c8c", linewidth=1)
    plt.axhline(0.18, linestyle="--", color="#8c8c8c", linewidth=1)
    plt.text(-1.14, 0.58, "Higher-skill workers sort toward higher-premium firms", fontsize=10, color="#374151")
    plt.xlabel("Worker skill or schooling index")
    plt.ylabel("Firm wage premium")
    plt.title("Worker-firm sorting schematic")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "05-worker-firm-sorting-schematic.png", dpi=220)
    plt.close()


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    mincer_profiles()
    ols_iv_objects()
    worker_firm_sorting()
    print(f"Wrote Week 5 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
