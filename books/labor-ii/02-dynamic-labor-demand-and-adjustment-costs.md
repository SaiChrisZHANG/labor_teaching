---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Dynamic Labor Demand and Adjustment Costs

## Learning objectives

By the end of Week 2, students should be able to:

1. explain why actual employment can remain away from the Week 1 static target when labor adjustment is costly;
2. distinguish target employment from actual employment, and reduced-form speed-of-adjustment estimates from structural adjustment-cost parameters;
3. write a dynamic labor-demand problem with adjustment costs and interpret the key state variables;
4. contrast convex adjustment costs with fixed or nonconvex costs, including the difference between smooth partial adjustment and lumpy inaction;
5. explain why hours, headcount, hiring, separations, and vacancies need not move at the same horizon;
6. interpret policy event studies and structural dynamic evidence without confusing timing responses with long-run effects;
7. connect Week 2 forward to Week 3 on personnel choices inside the firm.

The economic question for Week 2 is a direct continuation of Week 1: once the firm has a desired labor target, why does observed employment usually move toward that target gradually rather than instantly?

## Bridge

Week 1 derived the firm's static target. If wages, output demand, technology, or payroll taxes change, the firm has a new desired employment level. Week 2 asks why that destination does not instantly become the observed employment path. Hiring takes screening and onboarding. Firing can trigger legal, organizational, or morale costs. Reassigning workers, changing shifts, or expanding vacancies can be easier than changing core headcount right away [@nickell1986; @hamermesh1989].

That makes the basic Week 2 distinction unavoidable: the static benchmark tells us where the firm would like to be, but dynamic labor demand studies how the firm moves from its inherited workforce to that new target. The observed path reflects state dependence, the availability of alternative margins, and the firm's expectations about whether the shock will persist.

This week remains firmly inside the firm. It does not yet build a full search equilibrium, bargaining model, or monopsony framework. Those arrive later. The point here is narrower and foundational: before labor markets can be matched or bargained over, firms still face a dynamic employment problem. Week 3 will take that dynamic firm and ask how incentives, internal labor markets, and promotion structures reshape its personnel choices.

## Field Core

### From target employment to actual employment

Week 1 gave the static benchmark. We can summarize it as a target-employment object:

```{math}
:label: eq-lii-w2-target
L_t^{\ast} = L^{\ast}(w_t, p_t, K_t, A_t, q_t).
```

Equation {eq}`eq-lii-w2-target` is the correct bridge back to Week 1. The target {math}`L_t^{\ast}` depends on wages, productivity, output demand, and other state variables. Week 2 begins because actual employment {math}`L_t` need not equal {math}`L_t^{\ast}` each period. Firms inherit yesterday's workforce, not a blank slate.

```{figure} assets/figures/02-target-vs-actual-employment.png
:name: fig-lii-w2-target-vs-actual
Target versus actual employment after a positive labor-demand shock. The gap between the two is the central Week 2 object: the firm knows where it wants to go, but it gets there gradually.
```

Figure {numref}`fig-lii-w2-target-vs-actual` makes the main conceptual move visible. The empirical object is not just the new target after a shock. It is the gap between actual and target employment, how quickly that gap closes, and which margins close it first.

This is also the right place to introduce horizon language. In the short run, firms often move hours, overtime, or temporary labor before they move permanent headcount. In the medium run, hiring and separations begin to reshape the workforce. In the long run, capital, task allocation, and organizational structure may also adjust. A single employment estimate without a horizon is therefore incomplete [@shapiro1986; @hamermesh1989].

### The dynamic firm problem

The standard dynamic benchmark writes the firm's problem as

```{math}
:label: eq-lii-w2-bellman
V(L_{t-1}, s_t) = \max_{L_t} \left\{ \pi(L_t, s_t) - C(L_t-L_{t-1}) + \beta E_t\!\left[V(L_t, s_{t+1})\right] \right\},
```

where {math}`s_t` collects wages, demand, productivity, policy, and other states. Equation {eq}`eq-lii-w2-bellman` says that labor demand is dynamic because employment today changes both current profits and tomorrow's feasible choices. The inherited workforce {math}`L_{t-1}` is a state variable, not just yesterday's accounting outcome.

Three ideas follow immediately.

1. Employment persistence is not automatically proof of adjustment costs. Persistence can also reflect persistent shocks, measurement timing, or other omitted states.
2. The cost function {math}`C(\cdot)` is the central Week 2 object because it determines how painful it is to move employment.
3. If hours, overtime, vacancies, or temporary workers are cheaper to vary than core headcount, those margins will absorb more of the short-run response.

```{include} assets/tables/02-adjustment-cost-taxonomy.md
```

Table {numref}`tbl:adjustment-taxonomy` summarizes the main friction types. The key distinction is not merely between "fast" and "slow" firms. It is between cost structures that imply smooth adjustment and cost structures that imply inaction punctuated by jumps.

### Convex adjustment costs and partial adjustment

The cleanest benchmark uses convex costs, often quadratic in employment changes. In that case, large employment changes are disproportionately expensive, so the firm spreads adjustment across time [@nickell1986; @shapiro1986].

```{math}
:label: eq-lii-w2-partial-adjustment
L_t - L_{t-1} = \lambda \left(L_t^{\ast} - L_{t-1}\right),
\qquad 0 < \lambda \le 1.
```

Equation {eq}`eq-lii-w2-partial-adjustment` is the textbook partial-adjustment law. If {math}`\lambda = 1`, the firm jumps immediately to target. If {math}`\lambda` is small, adjustment is gradual. Empirically, {math}`\lambda` is often estimated as a reduced-form speed-of-adjustment parameter. It is useful, but it is not itself a primitive structural cost parameter. Mapping from {math}`\lambda` to deep costs requires stronger model discipline than a one-equation estimate provides [@hamermesh1989].

Convex costs imply frequent but modest changes. That matters for policy interpretation. When a payroll-tax cut lowers labor cost today, the employment response may unfold over multiple horizons even if the new target is known immediately. Short-run incidence can therefore differ sharply from medium-run and long-run incidence.

```{figure} assets/figures/02-convex-vs-nonconvex-adjustment.png
:name: fig-lii-w2-convex-nonconvex
Convex costs generate smooth partial adjustment, while fixed or nonconvex costs generate inaction followed by larger jumps.
```

Figure {numref}`fig-lii-w2-convex-nonconvex` highlights what convex costs do not predict. If the data show many zero adjustments combined with occasional large spikes, the convex benchmark is incomplete.

### Fixed and nonconvex costs, inaction, and lumpiness

When adjustment triggers a fixed reorganization cost, a hiring cost, or a firing cost that does not scale smoothly with the size of the change, firms may wait until the gap is large enough to justify moving. A compact threshold representation is

```{math}
:label: eq-lii-w2-inaction
\text{adjust if } \left|L_t^{\ast} - L_{t-1}\right| > \bar{\Delta}.
```

Equation {eq}`eq-lii-w2-inaction` is not a full model, but it captures the central intuition behind nonconvex adjustment. Small shocks generate inaction. Large shocks generate lumpy adjustments. This is the language students need before reading plant-level evidence on hazards, zeros, and spikes in employment change [@caballeroEngelHaltiwanger1997].

The substantive contrast with convex costs is sharp.

1. Convex costs predict smooth employment paths and many small adjustments.
2. Fixed or nonconvex costs predict long spells of no change and occasional large adjustments.
3. Firing costs can generate asymmetry: contraction after negative shocks may be slower or differently timed than expansion after positive shocks [@bentolilaBertola1990].

Micro lumpiness does not imply aggregate chaos. Many plants can adjust at different times, so aggregate employment still looks smoother than establishment-level behavior. That is one reason macro employment persistence alone is not enough to identify the micro cost structure.

### Which margin adjusts first?

Dynamic labor demand is not only about how much employment moves. It is also about which margin moves first. Hours and overtime are often quicker to vary than permanent headcount. Hiring and vacancies are more informative after positive shocks; layoffs and separations are more informative after negative shocks. Temporary labor can buffer the core workforce. Labor hoarding means a firm may keep headcount high after a temporary downturn while reducing hours, effort, or utilization.

```{figure} assets/figures/02-hours-vs-headcount-adjustment.png
:name: fig-lii-w2-hours-headcount
Hours often absorb more of the short-run response than headcount. That is why headcount-based estimates alone can understate early labor-demand adjustment.
```

Figure {numref}`fig-lii-w2-hours-headcount` is a warning against one-margin empirics. A weak contemporaneous employment effect does not imply that labor demand failed to respond. It may imply that the firm used the intensive margin first.

```{include} assets/tables/02-observed-margins-map.md
```

Table {numref}`tbl:observed-margins-week2` should be read before any empirical result is interpreted. The first question is always: what labor margin is observed? The second is: which margins were available but unobserved?

### Empirical designs and what they identify

Week 2 evidence is easiest to organize by identifying variation rather than by chronology.

```{include} assets/tables/02-design-map.md
```

Plant and establishment panels track repeated outcomes for the same firm or production unit. The identifying variation comes from within-unit changes over time, and the observed margins are often employment, hours, hires, or separations. These designs are useful for persistence, hazard, and lumpiness, but unobserved shocks can still masquerade as adjustment frictions [@hamermesh1989; @caballeroEngelHaltiwanger1997].

Policy timing designs use labor-cost reforms or payroll-tax changes as the shock. The identifying variation is a change in labor cost, and the observed margin may include employment, hours, wages, or profits over event time. These designs identify dynamic incidence paths rather than a timeless elasticity [@saezSchoeferSeim2019].

Survey or expectation-based designs are especially useful when the question is whether uncertainty changes the timing of adjustment. In `@dibiasiMikoschSarferaz2025`, the identifying variation comes from differences in uncertainty and firm beliefs, while the observed objects are expected and realized employment responses. That is informative about delay and state dependence, but it is not the same as observing every margin of actual headcount change in administrative payroll records.

Structural dynamic estimation goes one step further by imposing a model like Equation {eq}`eq-lii-w2-bellman` and estimating deep cost parameters. That can support counterfactual policy analysis, but only if the state space, the choice set, and measurement of margins are credible. This is why a reduced-form speed-of-adjustment estimate and a structural cost estimate answer related but distinct questions.

### Policy timing and incidence over the adjustment path

Dynamic labor demand matters for policy because incidence is a path, not just an endpoint. If a payroll tax changes at {math}`t`, the relevant object is

```{math}
:label: eq-lii-w2-policy-timing
\frac{\partial L_{t+h}}{\partial \tau_t},
\qquad h = 0,1,2,\ldots
```

Equation {eq}`eq-lii-w2-policy-timing` forces the timing question into the notation. The contemporaneous effect {math}`h=0` can be modest if firms first adjust hours, vacancies, or prices. Medium-run effects may be larger as headcount changes accumulate. Long-run effects may differ again once capital and organization adjust.

```{figure} assets/figures/02-policy-incidence-over-time.png
:name: fig-lii-w2-policy-timing
The employment effect of a labor-cost shock often builds over time. Short-run, medium-run, and long-run incidence need not coincide.
```

Figure {numref}`fig-lii-w2-policy-timing` is the clean bridge from theory to applied policy work. `@saezSchoeferSeim2019` is useful here because the identifying variation is a payroll-tax reform, the observed margins include both wages and employment, and the key result is dynamic incidence rather than a single static elasticity. The same reform can look small in the short run and substantial over longer horizons because the firm's adjustment margins are sequenced.

The dynamic policy lesson is broader than payroll taxes. Employment protection, firing costs, and hiring subsidies all reshape the timing margin. The central Week 2 habit is therefore to report both the shock and the horizon.

## Research Lab

The frontier lesson from Week 2 is that observed persistence is economically ambiguous until we name the target, the horizon, and the observed margin. A plant panel with many zero employment changes points toward nonconvex adjustment, but it may also reflect uncertainty, measurement intervals, or the availability of off-margin responses. A policy event study with a flat contemporaneous estimate may still hide meaningful medium-run employment adjustment if firms move hours or wages first.

`@dibiasiMikoschSarferaz2025` is a strong lab anchor because it pushes students to interpret dynamic responses through firm beliefs and uncertainty rather than through one-shot elasticities alone. `@caballeroEngelHaltiwanger1997` is the complementary challenge anchor because it asks what aggregate employment dynamics imply once micro-level inaction and lumpiness are present.

### Optional extension block

One optional extension is uncertainty and the option value of waiting. If adjustment is partly irreversible, firms may delay employment changes when the environment is noisy even if the static target has already shifted. This is the cleanest route from dynamic labor demand into beliefs, expectations, and survey evidence [@dibiasiMikoschSarferaz2025].

The second optional extension is structural estimation. Here the goal is to recover deep adjustment-cost parameters rather than only a reduced-form response speed. That move is valuable for counterfactual policy analysis, but it requires stronger assumptions about the state space, the firm's information set, and which margins are observed.

## Methods Box

Week 2 only works if the empirical language stays disciplined.

1. Target employment {math}`L_t^{\ast}` is the Week 1 object; actual employment {math}`L_t` is the Week 2 object.
2. Convex costs imply partial adjustment; fixed or nonconvex costs imply inaction bands and lumps.
3. Hours versus headcount and hiring versus firing are not interchangeable margins.
4. Short-run, medium-run, and long-run responses can differ even under the same eventual target.
5. A reduced-form speed-of-adjustment estimate is not the same object as a structural cost parameter.
6. Policy event studies identify dynamic timing responses to a shock; structural dynamic models try to recover primitives that support counterfactuals.
7. Do not report an empirical result without naming both the identifying variation and the observed margin.

## Reading ladder

### Bucket A. Dynamic benchmark

- `@nickell1986` for the canonical field-style overview of dynamic labor-demand models.
- `@shapiro1986` for a dynamic factor-demand benchmark that helps students see why adjustment speed is an equilibrium object inside the firm.
- `@hamermesh1989` for the structure of adjustment costs and the distinction between reduced-form adjustment patterns and underlying cost primitives.

### Bucket B. Adjustment frictions and firing costs

- `@bentolilaBertola1990` for the logic of firing costs and asymmetric adjustment.
- `@caballeroEngelHaltiwanger1997` for the connection between establishment-level lumpiness and aggregate employment dynamics.

### Bucket C. Modern measurement of dynamic frictions

- `@dibiasiMikoschSarferaz2025` for evidence linking uncertainty, firm beliefs, and adjustment costs to employment timing.

### Bucket D. Policy timing and incidence bridge

- `@saezSchoeferSeim2019` for payroll-tax incidence over the adjustment path and the bridge from dynamic labor demand to later wage-setting weeks.

## Exercises / discussion prompts

1. Use Equations {eq}`eq-lii-w2-target` and {eq}`eq-lii-w2-partial-adjustment` to explain why a contemporaneous employment estimate can understate the eventual effect of a labor-cost shock.
2. What features of plant-level data would make you favor Equation {eq}`eq-lii-w2-inaction` over Equation {eq}`eq-lii-w2-partial-adjustment`?
3. Why can two studies of the same reform disagree if one observes hours and the other observes headcount?
4. In Table {numref}`tbl:design-map-week2`, which designs speak most directly to policy timing, and which speak most directly to structural cost parameters?
5. How does Week 2 change the interpretation of the Week 1 target employment object?

## Reproducibility or code lab note

The Week 2 lab follows the standard `Reproduce -> Diagnose -> Transfer` structure. The bounded reproduction path uses a local synthetic firm panel inspired by `@dibiasiMikoschSarferaz2025` so students can trace target versus actual employment, hours, and uncertainty without confidential microdata. The diagnose step asks them to name the identifying variation, the observed margin, and the implied dynamic object. The transfer step then compares convex and nonconvex adjustment paths with `@caballeroEngelHaltiwanger1997` as the challenge anchor and `@saezSchoeferSeim2019` as the optional policy-timing extension. The local handout lives at [labs/02-dynamic-labor-demand-and-adjustment-costs/lab.md](labs/02-dynamic-labor-demand-and-adjustment-costs/lab.md).

## Slide companion note

The slide deck at [slides/week2/02-dynamic-labor-demand-and-adjustment-costs.tex](slides/week2/02-dynamic-labor-demand-and-adjustment-costs.tex) should stay tighter than the chapter: central question, Week 1 to Week 2 bridge, target versus actual employment, dynamic objective, convex partial adjustment, fixed-cost inaction, margins of adjustment, empirical design buckets, policy timing, and the bridge forward to Week 3 personnel economics.
