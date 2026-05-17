from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


BRANCHES = [
    {"branch": "Infantry", "capacity": 20, "hard_to_staff": 0.70, "training_intensity": 0.78},
    {"branch": "Cyber", "capacity": 18, "hard_to_staff": 0.58, "training_intensity": 0.92},
    {"branch": "Logistics", "capacity": 22, "hard_to_staff": 0.44, "training_intensity": 0.62},
    {"branch": "Engineering", "capacity": 20, "hard_to_staff": 0.53, "training_intensity": 0.81},
    {"branch": "Intelligence", "capacity": 18, "hard_to_staff": 0.49, "training_intensity": 0.86},
    {"branch": "Medical Service", "capacity": 22, "hard_to_staff": 0.38, "training_intensity": 0.69},
]

SCHOOLS = [
    {"school": "North High", "capacity": 10, "hard_to_staff": 0.34, "student_need": 0.42},
    {"school": "East Middle", "capacity": 10, "hard_to_staff": 0.71, "student_need": 0.78},
    {"school": "Riverside Elementary", "capacity": 10, "hard_to_staff": 0.63, "student_need": 0.72},
    {"school": "Central High", "capacity": 10, "hard_to_staff": 0.41, "student_need": 0.50},
    {"school": "Hilltop Middle", "capacity": 10, "hard_to_staff": 0.56, "student_need": 0.66},
    {"school": "South Elementary", "capacity": 10, "hard_to_staff": 0.77, "student_need": 0.83},
    {"school": "West High", "capacity": 10, "hard_to_staff": 0.47, "student_need": 0.54},
    {"school": "Lakeside K8", "capacity": 10, "hard_to_staff": 0.60, "student_need": 0.70},
]


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def safe_mean(values: list[float]) -> float:
    return mean(values) if values else 0.0


def branch_affinity(officer_number: int, branch_index: int) -> float:
    return clamp(0.18 + ((officer_number * (branch_index + 5) + branch_index * 17) % 80) / 100)


def school_affinity(teacher_number: int, school_index: int) -> float:
    return clamp(0.20 + ((teacher_number * (school_index + 3) + school_index * 13) % 75) / 100)


def make_officers() -> list[dict[str, object]]:
    officers: list[dict[str, object]] = []

    for officer_number in range(1, 121):
        performance = clamp(0.36 + ((officer_number * 17) % 60) / 100)
        leadership = clamp(0.34 + ((officer_number * 19) % 62) / 100)
        outside_option = clamp(0.24 + ((officer_number * 7) % 58) / 100)
        mission_commitment = clamp(0.30 + ((officer_number * 11) % 63) / 100)
        mobility_preference = clamp(0.28 + ((officer_number * 23) % 61) / 100)
        service_commitment_interest = clamp(0.25 + ((officer_number * 29) % 64) / 100)

        affinities = {
            branch["branch"]: branch_affinity(officer_number, branch_index)
            for branch_index, branch in enumerate(BRANCHES)
        }
        priorities = {
            branch["branch"]: clamp(
                0.18
                + 0.36 * performance
                + 0.24 * leadership
                + 0.12 * affinities[branch["branch"]]
                + 0.10 * service_commitment_interest
                + ((officer_number + branch_index * 5) % 7) / 100
            )
            for branch_index, branch in enumerate(BRANCHES)
        }
        preferences = sorted(
            [branch["branch"] for branch in BRANCHES],
            key=lambda branch_name: (
                0.52 * affinities[branch_name]
                + 0.18 * mobility_preference
                + 0.14 * mission_commitment
                - 0.10 * next(item["hard_to_staff"] for item in BRANCHES if item["branch"] == branch_name)
            ),
            reverse=True,
        )

        officers.append(
            {
                "officer_id": f"O{officer_number:03d}",
                "performance_index": round(performance, 3),
                "leadership_index": round(leadership, 3),
                "outside_option_index": round(outside_option, 3),
                "mission_commitment_index": round(mission_commitment, 3),
                "mobility_preference_index": round(mobility_preference, 3),
                "service_commitment_interest": round(service_commitment_interest, 3),
                "preferences": preferences,
                "priority_scores": priorities,
                "affinity_scores": affinities,
            }
        )

    return officers


def deferred_acceptance_assignments(officers: list[dict[str, object]]) -> dict[str, str]:
    capacities = {branch["branch"]: int(branch["capacity"]) for branch in BRANCHES}
    proposals_used = {str(officer["officer_id"]): 0 for officer in officers}
    officer_by_id = {str(officer["officer_id"]): officer for officer in officers}
    tentative: dict[str, list[str]] = {branch["branch"]: [] for branch in BRANCHES}
    free = [str(officer["officer_id"]) for officer in officers]

    while free:
        next_free: list[str] = []
        for officer_id in free:
            officer = officer_by_id[officer_id]
            preferences = list(officer["preferences"])
            proposal_index = proposals_used[officer_id]
            if proposal_index >= len(preferences):
                continue
            branch_name = str(preferences[proposal_index])
            proposals_used[officer_id] += 1
            tentative[branch_name].append(officer_id)

        for branch_name, candidates in tentative.items():
            priority_sorted = sorted(
                candidates,
                key=lambda candidate_id: float(officer_by_id[candidate_id]["priority_scores"][branch_name]),
                reverse=True,
            )
            accepted = priority_sorted[: capacities[branch_name]]
            rejected = priority_sorted[capacities[branch_name] :]
            tentative[branch_name] = accepted
            next_free.extend(rejected)
        free = next_free

    return {
        officer_id: branch_name
        for branch_name, candidates in tentative.items()
        for officer_id in candidates
    }


def manager_directed_assignments(officers: list[dict[str, object]]) -> dict[str, str]:
    remaining = {branch["branch"]: int(branch["capacity"]) for branch in BRANCHES}
    assignments: dict[str, str] = {}
    sorted_officers = sorted(
        officers,
        key=lambda officer: (
            0.42 * float(officer["performance_index"])
            + 0.33 * float(officer["leadership_index"])
            + 0.25 * float(officer["mission_commitment_index"])
        ),
        reverse=True,
    )

    for officer in sorted_officers:
        best_branch = None
        best_score = -1.0
        preferences = list(officer["preferences"])
        for branch in BRANCHES:
            branch_name = branch["branch"]
            if remaining[branch_name] <= 0:
                continue
            preference_rank = preferences.index(branch_name) + 1
            manager_score = (
                0.47 * float(officer["priority_scores"][branch_name])
                + 0.30 * float(branch["hard_to_staff"])
                + 0.15 * float(branch["training_intensity"])
                - 0.03 * preference_rank
            )
            if manager_score > best_score:
                best_branch = branch_name
                best_score = manager_score
        if best_branch is None:
            raise ValueError("No branch capacity remained for assignment.")
        assignments[str(officer["officer_id"])] = str(best_branch)
        remaining[str(best_branch)] -= 1

    return assignments


def branch_lookup(branch_name: str) -> dict[str, object]:
    return next(branch for branch in BRANCHES if branch["branch"] == branch_name)


def assignment_outcomes(
    officers: list[dict[str, object]],
    assignments: dict[str, str],
    mechanism: str,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for officer in officers:
        officer_id = str(officer["officer_id"])
        branch_name = assignments[officer_id]
        branch = branch_lookup(branch_name)
        preferences = list(officer["preferences"])
        preference_rank = preferences.index(branch_name) + 1
        priority_score = float(officer["priority_scores"][branch_name])
        affinity_score = float(officer["affinity_scores"][branch_name])
        outside_option = float(officer["outside_option_index"])
        mission_commitment = float(officer["mission_commitment_index"])
        mobility_preference = float(officer["mobility_preference_index"])
        service_interest = float(officer["service_commitment_interest"])
        leadership = float(officer["leadership_index"])
        training_intensity = float(branch["training_intensity"])
        hard_to_staff = float(branch["hard_to_staff"])

        training_value = clamp(0.25 + 0.32 * affinity_score + 0.24 * training_intensity + 0.10 * service_interest)
        internal_mobility_value = clamp(
            0.20 + 0.28 * ((6 - preference_rank) / 5) + 0.24 * mobility_preference + 0.14 * training_value - 0.10 * outside_option
        )
        predicted_retention = clamp(
            0.34
            + 0.08 * ((6 - preference_rank) / 5)
            + 0.15 * priority_score
            + 0.13 * mission_commitment
            + 0.11 * service_interest
            + 0.08 * internal_mobility_value
            - 0.12 * outside_option
        )
        promotion_readiness = clamp(0.24 + 0.24 * priority_score + 0.20 * training_value + 0.18 * leadership + 0.10 * predicted_retention)
        public_staffing_value = clamp(0.18 + 0.34 * hard_to_staff + 0.24 * priority_score + 0.18 * mission_commitment)
        worker_welfare_index = clamp(
            0.22
            + 0.18 * ((6 - preference_rank) / 5)
            + 0.18 * training_value
            + 0.16 * internal_mobility_value
            + 0.12 * predicted_retention
            + 0.08 * service_interest
            - 0.10 * outside_option
        )
        transfer_risk = clamp(0.64 - 0.20 * ((6 - preference_rank) / 5) - 0.16 * predicted_retention + 0.12 * outside_option)

        rows.append(
            {
                "mechanism": mechanism,
                "officer_id": officer_id,
                "assigned_branch": branch_name,
                "preference_rank": preference_rank,
                "top_three_assignment": int(preference_rank <= 3),
                "priority_alignment_index": round(priority_score, 3),
                "hard_to_staff_index": round(hard_to_staff, 3),
                "training_value_index": round(training_value, 3),
                "internal_mobility_value_index": round(internal_mobility_value, 3),
                "predicted_retention_index": round(predicted_retention, 3),
                "promotion_readiness_index": round(promotion_readiness, 3),
                "public_staffing_value_index": round(public_staffing_value, 3),
                "worker_welfare_index": round(worker_welfare_index, 3),
                "transfer_risk_index": round(transfer_risk, 3),
                "outside_option_index": round(outside_option, 3),
            }
        )

    return rows


def summarize_assignment(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["mechanism"])].append(row)

    output: list[dict[str, object]] = []
    for mechanism in ("deferred_acceptance", "manager_directed"):
        group = grouped[mechanism]
        output.append(
            {
                "mechanism": mechanism,
                "officers": len(group),
                "mean_preference_rank": round(safe_mean([float(row["preference_rank"]) for row in group]), 4),
                "top_three_assignment_share": round(safe_mean([float(row["top_three_assignment"]) for row in group]), 4),
                "mean_priority_alignment_index": round(safe_mean([float(row["priority_alignment_index"]) for row in group]), 4),
                "mean_hard_to_staff_index": round(safe_mean([float(row["hard_to_staff_index"]) for row in group]), 4),
                "mean_public_staffing_value_index": round(safe_mean([float(row["public_staffing_value_index"]) for row in group]), 4),
                "mean_training_value_index": round(safe_mean([float(row["training_value_index"]) for row in group]), 4),
                "mean_internal_mobility_value_index": round(safe_mean([float(row["internal_mobility_value_index"]) for row in group]), 4),
                "mean_predicted_retention_index": round(safe_mean([float(row["predicted_retention_index"]) for row in group]), 4),
                "mean_promotion_readiness_index": round(safe_mean([float(row["promotion_readiness_index"]) for row in group]), 4),
                "mean_worker_welfare_index": round(safe_mean([float(row["worker_welfare_index"]) for row in group]), 4),
                "mean_transfer_risk_index": round(safe_mean([float(row["transfer_risk_index"]) for row in group]), 4),
            }
        )
    return output


def metric_difference(summary: list[dict[str, object]], metric: str) -> float:
    by_mechanism = {str(row["mechanism"]): row for row in summary}
    return round(float(by_mechanism["deferred_acceptance"][metric]) - float(by_mechanism["manager_directed"][metric]), 4)


def design_diagnostics(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {
            "design_object": "preference_alignment",
            "observed_margin": "mean preference rank and top-three assignment share",
            "deferred_acceptance_minus_manager_directed": metric_difference(summary, "top_three_assignment_share"),
            "identification_design": "compare mechanism-assigned synthetic markets with identical preferences and capacities",
            "remaining_threat": "preference ranks do not reveal training quality, manager information, or public staffing value",
            "welfare_object": "worker preference satisfaction and assignment legitimacy",
        },
        {
            "design_object": "priority_alignment",
            "observed_margin": "assigned branch priority index",
            "deferred_acceptance_minus_manager_directed": metric_difference(summary, "mean_priority_alignment_index"),
            "identification_design": "hold officer traits fixed and alter assignment rule",
            "remaining_threat": "priority scores may encode organizational objectives imperfectly",
            "welfare_object": "organizational fit and public mission value",
        },
        {
            "design_object": "hard_to_staff_units",
            "observed_margin": "mean hard-to-staff index of assigned branch",
            "deferred_acceptance_minus_manager_directed": metric_difference(summary, "mean_hard_to_staff_index"),
            "identification_design": "compare staffing burden under preference-sensitive and manager-directed rules",
            "remaining_threat": "filling hard-to-staff units may reduce retention or worker welfare",
            "welfare_object": "public staffing needs and service coverage",
        },
        {
            "design_object": "career_ladder_and_training",
            "observed_margin": "training value, promotion readiness, and internal mobility",
            "deferred_acceptance_minus_manager_directed": metric_difference(summary, "mean_training_value_index"),
            "identification_design": "map assignments into synthetic training and ladder values",
            "remaining_threat": "later promotions depend on unobserved supervisors, peer effects, and vacancies",
            "welfare_object": "dynamic career formation",
        },
        {
            "design_object": "retention_and_exit",
            "observed_margin": "predicted retention and transfer risk",
            "deferred_acceptance_minus_manager_directed": metric_difference(summary, "mean_predicted_retention_index"),
            "identification_design": "combine assignment quality, outside options, and service interest",
            "remaining_threat": "outside labor-market shocks and private-sector offers are not randomized",
            "welfare_object": "worker continuation, staffing stability, and exit risk",
        },
    ]


def officer_preference_rows(officers: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for officer in officers:
        preferences = list(officer["preferences"])
        row = {
            "officer_id": officer["officer_id"],
            "performance_index": officer["performance_index"],
            "leadership_index": officer["leadership_index"],
            "outside_option_index": officer["outside_option_index"],
            "mission_commitment_index": officer["mission_commitment_index"],
            "mobility_preference_index": officer["mobility_preference_index"],
            "service_commitment_interest": officer["service_commitment_interest"],
        }
        for rank, branch_name in enumerate(preferences, start=1):
            row[f"preference_{rank}"] = branch_name
        rows.append(row)
    return rows


def teacher_public_service_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    remaining = {school["school"]: int(school["capacity"]) for school in SCHOOLS}

    teachers: list[dict[str, object]] = []
    for teacher_number in range(1, 81):
        subject_shortage = 1 if teacher_number % 4 in (0, 1) else 0
        mission_value = clamp(0.28 + ((teacher_number * 11) % 64) / 100)
        outside_option = clamp(0.20 + ((teacher_number * 13) % 62) / 100)
        local_tie = clamp(0.22 + ((teacher_number * 17) % 60) / 100)
        novice = 1 if teacher_number <= 48 else 0
        affinities = {
            school["school"]: school_affinity(teacher_number, school_index)
            for school_index, school in enumerate(SCHOOLS)
        }
        preferences = sorted(
            [school["school"] for school in SCHOOLS],
            key=lambda school_name: 0.55 * affinities[school_name] + 0.22 * local_tie - 0.08 * outside_option,
            reverse=True,
        )
        teachers.append(
            {
                "teacher_id": f"T{teacher_number:03d}",
                "subject_shortage": subject_shortage,
                "mission_value_index": round(mission_value, 3),
                "outside_option_index": round(outside_option, 3),
                "local_tie_index": round(local_tie, 3),
                "novice_teacher": novice,
                "preferences": preferences,
                "affinity_scores": affinities,
            }
        )

    sorted_teachers = sorted(
        teachers,
        key=lambda teacher: 0.42 * int(teacher["subject_shortage"]) + 0.36 * float(teacher["mission_value_index"]) - 0.16 * float(teacher["outside_option_index"]),
        reverse=True,
    )

    for teacher in sorted_teachers:
        best_school = None
        best_score = -1.0
        preferences = list(teacher["preferences"])
        for school in SCHOOLS:
            school_name = school["school"]
            if remaining[school_name] <= 0:
                continue
            preference_rank = preferences.index(school_name) + 1
            score = (
                0.36 * float(school["student_need"])
                + 0.28 * float(school["hard_to_staff"])
                + 0.16 * int(teacher["subject_shortage"])
                + 0.14 * float(teacher["mission_value_index"])
                - 0.025 * preference_rank
            )
            if score > best_score:
                best_score = score
                best_school = school_name
        if best_school is None:
            raise ValueError("No school capacity remained for assignment.")
        remaining[best_school] -= 1

        school = next(item for item in SCHOOLS if item["school"] == best_school)
        preference_rank = preferences.index(best_school) + 1
        entry_probability = clamp(0.42 + 0.18 * float(teacher["mission_value_index"]) + 0.10 * int(teacher["subject_shortage"]) - 0.14 * float(teacher["outside_option_index"]))
        retention_probability = clamp(
            0.38
            + 0.13 * ((8 - preference_rank) / 7)
            + 0.14 * float(teacher["mission_value_index"])
            + 0.12 * float(teacher["local_tie_index"])
            + 0.08 * float(school["student_need"])
            - 0.12 * float(teacher["outside_option_index"])
        )
        service_output = clamp(
            0.25
            + 0.26 * float(school["student_need"])
            + 0.20 * int(teacher["subject_shortage"])
            + 0.18 * float(teacher["mission_value_index"])
            + 0.10 * retention_probability
        )
        exit_risk = clamp(0.66 - 0.18 * retention_probability + 0.16 * float(teacher["outside_option_index"]) - 0.08 * float(teacher["local_tie_index"]))

        rows.append(
            {
                "teacher_id": teacher["teacher_id"],
                "assigned_school": best_school,
                "preference_rank": preference_rank,
                "hard_to_staff_index": round(float(school["hard_to_staff"]), 3),
                "student_need_index": round(float(school["student_need"]), 3),
                "subject_shortage": teacher["subject_shortage"],
                "novice_teacher": teacher["novice_teacher"],
                "mission_value_index": teacher["mission_value_index"],
                "outside_option_index": teacher["outside_option_index"],
                "entry_probability": round(entry_probability, 3),
                "retention_probability": round(retention_probability, 3),
                "service_output_index": round(service_output, 3),
                "exit_risk_index": round(exit_risk, 3),
            }
        )

    return rows


def public_sector_entry_exit_diagnostics(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    high_outside = [row for row in rows if float(row["outside_option_index"]) >= 0.55]
    low_outside = [row for row in rows if float(row["outside_option_index"]) < 0.55]
    hard_to_staff = [row for row in rows if float(row["hard_to_staff_index"]) >= 0.60]
    other = [row for row in rows if float(row["hard_to_staff_index"]) < 0.60]

    return [
        {
            "diagnostic": "public_private_outside_options",
            "comparison": "high outside option teachers minus lower outside option teachers",
            "entry_probability_difference": round(
                safe_mean([float(row["entry_probability"]) for row in high_outside]) - safe_mean([float(row["entry_probability"]) for row in low_outside]),
                4,
            ),
            "retention_probability_difference": round(
                safe_mean([float(row["retention_probability"]) for row in high_outside]) - safe_mean([float(row["retention_probability"]) for row in low_outside]),
                4,
            ),
            "interpretation": "outside options change who enters and who remains in public-service work",
        },
        {
            "diagnostic": "hard_to_staff_public_objective",
            "comparison": "hard-to-staff schools minus other schools",
            "entry_probability_difference": round(
                safe_mean([float(row["entry_probability"]) for row in hard_to_staff]) - safe_mean([float(row["entry_probability"]) for row in other]),
                4,
            ),
            "retention_probability_difference": round(
                safe_mean([float(row["retention_probability"]) for row in hard_to_staff]) - safe_mean([float(row["retention_probability"]) for row in other]),
                4,
            ),
            "interpretation": "public staffing goals can conflict with retention and preference satisfaction",
        },
    ]


def ladder_training_rows(assignment_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in assignment_rows:
        ladder_group = "high_outside_option" if float(row["outside_option_index"]) >= 0.55 else "lower_outside_option"
        grouped[(str(row["mechanism"]), ladder_group)].append(row)

    output: list[dict[str, object]] = []
    for mechanism in ("deferred_acceptance", "manager_directed"):
        for ladder_group in ("high_outside_option", "lower_outside_option"):
            group = grouped[(mechanism, ladder_group)]
            output.append(
                {
                    "mechanism": mechanism,
                    "outside_option_group": ladder_group,
                    "officers": len(group),
                    "mean_training_value_index": round(safe_mean([float(row["training_value_index"]) for row in group]), 4),
                    "mean_promotion_readiness_index": round(safe_mean([float(row["promotion_readiness_index"]) for row in group]), 4),
                    "mean_internal_mobility_value_index": round(safe_mean([float(row["internal_mobility_value_index"]) for row in group]), 4),
                    "mean_transfer_risk_index": round(safe_mean([float(row["transfer_risk_index"]) for row in group]), 4),
                    "teaching_point": "Job ladders and on-the-job search mediate the long-run welfare effect of initial assignment.",
                }
            )
    return output


def transfer_rows() -> list[dict[str, object]]:
    return [
        {
            "setting": "army_officer_branching",
            "rule": "deferred-acceptance-style branch assignment with priorities",
            "labor_margin": "preference rank, priority alignment, retention, training value",
            "counterfactual_rule": "manager-directed assignment with stronger staffing weights",
            "data_requirement": "preference lists, branch capacities, priorities, assignments, later retention and promotion",
            "welfare_object": "officer welfare, organizational staffing, training, and career progression",
            "main_threat": "manager communication and unobserved branch information can affect both rankings and outcomes",
        },
        {
            "setting": "teacher_or_public_service_placement",
            "rule": "centralized placement with school priorities and worker preferences",
            "labor_margin": "school match, hard-to-staff fill, retention, service output",
            "counterfactual_rule": "decentralized placement or older priority rule",
            "data_requirement": "teacher preferences, school priorities, assignments, vacancies, retention, student or service outcomes",
            "welfare_object": "worker welfare, school staffing, equity, and public-service quality",
            "main_threat": "assignment gains may reflect selection into the applicant pool rather than rule effects",
        },
        {
            "setting": "public_sector_recruitment_contract",
            "rule": "performance contract, mission bonus, or service commitment at entry",
            "labor_margin": "application, acceptance, effort, retention, exit",
            "counterfactual_rule": "standard civil-service contract",
            "data_requirement": "applicant pool, randomized or quasi-random contract terms, post-entry outcomes",
            "welfare_object": "selection, effort, worker risk, and public output",
            "main_threat": "contract terms can change both who enters and how selected workers behave",
        },
        {
            "setting": "internal_talent_market",
            "rule": "internal job bidding, transfer, or promotion matching rule",
            "labor_margin": "internal applications, transfers, promotions, retention",
            "counterfactual_rule": "managerial discretion or seniority-only reassignment",
            "data_requirement": "internal vacancies, worker bids, manager rankings, assignments, performance, exits",
            "welfare_object": "mismatch repair, promotion equity, productivity, and worker continuation",
            "main_threat": "manager discretion may contain private information or favoritism",
        },
        {
            "setting": "public_private_exit_margin",
            "rule": "pay scale, pension vesting, transfer right, or promotion ladder",
            "labor_margin": "public-sector entry, retention, transfer, private-sector exit",
            "counterfactual_rule": "old compensation or mobility rule",
            "data_requirement": "linked worker histories across public and private employers",
            "welfare_object": "public staffing stability, worker option value, and life-cycle career choice",
            "main_threat": "private labor-market shocks can confound public-sector rule effects",
        },
    ]


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
    officers = make_officers()
    da_assignments = deferred_acceptance_assignments(officers)
    manager_assignments = manager_directed_assignments(officers)
    assignment_rows = assignment_outcomes(officers, da_assignments, "deferred_acceptance")
    assignment_rows.extend(assignment_outcomes(officers, manager_assignments, "manager_directed"))
    assignment_summary = summarize_assignment(assignment_rows)
    teacher_rows = teacher_public_service_rows()

    write_csv(lab_dir / "original" / "reduced" / "army_officer_preferences_synthetic.csv", officer_preference_rows(officers))
    write_csv(lab_dir / "original" / "reduced" / "army_assignment_outcomes_synthetic.csv", assignment_rows)
    write_csv(lab_dir / "original" / "reduced" / "public_service_assignment_synthetic.csv", teacher_rows)
    write_csv(lab_dir / "output" / "reproduced" / "army_assignment_summary.csv", assignment_summary)
    write_csv(lab_dir / "output" / "diagnosed" / "design_diagnostics.csv", design_diagnostics(assignment_summary))
    write_csv(lab_dir / "output" / "diagnosed" / "ladders_training_mobility.csv", ladder_training_rows(assignment_rows))
    write_csv(lab_dir / "output" / "diagnosed" / "public_sector_entry_exit_diagnostics.csv", public_sector_entry_exit_diagnostics(teacher_rows))
    write_csv(lab_dir / "output" / "transfer" / "public_service_design_transfer.csv", transfer_rows())

    note = (
        "Synthetic Week 5 professional/public-sector design lab complete. "
        "Outputs compare deferred-acceptance-style and manager-directed Army assignment, "
        "diagnose staffing, career-ladder, training, retention, and outside-option margins, "
        "and transfer the design architecture to teacher placement, public-service recruitment, "
        "internal talent markets, and public-sector entry/exit.\n"
    )
    note_path = lab_dir / "output" / "reproduced" / "reproduction_note.txt"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8")
    print(note.strip())


if __name__ == "__main__":
    main()
