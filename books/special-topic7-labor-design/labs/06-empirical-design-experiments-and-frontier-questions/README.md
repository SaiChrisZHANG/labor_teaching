# Week 6 Lab: Empirical Design, Experiments, And Frontier Questions

This lab is the bounded Week 6 capstone path for Labor Market Design, Contracting, and Mechanism Design. It uses deterministic synthetic matching and assignment data to practice the `Reproduce -> Diagnose -> Transfer` workflow without claiming access to confidential medical match, Army, platform, public-sector, or personnel records.

Primary anchor: Agarwal on empirical evaluation of the medical match.

Challenge anchor: Davis, Greenberg, and Jones on deferred acceptance in Army officer labor markets.

Run the smoke path from this directory:

```bash
ENV_NAME=research bash smoke.sh
```

The script writes compact outputs under `original/reduced/`, `output/reproduced/`, `output/diagnosed/`, and `output/transfer/`.
