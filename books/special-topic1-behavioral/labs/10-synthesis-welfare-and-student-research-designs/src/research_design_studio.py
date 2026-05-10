#!/usr/bin/env python3
"""Generate a bounded Week 10 behavioral-labor research-design memo."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ANCHORS = {
    "muellerSpinnewijnTopa2021": {
        "label": "Mueller, Spinnewijn, and Topa (2021)",
        "course_block": "Beliefs, expectations, and job search",
        "puzzle": "Job seekers' subjective expectations differ systematically from realized employment prospects.",
        "behavioral_wedge": "Biased beliefs, heterogeneous updating, and duration-dependent expectations.",
        "labor_setting": "Unemployment spells with repeated belief measures and employment outcomes.",
        "labor_margin": "Search intensity, perceived job-finding probabilities, and unemployment exit.",
        "variation": "Within-person belief dynamics linked to realized job-finding outcomes.",
        "method": "Panel fixed effects, forecast-error diagnostics, and hazard or duration analysis.",
        "welfare_object": "Welfare depends on whether mistaken beliefs distort search effort, reservation choices, or training decisions.",
        "not_identified": "A pure welfare benchmark or general-equilibrium search response without additional assumptions.",
        "transfer_prompt": "Apply repeated beliefs and forecast-error logic to job search after a sectoral, technology, or displacement shock.",
        "default_compare": "bhargavaManoli2015",
    },
    "dellaVignaListMalmendierRao2022": {
        "label": "DellaVigna, List, Malmendier, and Rao (2022)",
        "course_block": "Incentives, contracts, reciprocity, and workplace behavior",
        "puzzle": "Workers may respond to wage gifts, contract framing, and employer actions in ways not captured by spot incentives alone.",
        "behavioral_wedge": "Social preferences, reciprocity, gift exchange, and expectations about employer intent.",
        "labor_setting": "Workplace effort provision under experimentally varied contract or gift-exchange environments.",
        "labor_margin": "Effort, output, quality, attendance, and response to incentive or gift treatments.",
        "variation": "Field-experimental variation in workplace treatment arms.",
        "method": "Treatment comparisons, ANCOVA or OLS, heterogeneity analysis, and contract-design inference.",
        "welfare_object": "Welfare depends on whether contracts improve surplus, distort effort, or shift rents between workers and firms.",
        "not_identified": "Long-run employment relationships, firm-wide culture effects, or equilibrium contract redesign.",
        "transfer_prompt": "Transfer the design to subjective evaluation, monitoring, feedback, or team-based incentives.",
        "default_compare": "muellerSpinnewijnTopa2021",
    },
    "bhargavaManoli2015": {
        "label": "Bhargava and Manoli (2015)",
        "course_block": "Behavioral policy design, take-up, and implementation",
        "puzzle": "Eligible households often fail to claim valuable benefits even when statutory incentives are large.",
        "behavioral_wedge": "Psychological frictions, inattention, complexity, perceived eligibility, and administrative burden.",
        "labor_setting": "Benefit claiming and policy take-up interfaces that affect earnings-linked program exposure.",
        "labor_margin": "Application completion, claiming, timing, persistence, and possible labor-supply interaction.",
        "variation": "Randomized notices, simplification, salience, or assistance treatments.",
        "method": "Randomized encouragement, treatment-effect summaries, heterogeneity analysis, and hazard-style claiming timing.",
        "welfare_object": "Welfare depends on whether non-take-up reflects mistakes, hassle costs, stigma, or low private value.",
        "not_identified": "Complete welfare without benefit values, costs, stigma, targeting, and equilibrium program response.",
        "transfer_prompt": "Apply take-up and implementation logic to UI, training, disability, EITC, or local job services.",
        "default_compare": "bernheimFradkinPopov2015",
    },
    "bernheimFradkinPopov2015": {
        "label": "Bernheim, Fradkin, and Popov (2015)",
        "course_block": "Defaults, retirement saving, and behavioral welfare",
        "puzzle": "Default options strongly affect retirement saving, but observed default choices need not reveal welfare.",
        "behavioral_wedge": "Inertia, procrastination, passive choice, choice overload, and default endorsement effects.",
        "labor_setting": "Employer-mediated retirement plans and payroll saving menus.",
        "labor_margin": "Plan participation, contribution rates, asset allocation, and persistence at defaults.",
        "variation": "Default assignment, plan design variation, and observed choice under alternative menu environments.",
        "method": "Treatment or design comparisons, calibrated welfare, sufficient-statistics logic, and structural interpretation.",
        "welfare_object": "Welfare requires a benchmark contribution or allocation rather than treating default adherence as revealed preference.",
        "not_identified": "A universal optimal default without heterogeneous preferences, liquidity needs, and employer menu response.",
        "transfer_prompt": "Transfer default-welfare logic to benefits, training enrollment, job-search platforms, or schedule selection.",
        "default_compare": "bhargavaManoli2015",
    },
}


FIELDS = [
    "cite_key",
    "anchor_label",
    "course_block",
    "puzzle",
    "behavioral_wedge",
    "labor_setting",
    "labor_margin",
    "variation",
    "method",
    "welfare_object",
    "not_identified",
    "transfer_prompt",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--anchor",
        choices=sorted(ANCHORS),
        default="muellerSpinnewijnTopa2021",
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


def row_for(key: str) -> dict[str, str]:
    meta = ANCHORS[key]
    return {
        "cite_key": key,
        "anchor_label": meta["label"],
        "course_block": meta["course_block"],
        "puzzle": meta["puzzle"],
        "behavioral_wedge": meta["behavioral_wedge"],
        "labor_setting": meta["labor_setting"],
        "labor_margin": meta["labor_margin"],
        "variation": meta["variation"],
        "method": meta["method"],
        "welfare_object": meta["welfare_object"],
        "not_identified": meta["not_identified"],
        "transfer_prompt": meta["transfer_prompt"],
    }


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_menu_rows() -> list[dict[str, str]]:
    return [row_for(key) for key in sorted(ANCHORS)]


def build_selected_rows(primary_key: str, comparison_key: str) -> list[dict[str, str]]:
    rows = []
    for role, key in (("primary", primary_key), ("comparison", comparison_key)):
        row = row_for(key)
        row = {"role": role, **row}
        rows.append(row)
    return rows


def build_memo(primary_key: str, comparison_key: str) -> str:
    primary = ANCHORS[primary_key]
    comparison = ANCHORS[comparison_key]

    return f"""# Week 10 behavioral-labor research-design memo

## Anchor selection

- Primary anchor: `{primary_key}` ({primary["label"]})
- Comparison anchor: `{comparison_key}` ({comparison["label"]})
- Studio logic: Reproduce -> Diagnose -> Transfer

## 1. Puzzle or fact

Starter puzzle from the primary anchor:
{primary["puzzle"]}

Your project question:
Replace this sentence with a labor-market fact or puzzle that is narrow enough to study.

## 2. Behavioral mechanism

- Primary wedge: {primary["behavioral_wedge"]}
- Comparison wedge: {comparison["behavioral_wedge"]}

Your task:
Name the behavioral wedge, one standard labor-economics alternative, and the evidence that would distinguish them.

## 3. Labor-market setting

- Primary setting: {primary["labor_setting"]}
- Comparison setting: {comparison["labor_setting"]}

Your task:
Explain why the institution, firm, market, platform, or policy environment makes the wedge first-order.

## 4. Outcome and unit of observation

- Primary labor margin: {primary["labor_margin"]}
- Comparison labor margin: {comparison["labor_margin"]}

Your task:
Name the observed outcome, unit of observation, and the broader labor-market object you are tempted to infer.

## 5. Identifying variation

- Primary variation: {primary["variation"]}
- Comparison variation: {comparison["variation"]}

Your task:
State the variation that identifies your bounded claim and one threat to interpretation.

## 6. Econometric method

- Primary method: {primary["method"]}
- Comparison method: {comparison["method"]}

Your task:
Choose the method because it matches the estimand, not because it is familiar.

## 7. Welfare or policy interpretation

- Primary welfare object: {primary["welfare_object"]}
- Comparison welfare object: {comparison["welfare_object"]}

Your task:
Define the benchmark action, long-run learning criterion, or welfare limitation.

## 8. Contribution relative to the frontier

Primary transfer prompt:
{primary["transfer_prompt"]}

Comparison transfer prompt:
{comparison["transfer_prompt"]}

Your task:
Say what the literature already knows, what your project adds, and why the added object matters for behavioral labor.

## What this design does not identify

Primary limitation:
{primary["not_identified"]}

Comparison limitation:
{comparison["not_identified"]}

Your task:
Add one honest sentence about a parameter, welfare claim, or equilibrium response that remains outside your design.

## Quick checklist

- [ ] I start from a labor-market fact or puzzle.
- [ ] I name the behavioral wedge and a standard alternative.
- [ ] I explain why the setting makes the wedge economically important.
- [ ] I state the identifying variation and econometric method.
- [ ] I separate treatment effect, behavioral parameter, welfare object, and equilibrium response.
- [ ] I define the welfare benchmark or decline the welfare claim.
- [ ] I state the contribution relative to the frontier.
"""


def main() -> None:
    args = parse_args()
    primary_key = args.anchor
    comparison_key = args.comparison or ANCHORS[primary_key]["default_compare"]

    outdir = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    write_csv(outdir / "anchor_menu.csv", build_menu_rows(), FIELDS)
    write_csv(
        outdir / "selected_anchor_diagnostic.csv",
        build_selected_rows(primary_key, comparison_key),
        ["role", *FIELDS],
    )
    (outdir / "research_design_memo.md").write_text(
        build_memo(primary_key, comparison_key),
        encoding="utf-8",
    )

    print(f"Wrote Week 10 studio artifacts to {outdir}")


if __name__ == "__main__":
    main()
