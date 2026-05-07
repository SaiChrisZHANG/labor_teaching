#!/usr/bin/env python3
"""Generate a bounded Week 13 research-design studio artifact."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ANCHORS = {
    "saezSchoeferSeim2019": {
        "label": "Saez, Schoefer, and Seim (2019)",
        "block": "Labor demand, incidence, and rent sharing",
        "mechanism": "Payroll-tax incidence interacts with labor demand, pass-through, and rent sharing inside firms.",
        "treatment_unit": "Firm-worker cost exposure through payroll-tax eligibility",
        "observation_unit": "Worker or firm-year, depending on implementation",
        "observed_margin": "Wages, employment, and incidence",
        "equilibrium_concern": "Pass-through, uncovered workers, and firm adjustment margins beyond the treated group",
        "extension_prompt": "Compare incidence under stronger versus weaker labor-market power or bargaining coverage.",
        "default_compare": "cengizDubeLindnerZipperer2019",
    },
    "yehMacalusoHershbein2022": {
        "label": "Yeh, Macaluso, and Hershbein (2022)",
        "block": "Monopsony and labor market power",
        "mechanism": "Labor supply to the firm creates markdowns between productivity and wages.",
        "treatment_unit": "Firm-occupation or labor-market power object rather than a policy treatment",
        "observation_unit": "Firm, worker-firm match, occupation, or local market",
        "observed_margin": "Markdowns, concentration proxies, mobility, and wages",
        "equilibrium_concern": "Concentration, mobility, and markdowns are related but not identical equilibrium objects",
        "extension_prompt": "Ask whether a policy or merger shock changes markdowns through mobility or bargaining channels.",
        "default_compare": "jagerNaiduSchoefer2024",
    },
    "cengizDubeLindnerZipperer2019": {
        "label": "Cengiz, Dube, Lindner, and Zipperer (2019)",
        "block": "Minimum wages and wage-setting policy",
        "mechanism": "A wage floor compresses the lower tail and shifts employment, composition, and spillovers.",
        "treatment_unit": "Jurisdiction-time minimum-wage change",
        "observation_unit": "State-border or wage-bin panel cells",
        "observed_margin": "Low-wage employment and wage distribution changes",
        "equilibrium_concern": "Hours, prices, turnover, compliance, and uncovered spillovers remain partly offstage",
        "extension_prompt": "Transfer the design to a new labor standard or ask whether effects differ by monopsony intensity.",
        "default_compare": "saezSchoeferSeim2019",
    },
    "jagerNaiduSchoefer2024": {
        "label": "Jager, Naidu, and Schoefer (2024)",
        "block": "Collective bargaining and institutions",
        "mechanism": "Collective bargaining changes wage-setting, compression, and worker voice through institutional coverage.",
        "treatment_unit": "Bargaining regime, contract coverage, or institutional reform",
        "observation_unit": "Worker, firm, sector, or country-industry panel",
        "observed_margin": "Wage structure, compression, and institutional coverage outcomes",
        "equilibrium_concern": "Coverage spillovers, coordination, and firm adjustment outside the directly organized sector",
        "extension_prompt": "Compare bargaining effects across legal regimes or link coverage to firm-side wage pass-through.",
        "default_compare": "yehMacalusoHershbein2022",
    },
    "acemogluRestrepo2020RobotsJobs": {
        "label": "Acemoglu and Restrepo (2020)",
        "block": "Technology shocks and local labor-market adjustment",
        "mechanism": "Robot adoption shifts task demand and local labor-market incidence through exposure differences.",
        "treatment_unit": "Shift-share robot exposure for local labor markets",
        "observation_unit": "Commuting-zone-period cell",
        "observed_margin": "Employment-to-population ratios and wages",
        "equilibrium_concern": "National product-demand, prices, migration, and offsetting sectoral adjustments",
        "extension_prompt": "Move from place incidence to worker trajectories, firm adoption, or longer-run adjustment margins.",
        "default_compare": "autorDornHanson2013ChinaSyndrome",
    },
    "autorDornHanson2013ChinaSyndrome": {
        "label": "Autor, Dorn, and Hanson (2013)",
        "block": "Trade shocks and local labor-market adjustment",
        "mechanism": "Import competition reallocates labor demand across exposed places through baseline industrial mix.",
        "treatment_unit": "Shift-share trade exposure for local labor markets",
        "observation_unit": "Commuting-zone panel",
        "observed_margin": "Employment, wages, unemployment, and nonparticipation",
        "equilibrium_concern": "Migration, worker transitions, consumer gains, and general-equilibrium price effects",
        "extension_prompt": "Track worker versus place adjustment, or compare import exposure to export or technology exposure.",
        "default_compare": "acemogluRestrepo2020RobotsJobs",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--anchor",
        choices=sorted(ANCHORS),
        default="saezSchoeferSeim2019",
        help="Primary anchor paper key.",
    )
    parser.add_argument(
        "--comparison",
        choices=sorted(ANCHORS),
        help="Optional comparison anchor. Defaults to the primary anchor's paired suggestion.",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("output/studio"),
        help="Directory for generated studio artifacts.",
    )
    return parser.parse_args()


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_menu_rows() -> list[dict[str, str]]:
    rows = []
    for key, meta in ANCHORS.items():
        rows.append(
            {
                "cite_key": key,
                "anchor_label": meta["label"],
                "course_block": meta["block"],
                "central_mechanism": meta["mechanism"],
                "treatment_unit": meta["treatment_unit"],
                "observation_unit": meta["observation_unit"],
                "observed_margin": meta["observed_margin"],
                "equilibrium_concern": meta["equilibrium_concern"],
                "extension_prompt": meta["extension_prompt"],
            }
        )
    return rows


def build_selected_rows(primary_key: str, comparison_key: str) -> list[dict[str, str]]:
    rows = []
    for role, key in (("primary", primary_key), ("comparison", comparison_key)):
        meta = ANCHORS[key]
        rows.append(
            {
                "role": role,
                "cite_key": key,
                "anchor_label": meta["label"],
                "course_block": meta["block"],
                "central_mechanism": meta["mechanism"],
                "treatment_unit": meta["treatment_unit"],
                "observation_unit": meta["observation_unit"],
                "observed_margin": meta["observed_margin"],
                "equilibrium_concern": meta["equilibrium_concern"],
                "extension_prompt": meta["extension_prompt"],
            }
        )
    return rows


def build_memo(primary_key: str, comparison_key: str) -> str:
    primary = ANCHORS[primary_key]
    comparison = ANCHORS[comparison_key]

    return f"""# Week 13 research-design memo scaffold

## Anchor selection

- Primary anchor: `{primary_key}` ({primary["label"]})
- Comparison anchor: `{comparison_key}` ({comparison["label"]})
- Diagnose -> Compare -> Design focus: mechanism, unit, observed margin, equilibrium scope, bounded extension

## 1. Question

State a labor-market question that is narrow enough to answer with one empirical object.

Starter based on the primary anchor:
How does the mechanism in **{primary["label"]}** travel to a new setting, margin, or population without changing the core Labor II logic?

## 2. Mechanism

- Primary mechanism: {primary["mechanism"]}
- Comparison mechanism: {comparison["mechanism"]}
- Your task: name one channel that is first-order and one channel that you are explicitly leaving offstage.

## 3. Treatment / exposure object

- Primary treatment unit: {primary["treatment_unit"]}
- Comparison treatment unit: {comparison["treatment_unit"]}
- Your task: say whether your project is about a policy treatment, a shock exposure, or a measurement object.

## 4. Unit of observation

- Primary observation unit: {primary["observation_unit"]}
- Comparison observation unit: {comparison["observation_unit"]}
- Your task: explain why the observation unit is the right one for the mechanism you care about.

## 5. Observed margin

- Primary observed margin: {primary["observed_margin"]}
- Comparison observed margin: {comparison["observed_margin"]}
- Your task: distinguish the observed outcome from the broader welfare or equilibrium object you might care about.

## 6. Identifying variation or descriptive design

Write two or three sentences on the design family you need:

- descriptive / measurement
- reduced-form causal
- structural / equilibrium

Then state why that design is enough for your bounded claim.

## 7. Key equilibrium concern

- Primary equilibrium concern: {primary["equilibrium_concern"]}
- Comparison equilibrium concern: {comparison["equilibrium_concern"]}
- Your task: name the main spillover, uncovered margin, or long-run adjustment channel that your design will not fully settle.

## 8. Proposed extension

Primary extension prompt:
{primary["extension_prompt"]}

Comparison prompt:
{comparison["extension_prompt"]}

Your task: propose one extension that is feasible for a field-paper or second-year project rather than a full dissertation.

## 9. Why the extension matters

Explain in three sentences:

1. what the literature already knows,
2. what your project adds,
3. why the added object matters for labor economics rather than only for a narrow setting.

## Quick checklist

- [ ] I named the central labor-market mechanism.
- [ ] I separated the unit of treatment from the unit of observation.
- [ ] I named the observed margin rather than implying a larger welfare object.
- [ ] I stated one equilibrium concern that stays offstage.
- [ ] I proposed a bounded extension that matches the design.
"""


def main() -> None:
    args = parse_args()
    primary_key = args.anchor
    comparison_key = args.comparison or ANCHORS[primary_key]["default_compare"]

    outdir = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    menu_rows = build_menu_rows()
    selected_rows = build_selected_rows(primary_key, comparison_key)

    write_csv(
        outdir / "anchor_menu.csv",
        menu_rows,
        [
            "cite_key",
            "anchor_label",
            "course_block",
            "central_mechanism",
            "treatment_unit",
            "observation_unit",
            "observed_margin",
            "equilibrium_concern",
            "extension_prompt",
        ],
    )
    write_csv(
        outdir / "selected_anchor_comparison.csv",
        selected_rows,
        [
            "role",
            "cite_key",
            "anchor_label",
            "course_block",
            "central_mechanism",
            "treatment_unit",
            "observation_unit",
            "observed_margin",
            "equilibrium_concern",
            "extension_prompt",
        ],
    )
    (outdir / "research_design_memo.md").write_text(
        build_memo(primary_key, comparison_key),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
