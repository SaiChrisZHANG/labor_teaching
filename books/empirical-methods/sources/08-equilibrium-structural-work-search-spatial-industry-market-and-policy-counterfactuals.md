# Equilibrium Structural Work: Search, Spatial, Industry/Market, and Policy Counterfactuals

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when an applied question requires equilibrium structure rather than only individual decision modeling;
2. distinguish search, spatial, and industry/market equilibrium objects and interpret their policy relevance;
3. connect equilibrium primitives to observed data, counterfactuals, and welfare objects;
4. articulate the validation burden and computational burden of equilibrium structural work;
5. map a research question into a **Reproduce → Diagnose → Transfer** workflow.

## Opening Orientation

Block 2 closes by asking what happens when one person's or firm's decision changes the environment faced by others. Once vacancies, prices, wages, rents, market shares, commuting flows, or firm entry respond endogenously, a partial-equilibrium structural model is often no longer enough. The lecture therefore moves from individual decision structure to **equilibrium structure**.

The key idea is not that equilibrium structure is always better. It is that some questions—search externalities, housing incidence, market power, equilibrium wage-setting, or policy counterfactuals with reallocation—cannot be answered credibly unless the researcher models the endogenous response of the surrounding system. The price of that richer answer is a heavier burden of assumptions, identification, fit, and computation.

:::{admonition} Core points
:class: important
- Equilibrium structural work is useful when a policy or shock changes the environment faced by many agents at once.
- Search, spatial, and industry equilibrium models all map primitives into endogenous prices, allocations, and welfare.
- The empirical gain is richer incidence and welfare analysis; the empirical risk is stronger assumptions and weaker transparency.
- A good equilibrium paper makes clear which equilibrium margin matters, which moments identify it, and why the extra structure is necessary.
:::

## Bridge

Lectures 6 and 7 asked when a static or dynamic behavioral model is needed and how such a model is estimated in practice. This lecture adds a new layer: **interaction through markets**. The same principles remain—identify primitives, connect them to moments, validate fit, and interpret counterfactuals carefully—but now the counterfactual changes wages, prices, rents, vacancies, firm entry, or job allocation endogenously.

## Field Core

### When Do We Need Equilibrium Structure?

The most useful starting question is not “can I write down an equilibrium model?” but “what is wrong with a partial-equilibrium comparison?” Equilibrium structure becomes especially valuable when:

1. the treatment changes prices or wages for many agents;
2. the intervention changes who matches with whom;
3. the intervention changes entry, exit, or location choices;
4. welfare depends on incidence through rents, markups, or congestion;
5. the policy counterfactual lies outside the observed support of historical variation.

A concise decision rule is:

```{math}
:label: eq:eq-need
\text{Need equilibrium structure if } \frac{\partial E_i}{\partial a_j} \neq 0 \text{ for many } i \neq j,
```

where \(a_j\) is the action of another worker, firm, or locality and \(E_i\) is the environment faced by agent \(i\). If actions or policies change the environment faced by many others, individual optimization alone is incomplete.

### Search and Matching Equilibrium

Search equilibrium models are useful when workers and firms meet through a market process and vacancies are endogenous. Let \(u\) denote unemployment, \(v\) vacancies, and \(m(u,v)\) a matching function. Market tightness is:

```{math}
:label: eq:tightness
\theta = \frac{v}{u}.
```

Then the job-finding and vacancy-filling rates are typically written as:

```{math}
:label: eq:meeting-rates
f(\theta) = \frac{m(u,v)}{u}, \qquad q(\theta) = \frac{m(u,v)}{v}.
```

A free-entry condition closes the equilibrium on the firm side:

```{math}
:label: eq:free-entry
\kappa = q(\theta) J,
```

where \(\kappa\) is the vacancy posting cost and \(J\) is the value of a filled job. With bargaining or wage posting, wages and surplus division become endogenous. This is the structural route when the researcher wants counterfactuals about unemployment, vacancy creation, wage incidence, or search frictions under new policies.

Empirically, the attraction of search equilibrium models is that they connect vacancy data, transitions, and wage-setting to policy or shock counterfactuals. The risk is that the matching technology, bargaining structure, and separation rules do a great deal of work.

### Spatial Equilibrium

Spatial equilibrium models become useful when workers choose locations, commute, migrate, or sort across places, and when rents or local prices adjust. A tractable spatial object starts with indirect utility in location \(j\):

```{math}
:label: eq:indirect-utility-location
V_j = w_j - r_j - c_j + a_j,
```

where \(w_j\) is local labor-market opportunity, \(r_j\) housing cost, \(c_j\) commuting or migration cost, and \(a_j\) local amenities. In richer models these are embedded in discrete choice, commuting flows, or spatial-equilibrium systems, but the empirical point is the same: wages alone are not welfare.

When mobility is sufficiently elastic, equilibrium requires utility equalization or migration/commuting shares consistent with these utilities. Market clearing in housing and labor then pins down rents, wages, commuting, and location decisions. A stylized spatial-equilibrium counterfactual can be written as:

```{math}
:label: eq:spatial-equilibrium
(w_j^\ast, r_j^\ast, N_j^\ast) = \mathcal{G}(\text{productivity}_j,\text{amenities}_j,\text{housing supply}_j,\text{mobility frictions}),
```

where \(N_j^\ast\) is equilibrium population or employment. This is the right framework when the researcher cares about location-specific shocks whose incidence depends on mobility and housing.

### Industry and Market Equilibrium

Industry or market equilibrium models matter when firms set prices, quantities, wages, or product mix strategically and labor outcomes depend on those choices. A reduced but useful formulation begins with demand:

```{math}
:label: eq:demand
q_j = D_j(p, x, \xi),
```

and a firm first-order condition such as:

```{math}
:label: eq:pricing-foc
p_j - mc_j = \mu_j(\theta),
```

where \(mc_j\) is marginal cost and \(\mu_j(\theta)\) is a markup object depending on demand elasticities, ownership, and competitive structure. If labor enters production or cost, then changes in technology affect employment and wages through both productivity and firm conduct.

These models are especially useful when the substantive claim involves rent capture, market power, platform pricing, or pass-through. The challenge is that demand, supply, and conduct assumptions all matter for labor incidence.

### Policy Counterfactuals and Welfare

The core appeal of equilibrium structural work is not just better fit; it is the ability to conduct policy counterfactuals when incidence is endogenous. A generic policy counterfactual can be written as a fixed-point problem:

```{math}
:label: eq:equilibrium-fixed-point
x^\ast(\tau) = \Phi\big(x^\ast(\tau), \tau; \theta\big),
```

where \(\tau\) is policy, \(\theta\) are primitives, and \(x^\ast(\tau)\) collects equilibrium objects such as wages, vacancies, rents, prices, entry, or matching rates.

A welfare object then depends on the equilibrium allocation:

```{math}
:label: eq:welfare
W(\tau) = \sum_i \omega_i U_i\big(x^\ast(\tau)\big) + \sum_f \pi_f\big(x^\ast(\tau)\big),
```

with distributional weights \(\omega_i\) and firm profits \(\pi_f\). The empirical question is whether the model identifies the relevant welfare margin and whether readers should trust the counterfactual at all.

### Computation: What Changes Once Equilibrium Enters?

Equilibrium structure also changes the computational problem. Researchers may use nested fixed point methods, MPEC, calibration-estimation hybrids, or simulation-based solvers. The gains are richer counterfactuals; the costs are greater opacity and sensitivity.

A useful practical checklist is:
- What equilibrium variables are solved endogenously?
- How are equilibrium moments mapped back to data?
- Which parameters are disciplined by direct evidence and which by model closure?
- Would a simpler reduced-form or partial-equilibrium design answer most of the substantive question?

### Gravity-Style Structural Work

Gravity-style structural models can fit here when the object of interest is equilibrium flows across locations or markets—trade, migration, commuting, or worker allocation. The reason they belong here is that they map bilateral frictions into equilibrium allocation and incidence. But they should be treated as a **subfamily** of spatial or flow equilibrium work, not as the core of the lecture.

A simple gravity-style object takes the form:

```{math}
:label: eq:gravity
M_{ij} = A_i B_j \tau_{ij}^{-\sigma},
```

where \(M_{ij}\) is a bilateral flow, \(\tau_{ij}\) a friction, and \(A_i, B_j\) origin and destination terms. In labor applications, the interesting question is what these flows represent—workers, commuters, vacancies, applications, or migration—and whether the equilibrium interpretation is credible. This is worth mentioning, but not pushing too hard unless the empirical question is genuinely flow-based.

### Research Architecture and Frontier Questions

A useful research sequence for equilibrium work is:

1. identify the margin that becomes endogenous;
2. decide whether equilibrium structure is necessary;
3. specify the primitive variation and the moments that discipline it;
4. decide what counterfactual or welfare object cannot be learned without equilibrium;
5. evaluate whether the validation burden is plausible.

The frontier is especially active where equilibrium response is visible but partially observed: firm-side AI adoption and labor demand, commuting and spatial labor incidence, market power and wage-setting, and policy reforms that reallocate workers, firms, or locations simultaneously.

## Research Lab

### Primary Anchor

A good primary anchor is **Hsieh and Moretti**. It is an excellent equilibrium structural paper because the core substantive claim is precisely about incidence and misallocation that cannot be learned from reduced-form local treatment effects alone.

### Challenge / Extension Anchor

A useful contrast paper is **Berry, Levinsohn, and Pakes** or a close descendant in market equilibrium. This shows students what changes when equilibrium structure is rooted in firm conduct and product demand rather than in search or space.

### Reproduce

Reproduce one core object from the anchor paper:
- a key equilibrium moment,
- a policy counterfactual,
- or a simple decomposition of incidence.

### Diagnose

Diagnose:
- which primitives are really identified by the data,
- which assumptions are closure assumptions,
- which equilibrium objects matter most for the main result,
- how validation is carried out,
- and where a simpler design would fail.

### Transfer

Transfer the logic to a different equilibrium environment:
- from spatial misallocation to commuting response,
- from search equilibrium to vacancy incidence,
- from BLP-style market structure to wage-setting or platform work.

The point is not to fit a giant model from scratch, but to teach students how to decide whether equilibrium structure is necessary and what evidence is required to make it credible.

## Methods Box

A compact empirical checklist for equilibrium structural work:

- **Search equilibrium** is best when vacancy creation, matching, and wage-setting all respond.
- **Spatial equilibrium** is best when workers, rents, and jobs adjust across locations.
- **Industry/market equilibrium** is best when prices, markups, and firm conduct shape labor outcomes.
- **Gravity-style models** are best when the empirical object is bilateral flows and the equilibrium incidence travels through trade, migration, or commuting.
- The strongest papers are explicit about:
  - what is observed,
  - what is latent,
  - which moments identify which primitives,
  - what counterfactual is gained,
  - and what validation burden remains.

## Reading Ladder And References

### Core theory and methods
- Mortensen, Dale T., and Christopher A. Pissarides. 1994. “Job Creation and Job Destruction in the Theory of Unemployment.” *Review of Economic Studies*.
- Berry, Steven, James Levinsohn, and Ariel Pakes. 1995. “Automobile Prices in Market Equilibrium.” *Econometrica*.
- Nevo, Aviv. 2001. “Measuring Market Power in the Ready-to-Eat Cereal Industry.” *Econometrica*.
- Diamond, Rebecca. 2016. “The Determinants and Welfare Implications of US Workers’ Diverging Location Choices by Skill.” *American Economic Review*.
- Hsieh, Chang-Tai, and Enrico Moretti. 2019. “Housing Constraints and Spatial Misallocation.” *American Economic Journal: Macroeconomics*.

### Optional extension
- Monte, Ferdinando, Stephen Redding, and Esteban Rossi-Hansberg. 2018. “Commuting, Migration, and Local Employment Elasticities.” *American Economic Review*.
- Artuç, Erhan, Shubham Chaudhuri, and John McLaren. 2010. “Trade Shocks and Labor Adjustment.” *American Economic Review*.
- Caliendo, Lorenzo, Maximiliano Dvorkin, and Fernando Parro. 2019. “Trade and Labor Market Dynamics.” *Econometrica*.

## Exercises And Discussion Prompts

1. Give one example where a partial-equilibrium treatment effect is probably enough and one where equilibrium structure is clearly necessary.
2. For search, spatial, and market equilibrium respectively, name the equilibrium object that is most substantively important.
3. What makes a spatial equilibrium counterfactual harder to trust than a reduced-form local treatment effect?
4. When does a gravity-style model belong in a labor-economics methods lecture?
5. How should a referee evaluate whether an equilibrium structural paper’s validation burden has been met?

## Reproducibility And Code Lab Note

The teaching lab for this lecture should be built as a bounded equilibrium demonstration:
- a reduced reproduction of one equilibrium object from the primary anchor,
- a diagnosis of which moments and assumptions drive the result,
- and a transfer to a nearby equilibrium setting.

If full replication materials are not available locally, a reduced synthetic path is acceptable as long as it is clearly labeled as pedagogical.

## Slide Companion Note

The slide deck should emphasize parallelism across equilibrium domains:
- search,
- spatial,
- and market equilibrium,
before moving to policy counterfactuals, welfare, and validation burdens.

## Bridge Forward

Block 2 closes here. The next blocks turn to flexible modern tools—machine learning, text/computation/LLMs, spatial methods, and network methods—but the structural lessons remain relevant: every tool is valuable only when the researcher knows what object is being identified, what assumptions are doing the work, and what counterfactual or welfare question is actually being answered.
