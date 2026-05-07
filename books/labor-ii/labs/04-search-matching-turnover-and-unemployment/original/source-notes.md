# Source notes for the bounded reproduction path

## Paper anchor

- Primary anchor: `@hallSchulhoferWohl2018`

## What the bounded path reproduces

The local synthetic file is a seeker-type by month panel. Each row records:

- a seeker type,
- the number of unemployed searchers in that type,
- the number of matches from unemployment to employment,
- and the vacancy count for the month.

This lets students recover:

1. the aggregate U-to-E job-finding rate,
2. type-specific job-finding rates,
3. a simple fixed-composition counterfactual.

## What the bounded path does not reproduce

- no confidential microdata;
- no exact CPS cleaning pipeline;
- no structural estimation of latent matching efficiency;
- no full decomposition of worker heterogeneity, geography, or search channels.

## Core teaching point

Students should leave this lab able to say:

- which transition margin is being measured;
- which hazard object is being approximated;
- why composition shifts can move the aggregate rate even when within-type rates do not move much;
- why the resulting decomposition is informative but still not a full structural search estimate.
