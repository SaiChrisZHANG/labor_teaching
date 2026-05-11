from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


CAUTIONS = {
    "law_on_books": "Do not interpret the estimate as enforcement unless implementation varies or is observed.",
    "enforcement": "Check whether inspector access is endogenous to local state capacity or labor demand.",
    "knowledge": "The intervention changes salience or information, not statutory protection or sanctions.",
    "state_capacity_bundle": "The measure may bundle legal text, bureaucracy, compliance, and worker outcomes.",
    "incidence_and_sorting": "Administrative coverage may miss informal workers and invisible firms.",
    "effective_compliance": "The design may mix enforcement, complaints, worker organization, and firm response.",
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
        identifies = row["expected_object"]
        counts[identifies] += 1
        classified.append(
            {
                "design_id": row["design_id"],
                "anchor": row["anchor"],
                "identifying_variation": row["variation"],
                "unit": row["unit"],
                "observed_margin": row["observed_margin"],
                "identifies": identifies,
                "diagnostic_caution": CAUTIONS[identifies],
            }
        )
    count_rows = [{"identifies": key, "design_count": value} for key, value in sorted(counts.items())]
    return classified, count_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 2 transfer note",
                "",
                "A design's identifying variation determines the object it identifies.",
                "Legal adoption and court-made variation primarily identify law on the books.",
                "Inspection access identifies enforcement intensity.",
                "Information experiments identify knowledge or salience.",
                "Linked administrative data are strongest for incidence and sorting when coverage is broad.",
                "Comparative state-capacity measures are useful for portability but can bundle several mechanisms.",
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
            "identifying_variation",
            "unit",
            "observed_margin",
            "identifies",
            "diagnostic_caution",
        ],
        classified,
    )
    write_csv(args.outdir / "design_object_counts.csv", ["identifies", "design_count"], count_rows)
    write_note(args.outdir / "transfer_note.txt")
    print(f"Wrote Week 2 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
