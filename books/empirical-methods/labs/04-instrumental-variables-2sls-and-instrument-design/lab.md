# Code Lab 04: Instrumental Variables, 2SLS, And Instrument Design

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 4 - instrumental variables, 2SLS, and instrument design  
**Associated chapter:** `04-instrumental-variables-2sls-and-instrument-design.md`  
**Lab slug:** `04-instrumental-variables-2sls-and-instrument-design`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** potential outcomes, basic regression, matrix notation, basic `pandas`  
**Core economic question:** What variation does an instrument isolate, for whom, and under which assumptions?  
**Core design / estimator:** first stage, reduced form, Wald IV, 2SLS, weak-IV diagnostics, complier interpretation, leave-out leniency diagnosis, and shift-share transfer diagnostics  
**Source paper spine:** Angrist and Krueger [@angrist1991], Oreopoulos [@oreopoulos2006], Autor, Kostol, Mogstad, and Setzler [@autorKostolMogstadSetzler2019], Adao, Kolesar, and Morales [@adaoKolesarMorales2019], and Borusyak, Hull, and Jaravel [@borusyakHullJaravel2022]

## Why This Lab Exists

The lecture argues that IV is a design logic, not just a regression recipe. This lab makes that claim executable. Students first work through a compulsory-schooling-style instrument where the first stage, reduced form, Wald ratio, and 2SLS estimate are all visible. They then diagnose the instrument as an applied researcher would: relevance, balance, exclusion threats, weak-IV diagnostics, and complier interpretation. The diagnosis memo explicitly compares the rule-based design to leave-out judge leniency: what random assignment must look like, why leave-one-out construction helps, and why exclusion can still fail. Finally, students transfer the same logic to a shift-share design.

The lab does not reproduce official published magnitudes. It reproduces design logic: what the instrument moves, what it identifies, what can go wrong, and what the estimate means.

## Learning Objectives

By the end of this lab, students should be able to:

1. estimate and interpret a first stage, reduced form, Wald ratio, and 2SLS coefficient;
2. explain why OLS and IV can differ when treatment is endogenous;
3. compute and interpret a partial first-stage `F` statistic;
4. describe compliers and explain why IV is local under heterogeneous effects;
5. diagnose balance and exclusion concerns for a rule-based instrument;
6. construct a shift-share instrument from exposure shares and shocks;
7. explain why shift-share inference and interpretation depend on the shock structure and exposure shares.

## Required Local Structure

```text
labs/04-instrumental-variables-2sls-and-instrument-design/
  README.md
  lab.md
  run-log.md
  smoke.sh
  environment/
    requirements.txt
  original/
    README.md
    source-notes.md
    reduced/
      compulsory_schooling_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      shift_share_places.csv
      sector_shocks.csv
  src/
    make_synthetic_data.py
    reproduce_iv_design.py
    transfer_shift_share_design.py
  output/
    reproduced/
    transfer/
```

## First Commands To Run

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs three steps:

```bash
python src/make_synthetic_data.py
python src/reproduce_iv_design.py --input original/reduced/compulsory_schooling_synthetic.csv --outdir output/reproduced
python src/transfer_shift_share_design.py --places transfer/data/shift_share_places.csv --shocks transfer/data/sector_shocks.csv --outdir output/transfer
```

## Part I. Reproduce The IV Logic

### Objective

Estimate what a compulsory-schooling-style instrument identifies.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path and open `output/reproduced/iv_estimates.csv`.
3. Compare the naive OLS estimate, first stage, reduced form, unadjusted Wald ratio, and adjusted 2SLS estimate.
4. Open `output/reproduced/first_stage_diagnostics.csv` and inspect the partial first-stage `F` statistic.
5. Write the interpretation sentence as a complier effect.

### Required Questions

- What is the treatment?
- What is the instrument?
- Why is treatment endogenous?
- What does the first stage mean economically?
- What does the reduced form measure?
- Why is the IV estimate local?

### Minimum Output

- `output/reproduced/iv_estimates.csv`;
- one paragraph describing the instrument and first stage;
- one sentence interpreting the IV estimate as a complier effect;
- one sentence explaining what the estimate does not identify.

## Part II. Diagnose The Instrument

### Objective

Evaluate the instrument as a research design.

### Student Tasks

1. Open `output/reproduced/balance_by_instrument.csv`.
2. Open `output/reproduced/complier_profile.csv`.
3. Open `output/reproduced/first_stage_by_cell.csv`.
4. Inspect `output/reproduced/treatment_by_instrument.png`.
5. Write a one-page Diagnose memo.

### Required Prompts

- Is the first stage strong in statistical and economic terms?
- Which observable covariates differ by instrument status?
- Who are the synthetic compliers?
- What is the most plausible exclusion threat?
- How would the same diagnostic logic apply to a leave-out judge-leniency instrument?
- At what level would inference be clustered in a real rule-based design?
- How would weak-IV robust inference change the way you report uncertainty?

### Minimum Output

- one first-stage paragraph;
- one balance paragraph;
- one complier paragraph;
- one exclusion-threat paragraph;
- one final interpretation sentence naming the estimand.

## Part III. Transfer To Shift-Share Design

### Objective

Use the same instrument-evaluation logic in a shift-share setting.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Run `src/transfer_shift_share_design.py`.
3. Open `output/transfer/shift_share_iv_estimates.csv`.
4. Open `output/transfer/shift_share_diagnostics.csv`.
5. Open `output/transfer/shock_level_summary.csv`.
6. Write a short transfer memo.

### Required Prompts

- What are the shares?
- What are the shocks?
- Does identification come from quasi-random shocks, as-good-as-random shares, or both?
- Are any shocks or sectors dominant?
- Are exposure shares correlated with baseline growth?
- Why might geographic clustering be insufficient?
- How would the design differ if this were a leave-out leniency instrument?

### Minimum Output

- shift-share estimate table;
- shock-level summary;
- dominant-exposure diagnostic;
- one paragraph on inference;
- one transfer memo with first-stage logic, exclusion threat, and interpretation.

## Deliverables Checklist

- [ ] run log;
- [ ] IV estimates table;
- [ ] first-stage diagnostics;
- [ ] balance table;
- [ ] complier profile;
- [ ] one-page Diagnose memo;
- [ ] shift-share estimates and diagnostics;
- [ ] transfer design memo;
- [ ] final paragraph stating what the instrument identifies and what it does not.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| First-stage, reduced-form, Wald, and 2SLS interpretation | 25 |
| Weak-IV diagnostic and first-stage content | 20 |
| Complier and LATE interpretation | 20 |
| Exclusion, independence, and balance diagnosis | 15 |
| Shift-share transfer memo | 15 |
| Code organization and communication | 5 |

## Instructor Notes

- The lab is intentionally synthetic so students can focus on design logic before wrestling with official replication-package details.
- The best class discussion asks what the first stage means economically and whether the exclusion restriction is credible.
- The transfer exercise should stay bounded. Students should not turn Week 4 into a full shift-share paper.
