---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Static Labor Supply

## Learning objectives

By the end of Week 2, students should be able to:

1. write down the static labor-supply problem and interpret its main comparative statics;
2. separate intensive-margin hours responses from extensive-margin participation responses in a policy-relevant way;
3. analyze piecewise-linear budget sets created by taxes and transfers;
4. explain why fixed work costs and benefit loss make nonparticipation a first-order object rather than a corner case to ignore;
5. interpret the EITC evidence as evidence about margins, information, and schedule geometry rather than as a single elasticity estimate;
6. connect the static benchmark back to Week 1 measurement objects and forward to Weeks 3, 11, and 12.

The economic question for the week is direct: once wages, taxes, transfers, and work costs are taken seriously, how do workers choose whether and how much to work in a static environment?

## Bridge

Week 1 gave us the empirical objects: participation, hours, earnings, and tax-adjusted incentives. Week 2 gives the first formal benchmark for organizing those objects. The static labor-supply model remains indispensable because it is the cleanest map from a policy wedge into behavioral predictions. When the after-tax return to work changes, the benchmark tells us where to look first: entry into work, hours conditional on work, or both.

The benchmark is intentionally narrow. It takes wages and the tax-transfer schedule as given. It abstracts from savings, learning, and dynamic adjustment. That narrowness is a feature before it becomes a limitation. It lets us say clearly what the theory predicts before later weeks add intertemporal substitution, persistence, and informational frictions. In that sense, static labor supply is the worker-side analogue of Week 1 measurement discipline: a minimal object that later extensions must respect rather than bypass.

:::{admonition} Core Material
:class: tip
- the static benchmark maps after-tax incentives into labor-supply behavior
- intensive-margin hours responses and extensive-margin participation responses are different objects
- nonlinear budget sets change local incentives across regions of the schedule
- fixed work costs and benefit loss make participation central rather than exceptional
- the EITC is the main applied bridge from geometry to evidence
:::

### The static benchmark

The canonical static problem is

```{math}
:label: eq-week2-static-problem
\max_{h \in [0,\bar h]} u(c,\bar h-h)
\quad \text{s.t.} \quad c = y + wh - T(wh).
```

Equation {eq}`eq-week2-static-problem` treats hours {math}`h` as the choice variable, nonlabor income {math}`y` as given, and {math}`T(\cdot)` as the full tax-transfer schedule rather than a single linear tax. The object of interest is already policy-facing: the return to an additional hour depends on where the worker sits on the schedule.

If the worker is interior, the key optimality condition is

```{math}
:label: eq-week2-foc
\frac{u_{\ell}(c,\ell)}{u_c(c,\ell)} = w\bigl(1-T'(wh)\bigr),
\qquad \ell = \bar h - h.
```

Equation {eq}`eq-week2-foc` says that the marginal rate of substitution between leisure and consumption must equal the net-of-tax wage. This is the static benchmark that underlies most comparative statics in public economics and labor supply. A tax change matters through the net reward to an extra unit of work, but the size and sign of the total response still depend on income effects, preference heterogeneity, and where the worker is relative to participation.

### Intensive versus extensive margins

The static model becomes policy-relevant only once we separate two margins. The intensive margin asks how hours change among those already working. The extensive margin asks whether work occurs at all. Many empirical debates that look like disagreements about “the labor-supply elasticity” are really disagreements about which of those two objects is moving, for whom, and under which policy environment [@blundellMaCurdy1999; @hausman1985].

That is why nonparticipation cannot be handled as a cosmetic corner solution. With a fixed work cost {math}`F`, the participation condition is

```{math}
:label: eq-week2-participation
V^{\text{work}}(w,y,F) \ge V^{\text{nonwork}}(y).
```

Equation {eq}`eq-week2-participation` makes the extensive margin threshold-based. A worker may face a modest hours response conditional on employment and still show a large participation response if policy changes move the value of work across the threshold created by childcare costs, commuting time, benefit loss, or administrative burden. That is the first reason the EITC literature became central to labor supply: it shifted the empirical center of gravity toward participation responses among populations close to the work/nonwork boundary.

```{figure} assets/figures/02-static-budget-sets.png
:name: fig-week2-budget-sets
Stylized budget sets for the static labor-supply problem. The figure contrasts a no-tax benchmark, a proportional tax, and a fixed-cost environment that introduces a participation wedge. The same wage change can therefore operate differently near the work/nonwork threshold than far from it.
```

Figure {numref}`fig-week2-budget-sets` is useful precisely because it puts Equations {eq}`eq-week2-static-problem` through {eq}`eq-week2-participation` on the same geometry. Proportional taxes flatten the line and mainly speak to the intensive condition in Equation {eq}`eq-week2-foc`. Fixed work costs create a discrete gap between nonwork and work, which is why the extensive margin often dominates for groups with low baseline attachment or high effective work costs.

## Field Core

### Taxes, transfers, and nonlinear budget sets

Real policy environments rarely offer the linear budget line that makes blackboard comparative statics feel clean. Taxes and transfers generate piecewise-linear schedules with kinks, plateaus, and phase-outs. Means-tested benefits can lower the effective return to earnings in one region and raise it in another. A single policy therefore need not move all workers in the same direction even when it applies to all of them.

The EITC is the most useful Week 2 bridge because its geometry makes this point immediately. In the phase-in region, earnings are subsidized and entry into work becomes more attractive. On the plateau, marginal incentives look different from average incentives. In the phase-out region, effective marginal tax rates rise, so the relevant labor-supply question becomes whether workers reduce hours, remain unchanged because of frictions or salience limits, or adjust along other margins.

```{figure} assets/figures/02-eitc-schematic.png
:name: fig-week2-eitc-schematic
Stylized piecewise-linear tax-transfer schedule with phase-in, plateau, and phase-out regions. The point is conceptual rather than calendar-specific: static labor supply under public policy is usually a problem with local slopes and threshold regions, not a single linear wage.
```

Figure {numref}`fig-week2-eitc-schematic` shows why the textbook linear model is not enough for policy interpretation. Once the slope changes across regions, the relevant treatment is local to the worker's position on the schedule. That is the geometric intuition behind kink-based evidence, bunching evidence, and heterogeneous EITC responses.

```{include} assets/tables/02-elasticity-taxonomy.md
```

Table {numref}`tbl:week2-elasticity-taxonomy` is a better organizer of the evidence than a list of headline numbers. It separates compensated from uncompensated intensive responses, distinguishes participation from hours, and warns that taxable-income elasticities need not be real labor-supply elasticities. This is where Chetty's synthesis matters most: different empirical designs recover different objects when adjustment costs and optimization frictions prevent all margins from moving freely [@chetty2012].

```{include} assets/tables/02-policy-margin-map.md
```

Table {numref}`tbl:week2-policy-margin-map` turns that taxonomy into policy language. An EITC expansion is not merely “a tax cut.” For many low-income single parents, it loads first on participation because it changes the value of entering work. A childcare subsidy can operate through both participation and hours because it directly lowers the fixed cost in Equation {eq}`eq-week2-participation`. A payroll-tax change may affect hours, employment, or wages depending on incidence. The policy lesson is that labor-supply debates are really about which margin the instrument is built to move.

### What empirical elasticities mean

The classic static model gives clean comparative statics, but empirical elasticities are recovered from environments in which workers may not know the schedule perfectly, may adjust with delay, or may face discrete constraints on hours. That is why the literature contains what at first looks like disagreement. A micro estimate from a tax reform, a bunching estimate around a kink, and an aggregate cross-regime comparison are not automatically measuring the same object [@blundellMaCurdy1999; @chetty2012].

Three distinctions keep the empirical interpretation disciplined.

First, uncompensated and compensated intensive elasticities answer different questions. The uncompensated object mixes substitution and income effects; the compensated object strips away the income channel but is harder to recover without stronger structure. Second, participation elasticities are inherently threshold-based, so they are sensitive to fixed costs, benefit cliffs, and household constraints. Third, taxable-income responses may reflect reporting, avoidance, timing, or real effort. In a nonlinear schedule, all three distinctions matter simultaneously.

Chetty's contribution is not merely to split the difference across papers. It is to explain why some environments generate small observed intensive responses even when underlying long-run labor-supply objects need not be tiny. Optimization frictions, salience limits, and adjustment costs can compress observed short-run responses, especially where the return to fine-tuning hours is modest [@chetty2012]. That interpretation is especially useful for connecting bunching evidence to the broader labor-supply literature rather than treating it as a separate tax niche.

### The EITC as the applied bridge

The EITC literature is the week's central empirical application because it links schedule geometry, participation, and policy interpretation in a single setting. Eissa and Liebman show that the 1986 expansion generated substantial participation responses among single mothers, with much weaker evidence of large hours changes conditional on work [@eissaLiebman1996]. The key lesson is not simply that labor supply exists; it is that the extensive margin can be the first-order policy channel when the schedule increases the payoff to entering employment.

Eissa and Hoynes extend the perspective to married couples and show why household context matters for the same policy [@eissaHoynes2004]. An EITC expansion can raise incentives for one spouse while reducing them for the secondary earner, depending on where family earnings place the household on the schedule. The static model therefore needs a household interpretation even before we reach the family module later in the semester.

The broader review in Eissa and Hoynes organizes the lesson cleanly: empirical labor-supply responses to the EITC are heterogeneous because the policy changes average and marginal incentives differently across families and across regions of the schedule [@eissaHoynes2006]. That is exactly the kind of policy-to-margin mapping summarized in Table {numref}`tbl:week2-policy-margin-map`.

Saez adds a complementary perspective by studying bunching at kink points in the tax schedule [@saez2010]. Bunching evidence is attractive because Figure {numref}`fig-week2-eitc-schematic` implies that local slope changes create local incentives to concentrate earnings near a kink. But the interpretation is subtle. Some taxpayers bunch strongly and others do not; some responses may reflect reporting or adjustment of taxable income rather than hours; and the amount of bunching can be dampened when the schedule is poorly understood or costly to optimize around.

Chetty, Friedman, and Saez sharpen that last point by showing that local knowledge and information frictions shape observed EITC responses [@chettyFriedmanSaez2013]. Their lesson is not that the static benchmark is wrong. It is that the benchmark delivers the right comparative statics only once we ask what workers know about the schedule and whether they can act on that knowledge. That is the bridge to Week 12, where information, attention, and behavioral responses stop being an add-on and become part of the model itself.

## Research Lab

The frontier issue is not whether the static model should be discarded. It is which empirical object remains informative once the environment includes nonlinear schedules, fixed costs, limited salience, and household interactions. One open research direction asks how far extensive-margin elasticities travel across institutional settings. A participation response to the EITC among single mothers in the 1990s is not automatically the right object for forecasting responses to childcare subsidies, payroll-tax changes, or reforms in countries with different transfer systems.

Another frontier issue is measurement of the relevant response variable. Bunching in taxable income is a sharp design, but taxable income can move because reported earnings move, timing shifts, deductions change, or formal labor supply changes. That makes Week 2 a natural bridge between labor economics and public finance rather than a purely worker-choice chapter.

The research payoff from the week comes from treating the benchmark as indispensable and incomplete at the same time. Week 3 will add intertemporal substitution and lifecycle adjustment. Week 11 will revisit the same margins in a broader worker-policy evaluation framework. Week 12 will ask how informational and behavioral frictions change both elasticities and welfare interpretation. Week 2 matters because those later modules only make sense if the static benchmark is already clear.

## Methods Box

Week 2 uses a simple translation rule from theory to empirical design.

1. Write the choice problem and identify whether the policy shifts the average return to work, the marginal return, or both.
2. Ask whether the relevant outcome is participation, hours conditional on work, earnings, or taxable income.
3. Check whether the budget set is linear, piecewise linear, kinked, or nonconvex.
4. Decide whether the design identifies a local response near a threshold or a broader behavioral object.
5. Interpret the estimate in light of information, adjustment, and reporting frictions.

The point is to keep Equations {eq}`eq-week2-static-problem`, {eq}`eq-week2-foc`, and {eq}`eq-week2-participation` tied to data rather than leaving them as pure diagrammatic intuition.

## Reading ladder

### Bridge

- Blundell and MaCurdy on the static benchmark and how labor-supply objects are defined [@blundellMaCurdy1999]
- Hausman on taxes, nonlinear budget sets, and the public-finance interpretation of labor supply [@hausman1985]

### Field Core

- Eissa and Liebman on single-mother participation responses to the EITC [@eissaLiebman1996]
- Eissa and Hoynes on married-couple labor-supply responses under the EITC [@eissaHoynes2004]
- Eissa and Hoynes on broader lessons from the EITC literature [@eissaHoynes2006]
- Chetty on labor-supply elasticities with optimization frictions [@chetty2012]

### Research Lab

- Saez on bunching at kink points and the interpretation of local nonlinear-budget responses [@saez2010]
- Chetty, Friedman, and Saez on knowledge frictions and EITC responses [@chettyFriedmanSaez2013]
- Optional structural extensions on work costs and piecewise-linear budgets [@heimMeyer2004; @fullertonGan2004]

## Exercises / discussion prompts

1. Use Equations {eq}`eq-week2-foc` and {eq}`eq-week2-participation` to explain why the same policy can generate small hours responses but large participation responses.
2. In Figure {numref}`fig-week2-eitc-schematic`, which region of the schedule is most naturally associated with entry into work, and which region is most naturally associated with hours adjustment? Defend your answer.
3. Why is the taxable-income elasticity in Table {numref}`tbl:week2-elasticity-taxonomy` not automatically a labor-supply elasticity?
4. Eissa and Hoynes show that married-couple responses need not match single-mother responses. Which object in the static model is doing the work?
5. If bunching is weak in a setting with strong formal incentives, what are the leading interpretations before concluding that labor supply is inelastic?

## Reproducibility or code lab note

The Week 2 lab is built around a bounded teaching path for [@saez2010]. Students reproduce a stylized bunching figure using the local synthetic dataset and the Python scripts in `labs/02-static-labor-supply/src/`, then transfer the same workflow to an alternative subgroup or bin-width choice. The full official AEA replication package remains the intellectual benchmark, but the bounded path deliberately avoids requiring the full external package for the smoke test. The lab note at [labs/02-static-labor-supply/lab.md](labs/02-static-labor-supply/lab.md) documents the exact external files still needed for a closer reproduction using the official materials.

## Slide companion note

The slide deck should isolate the benchmark problem, the margin decomposition, the nonlinear-budget geometry, and the empirical EITC lessons without turning the chapter into text-heavy slides. The deck at [slides/week2/02-static-labor-supply.tex](slides/week2/02-static-labor-supply.tex) therefore focuses on Equations {eq}`eq-week2-static-problem` through {eq}`eq-week2-participation`, Figures {numref}`fig-week2-budget-sets` and {numref}`fig-week2-eitc-schematic`, the elasticity taxonomy, and the forward link to Weeks 3, 11, and 12.
