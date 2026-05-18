# Labor Supply, Care Work, Fertility, And Household Allocation

## Learning Objectives

By the end of Week 2, students should be able to:

1. distinguish individual labor supply from household allocation;
2. write a compact household production and time-allocation object;
3. explain why fertility and care work can change participation, hours, earnings, job quality, occupation, and firm choice;
4. separate descriptive child-penalty event studies from causal fertility designs;
5. distinguish bargaining shifts from price and income effects;
6. map childcare and care-policy evidence to the labor margin it identifies;
7. explain why domestic responsibility allocation partly reflects gender norms and traditions without turning Week 2 into the norms lecture.

## Opening Orientation

Week 2 asks how care responsibilities, fertility, and household allocation shape labor supply and earnings trajectories. Week 1 taught students to name the labor-market object before naming the mechanism. This week applies that discipline to the household. Domestic work is not a residual category outside labor economics. It is a time-use, production, bargaining, and lifecycle allocation problem that changes who works, how much they work, which jobs are feasible, and how careers evolve.

The key move is to place paid work inside a household and lifecycle setting. A first birth can move extensive-margin employment, intensive-margin hours, annual earnings, occupation, firm attachment, schedule choice, promotion timing, and job quality. A childcare policy can relax a time constraint, but it may also reallocate care within the household. A transfer can act like income, but its effect may depend on who controls it. These distinctions are why child penalties, causal fertility effects, childcare-policy estimates, and bargaining evidence are related but not interchangeable.

:::{admonition} Core points
:class: important

- Care work is an allocation problem, not a residual category outside labor economics.
- Fertility and childcare generate dynamic effects on participation, hours, earnings, occupation, firm choice, and job quality.
- Household models differ sharply in whether they treat resources and preferences as pooled or bargained.
- Child penalties describe post-birth labor-market paths; causal fertility designs estimate effects of fertility variation on a particular margin.
- Household specialization is partly shaped by norms and traditions about caregiving, motherhood, breadwinning, and domestic responsibility. Week 5 studies those norms directly.

:::

## Bridge

Week 1 separated labor-market objects from mechanisms. Week 2 changes the unit of analysis. A person-level earnings path may be produced by individual wages, household care needs, partner responses, bargaining power, childcare availability, social expectations, and firm-side job design. The same observed annual earnings penalty can therefore reflect care-time reallocation, labor-market reallocation, wage growth, job-quality tradeoffs, or some combination of all four.

The first distinction is individual labor supply versus household allocation. In a standard individual labor-supply problem, the worker chooses market hours given wages, nonlabor income, preferences, and constraints. In a household allocation problem, market hours, care time, consumption, leisure, and sometimes fertility are jointly allocated across people. The labor outcome for one worker may therefore depend on the partner's wage, the price of childcare, the household's control over resources, and the social meaning of who does care.

The second distinction is static versus dynamic effects. A care shock may reduce hours this month, but it can also alter experience accumulation, promotion timing, firm attachment, occupation, and the future wage path. This is why child-penalty event studies became central to the modern gender literature [@klevenLandaisPoschSchmidtSogaard2019; @cortesPan2023].

The third distinction is descriptive gaps versus mechanisms. A child penalty tells us when and how sharply labor outcomes diverge around birth. It does not by itself prove that biology, preferences, childcare prices, employer flexibility, bargaining, or norms caused the divergence. Week 2 trains students to keep those claims separate.

```{include} assets/tables/02-household-allocation-map.md
```

The table anchors the week's scope. Each object is labor economics because it changes employment, hours, earnings, occupations, firms, schedules, and welfare.

## Field Core

### Household Production And Time Allocation

A compact starting point is a time constraint:

```{math}
:label: eq-week2-time
T_i = h_i + a_i + \ell_i,
```

where {math}`h_i` is market work, {math}`a_i` is unpaid care or home production, and {math}`\ell_i` is leisure. Equation {eq}`eq-week2-time` is simple, but it already changes the interpretation of labor supply. If care demand rises after a birth, the worker does not merely move along a wage-hours curve. The household must reallocate time across market work, care work, and leisure.

A household production object makes the same point more explicitly:

```{math}
:label: eq-week2-home-production
\max U(c_f, c_m, \ell_f, \ell_m, q)
\quad \text{s.t.} \quad
c_f + c_m + p_x x = w_f h_f + w_m h_m + y,
\quad
q = F(a_f, a_m, x).
```

The household good {math}`q` can be produced with care time from each partner, {math}`a_f` and {math}`a_m`, and market inputs {math}`x`, such as childcare or paid services. This is the Becker-style insight that time is an input into production as well as a source of utility [@becker1965allocation]. It is also why childcare prices, school schedules, remote-work possibilities, and job flexibility can change labor supply without changing wages.

Specialization can arise when partners have different wages or different home-production productivity. But gender-neutral comparative advantage is often insufficient as an explanation. It can rationalize some specialization when wage offers differ, yet it does not explain why care responsibilities remain gendered when women have similar or higher earnings potential, why fathers' careers are often less disrupted, or why domestic responsibility responds slowly to policy changes. Those patterns force the analyst to consider bargaining, childcare markets, employer behavior, and norms.

### Fertility, Timing, And Dynamic Labor Supply

Fertility is a labor-market shock because it changes the household's demand for care time and the timing of market work. The effects can be immediate, as with employment exits or hours reductions, and dynamic, as with lost experience, slower wage growth, reduced promotion probability, changed occupation, or sorting to more flexible but lower-paying firms.

The central descriptive object is the child-penalty event study:

```{math}
:label: eq-week2-child-penalty
Y_{it}^{g}
=
\sum_{k \neq -1}\beta_k^{g}\mathbf{1}\{t - B_i = k\}
+ \alpha_i + \gamma_t + \varepsilon_{it},
```

where {math}`B_i` is the timing of first birth, {math}`g` indexes a group such as mothers or fathers, and {math}`Y_{it}` can be employment, hours, earnings, occupation, firm assignment, or job quality. The coefficients {math}`\beta_k^{g}` trace the event-time path relative to the omitted pre-birth period. The object is dynamic: timing and persistence are part of the result.

Kleven, Landais, Posch, Steinhauer, and Sogaard make this object canonical by showing large and persistent gender divergence after children in Denmark [@klevenLandaisPoschSchmidtSogaard2019]. Cortes and Pan then place children at the center of the remaining gender gaps in modern labor markets [@cortesPan2023]. The interpretation, however, must stay disciplined. A child-penalty path is not automatically a causal effect of fertility. It is a descriptive lifecycle pattern unless the design supplies a causal fertility shock or a credible policy counterfactual.

### Intrahousehold Bargaining And Control Over Resources

The unitary household model treats the household as if it maximizes one stable objective with pooled resources. That benchmark is useful, but it can be too restrictive. If the recipient of income, the ownership of assets, or the outside option of one spouse changes behavior while total household resources remain fixed, the pooled-income interpretation is incomplete.

A compact collective representation is:

```{math}
:label: eq-week2-collective
\max \lambda U_f(c_f,\ell_f,q) + (1-\lambda)U_m(c_m,\ell_m,q),
\qquad 0 \leq \lambda \leq 1.
```

The weight {math}`\lambda` summarizes control over resources, outside options, distribution factors, or bargaining power. In this setting, a policy can affect labor supply through at least three channels. It can change prices, such as childcare costs. It can change income, such as a transfer or tax credit. Or it can change bargaining weights, such as by shifting who controls resources. These are not the same mechanism.

Collective labor-supply models provide the formal language for that distinction [@chiappori1992]. Bargaining approaches explain why distribution within marriage can matter for work and care allocation [@lundbergPollak1996]. Dynamic household models connect those choices to lifecycle labor supply and savings [@mazzocco2014]. The labor-economics payoff is practical: when a reform changes employment, students must ask whether it relaxed a price constraint, raised income, shifted control, or changed the household's bargaining environment.

### Childcare, Policy, And Constraints

Childcare policy belongs in Week 2 because childcare is both a market input and a time constraint. Lower childcare prices, more reliable availability, longer opening hours, or safer care options can raise market work by reducing the shadow value of parental care time. But the response can appear on different margins: labor-force participation, hours, earnings, occupation, job continuity, schedule choice, commuting radius, or job quality.

Policy evidence therefore needs a margin map. A childcare intervention may identify a constraint-relaxation effect rather than a general fertility effect. It may move single parents differently from partnered parents because there is less scope for within-household reallocation. It may shift mothers' market hours without changing fathers' care time, or it may change specialization within the household. Recent childcare evidence is especially useful because it connects care availability to both labor supply and business or job decisions [@bjorvatnFerrisJayachandran2025].

The policy discussion also helps separate care-time reallocation from labor-market reallocation. Care-time reallocation asks who performs unpaid care and how much time moves from parental care to market substitutes. Labor-market reallocation asks whether workers enter employment, increase hours, change firms, switch occupations, preserve promotion paths, or choose different job amenities. A serious empirical paper should say which margin moved.

### Norms Bridge To Week 5

Household specialization is not only prices and technology. Domestic responsibility allocation partly stems from gender norms and traditions about who should provide care, what counts as good parenting, whether mothers should prioritize flexibility, and how households respond when women out-earn men. Evidence on relative earnings and gender identity shows that household behavior can change around status and role expectations [@bertrandKamenicaPan2015]. Evidence on misperceived norms shows how beliefs about acceptable work can constrain labor supply even when private attitudes are more supportive [@bursztynGonzalezYanagizawaDrott2020].

This is only a bridge. Week 2 uses norms to explain why the residual allocation of care may not respond mechanically to wages, childcare prices, or fertility shocks. Week 5 studies norms, beliefs, identity, and institutions as independent labor-market mechanisms.

```{include} assets/tables/02-norms-bridge-map.md
```

### Empirical Designs And What They Identify

The same family-labor question can require different empirical designs. A birth event study describes the dynamic path of outcomes around first birth. An IVF or infertility design uses fertility variation to estimate a local causal fertility effect [@lundborgPlugRasmussen2017; @agueroMarks2008]. A timing design asks how delayed childbearing changes later outcomes [@buckles2008]. A childcare reform studies a policy constraint. A bargaining design studies control over resources or distribution factors.

```{include} assets/tables/02-identification-and-child-penalty-map.md
```

The table is the guardrail. Child penalties and fertility effects are not synonyms. Descriptive event studies and causal fertility designs do not answer the same question. Bargaining shifts should not be described as price effects unless the evidence actually moves prices. Care-time reallocation should not be described as labor-market reallocation unless employment, hours, earnings, occupation, firm choice, or job quality are observed.

## Research Lab

The research frontier is not whether children, care, and household allocation matter. It is which empirical object maps to which mechanism and counterfactual. A student reading this literature should be able to answer five questions before interpreting a coefficient:

1. Is the object a child penalty, a causal fertility effect, a childcare-policy effect, a bargaining shift, or a norms-related response?
2. Is the outcome extensive-margin employment, intensive-margin hours, earnings, wages, occupation, firm attachment, care time, or job quality?
3. Is the design descriptive, causal, structural, or a hybrid?
4. Is the mechanism price, income, bargaining, care constraint, employer response, or norms?
5. What would need to be measured to distinguish care-time reallocation from labor-market reallocation?

```{include} assets/tables/02-data-and-methods-map.md
```

The Week 2 lab is organized as **Reproduce -> Diagnose -> Transfer**. Students first reproduce a bounded synthetic child-penalty event-time exercise inspired by Kleven, Landais, Posch, Steinhauer, and Sogaard [@klevenLandaisPoschSchmidtSogaard2019]. They diagnose what the event-study path shows and what it does not identify. They then transfer the same logic to a synthetic IVF-style fertility design inspired by Lundborg, Plug, and Rasmussen [@lundborgPlugRasmussen2017]. The optional policy prompt asks how childcare availability could change the same allocation problem using Bjorvatn, Ferris, and Jayachandran as the frontier anchor [@bjorvatnFerrisJayachandran2025].

Open research questions remain visible:

1. How much of the child penalty comes through hours, employment, occupation, firm assignment, promotion, or job quality?
2. Which childcare policies relax a true care constraint, and which mostly reallocate care within households?
3. When do bargaining weights matter separately from income and prices?
4. How can researchers distinguish norms from unobserved constraints when both predict persistent specialization?
5. Which results travel across countries with different care regimes, tax systems, firm structures, and family norms?

## Methods Box

:::{admonition} Methods Box: Match The Claim To The Design
:class: note

**Child penalties versus fertility effects.** Child penalties trace dynamic labor-market paths around birth. Fertility effects require variation that changes fertility and can support a causal counterfactual.

**Descriptive event studies versus causal fertility designs.** Event studies are powerful for timing and persistence. IVF, infertility, twin, sex-composition, or other fertility designs target causal fertility margins, often locally.

**Bargaining shifts versus price and income effects.** A childcare subsidy changes the price of care. A cash transfer changes resources. A recipient-specific transfer or outside-option shock may change bargaining weights. These are different economic objects.

**Care-time reallocation versus labor-market reallocation.** Time-use data reveal care and housework changes. Payroll or survey labor data reveal participation, hours, earnings, occupations, firms, and job quality. One does not mechanically imply the other.

**Margin discipline.** Always state whether the outcome is extensive-margin employment, intensive-margin hours, earnings, wages, occupation, firm attachment, promotion, or job quality.

:::

## Reading Ladder And References

**Broad framing and review.** Start with Cortes and Pan for the central claim that children explain a large share of remaining gender gaps in labor markets [@cortesPan2023].

**Canonical child-penalty evidence.** Use Kleven, Landais, Posch, Steinhauer, and Sogaard to understand event-time child penalties and dynamic post-birth divergence [@klevenLandaisPoschSchmidtSogaard2019].

**Household allocation and bargaining.** Use Becker for time allocation, Chiappori for collective labor supply, Lundberg and Pollak for bargaining and distribution, and Mazzocco for household dynamics [@becker1965allocation; @chiappori1992; @lundbergPollak1996; @mazzocco2014].

**Causal fertility evidence.** Use Lundborg, Plug, and Rasmussen for IVF-based fertility effects, Aguero and Marks for infertility shocks, and Buckles for timing of childbearing [@lundborgPlugRasmussen2017; @agueroMarks2008; @buckles2008].

**Childcare and recent frontier work.** Use Bjorvatn, Ferris, and Jayachandran to connect childcare, labor supply, and business development [@bjorvatnFerrisJayachandran2025].

**Norms bridge to Week 5.** Use Bertrand, Kamenica, and Pan on relative income and household behavior, and Bursztyn, Gonzalez, and Yanagizawa-Drott on misperceived norms and women working outside the home [@bertrandKamenicaPan2015; @bursztynGonzalezYanagizawaDrott2020].

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week2-time` to explain why a first birth can reduce earnings even if hourly wages are unchanged.
2. In Equation {eq}`eq-week2-home-production`, describe the effect of a fall in {math}`p_x`. Which labor margins might move first?
3. In Equation {eq}`eq-week2-collective`, what kind of empirical variation would help distinguish a bargaining shift from a pure household-income effect?
4. Compare Equation {eq}`eq-week2-child-penalty` with an IVF-based fertility design. Which design is better for persistence? Which is better for a causal fertility estimand?
5. Use the identification table to classify a childcare reform, a first-birth event study, and a recipient-specific transfer. State the outcome, method, estimand, and main limitation for each.
6. Give one reason Week 2 must mention norms and one reason the full norms treatment belongs in Week 5.

## Reproducibility And Code Lab Note

The Week 2 code lab lives at `labs/02-labor-supply-care-work-fertility-and-household-allocation/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates local synthetic data, reproduces child-penalty event-time summaries, and transfers the design logic to an IVF-style fertility exercise. It runs without confidential microdata.

## Slide Companion Note

The Week 2 slide deck lives at `slides/week2/02-labor-supply-care-work-fertility-and-household-allocation.tex`. The deck is a conceptual map rather than a duplicate of the chapter. It defines the central question, bridges from Week 1, introduces household production, separates child penalties from fertility effects, maps bargaining and childcare mechanisms, and closes with a short bridge to Week 5 on norms.

## Bridge Forward

Week 3 moves from household allocation to education, skills, aspirations, and occupational sorting. Week 2 matters for that transition because care responsibilities and fertility timing can alter early investments, field choices, job search, and the value of flexible career paths. Week 5 later returns to the norms hinted at here: domestic responsibility allocation partly reflects gender norms and traditions, not only wages, childcare prices, or household technology.
