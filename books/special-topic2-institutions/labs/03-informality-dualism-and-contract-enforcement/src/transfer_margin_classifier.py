from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


OBJECT_LABELS = {
    "firm_compliance_registration": "firm compliance and registration",
    "wage_setting_worker_sorting": "wage-setting and worker sorting",
    "enforcement_formalization": "enforcement-driven formalization",
    "policy_welfare_incidence": "welfare under policy change",
    "contract_enforceability": "contract enforceability",
    "worker_sorting_mobility": "worker sorting and mobility",
    "equilibrium_reallocation": "equilibrium reallocation",
}

CAUTIONS = {
    "firm_compliance_registration": "Separate firm registration from payroll reporting and hidden employment.",
    "wage_setting_worker_sorting": "Do not interpret wage gaps without sorting, benefits, and search frictions.",
    "enforcement_formalization": "Check whether the observed response is formalization, employment loss, or reclassification.",
    "policy_welfare_incidence": "Name the benefit, tax, or eligibility margin before drawing welfare conclusions.",
    "contract_enforceability": "State whose claims became enforceable and how mobility or bargaining changed.",
    "worker_sorting_mobility": "Transitions identify mobility patterns but may not isolate firm compliance.",
    "equilibrium_reallocation": "Linked records help, but missing informal firms can still bias the reallocation picture.",
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
                "identifies": OBJECT_LABELS[identifies],
                "diagnostic_caution": CAUTIONS[identifies],
            }
        )
    count_rows = [
        {"identifies": OBJECT_LABELS[key], "design_count": value}
        for key, value in sorted(counts.items())
    ]
    return classified, count_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 3 transfer note",
                "",
                "The same word, formality, can refer to several margins.",
                "Worker panels are strongest for sorting and mobility.",
                "Firm-side models are strongest for registration, payroll reporting, scale, and evasion.",
                "Enforcement designs identify changes in expected detection or sanctions.",
                "Policy discontinuities identify benefit or tax wedges around formal status.",
                "Historical legal designs identify contract enforceability when legal variation changes credible claims.",
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
    print(f"Wrote Week 3 transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
