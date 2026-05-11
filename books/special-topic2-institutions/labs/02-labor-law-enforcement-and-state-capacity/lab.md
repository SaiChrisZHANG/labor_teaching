# Code Lab 2: Labor Law, Enforcement, and State Capacity

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 2 -- Labor Law, Enforcement, and State Capacity  
**Associated chapter:** `02-labor-law-enforcement-and-state-capacity.md`  
**Lab slug:** `02-labor-law-enforcement-and-state-capacity`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@almeidaCarneiro2012]  
**Secondary / challenge anchor:** [@autorDonohueSchwab2004]  
**Optional extension anchor:** [@bertrandCrepon2021]  

## Why This Lab Exists

Week 2 asks students to separate law on the books from effective law in practice. The lab uses synthetic data to practice three moves:

1. **Reproduce** a compact enforcement-and-informality pattern in the spirit of [@almeidaCarneiro2012].
2. **Diagnose** whether an empirical design identifies law, enforcement, knowledge, or effective compliance.
3. **Transfer** the same classification to new labor standards and implementation settings.

The lab is a teaching analog. It is not an official replication of any anchor paper.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small synthetic locality-year panel where enforcement changes compliance, benefits, wages, and formality;
2. distinguish legal rules, enforcement intensity, worker knowledge, realized compliance, and labor-market incidence in a data table;
3. explain why [@almeidaCarneiro2012] identifies enforcement more directly than law on the books;
4. compare the enforcement object to the court-made legal variation in [@autorDonohueSchwab2004];
5. transfer the Week 2 framework to another labor standard, worker-information treatment, or administrative-data design.

## Local Structure

```text
labs/02-labor-law-enforcement-and-state-capacity/
  lab.md
  smoke.sh
  src/
    build_week2_synthetic_data.py
    reproduce_enforcement_informality.py
    transfer_design_classifier.py
  original/
    source-notes.md
    reduced/
  transfer/
    data-notes.md
    data/
  output/
    reproduced/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week2_synthetic_data.py

conda run -n research python src/reproduce_enforcement_informality.py \
  --input original/reduced/enforcement_informality_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_design_classifier.py \
  --input transfer/data/implementation_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/enforcement_summary.csv`
- `output/reproduced/enforcement_by_tier.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the legal rule on the books?
- What varies in enforcement intensity?
- What role does worker knowledge play?
- Which observed margins are compliance, benefits, wages, and formality?
- Why should this factbook not be interpreted as a causal estimate without a stronger design?

## Part II. Diagnose

Write a short design memo comparing two objects:

1. **Almeida-Carneiro object:** effective labor regulation through inspection exposure, with informality and wage incidence as observed labor margins [@almeidaCarneiro2012].
2. **Autor-Donohue-Schwab object:** wrongful-discharge doctrine as court-made legal variation, with employment-sensitive margins as observed labor outcomes [@autorDonohueSchwab2004].

Use the following checklist:

- Does the design identify law on the books, enforcement, knowledge, or effective compliance?
- What is the unit of observation?
- Which labor-market margin is observed?
- Which implementation margin remains unobserved?
- What equilibrium response could change interpretation?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_object_counts.csv`
- `output/transfer/transfer_note.txt`

For each transfer design, state whether the design identifies:

- law on the books;
- enforcement;
- worker knowledge;
- effective compliance;
- broad state-capacity or labor-rights bundles;
- incidence and sorting.

Then propose one bounded transfer:

1. apply an inspection-intensity design to a different labor standard;
2. compare formalization versus wage incidence margins;
3. compare information and enforcement as separate implementation treatments.

## Challenge

Design a new synthetic panel for one labor standard: overtime, wage theft, severance, paid leave, anti-retaliation, or safety. Include one law-on-the-books variable, one enforcement variable, one knowledge variable, one compliance variable, and two labor outcomes.

## Deliverables Checklist

- [ ] reproduced enforcement summary CSV
- [ ] reproduced enforcement-tier CSV
- [ ] one-page diagnosis memo
- [ ] transfer classification CSV
- [ ] short paragraph distinguishing law, enforcement, knowledge, compliance, and incidence
