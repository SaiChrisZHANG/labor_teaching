# Week 2 Lab: Recruiting, Congestion, Timing, And Unraveling

## Purpose

This lab turns the recruiting-congestion lecture into a student-facing empirical design workflow. It does not replicate official estimates in Carrillo-Tudela, Menzio, and Visschers, Niederle and Roth, or Roth and Xing. Instead, it uses deterministic synthetic data to practice how labor economists move from a recruiting-process theory to observable vacancy, application, interview, offer, acceptance, and hire margins.

Primary anchor: Carrillo-Tudela, Menzio, and Visschers on recruitment policies, job-filling rates, and matching efficiency [@carrilloTudelaMenzioVisschers2023].

Challenge anchor: Niederle and Roth on unraveling and centralized clearing in gastroenterology, with Roth and Xing on timing institutions [@niederleRoth2003; @niederleRoth2007; @rothXing1994].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/vacancy_yield_summary.csv`.

The script creates a small vacancy-funnel dataset with:

- wage information and wage transparency;
- recruiting intensity;
- hiring standards;
- interview capacity;
- applications, qualified applicants, interviews, offers, hires, and vacancy duration;
- exploding-offer and offer-hold indicators.

The object to reproduce is a reduced within-vacancy fact:

```{math}
\text{vacancy yield}_v =
\frac{\text{accepted hires}_v}{\text{applications}_v}.
```

The smoke path compares low-, middle-, and high-recruiting-intensity vacancies. The exercise is pedagogical: it reproduces the design logic of opening the vacancy black box, not the official estimates of the anchor paper.

### Diagnose

Open `output/diagnosed/design_diagnostics.csv` and `output/diagnosed/timing_regime_comparison.csv`.

For each diagnostic, classify whether the observed difference most likely reflects:

- applicant-pool size or composition;
- interview bottlenecks;
- recruiting intensity;
- wage transparency;
- hiring standards;
- vacancy duration;
- exploding offers or early contracting;
- timing coordination.

Answer four questions:

1. Which margins are directly observed in the synthetic data?
2. Which margins would remain latent in a dataset with only vacancies and hires?
3. When does faster vacancy filling look like improved recruiting rather than lower standards?
4. What evidence would distinguish application congestion from unraveling?

### Transfer

Open `output/transfer/recruiting_design_transfer.csv`. The transfer exercise asks students to move the same architecture to neighboring labor markets:

- online job platforms;
- wage transparency policies;
- gastroenterology-like fellowship markets;
- judicial clerkships;
- public-service recruiting.

Write a short memo answering:

- What is the institution?
- What is the frictive object?
- What margin is observed?
- What data would reveal the mechanism?
- What counterfactual design should be compared?
- What identification strategy is credible?
- What welfare object matters?
- What is the main remaining threat?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table summarizing vacancy yield by recruiting-intensity group;
- one paragraph explaining why within-vacancy margins are not residual details;
- one paragraph comparing early decentralized offers with coordinated timing;
- one transfer memo naming the institution, frictive object, observed margin, data, counterfactual, identification strategy, welfare object, and main threat.
