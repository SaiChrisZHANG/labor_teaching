from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


DESIGN_LABELS = {
    "cross_country_index": "cross-country index construction",
    "within_country_comparative_reform": "within-country reform with comparative interpretation",
    "border_region_exposure": "border, region, or firm exposure design",
    "comparative_administrative_microdata": "comparative administrative microdata design",
    "supply_chain_governance_data": "supply-chain audit or governance-data design",
    "historical_comparative_classification": "historical-comparative institutional classification",
}

IDENTIFIES = {
    "cross_country_index": "variation in formal rules or institutional coding across countries",
    "within_country_comparative_reform": "effects of reform timing, rollout, or local exposure in one setting",
    "border_region_exposure": "effects of open-labor-market exposure across borders, regions, or firms",
    "comparative_administrative_microdata": "regime differences observed in harmonized worker or firm records",
    "supply_chain_governance_data": "effects of buyer pressure, audit, certification, or management exposure",
    "historical_comparative_classification": "labor outcomes associated with inherited institutional regimes",
}

CAUTIONS = {
    "cross_country_index": "Legal text is not enough without enforcement, coverage, and informality measures.",
    "within_country_comparative_reform": "A single-country reform still needs a clear comparative taxonomy.",
    "border_region_exposure": "Geography, skill composition, and firm technology may limit transportability.",
    "comparative_administrative_microdata": "Harmonization can hide different definitions of work, benefits, or coverage.",
    "supply_chain_governance_data": "Audit records may miss retaliation, worker voice, or unaudited suppliers.",
    "historical_comparative_classification": "Institutional categories can bundle many mechanisms.",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def classify(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    classified: list[dict[str, object]] = []
    counts: Counter[str] = Counter()
    for row in rows:
        family = row["design_family"]
        counts[family] += 1
        classified.append(
            {
                "design_id": row["design_id"],
                "anchor": row["anchor"],
                "setting": row["setting"],
                "comparison_class": row["comparison_class"],
                "design_family": DESIGN_LABELS[family],
                "identifying_variation": row["identifying_variation"],
                "observed_margin": row["observed_margin"],
                "identifies": IDENTIFIES[family],
                "portability_claim": row["portability_claim"],
                "main_caution": row["main_caution"],
                "standard_caution": CAUTIONS[family],
            }
        )
    count_rows = [
        {"design_family": DESIGN_LABELS[key], "design_count": value}
        for key, value in sorted(counts.items())
    ]
    return classified, count_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 9 transfer note",
                "",
                "Each comparative design should name the comparison class, identifying variation, observed labor margin, and portability claim.",
                "Use the caution columns to separate a portable mechanism from a setting-specific estimate.",
                "Supply-chain and migration designs expand comparative labor institutions beyond closed national labor markets.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    rows = read_rows(args.input)
    classified, count_rows = classify(rows)
    write_csv(
        args.outdir / "design_classification.csv",
        [
            "design_id",
            "anchor",
            "setting",
            "comparison_class",
            "design_family",
            "identifying_variation",
            "observed_margin",
            "identifies",
            "portability_claim",
            "main_caution",
            "standard_caution",
        ],
        classified,
    )
    write_csv(args.outdir / "design_family_counts.csv", ["design_family", "design_count"], count_rows)
    write_note(args.outdir / "transfer_note.txt")
    print(f"Wrote Week 9 transfer classifications to {args.outdir}")


if __name__ == "__main__":
    main()
