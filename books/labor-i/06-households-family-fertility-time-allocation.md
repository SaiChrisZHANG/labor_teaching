---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Households, Family, Fertility, and Time Allocation

## Learning Objectives

By the end of Week 6, students should be able to:

1. distinguish individual labor-supply problems from household labor-allocation problems;
2. write a compact time-allocation object that includes market work, home production or care, and leisure;
3. explain why childcare, schooling, and household-service prices shift labor supply through household production rather than only through wage changes;
4. distinguish unitary, collective, and bargaining interpretations of household choice;
5. connect childbirth, fertility, and caregiving to dynamic labor-market shocks in hours, participation, occupation, and earnings;
6. interpret IVF-based fertility designs and first-birth event studies as different empirical objects;
7. map family policy into the margin it moves inside the household allocation problem;
8. explain why Week 7 amenities and Week 8 inequality cannot be interpreted cleanly without household structure.

## Opening Orientation

The economic question for the week is direct: if Week 5 treated wages as market opportunities, how do households transform those opportunities into actual hours, earnings, and career paths once partners, children, and care demands enter the picture [@becker1965; @chiappori1992; @cortesPan2023]?

:::{admonition} Core materials
:class: tip
- household production and the shadow value of care time
- unitary versus collective models and what pooling restrictions imply
- childbirth and fertility as dynamic labor-market shocks
- IVF-based fertility designs versus first-birth event studies
- policy incidence through childcare, schooling, leave, and outsourcing
:::

## Bridge

Weeks 2 and 3 largely treated labor supply as an individual choice problem, and Weeks 4 and 5 connected skill accumulation to wage offers. Week 6 changes the unit of analysis. Observed person-level hours and earnings are often joint outcomes of household production, bargaining, fertility timing, and care constraints rather than pure individual responses to a wage [@becker1965; @gronau1977]. The central labor-market fact is therefore not just that two workers can face different wages. It is that two workers with similar wage opportunities can make very different labor-market choices because their household states differ.

That shift matters for three reasons. First, children and care needs raise the shadow value of nonmarket time. Second, household production makes the labor-supply response depend on the availability and price of substitutes such as childcare, schooling, or household services. Third, childbirth creates dynamic shocks to earnings paths, promotion timing, occupation choice, and firm attachment, which means the relevant outcome is often a full post-birth trajectory rather than a one-period hours response [@gelbach2002; @klevenLandaisSogaard2019].

The week is therefore a hinge in the course. Week 5 asked how markets price skill. Week 6 asks how families convert priced opportunities into realized labor outcomes. Week 7 will add job amenities and compensating differentials, which further broadens the utility object. Week 8 will then ask how inequality evolves once wages, families, and career interruptions all interact.

### A compact time-allocation benchmark

The shortest route into the week is a time constraint:

```{math}
:label: eq-week6-time
T_i = h_i + n_i + \ell_i,
```

where {math}`h_i` denotes market work, {math}`n_i` denotes home production or care, and {math}`\ell_i` denotes leisure. Equation {eq}`eq-week6-time` is elementary, but it already tells students why children matter. A childbirth shock does not simply change preferences. It changes the feasible and optimal allocation of time because the demand for household production rises and the value of market substitutes becomes more salient [@becker1965; @gronau1977].

```{figure} assets/figures/06-household-time-allocation-schematic.png
:name: fig-week6-time
Stylized household time allocation before and after childbirth. The point is not that every family fits one schedule. The point is that childbirth reallocates time across market work, care, and leisure, so labor supply becomes a household-allocation problem rather than only an individual wage response.
```

Figure {numref}`fig-week6-time` is the right opening picture because it makes clear that family formation changes the margin structure itself. The student should immediately see why household production belongs inside a labor field course rather than at its margins.


:::{admonition} Optional Extension Block
:class: note
- relative-income constraints and household norms in the spirit of [@bertrandKamenicaPan2015]
- long-run family-policy experimentation and gender inequality in the spirit of [@klevenLandaisPoschSteinhauerZweimueller2024]
:::

## Field Core

### Household production and the allocation of time

The natural next step is to embed Equation {eq}`eq-week6-time` in a household resource problem. A compact formulation is

```{math}
:label: eq-week6-homeprod
\max U(c_f, c_m, \ell_f, \ell_m, q)
\quad \text{s.t.} \quad
c_f + c_m + p_x x = w_f h_f + w_m h_m + y,
\quad
q = F(n_f, n_m, x).
```

Equation {eq}`eq-week6-homeprod` says that family labor supply is linked to the production of a household good {math}`q`, where care time {math}`n_f` and {math}`n_m` can be complemented or substituted by market inputs {math}`x`. This is exactly why childcare and household-service prices matter. A fall in {math}`p_x` can raise market labor supply even when wages do not change, because cheaper substitutes reduce the opportunity cost of market work for the spouse whose time is most intensely used in home production [@gronau1977; @cortesTessada2011].

The economic intuition is labor-specific. Week 2 taught students to ask whether a wage increase moves people along an intensive or extensive margin. Week 6 adds a prior question: how much of the relevant time constraint is governed by home production? That is why the same wage opportunity can generate very different observed hours in households with preschool children, school-age children, or access to reliable market substitutes.

```{figure} assets/figures/06-childcare-substitution-schematic.png
:name: fig-week6-substitution
Conceptual labor-supply response to a lower price of childcare or household-service substitutes. The figure emphasizes that family labor supply can shift because the home-production technology changes, not because the market wage changes.
```

Figure {numref}`fig-week6-substitution` makes the comparative static visual. Cheap childcare, public schooling, or outsourcing opportunities alter family labor supply by relaxing the household production constraint. Gelbach is the clean school-entry version of that logic, while Cort{\'e}s and Tessada provide a labor-market substitute version through cheaper household services [@gelbach2002; @cortesTessada2011].

### Unitary, collective, and bargaining models

The unitary benchmark treats the household as if it maximizes one stable objective with pooled resources. That benchmark is useful because it yields sharp comparative statics and income-pooling restrictions. But it is also easy to overuse. Once distribution factors or recipient-specific transfers matter, the pure pooling implication becomes too restrictive as a positive description of family behavior [@lundbergPollakWales1997].

The collective alternative keeps Pareto efficiency but allows distinct preferences and a sharing rule. A compact representation is

```{math}
:label: eq-week6-collective
\max \lambda U_f(\cdot) + (1-\lambda) U_m(\cdot),
\qquad 0 \leq \lambda \leq 1.
```

Equation {eq}`eq-week6-collective` is deliberately spare. Its pedagogical use is that shifts in {math}`\lambda` can change labor supply, expenditure patterns, and care allocation even when total household income is unchanged. Distribution factors matter because the same cash amount can have different labor-market incidence depending on who receives it and how bargaining weights move [@chiappori1992; @lundbergPollakWales1997].

That distinction is not merely philosophical. Unitary, collective, fertility-IV, and child-event-study approaches are matched to different empirical objects. The right question in class is never only whether a model is elegant. It is what it lets us test and what kind of policy incidence it can rationalize.

```{include} assets/tables/06-household-model-map.md
```

Table {numref}`tbl:week6-household-model-map` is the chapter's organizing map. The table works because it keeps the models and designs linked to identifiable labor-market uses: pooling tests, bargaining interpretation, care-price comparative statics, causal fertility margins, and dynamic post-birth paths.

### Fertility, marriage, and caregiving as labor-market shocks

Marriage, fertility, and caregiving should be read as shocks to the household allocation problem, not as demographic background. A first birth can change the timing of labor supply, the value of flexible jobs, the return to career investments with long horizons, and the desirability of firms with more stable schedules. A spouse's wage or job loss can matter both through standard income effects and through changes in specialization or bargaining positions. The key point is that the relevant response margin is often dynamic and multidimensional [@blundellPistaferriSaportaEksten2016; @cortesPan2023].

This is why the literature uses different empirical families. Fertility-IV designs ask for the effect of an additional child induced by plausibly exogenous fertility variation. Childcare and school-entry designs ask how care institutions move participation or hours. Event studies around first birth ask how the entire post-birth path diverges. These are related, but they are not interchangeable.

Lundborg, Plug, and Rasmussen are especially useful in a labor course because IVF success isolates a fertility margin without collapsing straight into descriptive parenthood gaps [@lundborgPlugRasmussen2017]. The design is labor-relevant precisely because the outcome is not merely whether a birth occurs. The outcome is how fertility shifts employment, earnings, and career continuity. That makes the paper a strong bridge between household theory and modern causal design.

### Child penalties and dynamic earnings paths

The empirical center of the week is the child-penalty event-study object:

```{math}
:label: eq-week6-eventstudy
Y_{it} = \sum_{k \neq -1} \beta_k \mathbf{1}\{t - b_i = k\} + \alpha_i + \gamma_t + \varepsilon_{it},
```

where {math}`b_i` denotes the timing of first birth and the coefficients {math}`\beta_k` trace the outcome path relative to the pre-birth normalization period. Equation {eq}`eq-week6-eventstudy` clarifies that the parameter of interest is not only a one-time level effect. It is the full dynamic profile after birth.

Kleven, Landais, and Sogaard show why this perspective changed the field. The earnings divergence after children is persistent and is tied not only to contemporaneous hours but also to career progression, occupation, and firm attachment [@klevenLandaisSogaard2019]. Cort{\'e}s and Pan then place that logic inside the broader question of why children explain so much of the remaining gender gap in modern labor markets [@cortesPan2023].

```{figure} assets/figures/06-child-penalty-event-study.png
:name: fig-week6-child-penalty
Stylized child-penalty event study in earnings. The purpose is to show dynamic divergence after first birth rather than a one-period motherhood effect. Persistent post-birth gaps are labor-market objects because they reflect hours, occupation, sector, firm continuity, and wage growth all at once.
```

Figure {numref}`fig-week6-child-penalty` should be read alongside Equation {eq}`eq-week6-eventstudy`. The event-study line is not itself a structural model, but it is exactly the right descriptive discipline for Week 6 because it shows persistence, timing, and asymmetry between mothers and fathers in one object.

### Family policy, childcare, and market substitutes

The cleanest way to teach policy in Week 6 is by the margin it moves. Childcare access mostly targets participation and re-entry timing. Public school entry can free maternal time at a well-defined threshold. Parental leave often changes short-run attachment and can alter long-run earnings through career continuity. Household-service outsourcing shifts time allocation by changing the home-production technology itself. Transfers to one spouse test whether resource pooling is descriptive or whether bargaining weights matter [@gelbach2002; @cortesTessada2011; @lundbergPollakWales1997].

```{include} assets/tables/06-policy-margin-map.md
```

Table {numref}`tbl:week6-policy-margin-map` disciplines those discussions. The point is not that one policy dominates everywhere. The point is that the same wage schedule can generate very different labor outcomes depending on which household margin is relaxed and on whether the response comes through participation, hours, occupation choice, or career continuity.

### Why Week 6 is the bridge to amenities and inequality

Week 7 asks why jobs with flexibility, schedule stability, remote options, or safety differences may pay differently. Week 6 makes clear why those amenities are not peripheral. Once care constraints bind, flexibility itself becomes a household input. Week 8 will ask how inequality evolves. Week 6 implies that observed earnings inequality partly reflects household structure, fertility timing, and access to care substitutes rather than only worker skill or firm pay policies. A labor field course that skipped this week would misread both amenities and inequality.

## Research Lab

The frontier issue is no longer whether family structure matters. It is which empirical object is appropriate for the family-labor question at hand. IVF-based fertility designs recover local causal fertility margins. First-birth event studies recover dynamic post-birth paths. Childcare and schooling reforms recover institutional relaxations of the household production constraint. Collective models recover structure on how resources are shared or bargained over [@lundborgPlugRasmussen2017; @klevenLandaisSogaard2019; @blundellPistaferriSaportaEksten2016].

That plurality is a feature, not a weakness. Labor economists need different designs because childbirth affects multiple margins at once: participation, hours, occupation, commuting tolerance, job flexibility, promotion timing, and future wage growth. The research challenge is therefore to keep causal language matched to the design and to avoid turning every family-labor paper into a generic statement about "women versus men."

The bounded Week 6 lab reflects that discipline. Students first reproduce a synthetic IVF-style fertility design in the spirit of [@lundborgPlugRasmussen2017], diagnose the resulting local birth effect on employment, hours, and earnings, and then transfer the workflow to a synthetic child-penalty event study in the spirit of [@klevenLandaisSogaard2019]. An optional extension note asks how school entry, childcare, outsourcing, or long-run family policy could move the same family-allocation problem using [@gelbach2002], [@cortesTessada2011], or [@klevenLandaisPoschSteinhauerZweimueller2024].

Open research questions should remain visible:

1. How portable are IVF-based fertility effects across institutional settings and across different fertility margins?
2. How much of the child penalty operates through hours, occupations, sectors, firms, or employer responses to flexibility demands?
3. Which family policies change short-run attachment and which change long-run earnings trajectories?
4. When do bargaining and norms matter separately from household technology and market substitutes?
5. How should inequality decompositions change once family structure is treated as endogenous labor-market allocation rather than background demographics?

## Methods Box

Week 6 adds one discipline to the worker-side models from Weeks 2--5: always state whether the relevant object is individual choice, household production, bargaining incidence, or a dynamic post-birth path.

1. Start with Equation {eq}`eq-week6-time` and ask where time can be reallocated.
2. Use Equation {eq}`eq-week6-homeprod` to identify whether market substitutes or care prices change the relevant shadow value.
3. Use Equation {eq}`eq-week6-collective` to ask whether the recipient of income or policy transfers should matter.
4. Use Equation {eq}`eq-week6-eventstudy` to separate dynamic child penalties from one-period fertility effects.
5. Before interpreting an observed earnings gap as a pure wage-market outcome, ask what portion is generated inside the family allocation problem.

## Reading Ladder And References

### Bridge

- Becker on time allocation as the primitive behind labor supply and home production [@becker1965]
- Gronau on leisure, work, and household production [@gronau1977]
- Lundberg, Pollak, and Wales on why income pooling is an empirical question rather than an axiom [@lundbergPollakWales1997]

### Field Core

- Chiappori on collective labor supply and welfare [@chiappori1992]
- Blundell, Pistaferri, and Saporta-Eksten on family labor supply and consumption inequality [@blundellPistaferriSaportaEksten2016]
- Lundborg, Plug, and Rasmussen on IVF-based fertility effects on careers [@lundborgPlugRasmussen2017]
- Kleven, Landais, and Sogaard on children and dynamic gender inequality [@klevenLandaisSogaard2019]
- Cort{\'e}s and Pan on children and the remaining gender gaps in labor markets [@cortesPan2023]

### Research Lab

- Gelbach on public schooling and maternal labor supply [@gelbach2002]
- Cort{\'e}s and Tessada on household-service substitutes and high-skill women's labor supply [@cortesTessada2011]
- Bertrand, Kamenica, and Pan on relative income and household specialization [@bertrandKamenicaPan2015]
- Kleven, Landais, Posch, Steinhauer, and Zweim{\"u}ller on long-run family-policy experimentation [@klevenLandaisPoschSteinhauerZweimueller2024]

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week6-time` to explain why childcare expansions can shift labor supply even when wages are unchanged.
2. In Equation {eq}`eq-week6-homeprod`, which comparative static captures the effect of a fall in the price of market substitutes {math}`p_x`, and which spouse is most likely to adjust on the market-work margin?
3. Why does Equation {eq}`eq-week6-collective` imply that transfer incidence may depend on the recipient even when total household income is fixed?
4. Compare a fertility-IV design with the child-penalty event study in Equation {eq}`eq-week6-eventstudy`. Which one is better suited to causal fertility effects, and which one is better suited to dynamic inequality accounting?
5. Use Table {numref}`tbl:week6-policy-margin-map` to explain why a childcare policy and a parental-leave policy can move different labor margins even if both are “family policy.”
6. Figure {numref}`fig-week6-child-penalty` shows a persistent post-birth earnings gap. Give two mechanisms inside the household allocation problem and two mechanisms inside the labor market that could generate that persistence.
7. Why is Week 6 a necessary bridge from wage determination in Week 5 to job amenities in Week 7 and inequality in Week 8?

## Reproducibility And Code Lab Note

The Week 6 lab is organized around a bounded `Reproduce -> Diagnose -> Transfer` path that runs fully locally. Students reproduce one synthetic IVF-style fertility design in the spirit of [@lundborgPlugRasmussen2017], diagnose what the resulting first stage and Wald object do and do not identify about family labor supply, and then transfer the workflow to a synthetic first-birth event study in the spirit of [@klevenLandaisSogaard2019]. An optional extension asks how school entry, household-service outsourcing, or broad family-policy reform changes the same time-allocation problem. The bounded workflow is documented in [labs/06-households-family-fertility-time-allocation/lab.md](labs/06-households-family-fertility-time-allocation/lab.md).

## Slide Companion Note

The Week 6 deck should isolate the move from individual labor supply to household allocation, the time-allocation and household-production objects, unitary versus collective models, fertility and childbirth as labor-market shocks, the child-penalty event-study figure, the two Week 6 tables, and the bridges to Week 7 amenities and Week 8 inequality rather than reproducing the chapter. The canonical source is [slides/week6/06-households-family-fertility-time-allocation.tex](slides/week6/06-households-family-fertility-time-allocation.tex).

## Bridge Forward

Use this closing bridge to carry the module's labor object, mechanism, and evidence into the next course step or research-design exercise.
