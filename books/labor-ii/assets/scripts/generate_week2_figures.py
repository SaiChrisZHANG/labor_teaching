#!/usr/bin/env python3
"""Generate the required Week 2 figures for Labor II."""
from __future__ import annotations

import os
from pathlib import Path
import sys
from tempfile import gettempdir

os.environ.setdefault("MPLCONFIGDIR", str(Path(gettempdir()) / "codex-mplconfig"))

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, apply_style, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_target_vs_actual() -> None:
    horizon = np.arange(0, 7)
    target = np.array([100, 112, 112, 112, 112, 112, 112], dtype=float)
    actual = np.array([100, 103, 106, 108, 109.5, 110.5, 111.2], dtype=float)

    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    ax.plot(horizon, target, linewidth=2.4, color=COLORS["navy"], label="Target employment")
    ax.plot(horizon, actual, linewidth=2.4, color=COLORS["rust"], label="Actual employment")
    ax.fill_between(horizon, actual, target, alpha=0.16, color=COLORS["navy"])
    ax.set_xlabel("Periods after shock")
    ax.set_ylabel("Employment index")
    ax.set_title("Target versus actual employment after a labor-demand shock")
    ax.legend(loc="lower right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "02-target-vs-actual-employment.png")
    plt.close(fig)


def make_convex_vs_nonconvex() -> None:
    horizon = np.arange(0, 7)
    target = np.full_like(horizon, 112, dtype=float)
    target[0] = 100
    convex = np.array([100, 103, 106, 108, 109.5, 110.5, 111.2], dtype=float)
    nonconvex = np.array([100, 100, 100, 109, 111.5, 112, 112], dtype=float)

    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    ax.plot(horizon, target, color=COLORS["muted"], linewidth=1.8, linestyle="--", label="Target")
    ax.plot(horizon, convex, linewidth=2.4, color=COLORS["navy"], label="Convex cost: partial adjustment")
    ax.plot(horizon, nonconvex, linewidth=2.4, color=COLORS["rust"], label="Fixed/nonconvex cost: inaction then jump")
    ax.set_xlabel("Periods after shock")
    ax.set_ylabel("Employment index")
    ax.set_title("Convex versus nonconvex adjustment")
    ax.legend(loc="lower right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "02-convex-vs-nonconvex-adjustment.png")
    plt.close(fig)


def make_hours_vs_headcount() -> None:
    horizon = np.arange(0, 7)
    target = np.array([100, 111, 111, 111, 111, 111, 111], dtype=float)
    hours = np.array([100, 108, 109.5, 110.2, 110.6, 110.8, 111], dtype=float)
    headcount = np.array([100, 101.5, 103, 105, 107, 108.5, 109.5], dtype=float)

    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    ax.plot(horizon, target, color=COLORS["muted"], linewidth=1.8, linestyle="--", label="Target labor services")
    ax.plot(horizon, hours, linewidth=2.4, color=COLORS["navy"], label="Hours / intensive margin")
    ax.plot(horizon, headcount, linewidth=2.4, color=COLORS["rust"], label="Headcount / extensive margin")
    ax.set_xlabel("Periods after shock")
    ax.set_ylabel("Index")
    ax.set_title("Hours tend to move before headcount")
    ax.legend(loc="lower right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "02-hours-vs-headcount-adjustment.png")
    plt.close(fig)


def make_policy_incidence() -> None:
    horizon = np.arange(0, 7)
    short_run = np.array([0.0, -0.3, -0.8, -1.2, -1.5, -1.7, -1.8])
    medium_run = np.array([0.0, -0.6, -1.4, -2.2, -2.9, -3.3, -3.5])
    long_run = np.array([0.0, -0.8, -1.8, -3.0, -4.0, -4.7, -5.0])

    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    ax.plot(horizon, short_run, linewidth=2.3, color=COLORS["navy"], label="Fast hours response only")
    ax.plot(horizon, medium_run, linewidth=2.3, color=COLORS["teal"], label="Hours plus gradual headcount")
    ax.plot(horizon, long_run, linewidth=2.3, color=COLORS["rust"], label="Long-run employment effect")
    ax.axhline(0.0, color=COLORS["muted"], linewidth=0.9)
    ax.set_xlabel("Periods after payroll-tax shock")
    ax.set_ylabel("Employment response (percent)")
    ax.set_title("Policy incidence is an adjustment path, not one number")
    ax.legend(loc="lower left")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "02-policy-incidence-over-time.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    make_target_vs_actual()
    make_convex_vs_nonconvex()
    make_hours_vs_headcount()
    make_policy_incidence()
    print(f"Saved Week 2 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
