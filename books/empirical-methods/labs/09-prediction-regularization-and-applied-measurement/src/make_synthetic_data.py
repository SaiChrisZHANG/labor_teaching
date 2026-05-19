"""Create deterministic synthetic data for the Week 9 prediction lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


TECH_TERMS = [
    "python",
    "sql",
    "cloud",
    "machine learning",
    "automation",
    "data pipeline",
    "api",
    "analytics",
    "dashboard",
    "model monitoring",
]

OPERATIONS_TERMS = [
    "scheduling",
    "inventory",
    "customer service",
    "compliance",
    "documentation",
    "quality checks",
    "team coordination",
    "procurement",
    "dispatch",
    "training",
]

REMOTE_TERMS = [
    "remote collaboration",
    "video meetings",
    "distributed team",
    "async communication",
    "hybrid schedule",
]

SECTORS = ["health", "logistics", "finance", "manufacturing", "education", "retail"]
REGIONS = ["Northeast", "Midwest", "South", "West"]


def choose_terms(rng: np.random.Generator, pool: list[str], low: int, high: int) -> list[str]:
    count = int(rng.integers(low, high + 1))
    return list(rng.choice(pool, size=count, replace=False))


def make_job_postings() -> pd.DataFrame:
    rng = np.random.default_rng(9091)
    rows: list[dict[str, object]] = []
    sector_tech_shift = {
        "health": -0.12,
        "logistics": -0.02,
        "finance": 0.24,
        "manufacturing": 0.04,
        "education": -0.16,
        "retail": -0.26,
    }
    region_shift = {"Northeast": 0.05, "Midwest": -0.04, "South": -0.02, "West": 0.12}
    base_titles = {
        "health": ["care coordinator", "clinical analyst", "patient operations associate"],
        "logistics": ["routing analyst", "warehouse coordinator", "supply chain associate"],
        "finance": ["risk analyst", "operations analyst", "portfolio data associate"],
        "manufacturing": ["process technician", "quality analyst", "production planner"],
        "education": ["student services analyst", "program coordinator", "learning systems associate"],
        "retail": ["store operations lead", "merchandising analyst", "customer insights associate"],
    }

    for posting_id in range(1, 281):
        sector = str(rng.choice(SECTORS))
        region = str(rng.choice(REGIONS))
        year = int(rng.choice([2021, 2022, 2023, 2024], p=[0.20, 0.24, 0.28, 0.28]))
        firm_size = int(rng.choice([50, 120, 300, 900, 2400], p=[0.22, 0.25, 0.25, 0.18, 0.10]))
        remote_signal = float(rng.binomial(1, 0.16 + 0.04 * (year - 2021) + (0.07 if region == "West" else 0.0)))
        logit = (
            -0.65
            + sector_tech_shift[sector]
            + region_shift[region]
            + 0.16 * np.log(firm_size / 100.0)
            + 0.18 * (year - 2021)
            + 0.34 * remote_signal
            + rng.normal(0.0, 0.62)
        )
        probability = 1.0 / (1.0 + np.exp(-logit))
        technology_intensive = int(rng.binomial(1, probability))
        tech_terms = choose_terms(rng, TECH_TERMS, 2 if technology_intensive else 0, 4 if technology_intensive else 1)
        operations_terms = choose_terms(rng, OPERATIONS_TERMS, 2, 4)
        remote_terms = choose_terms(rng, REMOTE_TERMS, 1, 2) if remote_signal else []
        title_prefix = "senior" if technology_intensive and rng.random() < 0.35 else "associate"
        title = f"{title_prefix} {rng.choice(base_titles[sector])}"
        text_terms = tech_terms + operations_terms + remote_terms
        rng.shuffle(text_terms)
        description = (
            f"{title}. This role supports {sector} teams with "
            + ", ".join(text_terms)
            + ". Candidates document workflows and communicate with managers."
        )
        # This column is intentionally post-outcome and should never be used as a feature.
        future_verified_skill_tag = int(technology_intensive and rng.random() < 0.92)
        rows.append(
            {
                "posting_id": posting_id,
                "year": year,
                "sector": sector,
                "region": region,
                "firm_size": firm_size,
                "title": title,
                "posting_text": description,
                "technology_intensive": technology_intensive,
                "remote_signal": int(remote_signal),
                "future_verified_skill_tag": future_verified_skill_tag,
            }
        )

    return pd.DataFrame(rows)


def make_occupation_titles() -> pd.DataFrame:
    rng = np.random.default_rng(9097)
    tech_titles = [
        "data analyst",
        "cloud support technician",
        "automation engineer",
        "business intelligence analyst",
        "machine learning associate",
        "software quality analyst",
        "analytics product specialist",
    ]
    nontech_titles = [
        "care coordinator",
        "warehouse supervisor",
        "retail shift lead",
        "training coordinator",
        "customer service manager",
        "procurement assistant",
        "production scheduler",
    ]
    rows: list[dict[str, object]] = []
    for title_id in range(1, 151):
        sector = str(rng.choice(SECTORS))
        region = str(rng.choice(REGIONS))
        year = int(rng.choice([2023, 2024, 2025], p=[0.20, 0.36, 0.44]))
        technology_occupation = int(rng.binomial(1, 0.34 + (0.18 if sector == "finance" else 0.0)))
        if technology_occupation:
            title = str(rng.choice(tech_titles))
            if rng.random() < 0.28:
                title = title.replace("data", "insights").replace("cloud", "platform")
        else:
            title = str(rng.choice(nontech_titles))
            if rng.random() < 0.18:
                title = title + " digital tools"
        rows.append(
            {
                "title_id": title_id,
                "year": year,
                "sector": sector,
                "region": region,
                "raw_title": title,
                "technology_occupation": technology_occupation,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    postings_path = ROOT / "original" / "reduced" / "job_postings_synthetic.csv"
    titles_path = ROOT / "transfer" / "data" / "occupation_titles_synthetic.csv"
    postings_path.parent.mkdir(parents=True, exist_ok=True)
    titles_path.parent.mkdir(parents=True, exist_ok=True)
    make_job_postings().to_csv(postings_path, index=False)
    make_occupation_titles().to_csv(titles_path, index=False)
    print(f"Wrote {postings_path}")
    print(f"Wrote {titles_path}")


if __name__ == "__main__":
    main()
