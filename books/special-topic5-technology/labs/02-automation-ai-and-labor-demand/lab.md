# Week 2 Lab: Automation, AI, And Labor Demand

## Purpose

This lab turns the Week 2 lecture into a bounded labor-demand exercise. It does not replicate the official estimates in Acemoglu and Restrepo or Aghion et al. Instead, it uses deterministic synthetic data to practice how local exposure, employment-wage incidence, and firm AI adoption identify different labor-demand margins.

Primary anchor: Acemoglu and Restrepo's robot exposure design for local labor markets [@acemogluRestrepo2020Robots].

Challenge paper: Aghion, Bergeaud, Boppart, Klenow, and Li's firm-level evidence on AI use and labor demand [@aghionBergeaudBoppartKlenowLi2025differentUsesAI].

## Workflow

### Reproduce

Run the synthetic exposure path and inspect `output/reproduced/local_robot_exposure.csv`.

The script defines:

- industries with robot adoption intensity and baseline growth;
- commuting zones with industry employment shares;
- exposed occupation shares;
- synthetic employment and wage changes.

The object to reproduce is the logic of a local exposure design:

```{math}
RobotExposure_c = \sum_i IndustryShare_{ci} \times RobotIntensity_i.
```

The exercise reproduces the structure of a shift-share exposure measure. It does not claim to recover the official robot exposure data or official treatment effects.

### Diagnose

Open `output/diagnosed/incidence_diagnosis.csv`. For each commuting zone, compare employment and wage patterns.

Answer three questions:

1. Does the pattern look like direct displacement, output-demand offset, composition, or ambiguous incidence?
2. Why might employment and wages move differently?
3. Which adjustment margins are visible in a commuting-zone design, and which remain offstage?

### Transfer

Open `output/transfer/firm_ai_transfer.csv`. The transfer exercise moves from local robot exposure to firm AI adoption, vacancy AI demand, and workforce task exposure.

Write a short memo answering:

- Which firm looks most exposed under task exposure?
- Which firm shows the strongest realized AI adoption?
- Which firm shows the strongest vacancy signal?
- When could firm AI adoption raise employment even if exposed tasks shrink?
- What would be needed to turn the transfer exercise into a causal design?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table describing local robot exposure and employment-wage incidence;
- one paragraph explaining why a local exposure design is an equilibrium incidence design;
- one paragraph comparing robot exposure with firm AI adoption;
- one transfer paragraph linking measurement choice to displacement, augmentation, output-demand effects, or new-task creation.
