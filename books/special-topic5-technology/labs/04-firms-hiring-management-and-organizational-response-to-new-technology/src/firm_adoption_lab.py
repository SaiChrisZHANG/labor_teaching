from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Firm:
    name: str
    sector: str
    baseline_employment: int
    routine_task_share: float
    baseline_ai_skill_share: float
    baseline_stem_share: float
    baseline_junior_share: float
    baseline_manager_share: float
    management_quality: float
    data_readiness: float
    adoption_year: int | None
    acquisition: float
    implementation: float
    usage: float
    reorganization: float
    incumbent_training: float
    new_hire_ai_training: float
    monitoring_intensity: float
    human_override: float
    transparency: float
    worker_trust: float
    manager_algorithm_trust: float
    replacement_concern: float
    perceived_fairness: float
    baseline_productivity_growth: float


@dataclass(frozen=True)
class VignetteArm:
    arm: str
    transparency: float
    human_override: float
    replacement_risk: float
    performance_feedback: float
    monitoring_intensity: float


FIRMS = [
    Firm(
        "Atlas Claims",
        "insurance services",
        980,
        0.62,
        0.045,
        0.22,
        0.30,
        0.18,
        0.72,
        0.78,
        2024,
        0.86,
        0.72,
        0.62,
        0.58,
        0.38,
        0.70,
        0.66,
        0.42,
        0.52,
        0.48,
        0.60,
        0.54,
        0.46,
        0.045,
    ),
    Firm(
        "Boreal Components",
        "durable manufacturing",
        1340,
        0.70,
        0.018,
        0.16,
        0.18,
        0.14,
        0.48,
        0.42,
        2025,
        0.44,
        0.30,
        0.22,
        0.24,
        0.18,
        0.28,
        0.58,
        0.35,
        0.34,
        0.30,
        0.38,
        0.68,
        0.32,
        0.018,
    ),
    Firm(
        "Civic Health Network",
        "health administration",
        760,
        0.44,
        0.030,
        0.27,
        0.24,
        0.20,
        0.66,
        0.70,
        2024,
        0.68,
        0.63,
        0.55,
        0.48,
        0.62,
        0.42,
        0.42,
        0.76,
        0.66,
        0.64,
        0.54,
        0.34,
        0.64,
        0.032,
    ),
    Firm(
        "Delta Logistics Platform",
        "logistics platform",
        2120,
        0.57,
        0.052,
        0.24,
        0.34,
        0.13,
        0.76,
        0.82,
        2023,
        0.92,
        0.84,
        0.76,
        0.74,
        0.46,
        0.78,
        0.84,
        0.30,
        0.48,
        0.42,
        0.66,
        0.64,
        0.40,
        0.056,
    ),
    Firm(
        "Evergreen Legal Services",
        "professional services",
        420,
        0.34,
        0.060,
        0.34,
        0.28,
        0.22,
        0.70,
        0.74,
        2024,
        0.78,
        0.68,
        0.60,
        0.46,
        0.64,
        0.52,
        0.36,
        0.82,
        0.72,
        0.70,
        0.50,
        0.30,
        0.68,
        0.040,
    ),
    Firm(
        "Foundry Retail Group",
        "retail operations",
        1850,
        0.52,
        0.020,
        0.13,
        0.22,
        0.16,
        0.44,
        0.46,
        None,
        0.18,
        0.12,
        0.06,
        0.08,
        0.16,
        0.18,
        0.30,
        0.56,
        0.38,
        0.40,
        0.30,
        0.48,
        0.42,
        0.010,
    ),
    Firm(
        "Granite Software",
        "enterprise software",
        640,
        0.22,
        0.120,
        0.56,
        0.42,
        0.17,
        0.84,
        0.88,
        2023,
        0.96,
        0.90,
        0.86,
        0.78,
        0.82,
        0.84,
        0.28,
        0.86,
        0.74,
        0.78,
        0.72,
        0.22,
        0.72,
        0.072,
    ),
    Firm(
        "Harbor Public Services",
        "public administration",
        1110,
        0.49,
        0.025,
        0.20,
        0.20,
        0.21,
        0.58,
        0.54,
        2025,
        0.52,
        0.34,
        0.24,
        0.22,
        0.42,
        0.26,
        0.36,
        0.80,
        0.70,
        0.56,
        0.36,
        0.30,
        0.60,
        0.014,
    ),
]

VIGNETTES = [
    VignetteArm("opaque_monitoring_no_override", 0.20, 0.10, 0.80, 0.20, 0.85),
    VignetteArm("transparent_with_human_override", 0.78, 0.82, 0.28, 0.62, 0.36),
    VignetteArm("high_performance_high_replacement", 0.60, 0.48, 0.76, 0.88, 0.58),
    VignetteArm("training_first_low_monitoring", 0.70, 0.76, 0.22, 0.54, 0.22),
    VignetteArm("manager_discretion_low_feedback", 0.46, 0.90, 0.34, 0.18, 0.40),
]


def clip(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def adoption_stage(firm: Firm) -> str:
    if firm.acquisition < 0.30:
        return "no_adoption"
    if firm.implementation < 0.45:
        return "acquisition_without_implementation"
    if firm.usage < 0.45:
        return "implementation_with_low_usage"
    if firm.reorganization < 0.45:
        return "usage_without_reorganization"
    return "reorganized_use"


def adoption_index(firm: Firm) -> float:
    return (firm.acquisition + firm.implementation + firm.usage + firm.reorganization) / 4


def substitution_index(firm: Firm) -> float:
    return clip(
        0.12
        + 0.34 * firm.routine_task_share
        + 0.24 * firm.acquisition
        + 0.18 * firm.monitoring_intensity
        - 0.18 * firm.incumbent_training
    )


def augmentation_index(firm: Firm) -> float:
    return clip(
        0.10
        + 0.34 * firm.usage
        + 0.18 * firm.incumbent_training
        + 0.14 * firm.worker_trust
        + 0.10 * firm.manager_algorithm_trust
    )


def scale_index(firm: Firm) -> float:
    return clip(
        0.08
        + 0.26 * adoption_index(firm)
        + 0.18 * firm.management_quality
        + 0.16 * firm.data_readiness
        + 1.10 * firm.baseline_productivity_growth
    )


def organizational_redesign_index(firm: Firm) -> float:
    return clip(
        0.12
        + 0.34 * firm.reorganization
        + 0.18 * firm.implementation
        + 0.14 * firm.monitoring_intensity
        + 0.12 * abs(firm.new_hire_ai_training - firm.incumbent_training)
    )


def principal_agent_tension(firm: Firm) -> float:
    trust_gap = abs(firm.worker_trust - firm.manager_algorithm_trust)
    return clip(
        0.10
        + 0.26 * firm.replacement_concern
        + 0.20 * firm.monitoring_intensity
        + 0.18 * (1 - firm.human_override)
        + 0.14 * (1 - firm.transparency)
        + 0.12 * trust_gap
        - 0.10 * firm.perceived_fairness
    )


def mechanism_label(firm: Firm) -> str:
    substitution = substitution_index(firm)
    augmentation = augmentation_index(firm)
    redesign = organizational_redesign_index(firm)
    tension = principal_agent_tension(firm)
    if adoption_stage(firm) == "no_adoption":
        return "nonadopter_baseline"
    if tension >= 0.58:
        return "high_tension_adoption"
    if substitution >= augmentation + 0.10:
        return "substitution_or_hiring_around_incumbents"
    if augmentation >= substitution + 0.10 and firm.incumbent_training >= 0.50:
        return "incumbent_augmentation"
    if redesign >= 0.58:
        return "organizational_redesign"
    return "mixed_adoption_mechanism"


def coefficient_warning(firm: Firm) -> str:
    if firm.acquisition - firm.usage >= 0.22:
        return "acquisition_overstates_realized_use"
    if firm.new_hire_ai_training - firm.incumbent_training >= 0.22:
        return "skill_upgrading_may_bypass_incumbents"
    if firm.management_quality >= 0.70 and firm.data_readiness >= 0.70:
        return "adopter_selection_is_likely"
    if principal_agent_tension(firm) >= 0.58:
        return "attitudes_and_control_shape_usage"
    return "interpret_as_joint_technology_and_organization_effect"


def reproduced_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for firm in FIRMS:
        index = adoption_index(firm)
        ai_skill_share_post = clip(
            firm.baseline_ai_skill_share
            + 0.030 * firm.acquisition
            + 0.035 * firm.usage
            + 0.030 * firm.new_hire_ai_training
        )
        stem_share_post = clip(
            firm.baseline_stem_share
            + 0.020 * firm.implementation
            + 0.025 * firm.new_hire_ai_training
            + 0.015 * firm.incumbent_training
        )
        junior_share_post = clip(
            firm.baseline_junior_share
            + 0.025 * firm.new_hire_ai_training
            + 0.018 * firm.usage
            - 0.010 * firm.incumbent_training
        )
        manager_share_post = clip(
            firm.baseline_manager_share
            - 0.018 * firm.reorganization
            + 0.010 * firm.monitoring_intensity
        )
        employment_growth = (
            0.010
            + 0.045 * scale_index(firm)
            + 0.020 * augmentation_index(firm)
            - 0.030 * substitution_index(firm)
            - 0.010 * principal_agent_tension(firm)
        )
        rows.append(
            {
                "firm": firm.name,
                "sector": firm.sector,
                "adoption_year": firm.adoption_year if firm.adoption_year is not None else "not_observed",
                "adoption_stage": adoption_stage(firm),
                "baseline_employment": firm.baseline_employment,
                "baseline_ai_skill_share": round(firm.baseline_ai_skill_share, 3),
                "post_ai_skill_share": round(ai_skill_share_post, 3),
                "baseline_stem_share": round(firm.baseline_stem_share, 3),
                "post_stem_share": round(stem_share_post, 3),
                "baseline_junior_share": round(firm.baseline_junior_share, 3),
                "post_junior_share": round(junior_share_post, 3),
                "baseline_manager_share": round(firm.baseline_manager_share, 3),
                "post_manager_share": round(manager_share_post, 3),
                "adoption_index": round(index, 3),
                "usage_index": round(firm.usage, 3),
                "reorganization_index": round(firm.reorganization, 3),
                "employment_growth_pct": round(100 * employment_growth, 2),
            }
        )
    return rows


def diagnosis_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for firm in FIRMS:
        rows.append(
            {
                "firm": firm.name,
                "adoption_stage": adoption_stage(firm),
                "substitution_index": round(substitution_index(firm), 3),
                "augmentation_index": round(augmentation_index(firm), 3),
                "scale_index": round(scale_index(firm), 3),
                "organizational_redesign_index": round(organizational_redesign_index(firm), 3),
                "principal_agent_tension": round(principal_agent_tension(firm), 3),
                "incumbent_training": round(firm.incumbent_training, 3),
                "new_hire_ai_training": round(firm.new_hire_ai_training, 3),
                "mechanism_label": mechanism_label(firm),
                "coefficient_warning": coefficient_warning(firm),
            }
        )
    return rows


def attitude_transfer_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for firm in FIRMS:
        aversion = clip(
            0.58
            - 0.30 * firm.worker_trust
            - 0.18 * firm.manager_algorithm_trust
            - 0.14 * firm.perceived_fairness
            + 0.18 * firm.replacement_concern
            + 0.10 * firm.monitoring_intensity
            - 0.08 * firm.human_override
        )
        voluntary_usage = clip(
            0.12
            + 0.32 * firm.worker_trust
            + 0.24 * firm.manager_algorithm_trust
            + 0.18 * firm.transparency
            + 0.14 * firm.perceived_fairness
            - 0.18 * firm.replacement_concern
            - 0.10 * firm.monitoring_intensity
        )
        productivity_gain = (
            0.012
            + 0.050 * firm.usage
            + 0.030 * augmentation_index(firm)
            + 0.020 * firm.management_quality
            - 0.026 * principal_agent_tension(firm)
        )
        if aversion >= 0.48 and firm.replacement_concern >= 0.55:
            label = "replacement_concern_limits_acceptance"
        elif voluntary_usage >= 0.58 and productivity_gain >= 0.06:
            label = "high_trust_augmented_use"
        elif firm.manager_algorithm_trust < 0.42:
            label = "manager_algorithm_aversion"
        elif firm.monitoring_intensity >= 0.65 and firm.human_override <= 0.45:
            label = "control_and_monitoring_tension"
        else:
            label = "mixed_attitude_path"
        rows.append(
            {
                "firm": firm.name,
                "worker_trust": round(firm.worker_trust, 3),
                "manager_algorithm_trust": round(firm.manager_algorithm_trust, 3),
                "perceived_fairness": round(firm.perceived_fairness, 3),
                "replacement_concern": round(firm.replacement_concern, 3),
                "human_override": round(firm.human_override, 3),
                "monitoring_intensity": round(firm.monitoring_intensity, 3),
                "algorithm_aversion_index": round(aversion, 3),
                "predicted_voluntary_usage": round(voluntary_usage, 3),
                "usage_gap_vs_implementation": round(firm.implementation - firm.usage, 3),
                "predicted_productivity_gain_pct": round(100 * productivity_gain, 2),
                "attitude_label": label,
            }
        )
    return rows


def design_variant_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for arm in VIGNETTES:
        acceptance = clip(
            0.22
            + 0.24 * arm.transparency
            + 0.22 * arm.human_override
            + 0.20 * arm.performance_feedback
            - 0.20 * arm.replacement_risk
            - 0.14 * arm.monitoring_intensity
        )
        usage_intent = clip(
            0.18
            + 0.28 * acceptance
            + 0.22 * arm.performance_feedback
            + 0.12 * arm.transparency
            - 0.10 * arm.replacement_risk
        )
        rows.append(
            {
                "arm": arm.arm,
                "transparency": arm.transparency,
                "human_override": arm.human_override,
                "replacement_risk": arm.replacement_risk,
                "performance_feedback": arm.performance_feedback,
                "monitoring_intensity": arm.monitoring_intensity,
                "predicted_acceptance": round(acceptance, 3),
                "predicted_usage_intent": round(usage_intent, 3),
                "design_note": design_note(arm, acceptance),
            }
        )
    return rows


def design_note(arm: VignetteArm, acceptance: float) -> str:
    if arm.replacement_risk >= 0.70:
        return "tests_whether_performance_information_offsets_replacement_risk"
    if arm.transparency >= 0.70 and arm.human_override >= 0.70:
        return "tests_transparency_and_control_as_acceptance_mechanisms"
    if arm.monitoring_intensity >= 0.75:
        return "tests_monitoring_as_a_worker_control_friction"
    if acceptance >= 0.55:
        return "candidate_low_friction_encouragement_arm"
    return "baseline_or_mixed_mechanism_arm"


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
        lab_dir / "output" / "reproduced" / "firm_ai_adoption_workforce.csv",
        reproduced_rows(),
    )
    write_csv(
        lab_dir / "output" / "diagnosed" / "adoption_mechanism_diagnosis.csv",
        diagnosis_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "ai_attitude_transfer.csv",
        attitude_transfer_rows(),
    )
    write_csv(
        lab_dir / "output" / "transfer" / "attitude_design_variants.csv",
        design_variant_rows(),
    )

    note = (
        "Synthetic Week 4 firm-adoption lab complete. Outputs reproduce "
        "firm AI-adoption and workforce-composition logic, diagnose adoption "
        "mechanisms and principal-agent tensions, and transfer the design to "
        "worker and manager AI-attitude measurement.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
