# Code Lab 7: Institutional Persistence, Path Dependence, and Historical Labor-Market Inequality

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 7 -- Institutional Persistence, Path Dependence, and Historical Labor-Market Inequality  
**Associated chapter:** `07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.md`  
**Lab slug:** `07-institutional-persistence-path-dependence-and-historical-labor-market-inequality`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@dell2010mita]  
**Secondary / challenge anchor:** [@naiduYuchtman2013coercive]  
**Optional extension anchors:** [@markevichZhuravskaya2018serfdom]; [@jonesSchmick2025reconstruction]  

## Why This Lab Exists

Week 7 asks students to discipline historical persistence claims. The lab uses deterministic synthetic data to practice three moves:

1. **Reproduce** a reduced Dell-style boundary comparison inspired by [@dell2010mita].
2. **Diagnose** whether a persistence claim is serial correlation, path dependence, or institutional persistence through a labor-market mechanism.
3. **Transfer** the diagnostic language to coercive contract enforcement, abolition, schooling, war shocks, forced migration, and slavery legacies.

This is a teaching analog. It is not an official replication of any anchor paper and does not use confidential or heavy archival data.

## Learning Objectives

By the end of the lab, students should be able to:

1. summarize treated and control places in a historical boundary design;
2. separate outcome differences from mechanism evidence;
3. classify persistence claims by mechanism strength and overclaiming risk;
4. explain what a coercive contract-enforcement design identifies;
5. transfer the same diagnostic language to new historical labor settings.

## Local Structure

```text
labs/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality/
  lab.md
  smoke.sh
  src/
    build_week7_synthetic_data.py
    reproduce_mita_boundary.py
    diagnose_persistence_mechanism.py
    transfer_historical_design_classifier.py
  original/
    source-notes.md
    reduced/
  transfer/
    data-notes.md
    data/
  output/
    reproduced/
    diagnostics/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week7_synthetic_data.py

conda run -n research python src/reproduce_mita_boundary.py \
  --input original/reduced/mita_boundary_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_persistence_mechanism.py \
  --input original/reduced/persistence_claims_synthetic.csv \
  --outdir output/diagnostics

conda run -n research python src/transfer_historical_design_classifier.py \
  --input transfer/data/historical_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and the Dell-style boundary script. Inspect:

- `output/reproduced/boundary_summary.csv`
- `output/reproduced/near_boundary_summary.csv`
- `output/reproduced/mechanism_differences.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which labor outcomes differ across exposed and comparison districts?
- Are the differences larger or smaller near the historical boundary?
- Which mechanism variables might connect historical exposure to modern labor outcomes?
- Why is this not enough, by itself, to prove institutional persistence?

## Part II. Diagnose

Run the diagnostic script. Inspect:

- `output/diagnostics/persistence_diagnostic.csv`
- `output/diagnostics/claim_type_counts.csv`
- `output/diagnostics/risk_level_counts.csv`
- `output/diagnostics/diagnostic_note.txt`

Use the following checklist:

- Is the claim serial correlation, path dependence, or institutional persistence through a labor channel?
- What is the first moving labor margin?
- What persistent fundamental could mimic the result?
- What data-source weakness matters most?
- Would you trust the claim as written, or require mechanism evidence?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_family_counts.csv`
- `output/transfer/transfer_note.txt`

For each transfer design, state whether it identifies:

- a historical border or discontinuity effect;
- coercive contract-enforcement effects on quitting costs and wages;
- abolition or reform effects on mobility, competition, or schooling;
- a war shock to demand, discrimination, or occupational openings;
- linked historical microdata evidence;
- migration, public-goods, or GIS-based persistence channels.

## Challenge

Add one row to `transfer/data/historical_designs_synthetic.csv` for a setting you might study: an internal passport reform, a school desegregation boundary, a mining-region labor draft, a plantation land registry, or a forced-migration settlement shock. Classify the design family, labor mechanism, data source, and main caution. Then write one paragraph explaining what would make the claim overreach.

## Deliverables Checklist

- [ ] boundary summary CSV
- [ ] near-boundary summary CSV
- [ ] mechanism-difference table
- [ ] persistence diagnostic CSV
- [ ] risk-level counts
- [ ] transfer classification CSV
- [ ] one-page memo: "What is the labor mechanism?"
