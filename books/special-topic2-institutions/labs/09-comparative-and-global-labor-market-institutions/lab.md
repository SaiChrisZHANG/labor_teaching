# Code Lab 9: Comparative and Global Labor-Market Institutions

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 9 -- Comparative and Global Labor-Market Institutions  
**Associated chapter:** `09-comparative-and-global-labor-market-institutions.md`  
**Lab slug:** `09-comparative-and-global-labor-market-institutions`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@boteroDjankovLaPortaLopezdeSilanesShleifer2004]  
**Challenge anchor:** [@beerliPeriRuffnerSiegenthaler2021]  
**Optional extension anchor:** [@distelhorstHainmuellerLocke2017]  

## Why This Lab Exists

Week 9 asks how comparative and global labor-market institutions should be studied without treating countries as self-explanatory cases. The lab uses deterministic synthetic data to practice three moves:

1. **Reproduce** a reduced labor-regulation index inspired by [@boteroDjankovLaPortaLopezdeSilanesShleifer2004].
2. **Diagnose** whether a comparative case identifies a portable mechanism, a setting-specific estimate, or only rules on paper.
3. **Transfer** the design logic to migration regimes, welfare-state comparisons, informality settings, and supply-chain governance.

This is a teaching analog. It is not an official replication and does not use confidential administrative microdata, proprietary audit records, or the original cross-country legal coding files.

## Learning Objectives

By the end of the lab, students should be able to:

1. construct and summarize a simple cross-country labor-regulation index;
2. compare a rules-on-paper index with an enforcement-adjusted protection index;
3. name the identifying variation and observed labor margin in comparative research;
4. classify implementation gaps and transportability risks;
5. transfer a country-specific or supply-chain design to a broader comparative taxonomy.

## Local Structure

```text
labs/09-comparative-and-global-labor-market-institutions/
  lab.md
  smoke.sh
  src/
    build_week9_synthetic_data.py
    reproduce_labor_regulation_index.py
    diagnose_transportability.py
    transfer_comparative_design_classifier.py
  original/
    reduced/
  transfer/
    data/
  output/
    reproduced/
    diagnostics/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week9_synthetic_data.py

conda run -n research python src/reproduce_labor_regulation_index.py \
  --input original/reduced/labor_regulation_index_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_transportability.py \
  --input original/reduced/comparative_cases_synthetic.csv \
  --outdir output/diagnostics

conda run -n research python src/transfer_comparative_design_classifier.py \
  --input transfer/data/comparative_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and the regulation-index script. Inspect:

- `output/reproduced/regulation_by_country.csv`
- `output/reproduced/regulation_summary_by_income.csv`
- `output/reproduced/regulation_gap_by_regime.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which countries have high rules-on-paper scores but lower enforcement-adjusted protection?
- How do coverage, membership, and enforcement differ?
- Why is the gap between legal text and effective protection larger in some regimes?
- What can and cannot be learned from cross-country indices alone?

## Part II. Diagnose

Run the diagnostic script. Inspect:

- `output/diagnostics/transportability_diagnostic.csv`
- `output/diagnostics/implementation_gap_counts.csv`
- `output/diagnostics/portability_risk_counts.csv`
- `output/diagnostics/diagnostic_note.txt`

Use the following checklist:

- What is the comparison unit: country, region, firm, worker group, border zone, or supply chain?
- What identifies the effect?
- What labor margin is observed?
- Is the paper learning a mechanism, an estimate, or a measurement fact?
- Which institutional complement limits portability?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_family_counts.csv`
- `output/transfer/transfer_note.txt`

For each design, state whether it identifies:

- cross-country rules-on-paper variation;
- within-country reform timing with comparative interpretation;
- border or region exposure to a migration regime;
- comparative administrative microdata across regimes;
- supply-chain audit, certification, or buyer-governance exposure;
- historical-comparative institutional classification.

## Challenge

Add one row to `transfer/data/comparative_designs_synthetic.csv` for a country or institutional setting you might study. It can be a migration opening, bargaining extension, informality enforcement campaign, social-insurance reform, or supply-chain audit regime. Classify the design family, identifying variation, observed labor margin, portability claim, and main caution. Then write one paragraph explaining what travels beyond the setting and what does not.

## Deliverables Checklist

- [ ] regulation-by-country CSV
- [ ] regulation summary by income group
- [ ] regime gap table
- [ ] transportability diagnostic CSV
- [ ] implementation-gap counts
- [ ] transfer design classification CSV
- [ ] one-page memo: "What travels from this setting?"
