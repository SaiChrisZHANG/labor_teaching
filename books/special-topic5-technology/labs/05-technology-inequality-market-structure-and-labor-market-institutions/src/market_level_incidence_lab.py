from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FirmMarket:
    industry: str
    firm: str
    baseline_market_share: float
    current_market_share: float
    baseline_labor_share: float
    current_labor_share: float
    technology_intensity: float
    intangible_intensity: float
    productivity_growth: float
    wage_premium: float
    union_coverage: float
    worker_voice: float
    employer_concentration: float
    platform_control: float


@dataclass(frozen=True)
class StructuralScenario:
    region: str
    initial_sector: str
    destination_sector: str
    employment_reallocation: float
    productivity_gain: float
    wage_gain: float
    formality_gain: float
    voice_gain: float
    mobility_cost: float
    technology_sophistication: float


@dataclass(frozen=True)
class FrontierScenario:
    place: str
    setting: str
    ai_adoption_capacity: float
    electricity_reliability: float
    data_center_demand: float
    outsourced_service_exposure: float
    informal_absorption: float
    training_capacity: float
    wage_floor_or_bargaining: float


FIRMS = [
    FirmMarket(
        "retail platforms",
        "Atlas Market",
        0.22,
        0.33,
        0.53,
        0.47,
        0.82,
        0.78,
        0.11,
        0.08,
        0.10,
        0.28,
        0.72,
        0.86,
    ),
    FirmMarket(
        "retail platforms",
        "Boreal Shops",
        0.18,
        0.16,
        0.61,
        0.58,
        0.38,
        0.30,
        0.03,
        0.02,
        0.18,
        0.42,
        0.50,
        0.36,
    ),
    FirmMarket(
        "retail platforms",
        "Cedar Local",
        0.14,
        0.08,
        0.66,
        0.64,
        0.24,
        0.18,
        0.00,
        -0.01,
        0.26,
        0.50,
        0.44,
        0.22,
    ),
    FirmMarket(
        "retail platforms",
        "Delta Commerce",
        0.24,
        0.29,
        0.50,
        0.44,
        0.76,
        0.70,
        0.09,
        0.06,
        0.08,
        0.24,
        0.68,
        0.80,
    ),
    FirmMarket(
        "retail platforms",
        "Evergreen Stores",
        0.22,
        0.14,
        0.64,
        0.62,
        0.30,
        0.22,
        0.01,
        0.00,
        0.24,
        0.46,
        0.46,
        0.30,
    ),
    FirmMarket(
        "business services",
        "Finch Analytics",
        0.16,
        0.25,
        0.58,
        0.52,
        0.84,
        0.82,
        0.13,
        0.12,
        0.06,
        0.34,
        0.60,
        0.42,
    ),
    FirmMarket(
        "business services",
        "Granite Support",
        0.26,
        0.22,
        0.67,
        0.63,
        0.44,
        0.35,
        0.04,
        0.03,
        0.12,
        0.40,
        0.50,
        0.36,
    ),
    FirmMarket(
        "business services",
        "Harbor Backoffice",
        0.28,
        0.19,
        0.71,
        0.69,
        0.32,
        0.24,
        0.02,
        0.01,
        0.16,
        0.44,
        0.46,
        0.30,
    ),
    FirmMarket(
        "business services",
        "Iris Cloud",
        0.12,
        0.20,
        0.55,
        0.48,
        0.90,
        0.88,
        0.15,
        0.14,
        0.05,
        0.30,
        0.64,
        0.50,
    ),
    FirmMarket(
        "business services",
        "Juniper Admin",
        0.18,
        0.14,
        0.69,
        0.67,
        0.36,
        0.28,
        0.03,
        0.01,
        0.14,
        0.38,
        0.48,
        0.28,
    ),
    FirmMarket(
        "advanced manufacturing",
        "Keystone Robotics",
        0.18,
        0.27,
        0.57,
        0.51,
        0.86,
        0.64,
        0.12,
        0.10,
        0.22,
        0.50,
        0.54,
        0.24,
    ),
    FirmMarket(
        "advanced manufacturing",
        "Lake Components",
        0.24,
        0.21,
        0.66,
        0.63,
        0.46,
        0.34,
        0.04,
        0.03,
        0.30,
        0.56,
        0.48,
        0.20,
    ),
    FirmMarket(
        "advanced manufacturing",
        "Mason Assembly",
        0.22,
        0.15,
        0.69,
        0.67,
        0.34,
        0.24,
        0.01,
        -0.01,
        0.34,
        0.60,
        0.44,
        0.18,
    ),
    FirmMarket(
        "advanced manufacturing",
        "Northstar Systems",
        0.15,
        0.22,
        0.59,
        0.55,
        0.74,
        0.58,
        0.09,
        0.07,
        0.26,
        0.48,
        0.52,
        0.22,
    ),
    FirmMarket(
        "advanced manufacturing",
        "Orchard Fabrication",
        0.21,
        0.15,
        0.68,
        0.66,
        0.40,
        0.28,
        0.03,
        0.01,
        0.28,
        0.54,
        0.46,
        0.16,
    ),
]


STRUCTURAL_SCENARIOS = [
    StructuralScenario("coastal high income", "manufacturing", "formal business services", 0.22, 0.16, 0.10, 0.08, -0.02, 0.18, 0.82),
    StructuralScenario("legacy manufacturing region", "manufacturing", "low-wage local services", 0.28, 0.03, -0.08, -0.10, -0.14, 0.34, 0.48),
    StructuralScenario("agrarian middle income", "agriculture", "light manufacturing", 0.31, 0.14, 0.09, 0.12, 0.05, 0.26, 0.54),
    StructuralScenario("urban global south", "agriculture", "informal services", 0.36, 0.02, -0.03, -0.18, -0.12, 0.22, 0.36),
    StructuralScenario("digital services hub", "routine services", "knowledge services", 0.24, 0.18, 0.12, 0.10, 0.04, 0.16, 0.74),
]


FRONTIER_SCENARIOS = [
    FrontierScenario("desert data corridor", "high-income infrastructure buildout", 0.82, 0.88, 0.90, 0.24, 0.08, 0.62, 0.50),
    FrontierScenario("outsourced service city", "AI-assisted knowledge services", 0.64, 0.66, 0.34, 0.82, 0.18, 0.70, 0.42),
    FrontierScenario("grid-constrained exporter", "AI adoption under electricity scarcity", 0.46, 0.38, 0.22, 0.62, 0.26, 0.52, 0.32),
    FrontierScenario("informal services metro", "labor-absorbing services with low diffusion", 0.32, 0.54, 0.18, 0.40, 0.70, 0.30, 0.20),
    FrontierScenario("public-sector digital hub", "state-supported AI diffusion", 0.58, 0.72, 0.44, 0.46, 0.22, 0.64, 0.68),
]


def clip(value: float, lower: float = -1.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def hhi(values: list[float]) -> float:
    return sum(value * value for value in values)


def firms_by_industry() -> dict[str, list[FirmMarket]]:
    grouped: dict[str, list[FirmMarket]] = {}
    for firm in FIRMS:
        grouped.setdefault(firm.industry, []).append(firm)
    return grouped


def aggregate_labor_share(firms: list[FirmMarket], period: str) -> float:
    if period == "baseline":
        return sum(firm.baseline_market_share * firm.baseline_labor_share for firm in firms)
    return sum(firm.current_market_share * firm.current_labor_share for firm in firms)


def within_component(firms: list[FirmMarket]) -> float:
    return sum(
        firm.baseline_market_share * (firm.current_labor_share - firm.baseline_labor_share)
        for firm in firms
    )


def between_component(firms: list[FirmMarket]) -> float:
    return sum(
        (firm.current_market_share - firm.baseline_market_share) * firm.baseline_labor_share
        for firm in firms
    )


def interaction_component(firms: list[FirmMarket]) -> float:
    return sum(
        (firm.current_market_share - firm.baseline_market_share)
        * (firm.current_labor_share - firm.baseline_labor_share)
        for firm in firms
    )


def dominant_mechanism(within: float, between: float, interaction: float) -> str:
    components = {
        "within_firm_labor_share_change": abs(within),
        "between_firm_market_share_reallocation": abs(between),
        "interaction_of_share_and_labor_share_change": abs(interaction),
    }
    return max(components, key=components.get)


def institutional_mediation(firms: list[FirmMarket]) -> float:
    return sum(
        firm.current_market_share
        * (0.40 * firm.union_coverage + 0.35 * firm.worker_voice + 0.25 * (1 - firm.platform_control))
        for firm in firms
    )


def employer_power_risk(firms: list[FirmMarket]) -> float:
    return sum(
        firm.current_market_share
        * (0.45 * firm.employer_concentration + 0.35 * firm.platform_control + 0.20 * (1 - firm.worker_voice))
        for firm in firms
    )


def technology_reallocation_index(firms: list[FirmMarket]) -> float:
    return sum(
        (firm.current_market_share - firm.baseline_market_share)
        * (firm.technology_intensity + firm.intangible_intensity)
        for firm in firms
    )


def reproduction_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for industry, firms in firms_by_industry().items():
        baseline_ls = aggregate_labor_share(firms, "baseline")
        current_ls = aggregate_labor_share(firms, "current")
        within = within_component(firms)
        between = between_component(firms)
        interaction = interaction_component(firms)
        baseline_hhi = hhi([firm.baseline_market_share for firm in firms])
        current_hhi = hhi([firm.current_market_share for firm in firms])
        rows.append(
            {
                "industry": industry,
                "baseline_labor_share": round(baseline_ls, 3),
                "current_labor_share": round(current_ls, 3),
                "labor_share_change": round(current_ls - baseline_ls, 3),
                "within_component": round(within, 3),
                "between_component": round(between, 3),
                "interaction_component": round(interaction, 3),
                "baseline_hhi": round(baseline_hhi, 3),
                "current_hhi": round(current_hhi, 3),
                "hhi_change": round(current_hhi - baseline_hhi, 3),
                "technology_reallocation_index": round(technology_reallocation_index(firms), 3),
                "dominant_mechanism": dominant_mechanism(within, between, interaction),
            }
        )
    return rows


def diagnosis_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for industry, firms in firms_by_industry().items():
        current_ls = aggregate_labor_share(firms, "current")
        baseline_ls = aggregate_labor_share(firms, "baseline")
        tech_intensity = sum(firm.current_market_share * firm.technology_intensity for firm in firms)
        intangible_intensity = sum(firm.current_market_share * firm.intangible_intensity for firm in firms)
        institution = institutional_mediation(firms)
        employer_power = employer_power_risk(firms)
        risk_score = clip(
            0.35 * employer_power
            + 0.25 * intangible_intensity
            + 0.20 * tech_intensity
            - 0.25 * institution,
            0.0,
            1.0,
        )
        if risk_score >= 0.45:
            incidence_label = "rents_likely_shift_away_from_broad_labor"
        elif institution >= 0.45:
            incidence_label = "institutions_may_mediate_rent_capture"
        else:
            incidence_label = "mixed_incidence_requires_worker_outcomes"
        rows.append(
            {
                "industry": industry,
                "technology_intensity": round(tech_intensity, 3),
                "intangible_intensity": round(intangible_intensity, 3),
                "labor_share_change": round(current_ls - baseline_ls, 3),
                "employer_power_risk": round(employer_power, 3),
                "institutional_mediation": round(institution, 3),
                "incidence_risk_score": round(risk_score, 3),
                "incidence_label": incidence_label,
                "measurement_warning": measurement_warning(tech_intensity, intangible_intensity, employer_power),
            }
        )
    return rows


def measurement_warning(tech_intensity: float, intangible_intensity: float, employer_power: float) -> str:
    if tech_intensity >= 0.70 and intangible_intensity >= 0.65:
        return "technology_and_intangible_rents_are_hard_to_separate"
    if employer_power >= 0.60:
        return "product_market_growth_may_hide_labor_market_power"
    if tech_intensity < 0.50:
        return "concentration_change_may_not_be_a_direct_technology_measure"
    return "interpret_as_market_level_incidence_not_worker_welfare"


def structural_transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for scenario in STRUCTURAL_SCENARIOS:
        job_quality_change = (
            0.35 * scenario.wage_gain
            + 0.25 * scenario.formality_gain
            + 0.25 * scenario.voice_gain
            - 0.15 * scenario.mobility_cost
        )
        welfare_reallocation = (
            0.30 * scenario.productivity_gain
            + 0.30 * scenario.wage_gain
            + 0.20 * scenario.formality_gain
            + 0.15 * scenario.voice_gain
            - 0.25 * scenario.mobility_cost
        )
        if scenario.employment_reallocation > 0.25 and job_quality_change < 0:
            label = "employment_reallocation_without_job_quality_gain"
        elif welfare_reallocation > 0.08:
            label = "welfare_improving_reallocation"
        elif scenario.destination_sector == "informal services":
            label = "informal_absorption_risk"
        elif scenario.destination_sector == "knowledge services":
            label = "technology_enabled_service_upgrade"
        else:
            label = "mixed_structural_change"
        rows.append(
            {
                "region": scenario.region,
                "initial_sector": scenario.initial_sector,
                "destination_sector": scenario.destination_sector,
                "employment_reallocation": scenario.employment_reallocation,
                "productivity_gain": scenario.productivity_gain,
                "job_quality_change": round(job_quality_change, 3),
                "welfare_reallocation_index": round(welfare_reallocation, 3),
                "technology_sophistication": scenario.technology_sophistication,
                "transfer_label": label,
            }
        )
    return rows


def frontier_transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for scenario in FRONTIER_SCENARIOS:
        infrastructure_labor_demand = (
            0.45 * scenario.data_center_demand
            + 0.20 * scenario.electricity_reliability
            + 0.15 * scenario.ai_adoption_capacity
        )
        service_channel = (
            0.45 * scenario.outsourced_service_exposure
            + 0.25 * scenario.training_capacity
            + 0.15 * scenario.ai_adoption_capacity
            - 0.20 * scenario.informal_absorption
        )
        institution_adjusted_incidence = (
            0.30 * infrastructure_labor_demand
            + 0.30 * service_channel
            + 0.20 * scenario.wage_floor_or_bargaining
            - 0.20 * scenario.informal_absorption
        )
        if scenario.data_center_demand >= 0.75:
            label = "ai_infrastructure_spatial_incidence"
        elif scenario.outsourced_service_exposure >= 0.75:
            label = "outsourced_digital_service_channel"
        elif scenario.electricity_reliability < 0.45:
            label = "energy_constraint_limits_ai_adoption"
        elif scenario.informal_absorption >= 0.60:
            label = "low_quality_service_absorption_risk"
        else:
            label = "institution_dependent_ai_diffusion"
        rows.append(
            {
                "place": scenario.place,
                "setting": scenario.setting,
                "ai_adoption_capacity": scenario.ai_adoption_capacity,
                "electricity_reliability": scenario.electricity_reliability,
                "data_center_demand": scenario.data_center_demand,
                "outsourced_service_exposure": scenario.outsourced_service_exposure,
                "infrastructure_labor_demand": round(infrastructure_labor_demand, 3),
                "service_channel": round(service_channel, 3),
                "institution_adjusted_incidence": round(institution_adjusted_incidence, 3),
                "frontier_label": label,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    lab_dir = Path(__file__).resolve().parents[1]

    write_csv(
        lab_dir / "output" / "reproduced" / "market_structure_labor_share.csv",
        reproduction_rows(),
    )
    write_csv(
        lab_dir / "output" / "diagnosed" / "incidence_diagnosis.csv",
        diagnosis_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "structural_change_transfer.csv",
        structural_transfer_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "global_ai_frontier_transfer.csv",
        frontier_transfer_rows(),
    )

    note = (
        "Synthetic Week 5 market-incidence lab complete. Outputs reproduce "
        "a concentration and labor-share decomposition, diagnose rent capture "
        "and institutional mediation, and transfer the logic to structural "
        "change, Global South diffusion, outsourcing, and AI infrastructure.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
