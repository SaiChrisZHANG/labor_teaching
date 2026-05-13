# Week 2 Lab: Housing, Rents, Moving Costs, And Labor-Market Adjustment

**Course:** Urban and Labor  
**Module / Week:** Week 2 - Housing, rents, moving costs, and labor-market adjustment  
**Associated chapter:** `02-housing-rents-moving-costs-and-labor-market-adjustment.md`  
**Lab slug:** `02-housing-rents-moving-costs-and-labor-market-adjustment`  
**Scope tier:** Standard  
**Primary language:** Python  
**Companion languages:** none for the local teaching path  
**Estimated student time:** 3 core hours + 2 optional hours  
**Prerequisites:** Week 1 spatial-access framework, basic CSV work, introductory Python  
**Core economic question:** When do housing constraints and moving costs keep workers from turning local productivity into real labor-market access?  
**Core design / estimator:** reduced city-level adjustment vector and incidence diagnosis  
**Primary reproduction anchor:** Hsieh and Moretti on housing constraints and spatial misallocation [@hsiehMoretti2019HousingConstraints]  
**Challenge / transfer anchor:** Notowidigdo on the incidence of local labor-demand shocks [@notowidigdo2020LocalDemandShocks]

## Why This Lab Exists

The Week 2 chapter argues that nominal wages are not enough. Students need to see the adjustment vector: wages, rents, population, employment, commuting, prices, and real access. Hsieh and Moretti are the primary anchor because the paper makes housing constraints central to spatial misallocation. The local lab does not rerun the full official package. It builds a reduced teaching path that lets students practice the same conceptual architecture immediately, then transfers the incidence logic to a local-demand shock inspired by Notowidigdo.

## Learning Goals

By the end of this lab, students should be able to:

1. reproduce a reduced city-level housing-constraint adjustment table;
2. distinguish nominal wage growth from rent-inclusive real access;
3. classify whether adjustment looks like price adjustment, quantity adjustment, commuting adjustment, or limited access;
4. diagnose who captures local opportunity: workers, landlords, incumbent homeowners, firms, commuters, or excluded migrants;
5. transfer the same logic to a bounded local-demand shock setting without claiming a full official replication;
6. document which outputs are pedagogical teaching objects and which would require external official materials.

## Setup

Run the bounded path from this folder:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs two scripts:

```bash
conda run -n research python src/reproduce_hsieh_moretti_reduced.py
conda run -n research python src/transfer_notowidigdo_incidence.py
```

No external downloads are required. The included CSVs are small deterministic teaching files.

## Primary Reproduction Anchor

The reproduction anchor is Hsieh and Moretti [@hsiehMoretti2019HousingConstraints]. The paper's full contribution is a quantitative account of housing constraints and spatial misallocation. The local teaching path focuses on one bounded object: a city-level table that asks whether high-productivity places adjust through wages, rents and prices, population and employment, commuting, or reduced real access.

The reduced file is `original/reduced/housing_constraints_reduced.csv`. It is synthetic and pedagogical. It is designed to resemble the objects students need to organize when reading the paper, not to reproduce published magnitudes.

## Challenge / Transfer Anchor

The transfer anchor is Notowidigdo [@notowidigdo2020LocalDemandShocks]. The local transfer path uses synthetic local-demand shocks to ask who gains or loses when a place receives a positive or negative demand shock and housing or moving frictions shape adjustment.

This folder does not claim to include an official Notowidigdo replication package. The transfer is a teaching application of the incidence logic.

## Reproduce

Run:

```bash
conda run -n research python src/reproduce_hsieh_moretti_reduced.py
```

The script reads `original/reduced/housing_constraints_reduced.csv` and writes:

- `output/reproduced/housing_constraint_adjustment.csv`
- `output/reproduced/housing_constraint_summary.csv`
- `output/reproduced/reproduction_note.txt`

The reproduced object is a reduced version of the paper architecture:

```{math}
\Delta Y_\ell =
\left(
\Delta w_\ell,\,
\Delta R_\ell,\,
\Delta N_\ell,\,
\Delta E_\ell,\,
\Delta C_\ell,\,
\Delta P_\ell
\right).
```

The core classroom task is to identify places where productivity and wages grow but rent and price adjustment absorb much of the gain, while population growth remains limited.

## Diagnose

Use `output/reproduced/housing_constraint_adjustment.csv` as the diagnosis table. For each place, answer:

1. Is the main response price adjustment, quantity adjustment, commuting adjustment, mixed adjustment, or limited access?
2. Is the apparent friction housing supply, moving cost, sorting, commuting access, or a combination?
3. Does real access rise after rents and commuting costs are counted?
4. Who appears to capture the local surplus: workers, landlords, incumbent homeowners, firms, commuters, or excluded would-be migrants?
5. Which margin is missing from the reduced teaching file that would matter for a closer paper replication?

Students should be especially careful about three interpretation errors:

- treating nominal wage growth as worker welfare;
- treating rent growth as the whole housing mechanism;
- treating low migration as proof of preferences rather than possible constraints.

## Transfer

Run:

```bash
conda run -n research python src/transfer_notowidigdo_incidence.py
```

The script reads `transfer/data/local_demand_shocks_synthetic.csv` and writes:

- `output/transfer/local_demand_incidence_transfer.csv`
- `output/transfer/incidence_summary_by_group.csv`
- `output/transfer/transfer_note.txt`

The transfer asks how a local labor-demand shock changes wages, rents, population, employment, commuting, and real access for different groups. The exercise is inspired by the incidence logic in Notowidigdo [@notowidigdo2020LocalDemandShocks], but it is not an official replication.

Interpret the transfer table by group:

- **low-wealth renters:** exposed to rent increases and moving frictions;
- **incumbent homeowners:** partly insulated by ownership and may gain from capitalization;
- **commuters:** may access job growth without residential relocation;
- **would-be migrants:** may face entry costs when housing is tight.

## Deliverables

Submit:

- one run log recording the commands used;
- `housing_constraint_adjustment.csv` with a short interpretation memo;
- one paragraph explaining the difference between nominal wage growth and real access;
- one diagnosis table that names the likely binding friction and incidence group for each place;
- `local_demand_incidence_transfer.csv` with a comparison across worker groups;
- one reflection memo explaining what the reduced path teaches and what the full official Hsieh-Moretti package would add.

## Reflection Questions

1. Which places in the reduced reproduction look most like housing-constrained productive places? What evidence supports that classification?
2. When does rent growth imply landlord or homeowner capture rather than worker gains?
3. How would commuting flows change the interpretation of a city-level wage or rent coefficient?
4. In the transfer exercise, which group benefits most from a positive demand shock and why?
5. What would you need from the official Hsieh-Moretti replication materials to move from this teaching path to a closer replication?
6. Why should the Notowidigdo transfer be described as a bounded application rather than an official replication?

