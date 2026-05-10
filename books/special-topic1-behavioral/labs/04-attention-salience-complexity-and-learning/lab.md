# Code Lab 4: Attention, Salience, Complexity, and Learning

**Course:** Behavioral Labor  
**Module / Week:** Week 4 -- Attention, Salience, Complexity, and Learning  
**Associated chapter:** `04-attention-salience-complexity-and-learning.md`  
**Lab slug:** `04-attention-salience-complexity-and-learning`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@kostolMyhre2021]  
**Secondary / challenge anchor:** [@bhargavaManoli2015]  
**Optional extension anchor:** [@abelerHuffmanRaymond2025]  

## Why This Lab Exists

Week 4 turns attention, salience, complexity, learning, and endogenous information acquisition into applied labor designs. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact Kostol-Myhre-style factbook on workers learning a tax-benefit schedule.
2. **Diagnose** whether a response reflects true schedule knowledge, salience, opacity, costly information acquisition, or dynamic learning.
3. **Transfer** the same diagnostic logic to benefit claiming and workplace incentive opacity.

The lab does not require administrative tax, benefit, employer, or payroll microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small schedule-learning factbook from local synthetic data;
2. compare true net returns with perceived net returns and observed hours;
3. diagnose whether an information treatment identifies learning, salience, or a reduced-form exposure effect;
4. classify take-up interventions by the object changed: awareness, salience, simplification, hassle, or perceived eligibility;
5. transfer the same framework to opaque workplace incentives and effort.

## Local Structure

```text
labs/04-attention-salience-complexity-and-learning/
  lab.md
  smoke.sh
  src/
    build_week4_synthetic_data.py
    reproduce_schedule_learning.py
    transfer_policy_navigation.py
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
conda run -n research python src/build_week4_synthetic_data.py

conda run -n research python src/reproduce_schedule_learning.py \
  --input original/reduced/schedule_learning_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_policy_navigation.py \
  --policy-input transfer/data/policy_navigation_synthetic.csv \
  --workplace-input transfer/data/workplace_complexity_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/schedule_learning_by_exposure.csv`
- `output/reproduced/schedule_learning_letter_effects.csv`
- `output/reproduced/schedule_learning_response.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the true schedule object: a marginal tax-benefit return, an eligibility rule, or a bonus formula?
- What is the perceived object: a subjective net return, a coarse rule of thumb, or missing information?
- Does the response appear immediately after information arrives, or does it evolve with exposure?
- Which labor margin is observed: hours, earnings, bunching, take-up, or effort?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Benchmark:** What would transparent labor supply predict if workers knew the schedule?
2. **Behavioral object:** Is the wedge low salience, opacity, missing information, costly attention, or dynamic learning?
3. **Margin:** Which outcome moves: hours, earnings, claiming, take-up, saving, training, or effort?
4. **Identification caution:** What standard explanation could generate a similar response: constraints, adjustment costs, liquidity, stigma, selection, or true low returns?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/policy_navigation_summary.csv`
- `output/transfer/policy_navigation_effects.csv`
- `output/transfer/workplace_complexity_summary.csv`
- `output/transfer/policy_navigation_and_complexity.png`
- `output/transfer/transfer_note.txt`

Use [@bhargavaManoli2015] to classify the policy-navigation design. Does the intervention primarily change awareness, salience, perceived eligibility, procedural hassle, or confidence? Then use [@abelerHuffmanRaymond2025] to classify the workplace extension: does effort change because the incentive level changes, because the formula becomes easier to decode, or because the worker pays more attention?

## Challenge

Propose one bounded transfer design:

- an EITC or benefit-schedule information intervention;
- a simplified claiming or recertification process;
- a payroll-linked saving disclosure;
- a training enrollment navigation tool;
- a workplace bonus formula with varying opacity.

For the chosen setting, state the labor margin, the behavioral object, the identifying variation, and the main standard alternative.

## Deliverables Checklist

- [ ] run log
- [ ] schedule-learning summary table
- [ ] letter-effect summary table
- [ ] reproduction figure
- [ ] one-page diagnosis memo
- [ ] policy-navigation summary and effects tables
- [ ] workplace complexity summary
- [ ] short transfer paragraph naming the mechanism and the observed margin
