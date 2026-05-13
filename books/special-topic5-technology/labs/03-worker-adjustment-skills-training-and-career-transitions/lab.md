# Week 3 Lab: Worker Adjustment, Skills, Training, And Career Transitions

## Purpose

This lab turns the Week 3 lecture into a bounded worker-adjustment exercise. It does not replicate official estimates in Kogan, Papanikolaou, Schmidt, and Seegmiller [@koganPapanikolaouSchmidtSeegmiller2021], Bertermann [@bertermann2025], or Muehlemann [@muehlemann2024]. Instead, it uses deterministic synthetic data to practice how worker-level exposure, adjustment margins, and training or retirement responses can be organized in a credible empirical design.

Primary anchor: worker-level technology exposure linked to worker outcomes [@koganPapanikolaouSchmidtSeegmiller2021].

Challenge papers: training and retirement responses to shocks [@bertermann2025] and AI adoption with workplace training [@muehlemann2024].

## Workflow

### Reproduce

Run the synthetic exposure path and inspect `output/reproduced/worker_exposure_outcomes.csv`.

The script defines:

- workers with task shares, occupations, employers, local labor markets, age, tenure, and baseline earnings;
- technology weights attached to tasks;
- skill portability, adjustment capacity, and worker-level exposure;
- synthetic earnings and employment outcomes after exposure.

The object to reproduce is the logic of a worker-level exposure design:

```{math}
WorkerExposure_i = \sum_k TaskShare_{ik} \times TechnologyWeight_k.
```

The exercise reproduces the structure of a worker exposure measure. It does not claim to recover official patent measures, official worker records, or official treatment effects.

### Diagnose

Open `output/diagnosed/adjustment_diagnosis.csv`. For each worker, compare exposure, skill portability, training probability, switching probability, and exit risk.

Answer three questions:

1. Does the worker appear to adjust through training, switching, staying, persistent loss, or exit?
2. Why can a high-exposure worker avoid large losses while another high-exposure worker suffers?
3. Which pieces of the diagnosis would be unobserved in a repeated cross-section?

### Transfer

Open `output/transfer/training_retirement_transfer.csv` and `output/transfer/ai_training_transfer.csv`.

The first transfer exercise moves from worker exposure to local training and retirement responses. The second transfer exercise moves to firm AI adoption and asks whether training is going to incumbents or new hires.

Write a short memo answering:

- Which local labor market adjusts mostly through training?
- Which local labor market adjusts mostly through retirement or exit?
- Which AI-adopting firm appears to upgrade skill composition by training new hires rather than incumbents?
- When can aggregate skill upgrading hide persistent losses for exposed incumbent workers?
- What would be needed to turn each transfer exercise into a causal design?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table describing worker-level exposure, skill portability, and worker outcomes;
- one paragraph explaining why worker-level incidence differs from aggregate adjustment;
- one paragraph diagnosing training, switching, and exit as distinct adjustment margins;
- one transfer paragraph explaining how training or retirement can substitute for occupational mobility;
- one transfer paragraph explaining why firm AI adoption can raise average skill demand while exposed incumbents remain worse off.
