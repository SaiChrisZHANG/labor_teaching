from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from statistics import mean


@dataclass(frozen=True)
class LocalIndustry:
    place: str
    industry: str
    baseline_share: float
    robot_adoption: float
    ai_task_exposure: float
    training_capacity: float
    union_or_voice: float
    service_absorption: float


@dataclass(frozen=True)
class TransferScenario:
    setting: str
    unit: str
    technology_margin: str
    adoption_or_use: float
    complementary_organization: float
    worker_training: float
    monitoring_risk: float
    wage_pass_through: float


LOCAL_INDUSTRIES = [
    LocalIndustry("River County", "auto parts", 0.34, 0.82, 0.44, 0.52, 0.34, 0.41),
    LocalIndustry("River County", "warehousing", 0.20, 0.42, 0.58, 0.40, 0.18, 0.55),
    LocalIndustry("River County", "business services", 0.26, 0.18, 0.76, 0.62, 0.22, 0.70),
    LocalIndustry("River County", "health services", 0.20, 0.08, 0.37, 0.58, 0.30, 0.74),
    LocalIndustry("Lake Metro", "auto parts", 0.18, 0.82, 0.44, 0.66, 0.42, 0.54),
    LocalIndustry("Lake Metro", "warehousing", 0.16, 0.42, 0.58, 0.55, 0.26, 0.62),
    LocalIndustry("Lake Metro", "business services", 0.40, 0.18, 0.76, 0.72, 0.30, 0.78),
    LocalIndustry("Lake Metro", "health services", 0.26, 0.08, 0.37, 0.68, 0.38, 0.80),
    LocalIndustry("Mesa Labor Market", "auto parts", 0.10, 0.82, 0.44, 0.38, 0.12, 0.46),
    LocalIndustry("Mesa Labor Market", "warehousing", 0.30, 0.42, 0.58, 0.34, 0.10, 0.52),
    LocalIndustry("Mesa Labor Market", "business services", 0.22, 0.18, 0.76, 0.48, 0.16, 0.64),
    LocalIndustry("Mesa Labor Market", "health services", 0.38, 0.08, 0.37, 0.50, 0.18, 0.72),
    LocalIndustry("Harbor City", "auto parts", 0.12, 0.82, 0.44, 0.70, 0.36, 0.63),
    LocalIndustry("Harbor City", "warehousing", 0.22, 0.42, 0.58, 0.58, 0.24, 0.68),
    LocalIndustry("Harbor City", "business services", 0.44, 0.18, 0.76, 0.78, 0.34, 0.82),
    LocalIndustry("Harbor City", "health services", 0.22, 0.08, 0.37, 0.62, 0.32, 0.76),
    LocalIndustry("Prairie Works", "auto parts", 0.42, 0.82, 0.44, 0.45, 0.22, 0.36),
    LocalIndustry("Prairie Works", "warehousing", 0.18, 0.42, 0.58, 0.36, 0.12, 0.48),
    LocalIndustry("Prairie Works", "business services", 0.18, 0.18, 0.76, 0.44, 0.14, 0.58),
    LocalIndustry("Prairie Works", "health services", 0.22, 0.08, 0.37, 0.48, 0.18, 0.62),
]


TRANSFER_SCENARIOS = [
    TransferScenario(
        "customer-support generative AI rollout",
        "worker-team",
        "worker use",
        0.78,
        0.62,
        0.70,
        0.36,
        0.42,
    ),
    TransferScenario(
        "firm-level AI adoption in business services",
        "firm",
        "firm adoption",
        0.66,
        0.74,
        0.58,
        0.40,
        0.34,
    ),
    TransferScenario(
        "algorithmic scheduling platform",
        "platform-worker",
        "organizational implementation",
        0.84,
        0.50,
        0.30,
        0.78,
        0.18,
    ),
    TransferScenario(
        "regional data-center buildout",
        "local labor market",
        "compute infrastructure",
        0.54,
        0.44,
        0.46,
        0.22,
        0.28,
    ),
    TransferScenario(
        "AI-assisted global service outsourcing",
        "country-sector",
        "task tradability",
        0.60,
        0.56,
        0.52,
        0.34,
        0.30,
    ),
]


def ensure_output_dirs(root: Path) -> None:
    for relative in [
        "output/reproduced",
        "output/diagnosed",
        "output/transfer",
    ]:
        (root / relative).mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"no rows to write for {path}")
    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def local_exposure_rows() -> list[dict[str, object]]:
    places = sorted({row.place for row in LOCAL_INDUSTRIES})
    rows: list[dict[str, object]] = []
    for place in places:
        local_rows = [row for row in LOCAL_INDUSTRIES if row.place == place]
        robot_exposure = sum(row.baseline_share * row.robot_adoption for row in local_rows)
        ai_exposure = sum(row.baseline_share * row.ai_task_exposure for row in local_rows)
        training = sum(row.baseline_share * row.training_capacity for row in local_rows)
        voice = sum(row.baseline_share * row.union_or_voice for row in local_rows)
        absorption = sum(row.baseline_share * row.service_absorption for row in local_rows)
        manufacturing_share = sum(
            row.baseline_share for row in local_rows if row.industry == "auto parts"
        )

        employment_change = (
            0.018
            - 0.082 * robot_exposure
            + 0.030 * training
            + 0.025 * absorption
            + 0.010 * voice
        )
        wage_change = (
            0.020
            - 0.026 * robot_exposure
            + 0.036 * training
            + 0.020 * voice
            + 0.006 * ai_exposure
        )
        mobility_cost = 0.12 + 0.18 * manufacturing_share - 0.10 * absorption
        welfare_proxy = wage_change + employment_change - 0.20 * mobility_cost + 0.018 * voice

        rows.append(
            {
                "place": place,
                "robot_exposure": round(robot_exposure, 4),
                "ai_task_exposure": round(ai_exposure, 4),
                "training_capacity": round(training, 4),
                "worker_voice": round(voice, 4),
                "service_absorption": round(absorption, 4),
                "manufacturing_share": round(manufacturing_share, 4),
                "employment_change": round(employment_change, 4),
                "wage_change": round(wage_change, 4),
                "mobility_cost": round(mobility_cost, 4),
                "welfare_proxy": round(welfare_proxy, 4),
            }
        )
    return rows


def slope(rows: list[dict[str, object]], x_name: str, y_name: str) -> float:
    xs = [float(row[x_name]) for row in rows]
    ys = [float(row[y_name]) for row in rows]
    x_bar = mean(xs)
    y_bar = mean(ys)
    numerator = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
    denominator = sum((x - x_bar) ** 2 for x in xs)
    if denominator == 0:
        return 0.0
    return numerator / denominator


def reduced_form_rows(exposure_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    outcomes = [
        ("employment_change", "employment incidence"),
        ("wage_change", "wage incidence"),
        ("welfare_proxy", "welfare proxy"),
        ("mobility_cost", "adjustment cost"),
    ]
    rows: list[dict[str, object]] = []
    for outcome, label in outcomes:
        rows.append(
            {
                "outcome": label,
                "x_variable": "robot_exposure",
                "slope": round(slope(exposure_rows, "robot_exposure", outcome), 4),
                "interpretation": "teaching reduced form; not a published estimate",
            }
        )
    return rows


def diagnosis_rows() -> list[dict[str, object]]:
    return [
        {
            "design_element": "technology measure",
            "diagnosis": "robot exposure uses baseline industry shares times adoption intensity",
            "risk": "exposure is not firm adoption or worker use",
            "fix": "state the margin and compare with adoption or use measures when possible",
        },
        {
            "design_element": "unit of analysis",
            "diagnosis": "commuting-zone logic captures local incidence",
            "risk": "firm hiring, incumbent training, and internal reallocation are hidden",
            "fix": "add firm, establishment, or worker panels for mechanism tests",
        },
        {
            "design_element": "counterfactual",
            "diagnosis": "less-exposed places serve as comparison units",
            "risk": "places may have different pre-trends or industry shocks",
            "fix": "inspect pre-trends and isolate plausibly exogenous adoption variation",
        },
        {
            "design_element": "timing",
            "diagnosis": "short-run employment and wage effects may precede training and mobility",
            "risk": "one post period can miss delayed adjustment",
            "fix": "separate immediate, medium-run, and long-run outcomes",
        },
        {
            "design_element": "welfare object",
            "diagnosis": "wages and employment miss autonomy, risk, mobility cost, and voice",
            "risk": "the design can understate worker welfare losses",
            "fix": "add job-quality and bargaining-power measures where feasible",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for scenario in TRANSFER_SCENARIOS:
        augmentation_score = (
            0.35 * scenario.adoption_or_use
            + 0.30 * scenario.complementary_organization
            + 0.25 * scenario.worker_training
            + 0.10 * scenario.wage_pass_through
        )
        worker_risk = (
            0.45 * scenario.monitoring_risk
            + 0.25 * scenario.adoption_or_use
            - 0.20 * scenario.worker_training
            - 0.10 * scenario.wage_pass_through
        )
        rows.append(
            {
                "setting": scenario.setting,
                "unit": scenario.unit,
                "technology_margin": scenario.technology_margin,
                "adoption_or_use": round(scenario.adoption_or_use, 3),
                "organization_complement": round(scenario.complementary_organization, 3),
                "worker_training": round(scenario.worker_training, 3),
                "monitoring_risk": round(scenario.monitoring_risk, 3),
                "wage_pass_through": round(scenario.wage_pass_through, 3),
                "augmentation_score": round(augmentation_score, 3),
                "worker_risk": round(worker_risk, 3),
            }
        )
    return rows


def opportunity_rows() -> list[dict[str, object]]:
    return [
        {
            "project_direction": "worker-level generative AI use",
            "labor_question": "who receives durable augmentation and wage gains",
            "status": "open if use can be linked to worker outcomes",
        },
        {
            "project_direction": "firm adoption versus usage",
            "labor_question": "whether adoption changes hiring, training, and organization",
            "status": "open because adoption measures often miss implementation",
        },
        {
            "project_direction": "robot local exposure",
            "labor_question": "local wage and employment incidence of embodied automation",
            "status": "saturated as a broad question; open with new mechanisms or settings",
        },
        {
            "project_direction": "platform governance",
            "labor_question": "how algorithmic rules change risk, bargaining, and voice",
            "status": "open when rules can be measured directly",
        },
        {
            "project_direction": "compute infrastructure",
            "labor_question": "which places and workers gain from data-center and grid buildout",
            "status": "open and measurement-intensive",
        },
        {
            "project_direction": "global service trade",
            "labor_question": "which service tasks become tradable, automated, or augmented",
            "status": "open with credible task-trade and job-quality measures",
        },
    ]


def write_note(root: Path) -> None:
    note = (
        "This synthetic teaching path reproduces the design logic of a local "
        "technology-exposure exercise. It does not use official robot, Census, "
        "firm-adoption, worker telemetry, platform, or linked employer-employee "
        "data and does not claim to reproduce published magnitudes.\n"
    )
    (root / "output/reproduced/reproduction_note.txt").write_text(note)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    ensure_output_dirs(root)

    exposure = local_exposure_rows()
    write_csv(root / "output/reproduced/local_exposure_design.csv", exposure)
    write_csv(root / "output/reproduced/reduced_form_incidence.csv", reduced_form_rows(exposure))
    write_csv(root / "output/diagnosed/design_diagnosis.csv", diagnosis_rows())
    write_csv(root / "output/transfer/ai_design_transfer.csv", transfer_rows())
    write_csv(root / "output/transfer/project_opportunities.csv", opportunity_rows())
    write_note(root)


if __name__ == "__main__":
    main()
