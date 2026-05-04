# Code Lab 01: Composition, Wages, and the Discipline of Labor-Market Measurement

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 1 — Labor market facts, measurement, and canonical questions  
**Associated chapter:** `01-labor-market-facts.md`  
**Lab slug:** `01-labor-market-facts`  
**Scope tier:** Standard  
**Primary language:** Python  
**Companion languages (optional):** Stata for the official replication package  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 1 module, basic command-line use, introductory `pandas`, weighted summary statistics  
**Core economic question:** How much do aggregate labor-market series reflect within-group wage change, and how much reflects changing composition in who is observed working?  
**Core design / estimator:** descriptive decomposition, labor-market accounting, and composition adjustment  
**Source paper for reproduction:** Daly, Mary C., and Bart Hobijn. 2017. *Composition and Aggregate Real Wage Growth*. *American Economic Review* 107(5): 349–352.  
**Replication package source:** AEA / openICPSR replication package, DOI `10.3886/E113514V1`  
**Transfer dataset source:** instructor-provided reduced CPS-style teaching extract, or a student-acquired public labor dataset with documented provenance

## Why this lab exists

Week 1 is about learning that labor-market facts are constructed, not simply observed. This lab asks students to reproduce a published result by Mary Daly and Bart Hobijn on composition and aggregate wage growth, diagnose how the code operationalizes the measured object, and then transfer the same accounting logic to a bounded new dataset. The point is not to turn the first week into a miniature dissertation. The point is to make students read a real replication package and then use that workflow to build a small labor-market factbook of their own.

## Learning objectives

By the end of this lab, students should be able to:

1. recover a headline result from a published labor-economics replication package or its reduced pedagogical path;
2. explain the paper's measured object, sample construction, and composition logic;
3. distinguish raw average wage movements from composition-adjusted movements and from within-group wage change;
4. navigate a mixed-language workflow in which the official package may differ from the course backbone language;
5. transfer a descriptive labor workflow to a bounded new dataset;
6. document code, data, and interpretation clearly enough for a classmate to reproduce the exercise.

## Scope rules

This lab is ambitious but bounded.

- Reproduce **one** headline result at most.
- Diagnose the design and code path in a short memo.
- Transfer the workflow to **one** new dataset or extension sample.
- Produce **one** transfer table or **one** transfer figure.
- Do not broaden the exercise into a full research paper.
- If the official package is computationally heavy, use the reduced pedagogical pathway for the core assignment and treat the full package as optional or instructor-led.

## Lab roadmap

1. **Reproduce** a headline descriptive result or its reduced-data pedagogical equivalent.  
2. **Diagnose** the estimand, sample, and composition logic.  
3. **Transfer** the workflow to a small new dataset or subgroup without changing the underlying accounting logic.  
4. **Reflect** on what changed once measurement choices became explicit.

The reproduce/transfer distinction matters. In the reproduce stage, students stay as close as possible to the Daly--Hobijn object and ask whether they can recover the same descriptive logic. In the transfer stage, students may change the subgroup or bounded sample, but they should keep the same Week 1 discipline: define the object, keep the denominator explicit, and separate composition effects from within-group change.

## Part 0. Setup and orientation

### Official package reality

The official replication package for Daly and Hobijn includes Stata code and a large matched CPS file. For classroom use, this lab therefore offers two pathways:

- **Official pathway:** inspect the original package and, if feasible, run the target Stata workflow.
- **Reduced pathway:** use the Python scripts in `src/` plus a reduced synthetic or instructor-provided teaching file to understand the logic of composition adjustment and fact-building.

### Required local structure

```text
labs/01-labor-market-facts/
  README.md
  lab.md
  run-log.md
  original/
    README.md
    source-notes.md
    reduced/
      composition_panel_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      labor_micro_synthetic.csv
  src/
    reproduce_composition_adjustment.py
    transfer_factbook.py
  output/
    reproduced/
    transfer/
  environment/
    requirements.txt
```

### First commands to run

```bash
conda run -n research python src/reproduce_composition_adjustment.py   --input original/reduced/composition_panel_synthetic.csv   --outdir output/reproduced
conda run -n research python src/transfer_factbook.py   --input transfer/data/labor_micro_synthetic.csv   --date-col date   --status-col employment_status   --weight-col weight   --hours-col hours   --earnings-col weekly_earnings   --group-col group   --outdir output/transfer
```

These commands verify that the pedagogical path is functional before any real data are added.

## Part I. Reproduce a headline result

### Objective

Recover the logic of the Daly--Hobijn composition-adjusted wage result and understand how it differs from a raw aggregate wage series.

### Student tasks

1. Read `original/source-notes.md`.
2. Inspect the official package structure and identify the file path that generates the target result.
3. If the official pathway is feasible, run the relevant Stata workflow.
4. Otherwise, run the reduced Python pathway on the teaching panel.
5. Save the resulting figure and a one-paragraph reproduction note in `output/reproduced/`.

### Required questions

- What is the paper trying to measure?
- Why can aggregate average wages move even when underlying wage offers do not?
- Which cells or worker groups drive the composition logic?
- Which parts of the official workflow are substantive rather than cosmetic?

### Minimum output

- one reproduced or pedagogically reconstructed figure;
- one note stating whether the result came from the official or reduced pathway;
- one short map of the file(s) that matter for the target result.

## Part II. Diagnose the code and the design

### Objective

Move from “I ran it” to “I understand the object being measured.”

### Student tasks

1. Write a short design memo explaining the paper's question and estimand.
2. Explain the role of sample construction, weighting, and composition.
3. Identify one implementation choice that is likely central to interpretation.
4. Identify one portability issue when moving from the official package to a smaller teaching workflow.

### Required prompts

- What exactly is being adjusted for in the composition-adjusted series?
- What would go wrong if we interpreted the raw series as the full story?
- Which assumptions are mild bookkeeping and which are substantive modeling choices?
- Does the reduced pedagogical pipeline preserve the same economic object?

### Minimum output

- a one-page design memo;
- one workflow map from raw or reduced data to the final figure;
- one paragraph on portability and reproducibility.

## Part III. Guided transfer exercise

### Objective

Use the same Week 1 measurement discipline to build a small labor-market factbook on a new sample.

### Acceptable transfer paths

Choose one:

1. **Subgroup extension:** use a reduced CPS-style file and build the same factbook for one subgroup.
2. **Period extension:** compare two periods and discuss whether composition changes differ across episodes.
3. **Local labor factbook:** acquire a bounded public dataset and build one labor-market fact panel for a place, industry, or demographic slice.

### Scope constraints

- Keep one main design family: descriptive composition-aware fact-building.
- Produce one main figure or one main summary table.
- Do not add multiple estimators.
- If you acquire a new dataset, document provenance and variable definitions in `transfer/data-notes.md`.

### Student tasks

1. Start by running `src/transfer_factbook.py` on the synthetic file.
2. Replace the synthetic data with a real small dataset or extension sample.
3. Keep the required columns and document any recoding.
4. Produce one time-series figure and one compact summary table.
5. Write a comparison paragraph: what is learned, and what remains unlearned, relative to Daly and Hobijn.

### Required prompts

- What is the new empirical object?
- Why is this extension informative rather than arbitrary?
- Which parts of the Week 1 accounting and composition logic carry over?
- Which parts do not carry over because the data are weaker, more aggregated, or differently defined?

### Minimum output

- one cleaned transfer dataset or clearly documented derived sample;
- one estimation or fact-building script;
- one main figure or table in `output/transfer/`;
- one comparison paragraph.

## Part IV. Reflection and communication

### Student prompts

1. What did you learn by reading a real replication package that a toy classroom example would not have taught?
2. Where exactly did measurement choices matter most?
3. Did your transfer exercise feel like a robustness exercise, an application, or a genuine replication extension?
4. What would be the most credible next extension if you had one more week?

### Final memo

Submit a short memo containing:

- the reproduced result or reduced-data reconstruction;
- a design diagnosis;
- the transfer figure or table;
- one main takeaway about measurement, composition, and the difference between description and mechanism;
- one limitation of the transfer exercise.

## Deliverables checklist

- [ ] run log  
- [ ] reproduced or pedagogically reconstructed output  
- [ ] file map / workflow note  
- [ ] design memo  
- [ ] transfer data note  
- [ ] transfer script  
- [ ] one transfer figure or table  
- [ ] final memo  
- [ ] clean README with run order

## Suggested grading rubric

| Component | Weight |
|---|---:|
| Reproduction completeness and accuracy | 25 |
| Understanding of measurement and composition logic | 25 |
| Quality of transfer exercise | 25 |
| Code organization and reproducibility | 15 |
| Interpretation and communication | 10 |

## Instructor notes

- The official package is large enough that the reduced-data pathway should be the default for first assignment use.
- The lab is strongest when paired with a short in-class walkthrough of how the official package maps files to outputs.
- Python remains the public backbone language even though the official package is Stata-based.
- The synthetic files in this folder exist only to make the workflow runnable out of the box; they are not substitutes for the real paper.
