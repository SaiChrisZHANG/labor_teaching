# Code Lab 3: Informality, Dualism, and Contract Enforcement

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 3 -- Informality, Dualism, and Contract Enforcement  
**Associated chapter:** `03-informality-dualism-and-contract-enforcement.md`  
**Lab slug:** `03-informality-dualism-and-contract-enforcement`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@ulyssea2018]  
**Secondary / challenge anchor:** [@meghirNaritaRobin2015]  
**Optional extension anchor:** [@samaniegoParraFernandezBujanda2024]  

## Why This Lab Exists

Week 3 treats informality as a two-sided labor-market institution. The lab uses synthetic data to practice three moves:

1. **Reproduce** a compact firm-side registration and payroll-reporting pattern in the spirit of [@ulyssea2018].
2. **Diagnose** whether an empirical design identifies worker sorting, firm registration, payroll compliance, wage-setting, contract enforceability, or equilibrium reallocation.
3. **Transfer** the same classification to worker-transition, enforcement, policy-discontinuity, and historical contract-enforcement settings.

The lab is a teaching analog. It is not an official replication of any anchor paper.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small synthetic firm-year panel where productivity, enforcement, and payroll costs predict registration and hidden employment;
2. distinguish firm registration, payroll reporting, benefit value, wage-setting, and contract enforceability in a data table;
3. explain why [@ulyssea2018] is a firm-side equilibrium anchor rather than a worker-only informality paper;
4. compare the firm-side object to the worker sorting and wage-setting object in [@meghirNaritaRobin2015];
5. transfer the Week 3 framework to an enforcement setting such as [@samaniegoParraFernandezBujanda2024].

## Local Structure

```text
labs/03-informality-dualism-and-contract-enforcement/
  lab.md
  smoke.sh
  src/
    build_week3_synthetic_data.py
    reproduce_firm_informality.py
    transfer_margin_classifier.py
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
conda run -n research python src/build_week3_synthetic_data.py

conda run -n research python src/reproduce_firm_informality.py \
  --input original/reduced/firm_informality_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_margin_classifier.py \
  --input transfer/data/informality_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/firm_margin_summary.csv`
- `output/reproduced/margins_by_enforcement.csv`
- `output/reproduced/margins_by_registration.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which variable represents firm registration?
- Which variable represents payroll reporting?
- Which variable represents hidden employment inside registered firms?
- Where do enforcement intensity, payroll costs, and productivity enter?
- Why is this a firm-side informality object rather than a worker-only object?

## Part II. Diagnose

Write a short design memo comparing two objects:

1. **Ulyssea object:** firms choose registration, payroll reporting, hidden employment, size, and compliance under enforcement and productivity heterogeneity [@ulyssea2018].
2. **Meghir-Narita-Robin object:** worker-firm matching, search, wages, and informality are jointly determined in equilibrium [@meghirNaritaRobin2015].

Use the following checklist:

- Does the design identify worker sorting, firm response, wage-setting, contract enforceability, formalization, or welfare?
- What is the unit of observation?
- Which labor-market margin is observed?
- Which side of the market is moving most clearly?
- What equilibrium response could change interpretation?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_object_counts.csv`
- `output/transfer/transfer_note.txt`

For each transfer design, state whether the design identifies:

- worker sorting;
- firm compliance or registration;
- wage-setting;
- contract enforceability;
- formalization;
- equilibrium reallocation;
- welfare under policy change.

Then propose one bounded transfer:

1. compare worker-side and firm-side incidence in a compliance setting;
2. compare dualist and equilibrium interpretations in one empirical setting;
3. adapt a worker-transition exercise to a firm-formalization setting.

## Challenge

Design a new synthetic panel with both a worker state and a firm state. Include one worker-side formality measure, one firm registration measure, one payroll-reporting measure, one benefit-valuation measure, and two labor outcomes. State which variable would move under an enforcement shock and which variable would move under a benefit-design shock.

## Deliverables Checklist

- [ ] reproduced firm margin summary CSV
- [ ] enforcement-tier summary CSV
- [ ] registration-status summary CSV
- [ ] one-page diagnosis memo
- [ ] transfer classification CSV
- [ ] short paragraph naming the observed margin and identifying variation
