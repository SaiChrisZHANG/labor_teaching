# Week 5 Lab: Technology, Inequality, Market Structure, And Labor-Market Institutions

## Purpose

This lab turns the Week 5 lecture into a bounded market-level exercise. It does not replicate official estimates in Autor, Dorn, Katz, Patterson, and Van Reenen [@autorDornKatzPattersonVanReenen2020], Ding, Fort, Michaels, Morrow, and Schott [@dingFortMichaelsMorrowSchott2022], or Cirera, Comin, Cruz, Lee, and Martins [@cireraCominCruzLeeMartins2024]. Instead, it uses deterministic synthetic data to practice how technology can change labor share, concentration, rent capture, structural change, job quality, and global incidence.

Primary anchor: market-share reallocation and labor-share decomposition in the superstar-firm literature [@autorDornKatzPattersonVanReenen2020].

Challenge papers: structural change within versus across firms [@dingFortMichaelsMorrowSchott2022] and cross-country establishment technology sophistication [@cireraCominCruzLeeMartins2024].

## Workflow

### Reproduce

Run the synthetic market-incidence path and inspect `output/reproduced/market_structure_labor_share.csv`.

The script defines firms within industries with:

- baseline and current market shares;
- baseline and current labor shares;
- technology intensity, intangible intensity, productivity growth, and wage premia;
- product-market concentration and employer-concentration proxies.

The object to reproduce is the logic of a market-share decomposition:

```{math}
\Delta LS_m
=
\sum_f s_{f0}\Delta LS_f
+
\sum_f \Delta s_f LS_{f0}
+
\sum_f \Delta s_f\Delta LS_f.
```

The exercise reproduces the structure of the design logic. It does not claim to recover official Economic Census measures, official Compustat estimates, or published magnitudes.

### Diagnose

Open `output/diagnosed/incidence_diagnosis.csv`.

For each industry, compare:

- concentration change;
- aggregate labor-share change;
- technology intensity;
- intangible intensity;
- employer-concentration risk;
- institutional mediation through unions, wage floors, and worker voice.

Answer three questions:

1. Is the labor-share decline mostly a within-firm change, a between-firm market-share shift, or an interaction?
2. Does the technology variable measure adoption directly, or is technology inferred from firm growth and reallocation?
3. Which worker outcomes are hidden if the only outcome is labor share?

### Transfer

Open `output/transfer/structural_change_transfer.csv` and `output/transfer/global_ai_frontier_transfer.csv`.

The first transfer exercise compares employment reallocation with job-quality reallocation across agriculture, manufacturing, formal services, informal services, and knowledge services. The second adds global diffusion, outsourcing, electricity constraints, data-center demand, and local labor-market incidence.

Write a short memo answering:

- Which scenario improves employment but not job quality?
- Which scenario improves productivity but weakens worker voice?
- Which scenario depends most on absorptive capacity?
- Which scenario is closest to a labor-absorbing service path?
- What data would be needed to turn the AI infrastructure transfer into a credible spatial labor-market design?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table describing the market-share and labor-share decomposition;
- one paragraph explaining whether the main result is within-firm or between-firm;
- one paragraph diagnosing product-market concentration versus labor-market power;
- one paragraph explaining how institutions mediate technology incidence;
- one transfer paragraph distinguishing employment reallocation from welfare-improving reallocation;
- one transfer paragraph on Global South diffusion, outsourcing, or AI infrastructure as a labor-market question.
