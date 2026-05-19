"""Create deterministic synthetic data for the Week 12 measurement lab."""

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

SERVICE_PHRASES = [
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


def make_job_postings() -> pd.DataFrame:
    rng = np.random.default_rng(1212)
    sector_shift = {
        "finance": 0.58,
        "health": -0.24,
        "education": 0.18,
        "manufacturing": -0.48,
        "retail": -0.52,
        "public": 0.04,
    }
    family_shift = {
        "analysis": 0.70,
        "customer": 0.10,
        "operations": -0.02,
        "production": -0.72,
        "care": -0.40,
        "administration": 0.34,
    }
    region_shift = {"Northeast": 0.08, "Midwest": -0.04, "South": -0.08, "West": 0.18}
    titles = {
        "analysis": ["data analyst", "policy analyst", "risk analyst"],
        "customer": ["client support associate", "service coordinator", "customer success lead"],
        "operations": ["operations planner", "logistics coordinator", "program operations associate"],
        "production": ["production technician", "warehouse lead", "equipment operator"],
        "care": ["care coordinator", "clinic scheduler", "patient support specialist"],
        "administration": ["administrative analyst", "grants coordinator", "records manager"],
    }

    rows: list[dict[str, object]] = []
    for posting_id in range(1, 321):
        sector = str(rng.choice(SECTORS))
        region = str(rng.choice(REGIONS))
        job_family = str(rng.choice(JOB_FAMILIES))
        year = int(rng.choice([2021, 2022, 2023, 2024], p=[0.18, 0.24, 0.29, 0.29]))
        firm_size = int(rng.choice([40, 90, 180, 450, 1200, 3000], p=[0.14, 0.20, 0.25, 0.21, 0.13, 0.07]))
        latent = (
            -0.55
            + sector_shift[sector]
            + family_shift[job_family]
            + region_shift[region]
            + 0.12 * (year - 2021)
            + 0.10 * np.log(firm_size / 100.0)
            + rng.normal(0.0, 0.62)
        )
        remote_probability = sigmoid(latent)
        remote_label = int(rng.binomial(1, remote_probability))
        has_remote_language = bool(rng.binomial(1, 0.84 if remote_label else 0.10))
        has_onsite_language = bool(rng.binomial(1, 0.22 if remote_label else 0.82))

        terms = choose_terms(rng, SERVICE_PHRASES, 2, 4)
        terms += choose_terms(rng, DIGITAL_PHRASES, 1 if remote_label else 0, 3 if remote_label else 2)
        if has_remote_language:
            terms += choose_terms(rng, REMOTE_PHRASES, 1, 3)
        if has_onsite_language:
            terms += choose_terms(rng, ONSITE_PHRASES, 1, 3)
        rng.shuffle(terms)

        title = str(rng.choice(titles[job_family]))
        seniority = str(rng.choice(["associate", "senior", "lead"], p=[0.48, 0.34, 0.18]))
        description = (
            f"{seniority} {title}. The role supports {sector} teams through "
            + ", ".join(terms)
            + ". Candidates document workflows and coordinate with managers."
        )
        applicant_interest = (
            2.2
            + 0.42 * remote_label
            + 0.11 * np.log(firm_size)
            + 0.09 * (region == "West")
            + 0.07 * (job_family == "analysis")
            + rng.normal(0.0, 0.28)
        )
        future_remote_badge = int(remote_label and rng.random() < 0.91)
        if not remote_label and rng.random() < 0.05:
            future_remote_badge = 1

        rows.append(
            {
                "posting_id": posting_id,
                "year": year,
                "sector": sector,
                "region": region,
                "job_family": job_family,
                "firm_size": firm_size,
                "posting_title": f"{seniority} {title}",
                "posting_text": description,
                "remote_label": remote_label,
                "applicant_interest": round(float(applicant_interest), 4),
                "future_remote_badge": future_remote_badge,
            }
        )

    return pd.DataFrame(rows)


def make_multimodal_records() -> pd.DataFrame:
    rng = np.random.default_rng(1234)
    organization_types = ["school", "clinic", "workforce agency", "city office", "training vendor"]
    text_remote = [
        "virtual intake",
        "online appointments",
        "remote service",
        "hybrid advising",
        "digital case files",
        "video check ins",
    ]
    text_onsite = [
        "walk in desk",
        "paper forms",
        "in person queue",
        "front counter",
        "onsite workshop",
        "posted office hours",
    ]
    neutral = [
        "eligibility review",
        "staff coordination",
        "participant outreach",
        "case notes",
        "program reporting",
        "manager approval",
    ]

    rows: list[dict[str, object]] = []
    for record_id in range(1, 151):
        organization_type = str(rng.choice(organization_types))
        region = str(rng.choice(REGIONS))
        type_shift = {
            "school": 0.14,
            "clinic": -0.12,
            "workforce agency": 0.28,
            "city office": -0.02,
            "training vendor": 0.38,
        }[organization_type]
        visual_infrastructure = float(np.clip(rng.normal(0.55 + type_shift / 4.0, 0.20), 0.02, 0.98))
        audio_clarity = float(np.clip(rng.normal(0.58 + (0.05 if region == "West" else 0.0), 0.18), 0.02, 0.98))
        video_interaction = float(np.clip(rng.normal(0.52 + type_shift / 5.0, 0.20), 0.02, 0.98))
        latent = (
            -0.40
            + type_shift
            + 1.05 * visual_infrastructure
            + 0.65 * audio_clarity
            + 0.75 * video_interaction
            + rng.normal(0.0, 0.62)
        )
        flexible_service_capacity = int(rng.binomial(1, sigmoid(latent)))
        terms = choose_terms(rng, neutral, 2, 4)
        if flexible_service_capacity:
            terms += choose_terms(rng, text_remote, 2, 4)
            if rng.random() < 0.25:
                terms += choose_terms(rng, text_onsite, 1, 1)
        else:
            terms += choose_terms(rng, text_onsite, 2, 4)
            if rng.random() < 0.18:
                terms += choose_terms(rng, text_remote, 1, 1)
        rng.shuffle(terms)
        policy_text = (
            f"{organization_type} service record. Staff describe "
            + ", ".join(terms)
            + " for participants and supervisors."
        )
        rows.append(
            {
                "record_id": record_id,
                "organization_type": organization_type,
                "region": region,
                "policy_text": policy_text,
                "image_infrastructure_score": round(visual_infrastructure, 4),
                "audio_clarity_score": round(audio_clarity, 4),
                "video_interaction_score": round(video_interaction, 4),
                "flexible_service_capacity": flexible_service_capacity,
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    postings_path = ROOT / "original" / "reduced" / "job_postings_remote_synthetic.csv"
    transfer_path = ROOT / "transfer" / "data" / "multimodal_work_records_synthetic.csv"
    postings_path.parent.mkdir(parents=True, exist_ok=True)
    transfer_path.parent.mkdir(parents=True, exist_ok=True)
    make_job_postings().to_csv(postings_path, index=False)
    make_multimodal_records().to_csv(transfer_path, index=False)
    print(f"Wrote {postings_path}")
    print(f"Wrote {transfer_path}")


if __name__ == "__main__":
    main()
