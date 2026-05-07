#!/usr/bin/env python3
"""
Generate the required Week 2 figures for Labor II.
"""
from __future__ import annotations

import os
from pathlib import Path
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_target_vs_actual() -> None:
    horizon = np.arange(0, 7)
    target = np.array([100, 112, 112, 112, 112, 112, 112], dtype=float)
    actual = np.array([100, 103, 106, 108, 109.5, 110.5, 111.2], dtype=float)

    plt.figure(figsize=(7.4, 5.2))
    plt.plot(horizon, target, linewidth=2.4, label="Target employment")
    plt.plot(horizon, actual, linewidth=2.4, label="Actual employment")
    plt.fill_between(horizon, actual, target, alpha=0.16, color="#7aa6c2")
    plt.xlabel("Periods after shock")
    plt.ylabel("Employment index")
    plt.title("Target versus actual employment after a labor-demand shock")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02-target-vs-actual-employment.png", dpi=220)
    plt.close()


def make_convex_vs_nonconvex() -> None:
    horizon = np.arange(0, 7)
    target = np.full_like(horizon, 112, dtype=float)
    target[0] = 100
    convex = np.array([100, 103, 106, 108, 109.5, 110.5, 111.2], dtype=float)
    nonconvex = np.array([100, 100, 100, 109, 111.5, 112, 112], dtype=float)

    plt.figure(figsize=(7.4, 5.2))
    plt.plot(horizon, target, color="black", linewidth=1.8, linestyle="--", label="Target")
    plt.plot(horizon, convex, linewidth=2.4, label="Convex cost: partial adjustment")
    plt.plot(horizon, nonconvex, linewidth=2.4, label="Fixed/nonconvex cost: inaction then jump")
    plt.xlabel("Periods after shock")
    plt.ylabel("Employment index")
    plt.title("Convex versus nonconvex adjustment")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02-convex-vs-nonconvex-adjustment.png", dpi=220)
    plt.close()


def make_hours_vs_headcount() -> None:
    horizon = np.arange(0, 7)
    target = np.array([100, 111, 111, 111, 111, 111, 111], dtype=float)
    hours = np.array([100, 108, 109.5, 110.2, 110.6, 110.8, 111], dtype=float)
    headcount = np.array([100, 101.5, 103, 105, 107, 108.5, 109.5], dtype=float)

    plt.figure(figsize=(7.4, 5.2))
    plt.plot(horizon, target, color="black", linewidth=1.8, linestyle="--", label="Target labor services")
    plt.plot(horizon, hours, linewidth=2.4, label="Hours / intensive margin")
    plt.plot(horizon, headcount, linewidth=2.4, label="Headcount / extensive margin")
    plt.xlabel("Periods after shock")
    plt.ylabel("Index")
    plt.title("Hours tend to move before headcount")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02-hours-vs-headcount-adjustment.png", dpi=220)
    plt.close()


def make_policy_incidence() -> None:
    horizon = np.arange(0, 7)
    short_run = np.array([0.0, -0.3, -0.8, -1.2, -1.5, -1.7, -1.8])
    medium_run = np.array([0.0, -0.6, -1.4, -2.2, -2.9, -3.3, -3.5])
    long_run = np.array([0.0, -0.8, -1.8, -3.0, -4.0, -4.7, -5.0])

    plt.figure(figsize=(7.4, 5.2))
    plt.plot(horizon, short_run, linewidth=2.3, label="Fast hours response only")
    plt.plot(horizon, medium_run, linewidth=2.3, label="Hours plus gradual headcount")
    plt.plot(horizon, long_run, linewidth=2.3, label="Long-run employment effect")
    plt.axhline(0.0, color="gray", linewidth=0.8)
    plt.xlabel("Periods after payroll-tax shock")
    plt.ylabel("Employment response (percent)")
    plt.title("Policy incidence is an adjustment path, not one number")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02-policy-incidence-over-time.png", dpi=220)
    plt.close()


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    make_target_vs_actual()
    make_convex_vs_nonconvex()
    make_hours_vs_headcount()
    make_policy_incidence()
    print(f"Saved Week 2 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
