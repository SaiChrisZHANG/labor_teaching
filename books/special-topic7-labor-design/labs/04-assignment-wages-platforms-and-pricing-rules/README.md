# Week 4 Lab: Assignment, Wages, Platforms, And Pricing Rules

This lab is the bounded Week 4 teaching path for Labor Market Design, Contracting, and Mechanism Design. It uses deterministic synthetic platform-market data to practice the `Reproduce -> Diagnose -> Transfer` workflow without claiming access to proprietary platform logs, confidential A/B tests, official replication packages, worker location traces, or platform pricing code.

Primary anchor: Pallais on information, reputation, and entry-level online hiring.

Challenge anchor: Barach and Horton on platform steering and guarantees, with wage-rule extensions through compensation history, pay transparency, and platform minimum-wage experiments.

Run the smoke path from this directory:

```bash
ENV_NAME=research bash smoke.sh
```

The script writes compact outputs under `original/reduced/`, `output/reproduced/`, `output/diagnosed/`, and `output/transfer/`.
