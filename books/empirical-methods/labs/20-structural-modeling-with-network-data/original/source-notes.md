# Source Notes

## Anchor Papers

The reproduce path uses Mele [@mele2017structural] as the primary structural-network anchor and Graham [@graham2017econometric] as the econometric companion for degree heterogeneity and network formation.

## Replication Status

No official replication files for these anchor papers are stored locally in this repository. The lab therefore uses a bounded synthetic path. It does not reproduce published coefficients, likelihood values, or structural primitives.

## Synthetic Data Design

The generated worker data include:

- worker group;
- occupation;
- neighborhood;
- seniority;
- skill;
- referral access;
- a synthetic wage outcome;
- a synthetic referral-offer outcome.

The dyad data include:

- same-group and same-occupation indicators;
- skill distance;
- geographic distance;
- seniority opportunity;
- referral opportunity;
- a realized link indicator;
- tie strength.

The directed edge list is constructed from realized undirected dyads. The generated outcome depends partly on network information exposure so students can see why formation assumptions affect counterfactuals.

## What Students Should Not Claim

Students should not claim that the exercise estimates Mele's model, Graham's model, or real labor-market referral effects. The exercise is a transparent teaching analogue for the structural workflow.
