"""Create deterministic synthetic data for the Week 14 LLM workflow lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

SECTORS = ["health", "manufacturing", "technology", "public", "retail", "education"]
REGIONS = ["Northeast", "Midwest", "South", "West"]
OCCUPATIONS = ["analysis", "care", "production", "administration", "customer", "operations"]

SKILL_GAP_PHRASES = [
    "lacks Python",
    "missing SQL",
    "needs EHR",
    "training required",
    "upskilling required",
    "needs forklift",
    "not familiar with dashboards",
    "missing equipment",
]

CREDENTIAL_GAP_PHRASES = [
    "license not held",
    "license pending",
    "certification missing",
    "credential missing",
    "degree requirement unmet",
    "clearance pending",
    "certification not current",
    "permit not current",
]

SCHEDULE_GAP_PHRASES = [
    "schedule conflict",
    "available only mornings",
    "cannot work nights",
    "onsite conflict",
    "childcare conflict",
    "transportation conflict",
    "weekend restriction",
]

SUPPORT_PHRASES = [
    "meets required credential",
    "credential verified",
    "completed onboarding",
    "ready for placement",
    "skills aligned",
    "schedule aligned",
    "license verified",
    "no training barrier",
]

AMBIGUOUS_PHRASES = [
    "could benefit from coaching",
    "transitioning from adjacent role",
    "some exposure",
    "partial fit",
    "informal experience",
    "may need support",
]


def choose(rng: np.random.Generator, values: list[str], low: int, high: int) -> list[str]:
    count = int(rng.integers(low, high + 1))
    return list(rng.choice(values, size=count, replace=False))


def make_source_records() -> pd.DataFrame:
    rng = np.random.default_rng(1414)
    sector_shift = {
        "health": 0.18,
        "manufacturing": 0.16,
        "technology": 0.10,
        "public": 0.04,
        "retail": 0.08,
        "education": 0.02,
    }
    occupation_shift = {
        "analysis": 0.10,
        "care": 0.20,
        "production": 0.23,
        "administration": 0.04,
        "customer": 0.08,
        "operations": 0.14,
    }
    titles = {
        "analysis": ["data analyst", "policy analyst", "benefits analyst"],
        "care": ["care coordinator", "clinic scheduler", "patient support specialist"],
        "production": ["production technician", "warehouse lead", "equipment operator"],
        "administration": ["records manager", "program assistant", "grants coordinator"],
        "customer": ["service representative", "client support lead", "intake specialist"],
        "operations": ["operations planner", "logistics coordinator", "program operations associate"],
    }

    rows: list[dict[str, object]] = []
    for doc_id in range(1, 181):
        sector = str(rng.choice(SECTORS))
        region = str(rng.choice(REGIONS))
        occupation_group = str(rng.choice(OCCUPATIONS))
        year = int(rng.choice([2022, 2023, 2024, 2025], p=[0.18, 0.28, 0.30, 0.24]))
        document_type = str(rng.choice(["job-match memo", "resume screen", "case review"], p=[0.42, 0.38, 0.20]))
        base = 0.18 + sector_shift[sector] + occupation_shift[occupation_group] + 0.03 * (region == "South")
        benchmark_mismatch = int(rng.random() < min(base, 0.78))

        if benchmark_mismatch:
            gap_type = str(rng.choice(["skill_gap", "credential_gap", "schedule_gap"], p=[0.43, 0.35, 0.22]))
            if gap_type == "skill_gap":
                evidence = choose(rng, SKILL_GAP_PHRASES, 1, 2)
            elif gap_type == "credential_gap":
                evidence = choose(rng, CREDENTIAL_GAP_PHRASES, 1, 2)
            else:
                evidence = choose(rng, SCHEDULE_GAP_PHRASES, 1, 2)
            if rng.random() < 0.22:
                evidence += choose(rng, AMBIGUOUS_PHRASES, 1, 1)
        else:
            gap_type = "none"
            evidence = choose(rng, SUPPORT_PHRASES, 1, 3)
            if rng.random() < 0.14:
                evidence += choose(rng, SKILL_GAP_PHRASES + CREDENTIAL_GAP_PHRASES, 2, 2)
            if rng.random() < 0.18:
                evidence += choose(rng, AMBIGUOUS_PHRASES, 1, 1)

        if benchmark_mismatch and rng.random() < 0.16:
            evidence += choose(rng, SUPPORT_PHRASES, 1, 1)

        rng.shuffle(evidence)
        title = str(rng.choice(titles[occupation_group]))
        demand_index = float(np.clip(rng.normal(0.55 + 0.08 * (sector == "technology"), 0.18), 0.05, 0.98))
        applicant_interest = float(
            3.1
            + 0.45 * demand_index
            - 0.42 * benchmark_mismatch
            + 0.10 * (region == "West")
            + rng.normal(0.0, 0.24)
        )
        source_text = (
            f"{document_type}. Job: {title} in {sector}. "
            f"Record note: {', '.join(evidence)}. "
            f"Applicant history includes {rng.choice(['two years of related work', 'recent training', 'prior sector experience', 'new labor-market entry'])}. "
            f"Manager asks whether the match is ready for placement."
        )
        rows.append(
            {
                "doc_id": doc_id,
                "year": year,
                "sector": sector,
                "region": region,
                "occupation_group": occupation_group,
                "document_type": document_type,
                "job_title": title,
                "source_text": source_text,
                "benchmark_mismatch": benchmark_mismatch,
                "benchmark_type": gap_type,
                "demand_index": round(demand_index, 4),
                "applicant_interest": round(applicant_interest, 4),
            }
        )
    return pd.DataFrame(rows)


def make_transfer_records() -> pd.DataFrame:
    rng = np.random.default_rng(1515)
    programs = ["training voucher", "workforce agency", "community college", "union pathway", "city contractor"]
    transfer_gap_terms = {
        "skill_gap": ["rapid upskilling", "digital intake coaching", "bridge credential", "needs platform practice"],
        "credential_gap": ["reciprocity unresolved", "license bridge", "credential bridge", "paperwork credential pending"],
        "schedule_gap": ["wraparound schedule", "shift barrier", "care hours conflict", "bus route barrier"],
    }
    transfer_support_terms = [
        "ready for placement",
        "credential verified",
        "schedule aligned",
        "skills aligned",
        "license verified",
        "no training barrier",
    ]
    rows: list[dict[str, object]] = []
    for case_id in range(1, 101):
        program_area = str(rng.choice(programs))
        region = str(rng.choice(REGIONS))
        year = int(rng.choice([2024, 2025]))
        benchmark_mismatch = int(rng.random() < (0.38 + 0.10 * (program_area in {"training voucher", "community college"})))
        if benchmark_mismatch:
            gap_type = str(rng.choice(["skill_gap", "credential_gap", "schedule_gap"], p=[0.40, 0.36, 0.24]))
            evidence = choose(rng, transfer_gap_terms[gap_type], 1, 2)
            if rng.random() < 0.22:
                evidence += choose(rng, AMBIGUOUS_PHRASES, 1, 1)
        else:
            gap_type = "none"
            evidence = choose(rng, transfer_support_terms, 1, 2)
            if rng.random() < 0.12:
                evidence += choose(rng, transfer_gap_terms["skill_gap"] + transfer_gap_terms["credential_gap"], 2, 2)
            if rng.random() < 0.15:
                evidence += choose(rng, AMBIGUOUS_PHRASES, 1, 1)
        rng.shuffle(evidence)
        placement_score = float(
            2.8
            - 0.36 * benchmark_mismatch
            + 0.16 * (program_area == "union pathway")
            + 0.08 * (region == "West")
            + rng.normal(0.0, 0.22)
        )
        case_text = (
            f"Workforce case note for {program_area}. "
            f"Counselor summary: {', '.join(evidence)}. "
            f"Participant is considering {rng.choice(['health support', 'logistics', 'public service', 'office administration'])} placement."
        )
        rows.append(
            {
                "case_id": case_id,
                "year": year,
                "program_area": program_area,
                "region": region,
                "case_text": case_text,
                "benchmark_mismatch": benchmark_mismatch,
                "benchmark_type": gap_type,
                "placement_score": round(placement_score, 4),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    source_dir = ROOT / "original" / "reduced"
    transfer_dir = ROOT / "transfer" / "data"
    source_dir.mkdir(parents=True, exist_ok=True)
    transfer_dir.mkdir(parents=True, exist_ok=True)
    source = make_source_records()
    transfer = make_transfer_records()
    source.to_csv(source_dir / "labor_mismatch_documents_synthetic.csv", index=False)
    transfer.to_csv(transfer_dir / "workforce_case_notes_synthetic.csv", index=False)
    print(f"Wrote {len(source)} source records and {len(transfer)} transfer records.")


if __name__ == "__main__":
    main()
