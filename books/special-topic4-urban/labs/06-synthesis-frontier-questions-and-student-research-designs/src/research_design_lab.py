from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DesignExample:
    broad_topic: str
    labor_outcome: str
    urban_mechanism: str
    geography: str
    comparison: str
    incidence_unit: str
    welfare_object: str
    portability_claim: str


@dataclass(frozen=True)
class FrontierIdea:
    topic: str
    labor_focus: int
    mechanism_clarity: int
    design_plausibility: int
    external_relevance: int
    next_narrowing_step: str


DESIGN_EXAMPLES = [
    DesignExample(
        broad_topic="remote work and city change",
        labor_outcome="worker outside options and earnings by occupation",
        urban_mechanism="hybrid work relaxes commuting constraints but changes local service demand",
        geography="metro labor markets linked to residence-workplace flows",
        comparison="pre/post remote-work exposure by occupation and telework feasibility",
        incidence_unit="remote-capable workers, local service workers, firms, landlords",
        welfare_object="real access net of rents, commuting, and local demand changes",
        portability_claim="reveals when digital work weakens or reinforces spatial labor frictions",
    ),
    DesignExample(
        broad_topic="zoning reform",
        labor_outcome="employment and commute-adjusted access for constrained workers",
        urban_mechanism="housing supply changes entry into high-wage labor markets",
        geography="reformed parcels, neighborhoods, and connected commuting zones",
        comparison="event study around reform timing with nearby unreformed areas",
        incidence_unit="incumbent renters, entrants, commuters, landlords, firms",
        welfare_object="real access after rent capitalization and commute changes",
        portability_claim="tests whether housing reform converts productivity into worker access",
    ),
    DesignExample(
        broad_topic="urban heat",
        labor_outcome="hours, absenteeism, and productivity for exposed workers",
        urban_mechanism="heat changes feasible work and adaptation costs",
        geography="workplaces, routes, and neighborhoods with measured heat exposure",
        comparison="high-frequency exposure variation within worker or workplace",
        incidence_unit="outdoor workers, indoor workers without adaptation, firms",
        welfare_object="lost work capacity and hidden exposure costs",
        portability_claim="identifies climate risk as a labor-market constraint in cities",
    ),
    DesignExample(
        broad_topic="redevelopment",
        labor_outcome="incumbent resident employment, commute burden, and retention",
        urban_mechanism="redevelopment changes local jobs, rents, and displacement risk",
        geography="treated neighborhoods plus connected workplace and residence zones",
        comparison="project timing, boundaries, or phased redevelopment exposure",
        incidence_unit="incumbent renters, homeowners, in-commuters, local firms",
        welfare_object="real access and displacement-adjusted labor gains",
        portability_claim="shows when neighborhood upgrading creates labor gains for incumbents",
    ),
]


FRONTIER_IDEAS = [
    FrontierIdea(
        "remote work and hybrid geography",
        5,
        4,
        4,
        5,
        "choose an occupation-specific labor outcome and a remote-work exposure measure",
    ),
    FrontierIdea(
        "housing reform and labor access",
        5,
        5,
        4,
        5,
        "define rent, entry, commute, and incumbent-worker incidence measures",
    ),
    FrontierIdea(
        "climate heat and urban labor",
        5,
        5,
        5,
        5,
        "match worker or workplace outcomes to high-frequency exposure data",
    ),
    FrontierIdea(
        "commuting and local labor market power",
        5,
        4,
        3,
        5,
        "identify a commute shock or spatial outside-option measure",
    ),
    FrontierIdea(
        "AI and digital infrastructure",
        4,
        3,
        3,
        5,
        "narrow to job search, remote work, screening, or local service demand",
    ),
    FrontierIdea(
        "redevelopment and displacement",
        5,
        4,
        4,
        5,
        "define incumbents before treatment and measure moves, rents, jobs, and commutes",
    ),
]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def design_rows() -> list[dict[str, object]]:
    return [example.__dict__ for example in DESIGN_EXAMPLES]


def failure_rows() -> list[dict[str, str]]:
    return [
        {
            "failure_mode": "mechanism_slippage",
            "weak_design": "treatment changes transit, rents, safety, and schools but claims one neighborhood effect",
            "repair": "state the main channel and measure or bracket the bundled channels",
        },
        {
            "failure_mode": "geography_mismatch",
            "weak_design": "county-level estimates are used to claim a tract-level exposure mechanism",
            "repair": "choose geography using commuting flows, boundaries, routes, or institutions",
        },
        {
            "failure_mode": "ignoring_equilibrium",
            "weak_design": "employment gains are reported without rents, migration, or commuting",
            "repair": "trace the most likely adjustment margins and define the incidence unit",
        },
        {
            "failure_mode": "nominal_outcome_bias",
            "weak_design": "wage increases are treated as welfare despite rent and commute changes",
            "repair": "state what wages identify and add real-access or welfare measures where possible",
        },
        {
            "failure_mode": "localism_without_mechanism",
            "weak_design": "the paper documents one city but never explains what travels",
            "repair": "write a portability claim tied to a general spatial labor mechanism",
        },
        {
            "failure_mode": "sorting_treatment_confusion",
            "weak_design": "neighborhood differences are interpreted causally without selection diagnostics",
            "repair": "use timing, boundaries, shocks, mover logic, or explicit selection checks",
        },
    ]


def frontier_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for idea in FRONTIER_IDEAS:
        total = (
            idea.labor_focus
            + idea.mechanism_clarity
            + idea.design_plausibility
            + idea.external_relevance
        )
        readiness = "memo_ready" if total >= 18 else "needs_narrowing"
        row = {
            "topic": idea.topic,
            "labor_focus": idea.labor_focus,
            "mechanism_clarity": idea.mechanism_clarity,
            "design_plausibility": idea.design_plausibility,
            "external_relevance": idea.external_relevance,
            "total_score": total,
            "readiness": readiness,
            "next_narrowing_step": idea.next_narrowing_step,
        }
        rows.append(row)
    return rows


def write_memo_template(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "# One-Page Urban-Labor Research Memo",
                "",
                "Title:",
                "",
                "Research question:",
                "",
                "Labor outcome:",
                "",
                "Urban mechanism:",
                "",
                "Unit of geography:",
                "",
                "Population and incidence unit:",
                "",
                "Counterfactual or identifying variation:",
                "",
                "Expected adjustment margins:",
                "",
                "Main empirical threats:",
                "",
                "Welfare object:",
                "",
                "Why this matters beyond one city:",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]
    write_csv(
        lab_dir / "output" / "reproduced" / "design_architecture_examples.csv",
        design_rows(),
    )
    write_csv(
        lab_dir / "output" / "diagnosed" / "failure_mode_checklist.csv",
        failure_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "frontier_project_scores.csv",
        frontier_rows(),
    )
    write_memo_template(
        lab_dir / "output" / "transfer" / "one_page_research_memo_template.md"
    )


if __name__ == "__main__":
    main()
