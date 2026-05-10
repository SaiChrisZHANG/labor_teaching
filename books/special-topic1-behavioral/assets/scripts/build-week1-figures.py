from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUT = Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(parents=True, exist_ok=True)

COLORS = {
    "pref": "#4C78A8",
    "belief": "#59A14F",
    "decision": "#F28E2B",
    "response": "#B07AA1",
    "neutral": "#F6F7F9",
    "line": "#2F3A45",
}


def box(ax, xy, text, color="neutral", width=0.22, height=0.12, fs=10):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.025",
        facecolor=COLORS[color],
        edgecolor=COLORS["line"],
        linewidth=1.0,
    )
    ax.add_patch(patch)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha="center", va="center", fontsize=fs)
    return patch


def arrow(ax, start, end, color="line", rad=0.0):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.1,
            color=COLORS[color],
        )
    )


def finish(fig, ax, name):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.savefig(OUT / name, dpi=220, bbox_inches="tight")
    plt.close(fig)


def taxonomy_domains():
    fig, ax = plt.subplots(figsize=(10, 5.6))
    left = [
        ("Nonstandard\npreferences", "pref"),
        ("Nonstandard\nbeliefs", "belief"),
        ("Decision-making,\nattention,\ncomplexity", "decision"),
        ("Firm, market,\npolicy responses", "response"),
    ]
    right = [
        "Labor supply\nand effort",
        "Job search",
        "Training and\nhuman capital",
        "Workplace\ncontracts",
        "Households\nand identity",
        "Policy take-up\nand design",
    ]
    ys_left = [0.76, 0.56, 0.36, 0.16]
    ys_right = [0.82, 0.68, 0.54, 0.40, 0.26, 0.12]
    for (label, color), y in zip(left, ys_left):
        box(ax, (0.05, y), label, color=color, width=0.26, height=0.10)
    for label, y in zip(right, ys_right):
        box(ax, (0.70, y), label, width=0.24, height=0.09, fs=9.5)
    links = {
        0: [0, 2, 3, 4],
        1: [1, 2, 5],
        2: [1, 2, 5],
        3: [3, 5, 0],
    }
    for i, js in links.items():
        for j in js:
            arrow(ax, (0.31, ys_left[i] + 0.05), (0.70, ys_right[j] + 0.045), rad=0.03 * (j - 2))
    ax.text(0.18, 0.94, "Behavioral wedge", ha="center", fontsize=11, weight="bold")
    ax.text(0.82, 0.94, "Labor domain", ha="center", fontsize=11, weight="bold")
    finish(fig, ax, "01-taxonomy-to-labor-domains.png")


def benchmark_wedge():
    fig, ax = plt.subplots(figsize=(10, 5.2))
    box(ax, (0.05, 0.48), "Benchmark\nlabor choice", width=0.22, height=0.16)
    box(ax, (0.40, 0.48), "Observed\nlabor action", width=0.22, height=0.16)
    box(ax, (0.73, 0.48), "Outcome:\nearnings, search,\neffort, take-up", width=0.22, height=0.16, fs=9.5)
    arrow(ax, (0.27, 0.56), (0.40, 0.56))
    arrow(ax, (0.62, 0.56), (0.73, 0.56))
    wedges = [
        ("Preferences", "pref", 0.78),
        ("Beliefs", "belief", 0.30),
        ("Attention /\nchoice set", "decision", 0.10),
        ("Firm / policy\nenvironment", "response", 0.78),
    ]
    for label, color, y in wedges[:3]:
        box(ax, (0.37, y), label, color=color, width=0.28, height=0.11)
        arrow(ax, (0.51, y + 0.055), (0.51, 0.64 if y > 0.5 else 0.48))
    box(ax, (0.69, wedges[3][2]), wedges[3][0], color=wedges[3][1], width=0.28, height=0.11)
    arrow(ax, (0.83, 0.78), (0.83, 0.64))
    ax.text(0.16, 0.28, "Standard parameters\nand budget set", ha="center", fontsize=9)
    ax.text(0.51, 0.28, "Behavioral representation\nchanges perceived problem", ha="center", fontsize=9)
    finish(fig, ax, "01-benchmark-vs-behavioral-wedge.png")


def methods_identification():
    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    rows = [
        ("Field experiment", "Treatment effect\non a margin", "effort, exercise,\nsearch intensity"),
        ("Information /\nsalience", "Beliefs or attention", "search, training,\ntake-up"),
        ("Administrative\nnudge", "Implementation\nand exposure", "benefits,\napplications"),
        ("Measured beliefs /\npreferences", "Behavioral object", "expectations,\nidentity, patience"),
        ("Structural\nestimation", "Deep parameter\nand counterfactual", "dynamic choice,\nwelfare"),
    ]
    y0 = 0.80
    for k, (design, obj, margin) in enumerate(rows):
        y = y0 - 0.16 * k
        box(ax, (0.05, y), design, width=0.24, height=0.10, fs=9.2)
        box(ax, (0.39, y), obj, width=0.24, height=0.10, fs=9.2)
        box(ax, (0.72, y), margin, width=0.24, height=0.10, fs=9.2)
        arrow(ax, (0.29, y + 0.05), (0.39, y + 0.05))
        arrow(ax, (0.63, y + 0.05), (0.72, y + 0.05))
    ax.text(0.17, 0.95, "Design", ha="center", fontsize=11, weight="bold")
    ax.text(0.51, 0.95, "Identified object", ha="center", fontsize=11, weight="bold")
    ax.text(0.84, 0.95, "Labor margin", ha="center", fontsize=11, weight="bold")
    finish(fig, ax, "01-methods-identification-map.png")


def welfare_equilibrium():
    fig, ax = plt.subplots(figsize=(10, 5.4))
    box(ax, (0.06, 0.55), "Behavioral\nwedge", color="decision", width=0.20, height=0.13)
    box(ax, (0.31, 0.55), "Worker\nchoice", color="neutral", width=0.20, height=0.13)
    box(ax, (0.56, 0.70), "Firm / market\nresponse", color="response", width=0.22, height=0.12)
    box(ax, (0.56, 0.38), "Policy\ndesign", color="belief", width=0.22, height=0.12)
    box(ax, (0.82, 0.55), "Observed\noutcome", width=0.16, height=0.13)
    arrow(ax, (0.26, 0.615), (0.31, 0.615))
    arrow(ax, (0.51, 0.615), (0.56, 0.76))
    arrow(ax, (0.51, 0.615), (0.56, 0.44))
    arrow(ax, (0.78, 0.76), (0.82, 0.64))
    arrow(ax, (0.78, 0.44), (0.82, 0.58))
    box(ax, (0.35, 0.13), "Welfare claim needs a\nnormative benchmark,\ninternality measure,\nand equilibrium account", width=0.36, height=0.16, fs=9.3)
    arrow(ax, (0.90, 0.55), (0.66, 0.29), rad=-0.18)
    finish(fig, ax, "01-welfare-equilibrium-caution.png")


if __name__ == "__main__":
    taxonomy_domains()
    benchmark_wedge()
    methods_identification()
    welfare_equilibrium()
