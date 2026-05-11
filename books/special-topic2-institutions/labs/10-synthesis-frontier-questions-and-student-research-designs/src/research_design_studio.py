#!/usr/bin/env python3
"""Generate a bounded Week 10 institutions-and-labor research memo."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ANCHORS = {
    "dell2010Mita": {
        "label": "Dell (2010)",
        "course_block": "Historical persistence and coercive labor institutions",
        "labor_outcome": "Modern household consumption, schooling, market access, public goods, and related labor-market conditions.",
        "institutional_mechanism": "A colonial forced-labor institution that altered local power, public goods, roads, land tenure, and outside options.",
        "comparison": "Districts on different sides of a historical mita boundary.",
        "data": "Historical boundary records linked to modern district and household outcomes.",
        "design": "Boundary-style comparison with institutional exposure defined by historical assignment.",
        "welfare_object": "Long-run distributional losses through lower public goods, mobility, market access, and worker opportunity.",
        "portability_claim": "Coercive labor institutions can persist through local public goods and market access, but magnitudes depend on local state capacity and geography.",
        "main_threat": "The historical boundary may correlate with geography, later policy, or other persistent fundamentals.",
        "transfer_prompt": "Use a historical institutional boundary to study a modern labor outcome while naming the channel that persists.",
    },
    "naiduYuchtman2013CoerciveContractEnforcement": {
        "label": "Naidu and Yuchtman (2013)",
        "course_block": "Contract enforcement, coercion, and worker mobility",
        "labor_outcome": "Worker mobility, employer discipline, wages, separations, and bargaining power.",
        "institutional_mechanism": "Master and servant law changed contract enforceability and made quitting more costly for workers.",
        "comparison": "Variation in the enforceability and salience of coercive labor-contract rules across time and place.",
        "data": "Historical court, legal, labor-market, and industrial records.",
        "design": "Historical institutional design connecting legal enforcement to labor-market behavior.",
        "welfare_object": "Distribution of surplus and autonomy between employers and workers when enforcement binds asymmetrically.",
        "portability_claim": "The mechanism travels to settings where contract enforcement changes exit options, but the estimate depends on legal reach and outside options.",
        "main_threat": "Legal enforcement may move with industrial change, worker organization, or local political economy.",
        "transfer_prompt": "Study a contract-enforcement change that alters worker exit, not just a law-on-the-books change.",
    },
    "beerliPeriRuffnerSiegenthaler2021": {
        "label": "Beerli, Peri, Ruffner, and Siegenthaler (2021)",
        "course_block": "Comparative institutions and migration regimes",
        "labor_outcome": "Firm performance, employment, worker outcomes, and matching after labor-supply access changed.",
        "institutional_mechanism": "Abolition of immigration restrictions increased access to cross-border workers.",
        "comparison": "Regions and firms with different exposure to a migration-regime opening.",
        "data": "Administrative firm and worker data linked to regional migration-rule exposure.",
        "design": "Differential exposure to policy liberalization across local labor markets.",
        "welfare_object": "Incidence across native workers, migrant workers, firms, and regions.",
        "portability_claim": "Migration rules shape matching and firm labor supply, but effects depend on geography, skill mix, and bargaining institutions.",
        "main_threat": "Exposed regions may differ in trends, firm composition, or commuting geography.",
        "transfer_prompt": "Adapt the exposure logic to a migration, commuting, credential-recognition, or work-permit reform.",
    },
    "distelhorstHainmuellerLocke2017": {
        "label": "Distelhorst, Hainmueller, and Locke (2017)",
        "course_block": "Global production and private labor governance",
        "labor_outcome": "Labor standards compliance and social performance in supplier factories.",
        "institutional_mechanism": "Buyer-supplier governance and management practices altered incentives for labor-standard compliance.",
        "comparison": "Supplier factories with different management practices, buyer pressure, or governance exposure.",
        "data": "Supply-chain audit, management, and factory records.",
        "design": "Factory-level comparison linking governance practices to measured labor-standard outcomes.",
        "welfare_object": "Worker protection, compliance quality, and incidence between buyers, suppliers, and workers.",
        "portability_claim": "Private governance can affect compliance, but effects depend on buyer commitment, audit credibility, and worker voice.",
        "main_threat": "Management practices and audit outcomes may be selected rather than assigned.",
        "transfer_prompt": "Transfer the logic to certification, buyer pressure, platform governance, or digital compliance systems.",
    },
}


FIELDS = [
    "cite_key",
    "anchor_label",
    "course_block",
    "labor_outcome",
    "institutional_mechanism",
    "comparison",
    "data",
    "design",
    "welfare_object",
    "portability_claim",
    "main_threat",
    "transfer_prompt",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--anchor",
        choices=sorted(ANCHORS),
        default="dell2010Mita",
        help="Primary anchor paper key.",
    )
    parser.add_argument(
        "--challenge",
        choices=sorted(ANCHORS),
        default="naiduYuchtman2013CoerciveContractEnforcement",
        help="Challenge anchor paper key.",
    )
    parser.add_argument(
        "--extension",
        choices=sorted(ANCHORS),
        default="beerliPeriRuffnerSiegenthaler2021",
        help="Optional extension anchor paper key.",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("output/studio"),
        help="Directory for generated studio artifacts.",
    )
    return parser.parse_args()


def row_for(key: str) -> dict[str, str]:
    meta = ANCHORS[key]
    return {
        "cite_key": key,
        "anchor_label": meta["label"],
        "course_block": meta["course_block"],
        "labor_outcome": meta["labor_outcome"],
        "institutional_mechanism": meta["institutional_mechanism"],
        "comparison": meta["comparison"],
        "data": meta["data"],
        "design": meta["design"],
        "welfare_object": meta["welfare_object"],
        "portability_claim": meta["portability_claim"],
        "main_threat": meta["main_threat"],
        "transfer_prompt": meta["transfer_prompt"],
    }


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_menu_rows() -> list[dict[str, str]]:
    return [row_for(key) for key in sorted(ANCHORS)]


def build_selected_rows(anchor_key: str, challenge_key: str, extension_key: str) -> list[dict[str, str]]:
    rows = []
    for role, key in (
        ("primary", anchor_key),
        ("challenge", challenge_key),
        ("extension", extension_key),
    ):
        row = {"role": role, **row_for(key)}
        rows.append(row)
    return rows


def build_memo(anchor_key: str, challenge_key: str, extension_key: str) -> str:
    anchor = ANCHORS[anchor_key]
    challenge = ANCHORS[challenge_key]
    extension = ANCHORS[extension_key]

    return f"""# Week 10 institutions-and-labor research-design memo

## Anchor selection

- Primary anchor: `{anchor_key}` ({anchor["label"]})
- Challenge anchor: `{challenge_key}` ({challenge["label"]})
- Optional extension anchor: `{extension_key}` ({extension["label"]})
- Studio logic: Reproduce -> Diagnose -> Transfer

## 1. Labor outcome

Primary anchor outcome:
{anchor["labor_outcome"]}

Your project:
Replace this sentence with the labor-market outcome you want to explain.

## 2. Institutional mechanism

Primary mechanism:
{anchor["institutional_mechanism"]}

Challenge mechanism:
{challenge["institutional_mechanism"]}

Your project:
Name the institutional channel and one alternative explanation.

## 3. Setting and leverage

Primary comparison:
{anchor["comparison"]}

Optional extension comparison:
{extension["comparison"]}

Your project:
Explain why the setting gives leverage on a broader labor question.

## 4. Counterfactual

Your project:
Define the comparison group, untreated group, less exposed group, boundary neighbor, pre-reform period, or alternative regime.

## 5. Data source

Primary data logic:
{anchor["data"]}

Your project:
Name the data source and say whether it observes both the labor outcome and the institutional mechanism.

## 6. Identification strategy

Primary design:
{anchor["design"]}

Challenge design:
{challenge["design"]}

Your project:
State the identifying variation, estimand, and one threat.

## 7. Portability claim

Primary portability claim:
{anchor["portability_claim"]}

Optional extension portability claim:
{extension["portability_claim"]}

Your project:
State what should travel, what is local, and which institutional complements matter.

## 8. Welfare or distributional object

Primary welfare object:
{anchor["welfare_object"]}

Your project:
State whose welfare, protection, bargaining power, mobility, risk, or income distribution the project speaks to.

## 9. Main threats

Primary threat:
{anchor["main_threat"]}

Challenge threat:
{challenge["main_threat"]}

Your project:
Add the two threats that a skeptical seminar participant would ask first.

## Transfer exercise

Primary transfer prompt:
{anchor["transfer_prompt"]}

Challenge transfer prompt:
{challenge["transfer_prompt"]}

Optional extension transfer prompt:
{extension["transfer_prompt"]}

Your project:
Write a five-sentence abstract using the sequence: outcome, mechanism, setting, design, portability, welfare.

## Quick checklist

- [ ] I start from a labor outcome.
- [ ] I name the institutional mechanism.
- [ ] I define the counterfactual.
- [ ] I explain why the setting provides leverage.
- [ ] I state what data observe.
- [ ] I state the identifying variation and main threat.
- [ ] I distinguish mechanism portability from estimate portability.
- [ ] I state a welfare or distributional object.
"""


def main() -> None:
    args = parse_args()
    outdir = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    write_csv(outdir / "anchor_menu.csv", build_menu_rows(), FIELDS)
    write_csv(
        outdir / "selected_anchor_diagnostic.csv",
        build_selected_rows(args.anchor, args.challenge, args.extension),
        ["role", *FIELDS],
    )
    (outdir / "research_design_memo.md").write_text(
        build_memo(args.anchor, args.challenge, args.extension),
        encoding="utf-8",
    )

    print(f"Wrote Week 10 research-design studio artifacts to {outdir}")


if __name__ == "__main__":
    main()
