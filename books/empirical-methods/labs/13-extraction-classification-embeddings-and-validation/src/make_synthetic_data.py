"""Create deterministic synthetic data for the Week 13 validation lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

SECTORS = ["finance", "health", "education", "manufacturing", "retail", "public"]
REGIONS = ["Northeast", "Midwest", "South", "West"]
JOB_FAMILIES = ["analysis", "customer", "operations", "production", "care", "administration"]

REMOTE_PHRASES = [
    "remote work",
    "work from home",
    "distributed team",
    "virtual meetings",
    "home office",
    "asynchronous communication",
    "flexible location",
    "hybrid schedule",
]

ONSITE_PHRASES = [
    "on site presence",
    "production floor",
    "front desk coverage",
    "field visits",
    "in person service",
    "warehouse shift",
    "storefront support",
    "physical equipment",
]

DIGITAL_PHRASES = [
    "cloud records",
    "data dashboards",
    "case management software",
    "online documentation",
    "shared workflow tools",
    "secure video calls",
]

GENERAL_PHRASES = [
    "customer follow up",
    "team coordination",
    "compliance documentation",
    "manager updates",
    "training support",
    "quality checks",
]


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + np.exp(-value))


def choose_terms(rng: np.random.Generator, pool: list[str], low: int, high: int) -> list[str]:
    count = int(rng.integers(low, high + 1))
    return list(rng.choice(pool, size=count, replace=False))


def noisy_label(
    rng: np.random.Generator,
    true_label: int,
    base_error: float,
    ambiguous: bool,
    hard_group: bool,
    missing_explicit_language: bool,
) -> int:
    error_probability = base_error
    if ambiguous:
        error_probability += 0.08
    if hard_group:
        error_probability += 0.10
    if missing_explicit_language:
        error_probability += 0.12
    if rng.random() < error_probability:
        return int(1 - true_label)
    return int(true_label)


def adjudicate_label(
    rng: np.random.Generator,
    true_label: int,
    rater_a: int,
    rater_b: int,
    hard_group: bool,
) -> int:
    if rater_a == rater_b:
        label = rater_a
    else:
        label = true_label if rng.random() < 0.92 else int(rng.choice([rater_a, rater_b]))
    if hard_group and rng.random() < 0.03:
        label = int(1 - label)
    return int(label)


def make_source_postings() -> pd.DataFrame:
    rng = np.random.default_rng(1313)
    sector_shift = {
        "finance": 0.55,
        "health": -0.18,
        "education": 0.18,
        "manufacturing": -0.55,
        "retail": -0.48,
        "public": 0.06,
    }
    family_shift = {
        "analysis": 0.72,
        "customer": 0.12,
        "operations": -0.04,
        "production": -0.78,
        "care": -0.42,
        "administration": 0.32,
    }
    region_shift = {"Northeast": 0.08, "Midwest": -0.05, "South": -0.10, "West": 0.20}
    titles = {
        "analysis": ["data analyst", "policy analyst", "risk analyst"],
        "customer": ["client support associate", "service coordinator", "customer success lead"],
        "operations": ["operations planner", "logistics coordinator", "program operations associate"],
        "production": ["production technician", "warehouse lead", "equipment operator"],
        "care": ["care coordinator", "clinic scheduler", "patient support specialist"],
        "administration": ["administrative analyst", "grants coordinator", "records manager"],
    }

    rows: list[dict[str, object]] = []
    for posting_id in range(1, 421):
        sector = str(rng.choice(SECTORS))
        region = str(rng.choice(REGIONS))
        job_family = str(rng.choice(JOB_FAMILIES))
        year = int(rng.choice([2021, 2022, 2023, 2024], p=[0.16, 0.24, 0.30, 0.30]))
        firm_size = int(rng.choice([45, 90, 160, 380, 900, 2400], p=[0.12, 0.20, 0.27, 0.23, 0.12, 0.06]))
        latent = (
            -0.50
            + sector_shift[sector]
            + family_shift[job_family]
            + region_shift[region]
            + 0.12 * (year - 2021)
            + 0.08 * np.log(firm_size / 100.0)
            + rng.normal(0.0, 0.64)
        )
        true_remote_label = int(rng.binomial(1, sigmoid(latent)))
        has_remote_language = bool(rng.binomial(1, 0.86 if true_remote_label else 0.12))
        has_onsite_language = bool(rng.binomial(1, 0.22 if true_remote_label else 0.84))

        terms = choose_terms(rng, GENERAL_PHRASES, 2, 4)
        terms += choose_terms(rng, DIGITAL_PHRASES, 1 if true_remote_label else 0, 3 if true_remote_label else 2)
        if has_remote_language:
            terms += choose_terms(rng, REMOTE_PHRASES, 1, 3)
        if has_onsite_language:
            terms += choose_terms(rng, ONSITE_PHRASES, 1, 3)
        rng.shuffle(terms)

        seniority = str(rng.choice(["associate", "senior", "lead"], p=[0.48, 0.34, 0.18]))
        title = str(rng.choice(titles[job_family]))
        posting_text = (
            f"{seniority} {title}. The role supports {sector} teams through "
            + ", ".join(terms)
            + ". Candidates document workflows and coordinate with managers."
        )
        ambiguous = "hybrid schedule" in terms or (has_remote_language and has_onsite_language)
        hard_group = job_family in {"production", "care"} or sector in {"manufacturing", "health"}
        missing_explicit_language = bool(true_remote_label and not has_remote_language)
        rater_a = noisy_label(rng, true_remote_label, 0.06, ambiguous, hard_group, missing_explicit_language)
        rater_b = noisy_label(rng, true_remote_label, 0.09, ambiguous, hard_group, missing_explicit_language)
        benchmark_label = adjudicate_label(rng, true_remote_label, rater_a, rater_b, hard_group)

        external_remote_audit = float(
            np.clip(
                0.12
                + 0.70 * true_remote_label
                + 0.10 * has_remote_language
                - 0.08 * has_onsite_language
                + 0.04 * (region == "West")
                + rng.normal(0.0, 0.12),
                0.01,
                0.99,
            )
        )
        applicant_interest = float(
            2.15
            + 0.48 * true_remote_label
            + 0.10 * np.log(firm_size)
            + 0.07 * (region == "West")
            + 0.06 * (job_family == "analysis")
            + rng.normal(0.0, 0.30)
        )

        rows.append(
            {
                "posting_id": posting_id,
                "year": year,
                "sector": sector,
                "region": region,
                "job_family": job_family,
                "firm_size": firm_size,
                "posting_title": f"{seniority} {title}",
                "posting_text": posting_text,
                "simulation_truth_label": true_remote_label,
                "rater_a_label": rater_a,
                "rater_b_label": rater_b,
                "benchmark_label": benchmark_label,
                "external_remote_audit": round(external_remote_audit, 4),
                "applicant_interest": round(applicant_interest, 4),
            }
        )

    return pd.DataFrame(rows)


def make_transfer_records() -> pd.DataFrame:
    rng = np.random.default_rng(1414)
    organization_types = ["school", "clinic", "workforce agency", "city office", "training vendor"]
    remote_service_terms = [
        "virtual intake",
        "tele-service",
        "mobile casework",
        "digital queue",
        "remote service window",
        "online appointments",
        "hybrid advising",
    ]
    onsite_service_terms = [
        "walk in desk",
        "paper forms",
        "front counter",
        "onsite workshop",
        "in person queue",
        "posted office hours",
    ]
    neutral_terms = [
        "eligibility review",
        "staff coordination",
        "participant outreach",
        "case notes",
        "program reporting",
        "manager approval",
    ]
    type_shift = {
        "school": 0.10,
        "clinic": -0.18,
        "workforce agency": 0.26,
        "city office": -0.04,
        "training vendor": 0.42,
    }

    rows: list[dict[str, object]] = []
    for record_id in range(1, 181):
        organization_type = str(rng.choice(organization_types))
        region = str(rng.choice(REGIONS))
        image_infrastructure_score = float(
            np.clip(
                rng.normal(0.55 + type_shift[organization_type] / 4.0 + 0.04 * (region == "West"), 0.19),
                0.02,
                0.98,
            )
        )
        latent = (
            -0.35
            + type_shift[organization_type]
            + 1.05 * image_infrastructure_score
            + 0.12 * (region == "West")
            - 0.06 * (region == "South")
            + rng.normal(0.0, 0.68)
        )
        flexible_service_label = int(rng.binomial(1, sigmoid(latent)))
        terms = choose_terms(rng, neutral_terms, 2, 4)
        if flexible_service_label:
            terms += choose_terms(rng, remote_service_terms, 2, 4)
            if rng.random() < 0.22:
                terms += choose_terms(rng, onsite_service_terms, 1, 1)
        else:
            terms += choose_terms(rng, onsite_service_terms, 2, 4)
            if rng.random() < 0.20:
                terms += choose_terms(rng, remote_service_terms, 1, 1)
        rng.shuffle(terms)
        policy_text = (
            f"{organization_type} service record. Staff describe "
            + ", ".join(terms)
            + " for participants and supervisors."
        )
        external_service_audit = float(
            np.clip(
                0.15
                + 0.58 * flexible_service_label
                + 0.24 * image_infrastructure_score
                + rng.normal(0.0, 0.13),
                0.01,
                0.99,
            )
        )
        rows.append(
            {
                "record_id": record_id,
                "organization_type": organization_type,
                "region": region,
                "policy_text": policy_text,
                "image_infrastructure_score": round(image_infrastructure_score, 4),
                "simulation_truth_label": flexible_service_label,
                "benchmark_label": flexible_service_label,
                "external_service_audit": round(external_service_audit, 4),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    source_path = ROOT / "original" / "reduced" / "validation_postings_synthetic.csv"
    transfer_path = ROOT / "transfer" / "data" / "service_records_shifted_synthetic.csv"
    source_path.parent.mkdir(parents=True, exist_ok=True)
    transfer_path.parent.mkdir(parents=True, exist_ok=True)
    make_source_postings().to_csv(source_path, index=False)
    make_transfer_records().to_csv(transfer_path, index=False)
    print(f"Wrote {source_path}")
    print(f"Wrote {transfer_path}")


if __name__ == "__main__":
    main()
