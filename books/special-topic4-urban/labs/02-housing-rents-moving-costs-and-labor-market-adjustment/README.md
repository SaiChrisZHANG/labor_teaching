# Week 2 Lab

This folder contains the Week 2 code lab for Urban and Labor.

The lab uses Hsieh and Moretti as the primary reproduction anchor and Notowidigdo as the conservative transfer anchor. It is a bounded Python teaching workflow, not a full official replication.

## Runnable Out Of The Box

Run from this folder:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path runs:

- `src/reproduce_hsieh_moretti_reduced.py`
- `src/transfer_notowidigdo_incidence.py`

It writes deterministic outputs under `output/reproduced/` and `output/transfer/`. No internet access, confidential data, or external downloads are required.

## What Requires External Official Materials

A closer Hsieh-Moretti replication would require the public openICPSR replication package and its documented data/code workflow. Those files are not shipped in this lab folder.

This folder does not claim an official Notowidigdo replication package. The Notowidigdo step is a bounded transfer exercise using synthetic local-demand shock data.

## Reduced Teaching Path

The reduced reproduction path uses `original/reduced/housing_constraints_reduced.csv` to approximate the paper architecture: productivity growth, housing-supply constraints, wages, rents, prices, population, employment, commuting, and real access.

The transfer path uses `transfer/data/local_demand_shocks_synthetic.csv` to practice incidence logic after local demand shocks. It asks which groups gain or lose once rents, ownership, moving costs, and commuting openness are counted.

