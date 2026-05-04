from __future__ import annotations

import argparse
import csv
from pathlib import Path


PLACEHOLDERS = {
    "anchor_label",
    "week_origin",
    "labor_object",
    "mechanism",
    "data_unit",
    "design_family",
    "primary_estimand",
    "labor_ii_bridge",
    "extension_prompt",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--template", required=True)
    parser.add_argument("--anchor", required=True)
    parser.add_argument("--outdir", required=True)
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def render_template(template_text: str, row: dict[str, str]) -> str:
    rendered = template_text
    for key in PLACEHOLDERS:
        rendered = rendered.replace(f"{{{{{key}}}}}", row[key])
    return rendered


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    template_path = Path(args.template)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = read_rows(input_path)
    try:
        row = next(item for item in rows if item["anchor_slug"] == args.anchor)
    except StopIteration as exc:
        available = ", ".join(item["anchor_slug"] for item in rows)
        raise SystemExit(f"Unknown anchor `{args.anchor}`. Available anchors: {available}") from exc

    template_text = template_path.read_text(encoding="utf-8")
    rendered = render_template(template_text, row)

    output_path = outdir / f"{row['anchor_slug']}-research-memo-template.md"
    output_path.write_text(rendered, encoding="utf-8")

    checklist = (
        "# Proposal checklist\n\n"
        f"- Anchor: {row['anchor_label']}\n"
        f"- Primary estimand: {row['primary_estimand']}\n"
        "- One main mechanism only\n"
        "- One primary outcome only\n"
        "- One explicit Labor I / Labor II boundary statement\n"
        "- One sentence on why the contribution belongs in labor economics\n"
    )
    (outdir / f"{row['anchor_slug']}-proposal-checklist.md").write_text(checklist, encoding="utf-8")

    print(f"Wrote proposal template to {output_path}")


if __name__ == "__main__":
    main()

