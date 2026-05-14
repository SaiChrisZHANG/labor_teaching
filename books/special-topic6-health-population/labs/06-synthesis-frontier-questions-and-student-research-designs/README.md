# Week 6 Lab: Synthesis, Frontier Questions, And Student Research Designs

This lab is the bounded Week 6 teaching path for Labor Market, Health, and Population. It uses deterministic synthetic data to practice the `Reproduce -> Diagnose -> Transfer` workflow without claiming access to official administrative earnings records, disability-program files, linked health records, pandemic real-time data, private payroll records, or firm accommodation data.

Primary anchor: Meyer and Mok on long-run disability incidence.

Challenge anchor: Albanesi and Kim on COVID labor-market incidence.

Run the smoke path from this directory:

```bash
ENV_NAME=research bash smoke.sh
```

The script writes compact outputs under `output/reproduced/`, `output/diagnosed/`, and `output/transfer/`.
