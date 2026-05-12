from __future__ import annotations

import csv
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def country_year_rows() -> list[dict[str, object]]:
    countries = [
        ("Aster", "high_income", 0.74, 2016, 0.62, 0.80, 0.41),
        ("Boreal", "middle_income", 0.58, 2017, 0.54, 0.78, 0.33),
        ("Canto", "middle_income", 0.48, 2018, 0.49, 0.77, 0.27),
        ("Dara", "emerging", 0.39, 2019, 0.42, 0.75, 0.21),
        ("Emin", "emerging", 0.31, 2020, 0.36, 0.73, 0.16),
    ]
    rows: list[dict[str, object]] = []
    for country, region, base_legal, reform_year, base_flfp, base_mlfp, base_authority in countries:
        for year in range(2012, 2022):
            trend = year - 2012
            post_reform = int(year >= reform_year)
            legal_access = min(0.95, base_legal + 0.012 * trend + 0.075 * post_reform)
            workplace_protection = min(0.96, base_legal + 0.018 * trend + 0.055 * post_reform - 0.03)
            family_law = min(0.94, base_legal + 0.010 * trend + 0.045 * post_reform - 0.04)
            paid_leave_weeks = 4 + int(12 * family_law) + 2 * post_reform
            female_lfp = min(0.82, base_flfp + 0.050 * post_reform + 0.006 * trend)
            male_lfp = min(0.88, base_mlfp + 0.010 * post_reform + 0.002 * trend)
            female_hours = 30.0 + 4.0 * legal_access + 0.2 * trend
            male_hours = 39.5 + 0.8 * legal_access + 0.1 * trend
            female_authority = min(0.55, base_authority + 0.030 * post_reform + 0.004 * trend)
            rows.append(
                {
                    "country": country,
                    "region": region,
                    "year": year,
                    "post_reform": post_reform,
                    "legal_access_score": round(legal_access, 3),
                    "workplace_protection_score": round(workplace_protection, 3),
                    "family_law_score": round(family_law, 3),
                    "paid_leave_weeks": paid_leave_weeks,
                    "female_lfp_rate": round(female_lfp, 3),
                    "male_lfp_rate": round(male_lfp, 3),
                    "female_employment_rate": round(female_lfp - 0.035 + 0.010 * post_reform, 3),
                    "male_employment_rate": round(male_lfp - 0.025, 3),
                    "female_weekly_hours": round(female_hours, 2),
                    "male_weekly_hours": round(male_hours, 2),
                    "female_authority_share": round(female_authority, 3),
                }
            )
    return rows


def child_penalty_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for event_time in range(-4, 9):
        for gender in ["female", "male"]:
            if gender == "female":
                post = max(event_time, 0)
                penalty = 0 if event_time < 0 else 30 - min(post * 2.5, 12)
                earnings = 100 - penalty + (event_time + 4) * 0.6
                hours = 100 - (0 if event_time < 0 else 22 - min(post * 1.8, 9))
                employment = 100 - (0 if event_time < 0 else 14 - min(post * 1.1, 5))
            else:
                earnings = 101 + (event_time + 4) * 0.7 + (2 if event_time >= 0 else 0)
                hours = 101 + (event_time + 4) * 0.2 + (1 if event_time >= 0 else 0)
                employment = 99 + (event_time + 4) * 0.1
            rows.append(
                {
                    "gender": gender,
                    "event_time": event_time,
                    "earnings_index": round(earnings, 2),
                    "hours_index": round(hours, 2),
                    "employment_index": round(employment, 2),
                }
            )
    return rows


def main() -> None:
    country_fields = [
        "country",
        "region",
        "year",
        "post_reform",
        "legal_access_score",
        "workplace_protection_score",
        "family_law_score",
        "paid_leave_weeks",
        "female_lfp_rate",
        "male_lfp_rate",
        "female_employment_rate",
        "male_employment_rate",
        "female_weekly_hours",
        "male_weekly_hours",
        "female_authority_share",
    ]
    event_fields = ["gender", "event_time", "earnings_index", "hours_index", "employment_index"]
    write_rows(
        LAB / "original" / "reduced" / "gendered_laws_workforce_synthetic.csv",
        country_fields,
        country_year_rows(),
    )
    write_rows(
        LAB / "transfer" / "data" / "child_penalty_event_time_synthetic.csv",
        event_fields,
        child_penalty_rows(),
    )


if __name__ == "__main__":
    main()
