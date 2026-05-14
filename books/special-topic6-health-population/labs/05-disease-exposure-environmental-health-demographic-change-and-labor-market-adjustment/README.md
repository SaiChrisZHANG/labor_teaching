# Week 5 Lab: Disease Exposure, Environmental Health, Demographic Change, And Labor-Market Adjustment

This lab is the bounded Week 5 teaching path for Labor Market, Health, and Population. It uses deterministic synthetic data to practice the `Reproduce -> Diagnose -> Transfer` workflow without claiming access to official COVID microdata, private-sector real-time data, South African mortality or labor records, public-health archives, payroll records, pollution microdata, or migration records.

Primary anchor: Albanesi and Kim on COVID labor-market incidence.

Challenge anchor: Chicoine on HIV/AIDS mortality and South African labor markets.

Run the smoke path from this directory:

```bash
ENV_NAME=research bash smoke.sh
```

The script writes compact outputs under `output/reproduced/`, `output/diagnosed/`, and `output/transfer/`.
