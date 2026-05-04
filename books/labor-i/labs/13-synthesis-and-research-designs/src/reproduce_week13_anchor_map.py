from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_counter(path: Path, header: str, counter: Counter[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([header, "count"])
        for key, value in sorted(counter.items()):
            writer.writerow([key, value])


def build_figure(rows: list[dict[str, str]], figure_path: Path) -> None:
    labels = [row["anchor_label"] for row in rows]
    scores = [int(row["bridge_score"]) for row in rows]
    colors = ["#355070" if score == 1 else "#6d597a" if score == 2 else "#b56576" for score in scores]

    fig, ax = plt.subplots(figsize=(9, 4.8))
    y_positions = range(len(labels))
    ax.barh(list(y_positions), scores, color=colors)
    ax.set_yticks(list(y_positions), labels)
    ax.set_xlim(0, 3.25)
    ax.set_xticks([1, 2, 3], ["Mostly Labor I", "Boundary", "Explicit Labor II bridge"])
    ax.set_xlabel("How quickly the anchor requires firm-side or equilibrium tools")
    ax.set_title("Week 13 anchor-paper bridge map")
    ax.grid(axis="x", alpha=0.25)
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(figure_path, dpi=200)
    plt.close(fig)


def write_note(path: Path, rows: list[dict[str, str]], design_counts: Counter[str]) -> None:
    strongest_bridge = max(rows, key=lambda row: int(row["bridge_score"]))
    line_items = "\n".join(f"- `{design}`: {count}" for design, count in sorted(design_counts.items()))
    text = (
        "# Reproduction note\n\n"
        "The Week 13 reproduced packet summarizes how a small set of Labor I anchor papers map into objects, "
        "mechanisms, designs, and the Labor I / Labor II boundary.\n\n"
        "## Design-family counts\n\n"
        f"{line_items}\n\n"
        "## Strongest immediate bridge\n\n"
        f"- `{strongest_bridge['anchor_label']}` is the closest direct bridge because its core object already depends on "
        "firm heterogeneity, sorting, and wage-setting.\n"
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = read_rows(input_path)
    design_counts = Counter(row["design_family"] for row in rows)
    bridge_counts = Counter(row["bridge_score"] for row in rows)

    write_counter(outdir / "anchor_design_family_counts.csv", "design_family", design_counts)
    write_counter(outdir / "anchor_bridge_score_counts.csv", "bridge_score", bridge_counts)
    build_figure(rows, outdir / "week13_anchor_bridge_map.png")
    write_note(outdir / "reproduction_note.md", rows, design_counts)

    print(f"Wrote outputs to {outdir}")


if __name__ == "__main__":
    main()

