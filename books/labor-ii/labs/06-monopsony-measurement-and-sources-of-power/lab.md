# Code Lab 06: Monopsony, Measurement, and Sources of Power

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 6 --- Monopsony, measurement, and sources of power  
**Associated chapter:** `06-monopsony-measurement-and-sources-of-power.md`  
**Lab slug:** `06-monopsony-measurement-and-sources-of-power`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 5 wage-setting, basic command-line use, introductory `pandas`, comfort reading grouped summaries and simple plots  
**Core economic question:** Which monopsony object is actually being measured, and how does that depend on the data and identifying variation?  
**Primary source anchor:** [@dubeJacobsNaiduSuri2020]  
**Secondary / challenge anchor:** [@yehMacalusoHershbein2022]  
**Optional extension anchor:** [@pragerSchmitt2021]

## Why this lab exists

Week 6 can become muddy if students treat every wage or concentration result as "a monopsony estimate." This lab forces discipline. [@dubeJacobsNaiduSuri2020] is the reproduction anchor because direct wage variation makes labor supply to the firm concrete. [@yehMacalusoHershbein2022] is the diagnose anchor because markdowns are a different monopsony object that require stronger structure. [@pragerSchmitt2021] is the transfer anchor because merger evidence is causal about changing market structure but still does not reveal the full underlying wedge.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded labor-supply-to-the-firm exercise using direct wage variation;
2. state clearly which monopsony object each anchor paper is measuring;
3. explain whether the identifying variation comes from wages, concentration, mergers, or production-side moments;
4. name the key unobserved object that remains latent in each design;
5. transfer the design logic to a public or synthetic setting such as online-task data, a stylized employer concentration panel, or a simulated plant markdown panel.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact Dube-style recruiting elasticity using a local synthetic task panel.
- Diagnose a Yeh-style markdown object using a synthetic plant panel.
- Transfer the design logic to a concentration-and-merger panel in the spirit of [@pragerSchmitt2021].
- Keep the smoke path fully local and synthetic.
- Do not turn the lab into a confidential microdata replication or a full structural model of labor market power.

## Lab roadmap

1. **Reproduce** a bounded online-labor elasticity object in the spirit of [@dubeJacobsNaiduSuri2020].
2. **Diagnose** how that object differs from a Yeh-style markdown.
3. **Transfer** the measurement logic to a stylized concentration and merger panel.
4. **Extend** the design to a public vacancy or local labor market dataset.

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not a literal replication package for the published papers. It is a synthetic teaching workflow that preserves the Week 6 identification logic while running locally without confidential microdata. The goal is to learn how monopsony objects differ, not to reproduce every institutional layer of the originals.

### First commands to run

```bash
conda run -n research python src/reproduce_dube_online_monopsony.py \
  --outdir output/reproduced

conda run -n research python src/transfer_monopsony_measurement.py \
  --outdir output/transfer
```

## Part I. Reproduce a bounded Dube-style object

### Objective

Recover a compact estimate of labor supply to the firm from direct wage variation in a synthetic online-task panel.

### Be explicit before you run anything

1. **Monopsony object:** labor supply elasticity to the firm through recruiting behavior.
2. **Identifying variation:** within-platform wage variation across otherwise similar tasks.
3. **Observed unit:** task or task-requester posting.
4. **Observed margin:** applications and fill probability.
5. **Key unobserved object:** the worker's broader outside-option set off the platform and any dynamic market response.

### Student tasks

1. Run `src/reproduce_dube_online_monopsony.py`.
2. Inspect `output/reproduced/dube_online_monopsony_summary.csv`.
3. Inspect `output/reproduced/dube_online_monopsony_by_quartile.csv`.
4. Open `output/reproduced/dube_online_monopsony_elasticity.png`.
5. Write a short note explaining what object was measured and why it is a labor-supply-to-the-firm object rather than a concentration object.

### Required questions

- What exactly is the monopsony object in [@dubeJacobsNaiduSuri2020]?
- Why is direct wage variation cleaner for measuring recruiting elasticity than cross-market concentration alone?
- Which margin is observed here that would be absent in a pure production-side markdown design?
- What remains latent even in this clean wage-variation setting?

## Part II. Diagnose the difference between elasticity and markdown objects

### Objective

Move from "we estimated an elasticity" to a disciplined explanation of why a production-side markdown estimate is a different object.

### Anchor comparison table

| Paper | Monopsony object | Identifying variation | Observed unit | Observed margin | Key unobserved object |
| --- | --- | --- | --- | --- | --- |
| [@dubeJacobsNaiduSuri2020] | labor supply elasticity to the firm | wage variation | task / posting | applications, fills | broader outside options and general equilibrium |
| [@yehMacalusoHershbein2022] | markdown {math}`MRPL / w` | production-side moments plus structure | plant / firm | wage and production moments | true MRPL and structural validity |
| [@pragerSchmitt2021] | reduced-form wage response to structure shock | merger-induced concentration change | market / worker-market | wage change after consolidation | full monopsony wedge and spillovers |

### Diagnosis checklist

1. **Dube-style object:** direct elasticity of worker response to own-firm wages.
2. **Yeh-style object:** wedge between pay and inferred marginal revenue product.
3. **Prager-Schmitt-style object:** causal wage response to changing employer concentration.
4. **Main lesson:** these are not competing labels for the same number; they are different windows into labor market power.

### Minimum output

- one short design memo comparing the three objects;
- one paragraph on why elasticity, markdown, and merger estimates need not match numerically;
- one paragraph naming the most important unobserved object in each design.

## Part III. Transfer the Week 6 logic

### Objective

Use a synthetic plant and market panel to compare markdown measurement with concentration and merger evidence.

### Be explicit before you interpret the transfer outputs

1. **Yeh-style synthetic panel**
   - Monopsony object: markdown.
   - Identifying variation: production-side moments generated across plants with different wage-setting wedges.
   - Observed unit: plant-year.
   - Observed margin: wages, revenue product index, and inferred markdown.
   - Key unobserved object in real data: true marginal revenue product.

2. **Prager-Schmitt-style synthetic panel**
   - Monopsony object: wage response to market-structure change.
   - Identifying variation: merger-induced rise in local concentration.
   - Observed unit: market-year.
   - Observed margin: wage change around merger.
   - Key unobserved object in real data: the deeper elasticity or markdown parameter behind the wage response.

### Student tasks

1. Run `src/transfer_monopsony_measurement.py`.
2. Inspect `output/transfer/monopsony_transfer_summary.csv`.
3. Open `output/transfer/monopsony_transfer_comparison.png`.
4. Explain why the markdown panel and the merger panel are informative about monopsony for different reasons.
5. Write one paragraph on how you would transfer one of these designs to a public or synthetic setting.

### Transfer directions you are allowed to propose

- a public vacancy or job-posting dataset with wage and applicant counts;
- a stylized employer concentration panel by commuting zone and occupation;
- a simulated plant markdown panel with heterogeneous wedges;
- a synthetic merger event study in a thin local labor market.

## Part IV. Optional extension

Choose one extension only.

1. Design a public-data transfer using vacancy postings and a recruiting elasticity object.
2. Design a synthetic plant panel that distinguishes markdowns from firm wage premia.
3. Design a merger panel that tracks wages, exits, and vacancies before and after consolidation.

## Limitations relative to the original papers

Students should say these plainly.

1. The bounded reproduction path uses synthetic task postings; it is not the original online labor platform in [@dubeJacobsNaiduSuri2020].
2. The bounded transfer path uses a stylized plant and market panel; it does not recover the full production-side and administrative detail in [@yehMacalusoHershbein2022].
3. The merger-style comparison is a synthetic teaching exercise; it does not reproduce the full hospital consolidation design in [@pragerSchmitt2021].
4. None of the bounded paths directly observes the worker's full outside-option set, the true marginal revenue product, or the full equilibrium spillover structure.

## Deliverables checklist

- [ ] reproduced summary table  
- [ ] reproduced quartile table  
- [ ] reproduced elasticity figure  
- [ ] short diagnose memo comparing Dube, Yeh, and Prager-Schmitt  
- [ ] transfer summary table and figure  
- [ ] short note on one public or synthetic transfer design  

## Instructor notes

- The highest-value habit is to ask "which monopsony object is this?" before any interpretation begins.
- The next highest-value habit is to separate identifying variation from the economic object identified.
- Students should leave the lab understanding why a recruiting elasticity, a markdown, and a merger effect can all be valid evidence on monopsony without being the same statistic.
