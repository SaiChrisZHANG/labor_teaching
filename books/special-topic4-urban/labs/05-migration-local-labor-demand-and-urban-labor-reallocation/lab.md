# Week 5 Lab: Migration, Local Labor Demand, And Urban Labor Reallocation

## Purpose

This lab turns Week 5 into a bounded empirical workflow. It does not reproduce confidential data or official estimates. Instead, it uses deterministic synthetic data to practice the design objects behind local labor-demand shocks, migration, commuting, incidence, gentrification, and diversification.

Primary anchor: Howard on the migration accelerator, where migration affects local labor markets through labor supply, housing demand, construction, and nontradable demand [@howard2020migration].

Transfer anchors: Monte, Redding, and Rossi-Hansberg on commuting and migration adjustment, Notowidigdo on incidence, Hershbein and Stuart on local recovery, Couture and coauthors on neighborhood change, and de Soyres and coauthors on diversification and resilience [@monteReddingRossiHansberg2018; @notowidigdo2020LocalDemandShocks; @hershbein2024evolution; @couture2023neighborhood; @desoyres2025diversity].

## Workflow

### Reproduce

Run the synthetic local-demand path and inspect `output/reproduced/local_adjustment_vector.csv`.

The script creates four local labor markets with different housing elasticity, commuting openness, moving frictions, and industry structure. A demand shock changes wages, rents, employment, population, commuting, firm entry, and incumbent real access. The object is the adjustment vector:

```{math}
\Delta Y_{\ell t}
=
\left(
\Delta w_{\ell t},
\Delta E_{\ell t},
\Delta U_{\ell t},
\Delta N_{\ell t},
\Delta C_{\ell t},
\Delta R_{\ell t},
\Delta F_{\ell t},
\Delta S_{\ell t}
\right).
```

The exercise asks students to interpret the pattern rather than one coefficient. A place with wage gains and rent growth may not generate incumbent renter gains. A place with employment growth may benefit commuters more than residents. A place with weak migration may still adjust through commuting.

### Diagnose

Open `output/diagnosed/incidence_diagnosis.csv`. For each synthetic claim, classify:

- the affected unit: incumbent worker, migrant, commuter, landlord, firm, or place;
- the main adjustment margin: migration, commuting, rents, wages, firm entry, persistence, or composition;
- the welfare object: nominal wage, real access, unemployment risk, moving cost, or capitalization;
- the main interpretation threat.

Answer four questions for each row:

1. Is the outcome place-based or person-based?
2. Which margin adjusts first?
3. Who captures the surplus or bears the loss?
4. What additional data would change the interpretation?

### Transfer A: Gentrification

Open `output/transfer/gentrification_restructuring.csv`. The transfer exercise models three neighborhoods with changes in professional inflow, service demand, rent pressure, and incumbent exposure. Interpret the output as labor-market restructuring:

- Which jobs are created?
- Which workers can reach or keep those jobs?
- Are incumbent renters better off after rents and commute changes?
- Is the observed job growth a resident gain, commuter gain, or composition change?

### Transfer B: Diversification

Open `output/transfer/diversification_resilience.csv`. The diversification scenario compares specialized and diversified places hit by the same sectoral shock. The output reports predicted employment loss, reallocation capacity, migration pressure, and worker insurance value.

The labor question is not whether diversity is aesthetically appealing. It is whether the local economy gives workers alternative job ladders after a shock without forcing costly migration.

## Bounded Extension

Add one worker group to the synthetic model: low-wealth renters, high-wealth owners, transit-dependent commuters, or sector-specific displaced workers. Recompute the incidence table and write a short memo explaining which result changes and why.

Keep the extension bounded. Do not turn it into a full urban model unless you can name the shock, geography, worker margin, housing margin, and welfare object.

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path runs the complete bounded exercise and checks that the core output files were written. No confidential data or external downloads are required.

## Submission Checklist

- one table interpreting the local adjustment vector;
- one paragraph distinguishing place recovery from worker recovery;
- one incidence diagnosis table naming who gains or loses;
- one gentrification memo that treats neighborhood change as labor restructuring;
- one diversification memo that distinguishes resilience from selection;
- one research-design paragraph naming the empirical setting, identification strategy, econometric method, labor margin, and welfare object.
