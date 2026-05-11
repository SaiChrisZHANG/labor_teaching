# Code Lab 8: Institutional Reform, Implementation, and Labor-Market Adjustment

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 8 -- Institutional Reform, Implementation, and Labor-Market Adjustment  
**Associated chapter:** `08-institutional-reform-implementation-and-labor-market-adjustment.md`  
**Lab slug:** `08-institutional-reform-implementation-and-labor-market-adjustment`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@bertrandCrepon2021]  
**Challenge anchor:** [@almeidaCarneiro2012]  
**Optional extension anchor:** [@bakerHalberstamKroftMasMessacar2023]  

## Why This Lab Exists

Week 8 asks why reforms do not travel mechanically from legal text to labor-market outcomes. The lab uses deterministic synthetic data to practice three moves:

1. **Reproduce** a reduced legal-information experiment inspired by [@bertrandCrepon2021].
2. **Diagnose** where a reform stalls in the transmission chain: implementation, knowledge, exposure, firm adaptation, worker response, or equilibrium spillovers.
3. **Transfer** the same language to enforcement, formalization, dismissal protection, transparency, and administrative reform.

This is a teaching analog. It is not an official replication and does not use confidential worker, firm, enforcement, or administrative data.

## Learning Objectives

By the end of the lab, students should be able to:

1. summarize treatment and comparison groups in a legal-information intervention;
2. separate knowledge effects from labor-market outcome effects;
3. identify the observed labor margin in a reform paper;
4. classify reform bottlenecks and welfare risks;
5. transfer a reform-transmission checklist to a new institutional setting.

## Local Structure

```text
labs/08-institutional-reform-implementation-and-labor-market-adjustment/
  lab.md
  smoke.sh
  src/
    build_week8_synthetic_data.py
    reproduce_legal_information_trial.py
    diagnose_reform_transmission.py
    transfer_reform_design_classifier.py
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
conda run -n research python src/build_week8_synthetic_data.py

conda run -n research python src/reproduce_legal_information_trial.py \
  --input original/reduced/legal_information_trial_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_reform_transmission.py \
  --input original/reduced/reform_cases_synthetic.csv \
  --outdir output/diagnostics

conda run -n research python src/transfer_reform_design_classifier.py \
  --input transfer/data/reform_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and the legal-information script. Inspect:

- `output/reproduced/legal_information_summary.csv`
- `output/reproduced/treatment_differences.csv`
- `output/reproduced/heterogeneity_by_baseline_knowledge.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Did the intervention move knowledge more than labor outcomes?
- Which outcomes are beliefs, and which are realized labor margins?
- Are effects larger for workers with low baseline legal knowledge?
- Why does a legal-information effect not equal the full effect of labor law?

## Part II. Diagnose

Run the diagnostic script. Inspect:

- `output/diagnostics/reform_transmission_diagnostic.csv`
- `output/diagnostics/bottleneck_counts.csv`
- `output/diagnostics/welfare_margin_counts.csv`
- `output/diagnostics/diagnostic_note.txt`

Use the following checklist:

- What changed: rights, information, procedures, enforcement, or administration?
- Which workers and firms are exposed?
- What is the observed labor margin?
- What prevents mechanical take-up or compliance?
- What welfare margin is easiest to miss?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_family_counts.csv`
- `output/transfer/transfer_note.txt`

For each transfer design, state whether it identifies:

- staggered adoption of a legal rule;
- enforcement-intensity effects on compliance and informality;
- randomized information or assistance effects;
- threshold or coverage effects;
- procedural or transparency effects on hiring and pay;
- administrative rollout effects on matching and job-finding.

## Challenge

Add one row to `transfer/data/reform_designs_synthetic.csv` for a reform you might study: a payroll-tax enforcement expansion, a pay-transparency mandate, a dismissal-protection exemption cutoff, a legal aid rollout, or a public employment-service reorganization. Classify the design family, observed margin, likely spillover, and main caution. Then write one paragraph explaining which part of the reform-transmission chain the design does not identify.

## Deliverables Checklist

- [ ] legal-information summary CSV
- [ ] treatment-difference table
- [ ] heterogeneity-by-baseline-knowledge table
- [ ] reform-transmission diagnostic CSV
- [ ] bottleneck counts
- [ ] transfer design classification CSV
- [ ] one-page memo: "Where does the reform bind?"
