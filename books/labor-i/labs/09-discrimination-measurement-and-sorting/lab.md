# Code Lab 09: Discrimination, Measurement, and Sorting

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 9 --- Discrimination, measurement, and sorting  
**Associated chapter:** `09-discrimination-measurement-and-sorting.md`  
**Lab slug:** `09-discrimination-measurement-and-sorting`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 4, 5, and 8; basic command-line use; introductory `pandas`; and comfort with grouped summaries and simple plots  
**Core economic question:** How should labor economists move from observed group gaps to disciplined discrimination objects, and how do average treatment effects differ from employer-level and sorting-oriented measurement?  
**Core design / estimator:** bounded correspondence-study reproduction plus a synthetic employer report-card transfer exercise  
**Source paper for reproduction:** Bertrand, Marianne, and Sendhil Mullainathan. 2004. *Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination.* *American Economic Review* 94(4): 991--1013.  
**Secondary / challenge anchor:** Kline, Patrick, Evan K. Rose, and Christopher R. Walters. 2024. *A Discrimination Report Card.* *American Economic Review* 114(8): 2472--2525.  
**Optional frontier extension anchor:** Hurst, Erik, Yona Rubinstein, and Kazuatsu Shimizu. 2024. *Task-Based Discrimination.* *American Economic Review* 114(6): 1723--1768.  

## Why this lab exists

Week 9 is the course's discrimination-architecture week. The bounded lab turns that architecture into a local workflow. Students first reproduce callback-gap objects from a synthetic correspondence-study file in the spirit of `@bertrandMullainathan2004`, then diagnose what those objects do and do not identify, and finally transfer the workflow to synthetic employer-level report cards in the spirit of `@klineRoseWalters2024`.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce an average callback-gap estimate from a bounded correspondence-study dataset;
2. explain why a hiring-stage treatment effect is narrower than a general labor-market discrimination object;
3. compare raw callback gaps with qualification-adjusted and segment-specific gaps;
4. transfer the workflow to employer-level discrimination measurement and explain why ranking uncertainty matters;
5. state how sorting and task assignment extend the Week 9 measurement problem beyond the callback stage.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact callback-gap factbook only.
- Diagnose the design in a short memo or notebook cell block.
- Transfer the workflow to one synthetic employer report-card exercise only.
- Keep the smoke path fully local and synthetic.
- Treat the task-based extension as conceptual unless the instructor assigns more advanced work.

## Lab roadmap

1. **Reproduce** a synthetic correspondence-study callback-gap summary.
2. **Diagnose** what the treatment effect identifies and what remains outside the design.
3. **Transfer** the workflow to employer-level report cards.
4. **Reflect** on how sorting and segmentation expand the discrimination problem.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship the original field-experiment resumes, a real employer experiment, or proprietary employer microdata. Instead, it builds deterministic synthetic teaching files that preserve the logic of callback-gap estimation and firm-level report-card measurement.

### Required local structure

```text
labs/09-discrimination-measurement-and-sorting/
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
      bertrand_mullainathan_callback_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      employer_report_card_synthetic.csv
  src/
    build_week9_synthetic_data.py
    reproduce_bertrand_mullainathan.py
    transfer_discrimination_report_cards.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week9_synthetic_data.py

conda run -n research python src/reproduce_bertrand_mullainathan.py \
  --input original/reduced/bertrand_mullainathan_callback_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_discrimination_report_cards.py \
  --input transfer/data/employer_report_card_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded callback-gap summary from a synthetic correspondence-study dataset.

### Student tasks

1. Run `src/build_week9_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/bertrand_mullainathan_callback_synthetic.csv`.
4. Inspect the callback-rate, segment-gap, and resume-quality outputs in `output/reproduced/`.
5. Write a short note on why the reproduced callback effect is a discrimination object at one margin rather than a universal discrimination measure.

### Required questions

- What is the treatment variation in the bounded correspondence design?
- Why is the callback effect narrower than a wage-gap estimate among employed workers?
- How do resume quality and firm segment change the interpretation of an average callback gap?
- What remains unobserved about post-callback sorting, task assignment, or promotion?

### Minimum output

- one reproduced figure;
- one callback summary CSV;
- one segment-gap CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "there is a callback gap" to a disciplined statement about what the design actually identifies.

### Student tasks

1. Distinguish the correspondence-study treatment effect from a regression residual in an observational wage dataset.
2. Explain why the same callback gap could still be consistent with different underlying mechanisms.
3. State one way in which post-treatment controls can distort discrimination inference.
4. Explain why selection into application pools complicates broader equilibrium interpretation.

### Minimum output

- a one-page design memo;
- one paragraph on the estimand;
- one paragraph on what remains outside the design;
- one paragraph linking the design to Week 8 sorting and Week 10 mobility.

## Part III. Transfer

### Objective

Use the same Week 9 logic on a synthetic employer-level report-card dataset.

### Bounded transfer path

Run `src/transfer_discrimination_report_cards.py` on the synthetic employer dataset and estimate firm-specific callback gaps, standard errors, and shrunken report-card scores.

### Student tasks

1. Produce one main transfer figure.
2. Save the employer report-card summary table.
3. Save the firm-ranking table.
4. Write a short paragraph explaining why employer rankings are noisy even with randomized treatment.
5. State how the transfer step broadens the Week 9 conversation beyond one average callback effect.

### Scope constraints

- Keep the same Week 9 empirical family.
- Produce one main figure and compact summary tables.
- Do not add external data pulls or proprietary files.
- Keep the transfer discussion focused on firm heterogeneity, uncertainty, and interpretation.

## Part IV. Optional frontier extension

Use `@hurstRubinsteinShimizu2024` to write a short note on how discrimination can operate through task assignment and occupational structure even when direct hiring-stage treatment effects are modest. The goal is not to estimate a structural model here. The goal is to recognize what the bounded callback path still abstracts from.

## Part V. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 9?
2. What would still be missing before claiming to measure the full labor-market consequences of discrimination?
3. How does the lab change the way you will read Week 10 mobility or Week 11 worker-policy evidence?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced callback-gap figure  
- [ ] callback summary CSV  
- [ ] design memo  
- [ ] transfer figure and report-card summary  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmarks  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from teaching students to separate average treatment effects from broader allocation and equilibrium questions.
- Use the report-card transfer step to prepare students for firm heterogeneity, segmentation, and mobility discussions.
