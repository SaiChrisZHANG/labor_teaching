# Code Lab 07: Minimum Wages and Wage Regulations

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 7 --- Minimum wages and wage regulations  
**Associated chapter:** `07-minimum-wages-and-wage-regulations.md`  
**Lab slug:** `07-minimum-wages-and-wage-regulations`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 6 monopsony, basic command-line use, introductory `pandas`, comfort reading grouped summaries and event-study style plots  
**Core economic question:** When minimum wages change, what exactly is the employment object, what is the treatment-intensity object, and how do different empirical designs observe different adjustment margins?  
**Primary source anchor:** `@cengizDubeLindnerZipperer2019`  
**Secondary / challenge anchor:** `@dubeLesterReich2010`  
**Optional extension anchor:** `@engbomMoser2022`

## Why this lab exists

Week 7 can become vague if students say "the minimum wage had no effect" or "the minimum wage killed jobs" without naming the object studied. This lab forces precision. `@cengizDubeLindnerZipperer2019` is the reproduction anchor because it reframes the employment question around jobs below and around the new floor. `@dubeLesterReich2010` is the diagnose anchor because it teaches why local comparison groups matter in policy evaluation. `@engbomMoser2022` is the optional extension because it adds bite, reallocation, and inequality in a high-exposure national setting.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded grouped wage-bin exercise in the spirit of `@cengizDubeLindnerZipperer2019`;
2. state clearly whether the employment object is headcount, hours, or jobs below a threshold;
3. identify the treatment-intensity or bite object rather than relying only on the nominal legal change;
4. explain the main identification challenge in a threshold design and in a border-county design;
5. transfer the design logic to a synthetic border panel or exposure-based regional panel.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact Cengiz-style grouped wage-bin design using synthetic local data.
- Diagnose the difference between grouped low-wage jobs and border-county restaurant employment.
- Transfer the design logic to a synthetic border panel with a bite measure.
- Keep the smoke path fully local and synthetic.
- Do not turn the lab into a full administrative-data replication package.

## Lab roadmap

1. **Reproduce** a grouped wage-bin panel in the spirit of `@cengizDubeLindnerZipperer2019`.
2. **Diagnose** how that object differs from the border-county design in `@dubeLesterReich2010`.
3. **Transfer** the logic to a synthetic border-county panel with explicit treatment intensity.
4. **Extend** the design to a national exposure setting in the spirit of `@engbomMoser2022`.

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not the published replication archive. It is a synthetic teaching workflow that preserves the Week 7 identification logic while running locally without confidential microdata. The goal is to learn what the employment object is and how identification works.

### First commands to run

```bash
conda run -n research python src/reproduce_cengiz_low_wage_jobs.py \
  --outdir output/reproduced

conda run -n research python src/transfer_minimum_wage_designs.py \
  --outdir output/transfer
```

## Part I. Reproduce a bounded Cengiz-style object

### Objective

Recover a compact estimate of wage-bin reshuffling around a new minimum wage using a synthetic grouped panel.

### Be explicit before you run anything

1. **Employment object:** jobs below the new floor and jobs just above it, not total headcount employment in the full labor market.
2. **Treatment-intensity object:** bite, summarized as a local Kaitz-style ratio.
3. **Identifying variation:** before-versus-after changes in grouped low-wage job counts where the policy binds more strongly.
4. **Observed unit:** region-month by wage-bin cell.
5. **Observed margin:** job counts and average wages in bins around the threshold.
6. **Key unobserved object:** the untreated counterfactual path of the low-wage job distribution.

### Student tasks

1. Run `src/reproduce_cengiz_low_wage_jobs.py`.
2. Inspect `output/reproduced/cengiz_low_wage_summary.csv`.
3. Inspect `output/reproduced/cengiz_low_wage_bins.csv`.
4. Open `output/reproduced/cengiz_low_wage_bins.png`.
5. Write a short note explaining why this design studies jobs below a threshold rather than all jobs.

### Required questions

- Is the employment object here headcount, hours, or jobs below a threshold?
- Why is a grouped wage-bin panel informative when total employment may move very little?
- What does the bite object add that the nominal legal change does not?
- What remains latent even after we see disappearing sub-minimum jobs?

## Part II. Diagnose the design difference

### Objective

Compare a threshold-based job-distribution object to a border-county employment object.

### Anchor comparison table

| Paper | Employment object | Identifying variation | Observed unit | Observed margin | Key unobserved object |
| --- | --- | --- | --- | --- | --- |
| `@cengizDubeLindnerZipperer2019` | jobs below and around the threshold | minimum-wage changes with differential bite | region-month by wage-bin | low-wage job counts and wages | untreated low-wage distribution |
| `@dubeLesterReich2010` | local sector employment | state-border minimum-wage differences | contiguous county pair by period | restaurant employment and earnings | untreated local labor-market path |
| `@engbomMoser2022` | wages, inequality, and reallocation under high bite | national reform with heterogeneous exposure | worker-firm or region panel | earnings distribution, reallocation | untreated formal/informal adjustment path |

### Diagnosis checklist

1. **Cengiz-style object:** jobs below a threshold and where they reappear.
2. **Dube-Lester-Reich-style object:** local employment and earnings under a credible nearby comparison market.
3. **Main lesson:** these papers need not report the same elasticity because they study different employment objects, horizons, and identifying comparisons.

### Minimum output

- one short design memo comparing grouped wage-bin and border-county designs;
- one paragraph on the main identification challenge in each design;
- one paragraph naming the key unobserved object in each design.

## Part III. Transfer the Week 7 logic

### Objective

Use a synthetic border panel to connect a local diff-in-diff design to an explicit bite measure.

### Be explicit before you interpret the transfer outputs

1. **Employment object**
   - Restaurant headcount employment in a border-county panel.
   - This is different from jobs below a threshold and different again from hours.

2. **Treatment-intensity object**
   - A local Kaitz-style bite measure.
   - The same nominal policy can bind differently across county pairs.

3. **Main identification challenge**
   - The treated border county must be comparable to the adjacent control county absent the policy.
   - Differential local shocks remain the main threat.

4. **Transfer target**
   - A small public or synthetic border panel, grouped wage-bin panel, or cross-region policy panel.

### Student tasks

1. Run `src/transfer_minimum_wage_designs.py`.
2. Inspect `output/transfer/minimum_wage_border_summary.csv`.
3. Inspect `output/transfer/minimum_wage_border_panel.csv`.
4. Open `output/transfer/minimum_wage_border_event.png`.
5. Explain why the border panel and grouped wage-bin panel complement each other rather than duplicate each other.

### Transfer directions you are allowed to propose

- a public or synthetic border-county panel with restaurant employment;
- a grouped low-wage-job panel by region and month;
- a cross-region policy panel with heterogeneous bite and dynamic treatment timing.

## Part IV. Optional extension

Choose one extension only.

1. Sketch a national exposure design in the spirit of `@engbomMoser2022` using heterogeneous bite across regions or industries.
2. Add an hours margin to the border panel and explain how that changes interpretation.
3. Add a compliance margin and explain how legal incidence could differ from observed incidence.

## Limitations relative to the original papers

Students should say these plainly.

1. The bounded reproduction path uses a synthetic grouped low-wage panel; it is not the original administrative job-bin panel in `@cengizDubeLindnerZipperer2019`.
2. The bounded transfer path uses a stylized border-county panel; it does not reproduce the full QCEW-based border design in `@dubeLesterReich2010`.
3. The optional extension is conceptual; it does not reproduce the full worker-firm and national exposure structure in `@engbomMoser2022`.
4. None of the bounded paths directly recover the full general-equilibrium counterfactual.

## Deliverables checklist

- [ ] reproduced summary table  
- [ ] reproduced wage-bin table  
- [ ] reproduced wage-bin figure  
- [ ] short diagnose memo comparing Cengiz and Dube-Lester-Reich  
- [ ] transfer summary table and border-panel figure  
- [ ] short note on one public or synthetic transfer design  

## Instructor notes

- The highest-value habit is to ask what the employment object is before interpreting any estimate.
- The next highest-value habit is to separate nominal policy change from treatment intensity or bite.
- Students should leave the lab understanding why threshold-based and border-based designs can both be credible while observing different margins.
