# Week 2 Lab: Recruiting, Congestion, Timing, And Unraveling

This lab is the bounded Week 2 teaching path for Labor Market Design, Contracting, and Mechanism Design. It uses deterministic synthetic vacancy-funnel and timing-regime data to practice the `Reproduce -> Diagnose -> Transfer` workflow without claiming access to proprietary vacancy records, job-board application logs, employer interview files, professional-market offer records, or official replication packages.

Primary anchor: Carrillo-Tudela, Menzio, and Visschers on recruitment policies, job-filling rates, and matching efficiency.

Challenge anchor: Niederle and Roth on gastroenterology with and without a centralized match, with Roth and Xing as the broader timing-institution frame.

Run the smoke path from this directory:

```bash
ENV_NAME=research bash smoke.sh
```

The script writes compact outputs under `original/reduced/`, `output/reproduced/`, `output/diagnosed/`, and `output/transfer/`.
