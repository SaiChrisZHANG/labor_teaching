# Week 4 Lab: Firms, Hiring, Management, And Organizational Response To New Technology

## Purpose

This lab turns the Week 4 lecture into a bounded firm-adoption exercise. It does not replicate official estimates in Babina, Fedyk, He, and Hodson [@babinaFedykHeHodson2023AIWorkforce], Aghion et al. [@aghionBunelJaravelMikaelsenRouletSogaard2025], or Dargnies, Hakimov, and Kubler [@dargniesEtAl2026]. Instead, it uses deterministic synthetic data to practice how firm AI adoption, workforce composition, internal labor markets, worker attitudes, and manager delegation choices can be organized in a credible empirical design.

Primary anchor: firm-level AI investment linked to workforce composition, hierarchy, and job-posting shifts [@babinaFedykHeHodson2023AIWorkforce].

Challenge papers: firm-level AI adoption by use case [@aghionBunelJaravelMikaelsenRouletSogaard2025] and algorithm aversion in hiring and delegation [@dargniesEtAl2026; @bansakEtAl2024].

## Workflow

### Reproduce

Run the synthetic adoption path and inspect `output/reproduced/firm_ai_adoption_workforce.csv`.

The script defines:

- firms with baseline employment, routine task share, skill mix, hierarchy, management quality, and data readiness;
- an adoption chain that separates acquisition, implementation, usage, and reorganization;
- incumbent training and new-hire AI training as separate margins;
- post-adoption workforce composition and employment-growth outcomes.

The object to reproduce is the logic of a firm-adoption design:

```{math}
AdoptionIndex_f
=
\frac{
Acquisition_f + Implementation_f + Usage_f + Reorganization_f
}{4}.
```

The exercise reproduces the structure of a firm AI-adoption and workforce-composition design. It does not claim to recover official resume measures, official job-posting measures, confidential firm outcomes, or official treatment effects.

### Diagnose

Open `output/diagnosed/adoption_mechanism_diagnosis.csv`. For each firm, compare the substitution, augmentation, scale, organizational-redesign, and principal-agent tension indexes.

Answer three questions:

1. Is the measured adoption coefficient more likely to reflect substitution, augmentation, scale, or organizational redesign?
2. Does AI adoption appear to train incumbents or hire around them?
3. Where would a simple adoption indicator overstate realized usage or hide worker incidence?

### Transfer

Open `output/transfer/ai_attitude_transfer.csv` and `output/transfer/attitude_design_variants.csv`.

The first transfer exercise adds worker trust, manager algorithm trust, perceived fairness, replacement concern, human override, transparency, and monitoring intensity. The second transfer exercise sketches vignette arms that vary transparency, human override, replacement risk, performance feedback, and monitoring.

Write a short memo answering:

- Which firms show high adoption but low voluntary usage?
- Which firms look like incumbent augmentation rather than hiring-around-incumbents?
- Which firms show the strongest principal-agent tension?
- Which attitude measures should be collected before rollout rather than after workers observe tool quality?
- Which vignette arm best separates algorithm aversion from rational concern about replacement or monitoring?
- What data would be needed to turn this synthetic transfer exercise into a causal design?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table describing the adoption chain from acquisition to reorganization;
- one paragraph explaining why adopters are selected;
- one paragraph diagnosing substitution, augmentation, scale, and organizational redesign as distinct mechanisms;
- one paragraph separating incumbent training from new-hire AI training;
- one transfer paragraph explaining how worker and manager AI attitudes can affect usage, productivity, and inequality.
