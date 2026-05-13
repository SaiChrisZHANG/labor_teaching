# Week 1 Lab: Technology Measures, Tasks, And Labor Exposure

## Purpose

This lab turns the Week 1 framework into a bounded measurement exercise. It does not replicate the official data or estimates in Webb, Kogan et al., or any related paper. Instead, it uses deterministic synthetic data to practice how labor economists construct exposure measures and how different measures imply different empirical objects.

Primary anchor: Webb's technology-to-task exposure logic [@webb2020].

Measurement contrast: Kogan, Papanikolaou, Schmidt, and Seegmiller's worker-level technology exposure logic [@koganPapanikolaouSchmidtSeegmiller2023].

## Workflow

### Reproduce

Run the synthetic exposure path and inspect `output/reproduced/exposure_by_occupation.csv`.

The script defines:

- task categories;
- technology descriptors;
- occupation task shares;
- measurement weights for patent-text-style capability exposure, robot-style embodied automation exposure, and vacancy-style skill-demand exposure.

The object to reproduce is the chapter's measurement bridge:

```{math}
Exposure_o = \sum_k TaskShare_{ok} \times TechTaskScore_k.
```

The exercise reproduces the logic of constructing an exposure measure from tasks. It does not claim to recover the full Webb index or any official replication estimate.

### Diagnose

Open `output/diagnosed/measurement_contrast.csv`. For each occupation, compare the rank implied by three technology measures:

- patent-text-style capability exposure;
- robot-style embodied automation exposure;
- vacancy-style skill-demand exposure.

Answer three questions:

1. Which measure is closest to invention or capability?
2. Which measure is closest to realized embodied adoption?
3. Which measure is closest to employer demand for new skills?

The diagnostic lesson is that disagreement across measures can be substantively informative. A payroll clerk may look exposed under software and AI text, while a production assembler may look exposed under robot adoption. Those are different labor-market objects.

### Transfer

Open `output/transfer/firm_measurement_contrast.csv`. The transfer exercise aggregates occupation task portfolios to synthetic firms. It asks whether a firm's workforce looks exposed to AI capabilities, robot-style automation, vacancy skill demand, or realized adoption.

Write a short memo answering:

- Which firm looks most exposed under each measure?
- Does the conclusion change when the unit moves from occupation to firm?
- Which measure would you use to study wages, employment, vacancies, training, or reorganization?
- What would be needed to turn exposure into a causal effect?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table describing occupation exposure under at least two measures;
- one paragraph explaining why exposure is not adoption;
- one paragraph explaining why patents and vacancies can rank occupations differently;
- one transfer paragraph linking the measurement choice to a proposed labor outcome.
