---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Unions, Collective Bargaining, and Worker Voice

## Learning Objectives

By the end of Week 8, students should be able to:

1. distinguish union membership, collective-bargaining coverage, union density, bargaining regime, and worker voice;
2. explain how collective bargaining changes wages, wage dispersion, amenities, job security, and workplace governance;
3. map organizing demand, certification, employer opposition, and bargaining law into observed union takeup and realized coverage;
4. separate direct effects on covered workers from spillovers and threat effects on uncovered workers;
5. interpret union evidence by naming the identifying variation, unit of observation, observed margin, and key unobserved object;
6. explain why disagreements in the literature often reflect different objects, settings, selection processes, and spillover concepts;
7. connect unions to Weeks 5--7 on bargaining, monopsony, and minimum wages and to Week 9 on labor regulation, enforcement, and insurance.

## Opening Orientation

The economic question for Week 8 is not whether unions are generically "good" or "bad." It is what collective bargaining changes in labor markets, how membership differs from coverage, how organizing differs from post-union outcomes, and how modern labor economics identifies direct effects, spillovers, and political feedbacks [@jagerNaiduSchoefer2024; @hirsch2008; @kaplanNaidu2025].

:::{admonition} Core materials
:class: tip
- membership, coverage, bargaining regime, and worker voice are distinct institutional objects
- organizing, certification, and realized coverage are different stages of the same broader process
- direct effects, spillovers, and threat effects should not be collapsed into one estimate
- collective bargaining changes wages, compression, amenities, and workplace governance
- Week 8 links bargaining institutions to the broader regulation and enforcement block
:::

## Bridge

Week 7 treated wage floors as rules imposed on decentralized wage-setting. Week 8 asks what changes when wages and workplace rules are shaped by organized worker voice rather than only by statutory floors or individual contracts. This is why unions belong in the middle of Labor II rather than at the edge of a labor-history survey. Weeks 5 and 6 taught us that wages depend on bargaining protocols and employer labor-market power. Week 7 showed that legal floors can compress wage-setting from the outside. Week 8 adds the central institution that changes wage-setting from inside the employment relationship: collective bargaining.

The bridge from Week 7 is especially useful because minimum wages and unions are related but distinct. A minimum wage is a legal floor that targets the lower tail of pay. Collective bargaining can instead reshape the whole wage structure, nonwage conditions, grievance procedures, staffing rules, and the distribution of rents inside the firm or sector. The bridge to Week 9 is equally important. Week 8 introduces bargaining institutions and organizing rules, but it does not yet become the labor-law and enforcement lecture. That next week will ask how regulation, insurance, and enforcement sustain or constrain the institutional environment introduced here.

This week keeps five distinctions explicit from the start.

1. union membership is not the same thing as collective-bargaining coverage;
2. firm-level bargaining is not the same thing as sectoral, multi-employer, or extension regimes;
3. organizing and certification are not the same thing as realized coverage or post-union wage effects;
4. direct effects on covered workers are not the same thing as spillovers or threat effects on uncovered workers;
5. labor-market effects of unions are not identical to unions' political effects, even though the two are linked.

```{include} assets/tables/08-collective-bargaining-concepts-map.md
```

Table {numref}`tbl:collective-bargaining-concepts-map` is the opening taxonomy for the week. It keeps the chapter from collapsing membership, coverage, bargaining regime, and worker voice into one generic "union" object.

```{figure} assets/figures/08-membership-vs-coverage-distinction.png
:name: fig-lii-w8-membership-coverage
Membership, coverage, and bargaining regime are distinct objects. Coverage can exceed membership, and bargaining institutions can matter even where dues-paying membership is limited.
```

Figure {numref}`fig-lii-w8-membership-coverage` is the first anchor for the lecture. It visually states the most common empirical confusion: bargaining coverage is often the more institutionally relevant object even when membership is the more visible political statistic.

## Field Core

### What unions and collective bargaining change

The core labor-economics reason to study unions is that they alter the mapping from firm rents and worker outside options into wages and workplace rules. In Week 5, bargaining was often bilateral. In Week 8, bargaining becomes collective. In Week 6, labor-market power was firm-facing. In Week 8, organized worker voice partly counteracts or redirects that power. In Week 7, wage floors compressed the lower tail from outside the firm. In Week 8, bargaining institutions can compress wages from inside the firm or sector.

The clean accounting identity is the right place to begin:

```{math}
:label: eq-lii-w8-membership-coverage
C_{rt} = M_{rt} + N_{rt}^{covered,nonmember},
\qquad
C_{rt} \geq M_{rt},
```

where {math}`M_{rt}` is union membership in region or regime {math}`r` at time {math}`t`, and {math}`C_{rt}` is collective-bargaining coverage. Equation {eq}`eq-lii-w8-membership-coverage` says that covered nonmembers are part of the labor-market institution even if they are not dues-paying union members. This distinction is essential in cross-country work, in U.S. public-sector settings, and in any application where contract extension rules matter [@jagerNaiduSchoefer2024; @hirschMacpherson2003].

```{figure} assets/figures/08-collective-bargaining-regimes.png
:name: fig-lii-w8-bargaining-regimes
Firm-level bargaining, sectoral bargaining, and extension regimes transmit worker voice into wages very differently. The membership rate alone cannot summarize that institutional structure.
```

Figure {numref}`fig-lii-w8-bargaining-regimes` is the institutional map for the week. Firm-level bargaining matters most directly for the U.S. private-sector certification literature. Sectoral and extension regimes matter most directly for the coverage and wage-structure literatures emphasized by [@jagerNaiduSchoefer2024].

The compact collective-bargaining object can be written as

```{math}
:label: eq-lii-w8-rentsharing
w_{ijt} = w^{0}_{ijt} + \beta_{jt} R_{jt},
```

where {math}`w^{0}_{ijt}` is the fallback or nonunion wage, {math}`R_{jt}` is rent or surplus available at establishment or bargaining unit {math}`j`, and {math}`\beta_{jt}` summarizes how bargaining institutions and worker power shift rent-sharing toward labor. Equation {eq}`eq-lii-w8-rentsharing` is deliberately schematic. It does not claim that every union estimate is a clean rent-sharing coefficient. It only states the channel: bargaining can raise the wage level, compress wage differences, or reallocate surplus toward covered workers.

The labor-market objects changed by unions are broader than wages alone. Bargaining can affect benefits, schedules, grievance procedures, job protection, promotion rules, and formal voice channels. [@harjuJagerSchoefer2025] is useful here because the identifying variation comes from workplace-level representation arrangements, the unit of observation is the workplace or worker-workplace relationship, the observed margin is voice and participation, and the key unobserved object is the full counterfactual governance structure absent representation. That is why worker voice belongs in the title of the week even though the empirical core remains about wages, employment, coverage, and spillovers.

[@hirsch2008] provides the right conceptual caution. Unions and competition can coexist, but that coexistence depends on what unions bargain over, whether gains come from rent-sharing or productivity changes, and how employers respond on employment, investment, and survival margins. Week 8 should therefore treat unions as wage-setting and governance institutions, not as a single reduced-form wage premium.

### Membership, coverage, bargaining regimes, and why the objects differ

Membership is the organizational attachment object. Coverage is the contract object. Density is the environment object. Bargaining regime is the institutional architecture. Worker voice is the governance object. The fact that these are separable is not semantic. It determines what the data mean and which comparisons are credible.

U.S. CPS and Unionstats data are especially useful because they separately observe membership and coverage. The identifying variation in those data is usually descriptive rather than causal. The unit is the worker-year or demographic cell. The observed margins are membership, coverage, wages, and inequality. The key unobserved object is the untreated counterfactual path of labor-market structure absent deunionization or institutional change [@hirschMacpherson2003; @farberHerbstKuziemkoNaidu2021]. That is why CPS/Unionstats panels are ideal for trend description and bounded teaching labs but not sufficient on their own for sharp causal claims.

Cross-country comparisons make the distinction even more concrete. [@jagerNaiduSchoefer2024] uses harmonized international data where bargaining coverage, not just membership, is central. The identifying variation is coverage and regime differences across countries and over time. The unit is the worker-country-year or sector-country-year cell. The observed margins are wage levels and dispersion. The key unobserved object is the bundle of other institutions that move with bargaining regimes. The paper is therefore powerful for teaching the membership-versus-coverage distinction and weaker as a one-number causal estimate.

This section is also where public-sector or education-sector bargaining should be separated from private-sector unionization if mentioned. Teacher salary schedules or public-sector bargaining laws often illuminate wage rules and worker voice, but they operate under different legal and fiscal institutions from private-sector certification and collective bargaining. Week 8 is anchored primarily in private-sector unionization and bargaining coverage unless the contrast itself is the point.

### Organizing, takeup, certification, and who gets covered

The organizing question is not "why did union density decline?" in the abstract. It is how worker demand for representation maps imperfectly into realized coverage once employer opposition, bargaining law, establishment characteristics, and labor-market conditions intervene.

The reduced-form organizing object can be written as

```{math}
:label: eq-lii-w8-organizing
\Pr(\text{UnionWin}_{jt}=1)
=
F(D_{jt}, O_{jt}, L_{jt}),
```

where {math}`D_{jt}` captures worker demand, {math}`O_{jt}` employer opposition or campaign response, and {math}`L_{jt}` the broader legal and labor-market environment. Equation {eq}`eq-lii-w8-organizing` is the key takeup object for the week. It says plainly that organizing success is not a pure preference measure.

```{figure} assets/figures/08-certification-to-coverage-pipeline.png
:name: fig-lii-w8-certification-pipeline
Observed coverage is the end of a pipeline from worker demand to organizing, election, bargaining, and contract realization. Attrition at each stage makes union desire different from observed unionization.
```

Figure {numref}`fig-lii-w8-certification-pipeline` is the organizing backbone for the lecture. It keeps students from interpreting a certification-election estimate as if it were the same object as a coverage premium or an equilibrium union-density effect.

```{include} assets/tables/08-union-takeup-coverage-and-spillovers-map.md
```

Table {numref}`tbl:union-takeup-coverage-spillovers-map` organizes the evidence by margin rather than chronology. It is particularly useful because it puts organizing, certification, coverage, spillovers, and political spillovers in one map without treating them as the same estimand.

[@dinlersozGreenwoodHyatt2017] is the clean life-cycle organizing paper for this week. The identifying variation comes from NLRB election data linked to establishment characteristics. The unit of observation is the establishment or election episode. The observed margin is where organizing occurs. The key unobserved object is latent worker demand absent employer and legal frictions. The main lesson is that who gets organized is itself selective and economically structured.

[@pezoldRothSchoefer2023] brings labor-market tightness directly into the takeup discussion. The identifying variation comes from changes in local labor-market conditions interacted with union activity. The unit is the election, campaign, or local labor-market environment. The observed margin is union activity and organizing intensity. The key unobserved object is whether tightness shifts worker beliefs, employer vulnerability, or both. This is exactly the kind of Week 8 link back to Weeks 4 and 6 that students should see clearly: organizing depends partly on outside options and bargaining conditions in the market.

Certification elections are central in the U.S. literature because they generate quasi-experimental variation near the win threshold, but they remain only one object. Close-election designs tell us about marginal elections near the cutoff, not about all workplaces that might desire a union or about countries where sectoral coverage expands without establishment-level certification.

### Direct effects on covered workers: premia, compression, selection, and survival

The direct-effect literature is where many students first look for "the union effect," but Week 8 needs more discipline. A union wage premium for newly organized private-sector workers is not the same object as a broad coverage effect in a sectoral regime. A within-firm compression effect is not the same object as an average wage premium. An employment or survival effect for establishments after close election wins is not the same object as the long-run role of unions in aggregate inequality.

[@dinardoLee2004] is the canonical certification-election regression discontinuity design. The identifying variation is a close union win versus a close union loss at the certification threshold. The unit of observation is the establishment or election. The observed margins are wages, employment, survival, and firm outcomes after unionization. The key unobserved object is the counterfactual path for non-close elections and the broader equilibrium environment. The main teaching value is that the paper identifies a local causal effect of marginal union victories, not the full aggregate effect of union institutions.

[@frandsen2021] uses matched employer-employee data around close elections. The identifying variation is again near-threshold union victories, but the observed unit is the worker-firm match rather than only the establishment. The observed margins include earnings, employment, and worker composition. The key unobserved object is longer-run equilibrium sorting outside the treated match. The paper matters because it shows how a similar certification design can reveal more about payroll, worker composition, and heterogeneous treatment than a pure establishment panel.

[@farberHerbstKuziemkoNaidu2021] is the central wage-structure anchor. The identifying variation is long-run survey variation in union status and union exposure over time. The unit is the worker-year, state-year, or distributional cell, depending on the decomposition. The observed margins are wage dispersion, unionization, and inequality over the twentieth century. The key unobserved object is the untreated distributional path absent deunionization and the exact division between direct and spillover channels. The paper is therefore strongest for teaching unions as a distributional institution rather than as a single marginal private-sector RD treatment.

The wage-structure insight is the non-negotiable direct-effect lesson. Unions can raise pay for covered workers and compress wages at the same time. Compression may operate through narrower occupation differentials, flatter within-firm wage ladders, or stronger floors for lower-paid covered workers. That compression is often more important for inequality than the average premium alone.

Selection remains central throughout. Workers who sort into union jobs may differ in unobserved attachment, preferences, and outside options. Firms or establishments where organizing succeeds may differ in rents, technology, conflict, or workforce composition. This is why direct effects estimated from cross-sectional coverage premia, certification RDs, and matched employer-employee designs can disagree without logical contradiction.

### Spillovers and threat effects on nonunion workers

Week 8 is incomplete without spillovers because unions can reshape wages outside the formal bargaining unit. The direct treatment of covered workers is only part of the equilibrium story. Uncovered workers can gain if union wage norms raise outside options or if nonunion firms pay more to avoid organizing. They can lose if bargaining reallocates employment, compresses differentials only inside the covered sector, or changes firm composition in ways that crowd workers into the uncovered sector.

The reduced-form spillover object is

```{math}
:label: eq-lii-w8-spillovers
w^N_{rt}
=
\alpha
+ \gamma \,\text{UnionPresence}_{rt}
+ X_{rt}'\delta
+ \varepsilon_{rt},
```

where {math}`w^N_{rt}` is the wage of nonunion or uncovered workers and {math}`\gamma` captures spillover, threat, or crowd-out effects associated with union presence. Equation {eq}`eq-lii-w8-spillovers` is not a full equilibrium model. It only clarifies that the nonunion wage response is a separate estimand from the covered-worker premium.

```{figure} assets/figures/08-union-wage-compression-and-spillovers.png
:name: fig-lii-w8-compression-spillovers
Collective bargaining can compress wages directly for covered workers and indirectly through spillovers, threat effects, or labor reallocation in uncovered markets.
```

Figure {numref}`fig-lii-w8-compression-spillovers` is the distributional anchor for the week. It emphasizes that compression can arise through both direct contract effects and broader wage-setting spillovers.

[@fortinLemieuxLloyd2021] is the core spillover paper. The identifying variation comes from differences in labor-market institutions and union exposure combined with distributional wage analysis. The unit is the worker, region, or wage-distribution cell depending on the specification. The observed margin is wages across the distribution, especially for uncovered workers. The key unobserved object is the untreated wage structure absent institutional spillovers. The paper is central because it shows why focusing only on members or covered workers understates the aggregate role of unions in inequality.

[@fortinLemieuxLloyd2022] sharpens the threat-effect discussion using right-to-work and related institutional changes. The identifying variation is policy reform timing and exposure. The unit is the state-year, sector-year, or worker-region cell. The observed margins are unionization and wage-setting outcomes for both union and nonunion workers. The key unobserved object is policy endogeneity and the untreated institutional path. This is the best point in the lecture to say explicitly that threat effects, positive spillovers, and negative crowd-out are different notions of spillover and can generate different empirical signs.

This is also why nonunion workers inside partially unionized firms are not automatically clean controls. They may be affected by common firm wage policies, internal equity norms, bargaining spillovers, or employer anti-organizing responses. Week 8 should make that point early, because it helps students understand why aggregate inequality decompositions and matched employer-employee designs often treat spillovers as first-order rather than secondary.

### Data and empirical designs: what each design identifies

```{include} assets/tables/08-identification-and-political-economy-bridge.md
```

Table {numref}`tbl:union-identification-political-economy-bridge` is the empirical design map for Week 8. It should be read as a guide to objects, not as a ranking of papers.

Certification-election RD designs vary close election outcomes around the legal win threshold. The unit is the establishment or election. The object identified is the local causal effect of marginal union victories. The key limitation is local external validity and the fact that the design starts after the organizing pipeline has already selected a set of workplaces into election.

Matched employer-employee union designs vary unionization at the firm-worker match and observe payroll and composition more directly. The unit is the worker-firm match. The object identified is the direct effect on earnings, employment, and composition in matched data. The key limitation is that spillovers and longer-run general equilibrium resorting remain only partially observed [@frandsen2021].

Historical survey and decomposition designs vary unionization, coverage, and institutional exposure over long horizons. The unit is the worker-year, state-year, or wage-distribution cell. The object identified is the contribution of unions to long-run wage compression and inequality. The key limitation is that stronger modeling assumptions are needed to separate direct effects, selection, and spillovers [@farberHerbstKuziemkoNaidu2021].

Cross-country coverage comparisons vary bargaining regime and contract coverage across countries or sectors. The unit is the worker-country-year or sector-country-year cell. The object identified is the association between coverage institutions and wage structure. The key limitation is that many institutions move jointly with coverage, so transportable causal interpretation is difficult [@jagerNaiduSchoefer2024].

Policy-shock and event-study designs vary bargaining law, right-to-work status, or extension rules over time. The unit is usually the state-year, sector-year, or country-year cell. The object identified is the effect of legal and institutional reforms on wage-setting and sometimes politics. The key limitation is policy endogeneity and exposure measurement.

Descriptive CPS and Unionstats panels vary union membership and coverage across states, sectors, and demographic cells. The unit is the worker-year or state-year cell. The object identified is trend and heterogeneity description, with bounded transfer value for teaching labs. The key limitation is that descriptive movement is not by itself causal [@hirschMacpherson2003].

### Brief political-economy bridge

Unions are labor-market institutions first and political actors second in this lecture, but the second role cannot be ignored. Bargaining institutions affect voting, party coalitions, lobbying, and support for labor regulation. Political channels can then feed back into labor-market institutions through labor law, enforcement, social insurance, and public spending.

```{figure} assets/figures/08-political-economy-bridge.png
:name: fig-lii-w8-political-bridge
Collective bargaining can transmit workplace organization into political participation, lobbying, and regulation, but those political effects remain an adjacent bridge rather than the main estimand of Week 8.
```

Figure {numref}`fig-lii-w8-political-bridge` is intentionally small and explicit. It bridges outward without turning the chapter into a general political-economy survey.

[@kaplanNaidu2025] is the anchor here. The identifying variation comes from institutional change, political data, and the interaction between labor organizations and electoral or policy outcomes. The unit is the worker, union, region, or political jurisdiction depending on the design. The observed margins are turnout, policy support, coalition formation, and regulation. The key unobserved object is the full counterfactual political environment absent labor organization. The point for Labor II is not to re-teach political economy. It is to say clearly why labor economists care: workplace organization can shift both wage-setting and the rules under which wage-setting occurs.

## Research Lab

The optional extension block for Week 8 should feel like a research workshop on institutions rather than a catch-all appendix. Four directions are especially productive.

First, coverage regimes vary far more across countries than union membership does, which makes international comparisons especially useful for distinguishing bargaining architecture from organizational density [@jagerNaiduSchoefer2024]. Second, unions and monopsony interact: collective bargaining can counter employer wage-setting power, but the size of that correction depends on outside options, product-market rents, and who gets organized. Third, spillovers inside partially unionized firms remain undermeasured because uncovered workers are often affected by common wage policies and threat effects. Fourth, new data on union campaigns, elections, and worker beliefs create better opportunities to study organizing demand separately from realized certification outcomes [@pezoldRothSchoefer2023].

The bounded Week 8 lab follows `Reproduce -> Diagnose -> Transfer`. The reproduction anchor is [@farberHerbstKuziemkoNaidu2021], where the object is the contribution of union coverage and related exposure to wage compression and inequality over time. The diagnose anchor is [@dinardoLee2004], where the object is the local causal effect of close certification wins on establishments and workers near the threshold. The optional extension anchor is [@fortinLemieuxLloyd2021], where the object is spillovers onto uncovered workers and the aggregate wage distribution. The lab handout lives at [labs/08-unions-collective-bargaining-and-worker-voice/lab.md](labs/08-unions-collective-bargaining-and-worker-voice/lab.md).

The research extension should explicitly push students to ask four questions of any new paper.

1. Is the paper estimating membership, coverage, organizing, or bargaining regime?
2. Is the effect direct on covered workers, indirect through spillovers, or threat-based on uncovered workers?
3. What identifying variation makes the result credible?
4. What key object remains latent: worker demand for unions, employer opposition, uncovered spillovers, or the untreated political environment?

## Methods Box

Week 8 only works if the empirical objects remain separate.

1. Union membership is not the same thing as collective-bargaining coverage.
2. Firm-level bargaining is not the same thing as sectoral bargaining, multi-employer bargaining, or extension regimes.
3. Direct effects on covered workers are not the same thing as spillovers or threat effects on uncovered workers.
4. Certification-election RD designs identify marginal organizing victories, not the full aggregate role of unions.
5. Matched employer-employee designs reveal payroll, employment, and composition more directly, but still do not automatically solve spillover and general-equilibrium problems.
6. Historical decompositions and distributional studies are especially informative about wage compression and inequality, but they rely on stronger assumptions than close-election designs.
7. Private-sector unionization should not be conflated with public-sector or education-sector bargaining when the legal environment differs.
8. Different papers can disagree because they study different objects: membership versus coverage, wages versus employment versus survival, selection into organizing, and different notions of spillover.
9. Every empirical claim in this week should name the identifying variation, unit of observation, observed margin, and key unobserved object.

## Reading Ladder And References

### Required / field core

- [@jagerNaiduSchoefer2024] for the membership-versus-coverage distinction and the international wage-structure perspective.
- [@farberHerbstKuziemkoNaidu2021] for unions as a distributional institution shaping wage compression and inequality over time.
- [@dinardoLee2004] for the canonical certification-election RD and the local causal effect of marginal union victories.

### Strong complements

- [@frandsen2021] for matched employer-employee evidence on earnings, payroll, and employment after close election wins.
- [@dinlersozGreenwoodHyatt2017] for who gets organized and why takeup differs across establishments.
- [@pezoldRothSchoefer2023] for organizing and labor-market tightness.
- [@fortinLemieuxLloyd2021] for spillovers and the wage-distribution role of labor-market institutions.
- [@hirsch2008] for the competition, productivity, and coexistence perspective.

### Optional / frontier / bridge outward

- [@fortinLemieuxLloyd2022] for right-to-work, unionization, and wage-setting under policy change.
- [@kaplanNaidu2025] for the political-economy bridge from labor organization to policy and coalitions.
- [@harjuJagerSchoefer2025] for worker voice beyond a pure wage-premium interpretation.
- [@hirschMacpherson2003] for CPS/Unionstats measurement of membership and coverage.

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-lii-w8-membership-coverage` to explain why a decline in union membership need not imply a one-for-one decline in bargaining coverage.
2. Why is Equation {eq}`eq-lii-w8-rentsharing` only a schematic bargaining object rather than a literal estimate of every union effect?
3. In [@dinlersozGreenwoodHyatt2017], what is the observed unit, and why does that matter for interpreting organizing selection?
4. In [@dinardoLee2004], what variation identifies the estimate, what margin is observed, and what broader object remains unobserved?
5. How does [@frandsen2021] change what we learn relative to a pure establishment-level close-election design?
6. Use Equation {eq}`eq-lii-w8-spillovers` to distinguish positive spillovers, threat effects, and negative crowd-out in the uncovered sector.
7. Why can a country with modest union membership still have high bargaining coverage and substantial wage compression?
8. Why are nonunion workers inside partially unionized firms not automatically clean controls for covered workers?
9. In [@farberHerbstKuziemkoNaidu2021], what makes the object a distributional decomposition rather than a local organizing treatment effect?
10. Propose one transfer design using a CPS/Unionstats panel, certification-election panel, or synthetic coverage-inequality panel. Name the observed unit, observed margin, identifying variation, and key unobserved object.

## Reproducibility And Code Lab Note

The Week 8 code lab is deliberately bounded and fully local. The reproduction step uses a synthetic state-year panel in the spirit of [@farberHerbstKuziemkoNaidu2021] so students can separate membership, coverage, direct compression, and spillover compression without requiring confidential microdata. The diagnose step uses a synthetic certification-election panel in the spirit of [@dinardoLee2004], forcing students to say explicitly that the object is organizing success near a legal threshold rather than broad coverage or equilibrium union density. The optional extension asks how the same logic transfers to a public CPS/Unionstats panel or to a spillover design inspired by [@fortinLemieuxLloyd2021]. The bounded path runs locally; the handout lives at [labs/08-unions-collective-bargaining-and-worker-voice/lab.md](labs/08-unions-collective-bargaining-and-worker-voice/lab.md).

## Slide Companion Note

The Week 8 slide deck is designed to stay lighter than the chapter even though this is a heavy institution week. The deck should define the question, isolate the membership-versus-coverage distinction, show the collective-bargaining and organizing pipelines, separate direct from spillover effects, and end by bridging backward to Week 7 minimum wages and forward to Week 9 labor regulation, enforcement, and insurance. The canonical source is [slides/week8/08-unions-collective-bargaining-and-worker-voice.tex](slides/week8/08-unions-collective-bargaining-and-worker-voice.tex).

## Bridge Forward

Use this closing bridge to carry the module's labor object, mechanism, and evidence into the next course step or research-design exercise.
