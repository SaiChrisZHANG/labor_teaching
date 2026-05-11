from __future__ import annotations

import csv
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def binary_from_rate(index: int, rate: float) -> int:
    threshold = int(round(rate * 1000))
    return int((index * 41 + 29) % 1000 < threshold)


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def resume_audit_rows() -> list[dict[str, object]]:
    groups = [
        ("white_name_local_credential", 0.000, "local"),
        ("black_name_local_credential", -0.060, "local"),
        ("immigrant_name_local_credential", -0.045, "local"),
        ("immigrant_name_foreign_credential", -0.085, "foreign"),
    ]
    occupations = [
        ("administrative", 0.000),
        ("sales", -0.010),
        ("professional", 0.020),
    ]
    rows: list[dict[str, object]] = []
    for group_index, (group, group_penalty, credential_origin) in enumerate(groups):
        for resume in range(120):
            row_index = group_index * 120 + resume
            occupation, occupation_effect = occupations[(resume + group_index) % len(occupations)]
            resume_quality = "high" if (resume + 2 * group_index) % 5 in {0, 1} else "standard"
            quality_effect = 0.075 if resume_quality == "high" else 0.000
            neighborhood_signal = "disadvantaged" if (resume + group_index) % 4 == 0 else "neutral"
            neighborhood_effect = -0.030 if neighborhood_signal == "disadvantaged" else 0.000
            employer_sector = "public" if (resume + 3 * group_index) % 6 == 0 else "private"
            sector_effect = -0.006 if employer_sector == "public" else 0.000
            local_experience = 1 if credential_origin == "local" or resume % 3 != 0 else 0
            experience_effect = 0.020 * local_experience
            callback_rate = clamp(
                0.205
                + group_penalty
                + quality_effect
                + neighborhood_effect
                + occupation_effect
                + sector_effect
                + experience_effect,
                0.045,
                0.420,
            )
            rows.append(
                {
                    "application_id": f"wk6-app-{row_index + 1:04d}",
                    "group_signal": group,
                    "credential_origin": credential_origin,
                    "resume_quality": resume_quality,
                    "local_experience": local_experience,
                    "neighborhood_signal": neighborhood_signal,
                    "occupation": occupation,
                    "employer_sector": employer_sector,
                    "callback": binary_from_rate(row_index + 31, callback_rate),
                }
            )
    return rows


def barrier_rows() -> list[dict[str, object]]:
    return [
        {
            "case_id": "race_name_resume_audit",
            "anchor": "Bertrand-Mullainathan 2004",
            "category_signal": "race-coded name",
            "institutional_gate": "first-stage hiring callback",
            "expected_barrier": "belief_based_screening",
            "evidence_level": "micro",
            "observed_margin": "callback access",
            "week_boundary": "Week 6 hierarchy",
        },
        {
            "case_id": "skilled_immigrant_foreign_credentials",
            "anchor": "Oreopoulos 2011",
            "category_signal": "immigrant background and foreign credential",
            "institutional_gate": "resume screening and credential recognition",
            "expected_barrier": "credential_recognition",
            "evidence_level": "micro",
            "observed_margin": "interview access and occupational matching",
            "week_boundary": "Week 6 hierarchy",
        },
        {
            "case_id": "caste_network_occupation_persistence",
            "anchor": "Munshi-Rosenzweig 2006",
            "category_signal": "caste network",
            "institutional_gate": "schooling, referrals, and occupation choice",
            "expected_barrier": "network_based_access",
            "evidence_level": "meso",
            "observed_margin": "occupation persistence and mobility",
            "week_boundary": "Week 6 hierarchy",
        },
        {
            "case_id": "collaborative_caste_contact",
            "anchor": "Lowe 2021",
            "category_signal": "caste category in designed interaction",
            "institutional_gate": "team assignment and contact structure",
            "expected_barrier": "contact_integration_design",
            "evidence_level": "micro",
            "observed_margin": "cooperation and social distance",
            "week_boundary": "Week 6 hierarchy",
        },
        {
            "case_id": "federal_employment_segregation",
            "anchor": "Aneja-Xu 2020",
            "category_signal": "race in public employment",
            "institutional_gate": "public-sector assignment and promotion",
            "expected_barrier": "legal_public_rule",
            "evidence_level": "meso",
            "observed_margin": "public jobs and earnings",
            "week_boundary": "Week 6 hierarchy",
        },
        {
            "case_id": "segregated_commuting_zone",
            "anchor": "local governance extension",
            "category_signal": "neighborhood and group residence",
            "institutional_gate": "commuting, safety, and local enforcement",
            "expected_barrier": "spatial_local_governance",
            "evidence_level": "meso",
            "observed_margin": "job access and protection",
            "week_boundary": "Week 6 hierarchy",
        },
        {
            "case_id": "race_gender_talent_misallocation",
            "anchor": "Hsieh-Hurst-Jones-Klenow 2019",
            "category_signal": "race and gender barriers",
            "institutional_gate": "occupation entry and talent allocation",
            "expected_barrier": "macro_misallocation",
            "evidence_level": "macro",
            "observed_margin": "aggregate output and occupation shares",
            "week_boundary": "Week 6 hierarchy",
        },
        {
            "case_id": "family_role_conduct_boundary",
            "anchor": "Week 5 boundary case",
            "category_signal": "gendered family-role expectation",
            "institutional_gate": "acceptable conduct and labor supply",
            "expected_barrier": "conduct_norm_boundary",
            "evidence_level": "micro",
            "observed_margin": "work entry and hours",
            "week_boundary": "Week 5 conduct norm",
        },
    ]


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "design_id": "resume_audit_race_names",
            "anchor": "Bertrand-Mullainathan 2004",
            "variation": "randomized race-coded names on otherwise similar resumes",
            "unit": "application-employer pair",
            "observed_margin": "callbacks",
            "expected_object": "audit_differential_treatment",
        },
        {
            "design_id": "immigrant_credential_resume_experiment",
            "anchor": "Oreopoulos 2011",
            "variation": "foreign name, foreign credential, and local experience signals vary across resumes",
            "unit": "application-employer pair",
            "observed_margin": "callbacks and interview access",
            "expected_object": "credential_resume_screening",
        },
        {
            "design_id": "caste_network_schooling_occupation",
            "anchor": "Munshi-Rosenzweig 2006",
            "variation": "caste-linked networks and community-specific transitions",
            "unit": "student, worker, caste network",
            "observed_margin": "schooling, occupation choice, mobility",
            "expected_object": "network_occupation_persistence",
        },
        {
            "design_id": "collaborative_caste_contact_experiment",
            "anchor": "Lowe 2021",
            "variation": "randomized collaborative or adversarial contact across caste groups",
            "unit": "participant pair or group",
            "observed_margin": "cooperation and social distance",
            "expected_object": "contact_integration",
        },
        {
            "design_id": "public_employment_segregation_shock",
            "anchor": "Aneja-Xu 2020",
            "variation": "federal-government segregation under Woodrow Wilson",
            "unit": "public employee or agency",
            "observed_margin": "public employment, job ladder, earnings",
            "expected_object": "public_rule_state_action",
        },
        {
            "design_id": "occupation_barriers_talent_allocation",
            "anchor": "Hsieh-Hurst-Jones-Klenow 2019",
            "variation": "race and gender barriers to occupations decline over time",
            "unit": "group-occupation-time cell",
            "observed_margin": "occupation shares, output, growth",
            "expected_object": "macro_talent_misallocation",
        },
        {
            "design_id": "stratification_economics_synthesis",
            "anchor": "Darity 2022",
            "variation": "intergroup position and possessions reproduce inequality across domains",
            "unit": "group and institutional domain",
            "observed_margin": "intergroup inequality and labor-market position",
            "expected_object": "stratification_synthesis",
        },
    ]


def main() -> None:
    write_rows(
        LAB / "original" / "reduced" / "resume_audit_synthetic.csv",
        [
            "application_id",
            "group_signal",
            "credential_origin",
            "resume_quality",
            "local_experience",
            "neighborhood_signal",
            "occupation",
            "employer_sector",
            "callback",
        ],
        resume_audit_rows(),
    )
    write_rows(
        LAB / "original" / "reduced" / "hierarchy_barriers_synthetic.csv",
        [
            "case_id",
            "anchor",
            "category_signal",
            "institutional_gate",
            "expected_barrier",
            "evidence_level",
            "observed_margin",
            "week_boundary",
        ],
        barrier_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "hierarchy_designs_synthetic.csv",
        ["design_id", "anchor", "variation", "unit", "observed_margin", "expected_object"],
        transfer_rows(),
    )
    print("Wrote Week 6 synthetic hierarchy data.")


if __name__ == "__main__":
    main()
