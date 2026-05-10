# Code Lab 1: What Is Behavioral Labor?

**Course:** Behavioral Labor  
**Module / Week:** Week 1 -- What Is Behavioral Labor?  
**Associated chapter:** `01-what-is-behavioral-labor.md`  
**Lab slug:** `01-what-is-behavioral-labor`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@royerStehrSydnor2015]  
**Secondary / challenge anchor:** [@altmannFalkJaegerZimmermann2018]  
**Optional frontier anchor:** [@bertrandKamenicaPan2015]  

## Why This Lab Exists

Week 1 teaches students to classify behavioral labor evidence before they over-interpret it. The bounded path uses synthetic data to practice three moves:

1. **Reproduce** a compact Royer-Stehr-Sydnor-style worker wellness factbook.
2. **Diagnose** whether the design speaks to incentives, commitment demand, habit formation, or welfare.
3. **Transfer** the classification logic to job search information and motivation.

The lab does not require confidential employer records or official replication packages.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small behavioral labor factbook from local synthetic data;
2. identify the labor margin moved by an intervention;
3. distinguish a reduced-form treatment effect from a behavioral mechanism;
4. explain why commitment demand is informative about dynamic self-control but not a complete welfare claim;
5. transfer the same diagnostic framework to a job-search information intervention.

## Local Structure

```text
labs/01-what-is-behavioral-labor/
  lab.md
  smoke.sh
  src/
    build_week1_synthetic_data.py
    reproduce_royer_stehr_sydnor.py
    transfer_altmann_job_search.py
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
conda run -n research python src/build_week1_synthetic_data.py

conda run -n research python src/reproduce_royer_stehr_sydnor.py \
  --input original/reduced/royer_stehr_sydnor_worker_wellness_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_altmann_job_search.py \
  --input transfer/data/altmann_job_search_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/arm_summary.csv`
- `output/reproduced/program_effects.csv`
- `output/reproduced/reproduction_worker_wellness.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the treatment variation?
- Which labor margin moves during the program period?
- What does commitment take-up reveal that a simple incentive contrast would not reveal?
- What would be needed before calling the post-program pattern habit formation?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Benchmark:** What would a standard incentive model predict?
2. **Wedge:** Which behavioral object is plausible: present bias, commitment demand, habit formation, or attention?
3. **Margin:** Is the identified margin participation, persistence, take-up, or welfare?
4. **Caution:** What standard alternative or equilibrium response remains?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/search_arm_summary.csv`
- `output/transfer/search_effects.csv`
- `output/transfer/transfer_job_search.png`
- `output/transfer/transfer_note.txt`

Use the same classification logic for the job-search intervention inspired by [@altmannFalkJaegerZimmermann2018]. State whether the design most directly identifies beliefs, motivation, attention, or a reduced-form search response.

## Challenge

Use [@bertrandKamenicaPan2015] to sketch how the same Week 1 taxonomy would classify identity and household labor allocation. Do not estimate anything. State the benchmark, wedge, labor margin, evidence, and welfare caution.

## Deliverables Checklist

- [ ] run log
- [ ] reproduction figure
- [ ] arm-summary and effect CSVs
- [ ] one-page design memo
- [ ] transfer figure and tables
- [ ] short paragraph distinguishing treatment effects, mechanisms, welfare, and response

