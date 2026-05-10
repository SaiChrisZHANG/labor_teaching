# Code Lab 7: Experiments, Measurement, and Behavioral Identification in Labor

**Course:** Behavioral Labor  
**Module / Week:** Week 7 -- Experiments, Measurement, and Behavioral Identification in Labor  
**Associated chapter:** `07-experiments-measurement-and-behavioral-identification-in-labor.md`  
**Lab slug:** `07-experiments-measurement-and-behavioral-identification-in-labor`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@altmannFalkJaegerZimmermann2018]  
**Secondary / challenge anchor:** [@dellaVignaListMalmendierRao2022]  
**Optional extension anchor:** [@chettyFriedmanSaez2013] or [@kaurKremerMullainathan2015]  

## Why This Lab Exists

Week 7 trains the empirical move from behavioral object to labor setting to data design to econometric method. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact job-search information experiment inspired by [@altmannFalkJaegerZimmermann2018].
2. **Diagnose** the behavioral object, labor margin, identifying variation, estimator, assumptions, and interpretation.
3. **Transfer** the same design-to-method logic to workplace gift exchange, structural moments, and nonlinear schedules.

The lab does not require confidential unemployment, tax, employer, or official replication data.

## Learning Objectives

By the end of the lab, students should be able to:

1. estimate simple experimental contrasts and ANCOVA-style adjusted effects;
2. summarize a discrete-time hazard object for unemployment exit;
3. distinguish beliefs, salience, procedural knowledge, and motivation in an information intervention;
4. classify a design as reduced form, measurement-based, quasi-experimental, or structural;
5. state which empirical method fits a repeated beliefs panel, search-duration setting, nonlinear schedule, or parameter-recovery problem;
6. transfer a behavioral design to a nearby labor setting and name the method they would actually estimate.

## Local Structure

```text
labs/07-experiments-measurement-and-behavioral-identification-in-labor/
  lab.md
  smoke.sh
  src/
    build_week7_synthetic_data.py
    reproduce_information_design.py
    transfer_method_bridge.py
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
conda run -n research python src/build_week7_synthetic_data.py

conda run -n research python src/reproduce_information_design.py \
  --worker-input original/reduced/job_search_information_synthetic.csv \
  --duration-input original/reduced/job_search_duration_panel_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_method_bridge.py \
  --gift-input transfer/data/gift_exchange_method_synthetic.csv \
  --schedule-input transfer/data/schedule_bunching_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/information_rct_summary.csv`
- `output/reproduced/information_treatment_effects.csv`
- `output/reproduced/duration_hazard_summary.csv`
- `output/reproduced/information_reproduction.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the behavioral object: belief level, salience, procedural knowledge, motivation, or a bundle?
- Which labor margin moves: applications, search planning, unemployment exit, or duration?
- Which estimator is natural for the worker-level outcomes: OLS, ANCOVA, randomization inference, or heterogeneity analysis?
- Which estimator is natural for the spell outcome: discrete-time hazard, Cox-style hazard, or a simpler reduced-form exit contrast?
- What identifying assumptions make the treatment effect interpretable?

## Part II. Diagnose

Write a short design-to-method memo with six paragraphs:

1. **Behavioral object:** What is the object that the intervention or measurement tries to move?
2. **Observed margin:** Which labor outcome is actually observed?
3. **Identifying variation:** What varies across workers or time?
4. **Econometric method:** What would you estimate first, and why does it fit the data structure?
5. **Identifying assumptions:** What has to be true for the interpretation to hold?
6. **Interpretation limit:** Is the evidence reduced form, measurement-based, quasi-experimental, or structural?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/gift_exchange_method_summary.csv`
- `output/transfer/gift_exchange_moment_targets.csv`
- `output/transfer/schedule_bunching_summary.csv`
- `output/transfer/schedule_local_elasticity.csv`
- `output/transfer/method_bridge_transfer.png`
- `output/transfer/transfer_note.txt`

Use [@dellaVignaListMalmendierRao2022] to classify the gift-exchange transfer. Which moments would identify a reciprocity or social-preference parameter? When would OLS treatment effects be enough, and when would MLE or SMM be useful?

Then use [@chettyFriedmanSaez2013] or [@kaurKremerMullainathan2015] for the challenge transfer. Does the design require bunching, a local elasticity, a hazard model, a panel model, or structural parameter recovery?

## Challenge

Propose one bounded transfer design:

- job-search reminders for long-duration unemployment;
- benefit take-up with unclear eligibility;
- nonlinear earnings schedules with poor worker knowledge;
- workplace gift exchange with repeated effort tasks;
- self-control at work with commitment contracts;
- remote-work productivity feedback and salience.

For the chosen setting, state the behavioral object, labor margin, identifying variation, estimand, method, and welfare limit.

## Deliverables Checklist

- [ ] run log
- [ ] information-experiment summary table
- [ ] ANCOVA-style treatment-effect table
- [ ] duration hazard summary
- [ ] one-page design-to-method memo
- [ ] transfer moment table for gift exchange
- [ ] schedule-response summary
- [ ] short transfer paragraph naming the method and interpretation limit
