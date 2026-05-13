# Week 6 Lab: Synthesis, Frontier Questions, And Student Research Designs

## Purpose

This lab turns the capstone week into a concrete research-design exercise. It does not replicate official estimates in Acemoglu and Restrepo [@acemogluRestrepo2020Robots], Brynjolfsson, Li, and Raymond [@brynjolfssonLiRaymond2025GenerativeAI], or Aghion, Bunel, Jaravel, Mikaelsen, Roulet, and Sogaard [@aghionBunelJaravelMikaelsenRouletSogaard2025]. Instead, it uses deterministic synthetic data to practice how technology exposure, adoption, worker use, firm organization, and labor outcomes fit together.

Primary anchor: local robot exposure and labor-market incidence [@acemogluRestrepo2020Robots].

Challenge transfer: generative AI worker use and firm adoption by use case [@brynjolfssonLiRaymond2025GenerativeAI; @aghionBunelJaravelMikaelsenRouletSogaard2025].

## Workflow

### Reproduce

Run the synthetic capstone path and inspect:

- `output/reproduced/local_exposure_design.csv`;
- `output/reproduced/reduced_form_incidence.csv`;
- `output/reproduced/reproduction_note.txt`.

The script builds local technology exposure from baseline industry shares and technology adoption intensity:

```{math}
Exposure_m = \sum_j s_{jm0} Tech_j.
```

It then reports simple reduced-form slopes for employment, wages, mobility costs, and a welfare proxy. The exercise reproduces design logic only. It does not claim to recover published robot-exposure magnitudes.

### Diagnose

Open `output/diagnosed/design_diagnosis.csv`.

For each design element, answer:

1. Does the technology measure capture invention, exposure, adoption, use, or implementation?
2. Is the unit of analysis aligned with the mechanism?
3. What is the counterfactual?
4. What timing of adjustment is visible?
5. Which welfare margins are missing?

### Transfer

Open:

- `output/transfer/ai_design_transfer.csv`;
- `output/transfer/project_opportunities.csv`.

The transfer exercise asks students to redesign the logic for generative AI and frontier technology settings. A local robot-exposure design cannot simply be relabeled as an AI design. Students must decide whether the right unit is a worker, firm, team, platform, local labor market, or country-sector, and whether the treatment is adoption, use, exposure, organizational implementation, task tradability, or compute infrastructure.

Write a short memo answering:

- Which transfer setting is closest to a worker-use design?
- Which setting is closest to a firm-adoption design?
- Which setting mainly changes worker voice, monitoring, or bargaining power?
- Which setting would require spatial data on infrastructure or electricity?
- Which broad question is saturated, and what narrower version remains open?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one paragraph interpreting the local exposure measure;
- one paragraph explaining why exposure is not the same as adoption or use;
- one paragraph diagnosing the unit of analysis and counterfactual;
- one paragraph explaining why wages and employment do not exhaust welfare;
- one transfer paragraph that redesigns the logic for generative AI worker use or firm adoption;
- one project paragraph identifying a saturated question and a still-open student entry point.
