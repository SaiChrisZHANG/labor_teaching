# Code Lab 02: Static Labor Supply, Nonlinear Budget Sets, and Bunching

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 2 — Static labor supply  
**Associated chapter:** `02-static-labor-supply.md`  
**Lab slug:** `02-static-labor-supply`  
**Scope tier:** Standard  
**Primary language:** Python  
**Companion languages (optional):** Stata for the official replication package  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 2 module, basic command-line use, introductory `pandas`, histogram/binning intuition  
**Core economic question:** What can bunching near a kink teach us about labor-supply responses to nonlinear schedules, and what can it not teach us on its own?  
**Core design / estimator:** binned earnings density around a policy kink, reduced bunching diagnostic  
**Source paper for reproduction:** Saez, Emmanuel. 2010. *Do Taxpayers Bunch at Kink Points?* *American Economic Journal: Economic Policy* 2(3): 180--212.  
**Replication package source:** AEA data and code archive for `@saez2010`  
**Transfer dataset source:** local synthetic teaching files included in this folder, plus an optional instructor-provided extension sample

## Why this lab exists

Week 2 is where the course stops treating labor supply as a single linear-budget diagram and starts treating schedule geometry as empirical content. `@saez2010` is a strong anchor because it forces students to look at a nonlinear budget set through data: if marginal incentives change sharply at a kink, do earnings cluster locally? The lab keeps that logic but uses a bounded teaching path so students can run the workflow immediately without needing the full external package.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a reduced bunching-style figure around a kink using the local teaching workflow;
2. explain how nonlinear schedules turn the static model into a local empirical design;
3. distinguish what a histogram-density object reveals about behavior from what it leaves unresolved;
4. transfer the same workflow to one alternative subgroup or bin-width choice;
5. document the difference between a bounded teaching reproduction and the official paper package.

## Scope rules

This lab is intentionally bounded.

- Reproduce **one** bunching-style figure only.
- Diagnose the interpretation in a short memo.
- Transfer the workflow to **one** alternative subgroup, window, or bin-width choice.
- Do not turn the lab into a full structural bunching exercise.
- Keep the teaching path runnable without the official external package.

## Lab roadmap

1. **Reproduce** a stylized bunching figure using the local reduced dataset.
2. **Diagnose** the design: what does local excess mass near a kink measure?
3. **Transfer** the workflow to one bounded alternative.
4. **Reflect** on what is learned about static labor supply and what still requires richer data.

## Part 0. Setup and orientation

### Official package reality

The official `@saez2010` replication materials are the benchmark source for the paper's data workflow. The bounded course path does **not** ship those external files. Instead, the local lab includes a synthetic reduced dataset that preserves the logic of the bunching exercise while keeping the smoke test lightweight and deterministic.

### External files still needed for a closer official replication

The following items are still required if the class wants to move beyond the bounded teaching path:

- the official AEA `@saez2010` replication package itself;
- the package readme describing exact file dependencies and run order;
- any earnings microdata extracts or processed files referenced by the official scripts;
- the original do-files or scripts that construct the paper's target bunching objects.

Those external files are **not** needed for the reduced teaching path or the smoke test.

### Required local structure

```text
labs/02-static-labor-supply/
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
      saez_bunching_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      saez_transfer_synthetic.csv
  src/
    reproduce_saez_bunching.py
    transfer_bunching_design.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/reproduce_saez_bunching.py \
  --input original/reduced/saez_bunching_synthetic.csv \
  --earnings-col earnings \
  --kink 30 \
  --bin-width 1 \
  --window 12 \
  --outdir output/reproduced

conda run -n research python src/transfer_bunching_design.py \
  --input transfer/data/saez_transfer_synthetic.csv \
  --earnings-col earnings \
  --group-col group \
  --kink 30 \
  --bin-width 2 \
  --window 14 \
  --outdir output/transfer
```

## Part I. Reproduce a bounded bunching object

### Objective

Recover the visual logic of a bunching design around a kink and relate it back to Week 2's nonlinear-budget-set model.

### Student tasks

1. Read `original/source-notes.md`.
2. Run the reduced script on the synthetic bunching file.
3. Inspect the binned output and figure in `output/reproduced/`.
4. Write a short note explaining where local mass appears and why that does not automatically identify a global labor-supply elasticity.

### Required questions

- What does a kink-based bunching graph reveal in the most direct way?
- Why is the object local rather than global?
- Which responses might reflect taxable-income adjustment rather than real hours?
- How does this connect back to the static schedule geometry in Week 2?

### Minimum output

- one reproduced bunching-style histogram;
- one CSV of binned counts;
- one short reproduction note.

## Part II. Diagnose the design

### Objective

Move from “there is a spike near the kink” to “I know what that spike can and cannot mean.”

### Student tasks

1. Explain the estimand informally: local excess mass relative to nearby bins.
2. List at least two threats to interpreting bunching as pure hours adjustment.
3. Explain how information or salience limits would change the observed pattern.
4. Map the empirical graph back to the policy regions in the EITC-style schematic from the chapter.

### Minimum output

- a one-page design memo;
- one workflow map from raw earnings values to binned counts;
- one paragraph on interpretation risk.

## Part III. Guided transfer exercise

### Objective

Use the same bunching workflow on one bounded alternative without changing the design family.

### Acceptable transfer paths

Choose one:

1. change the bin width;
2. compare two subgroups;
3. change the window around the kink and discuss sensitivity.

### Scope constraints

- Keep one histogram-based design.
- Produce one main figure and one compact summary table.
- Do not add structural estimation.
- If you import external data, document provenance in `transfer/data-notes.md`.

### Student tasks

1. Start by running `src/transfer_bunching_design.py` on the included synthetic subgroup file.
2. Produce one grouped bunching figure.
3. Save the summary table of near-kink counts.
4. Write a short comparison paragraph explaining whether the alternative path changes the interpretation or only the presentation.

## Part IV. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 2?
2. What does it fail to recover from the full `@saez2010` exercise?
3. How would information frictions, as in `@chettyFriedmanSaez2013`, change the way you read the bunching graph?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced bunching figure  
- [ ] binned-count CSV  
- [ ] design memo  
- [ ] transfer data note  
- [ ] transfer figure and summary table  
- [ ] final reflection memo  
- [ ] clean README with run order

## Instructor notes

- The bounded path is the default for routine course use.
- The official package should be introduced as the empirical benchmark, not hidden.
- The strongest classroom payoff comes from showing that kink-based evidence is disciplined but local.
