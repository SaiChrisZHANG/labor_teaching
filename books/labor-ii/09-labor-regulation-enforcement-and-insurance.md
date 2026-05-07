---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Labor Regulation, Enforcement, and Insurance

## Learning objectives

By the end of Week 9, students should be able to:

1. classify labor regulations into a small set of analytically useful families rather than a bucket of policies;
2. distinguish worker-targeted, firm-targeted, and regulator-targeted interventions;
3. separate regulation on the books from effective regulation once enforcement, knowledge, and compliance matter;
4. explain how dismissal rules, labor standards, insurance, and information policies fit inside one labor-market framework;
5. distinguish direct partial-equilibrium effects from equilibrium effects operating through vacancies, informality, prices, and uncovered workers;
6. interpret empirical designs in this literature by naming the identifying variation, unit of observation, observed margin, and key unobserved object;
7. evaluate effectiveness, spillovers, inequality implications, and welfare tradeoffs without treating employment as the only outcome;
8. connect Week 9 back to Weeks 7 and 8 and forward to Week 10 on aggregate labor-market adjustment.

The economic question for Week 9 is not whether regulation is generically pro-worker or anti-firm. It is how labor economists should study rules that change contracting, separations, compliance, search, insurance, and information once both sides of the labor market and the regulator are inside the model. This chapter is organized around four linked questions.

1. What is a useful general framework for understanding different types of labor regulations?
2. How do regulations affect both sides of the labor market, and what key equilibrium effects matter?
3. Empirically, how effective are regulations once enforcement, spillovers, and inequality implications are considered?
4. What are the welfare implications?

## Bridge

Week 7 treated minimum wages as a targeted intervention in wage-setting. Week 8 treated collective bargaining as an institution that changes wage-setting, rent-sharing, and worker voice from inside the employment relationship. Week 9 generalizes that logic. The relevant object is now the wider class of labor-market rules that alter hiring, firing, pay, hours, compliance, search, benefits, and information. The bridge from Week 8 matters because bargaining power and legal protection are complements rather than substitutes. Collective institutions operate inside a legal environment; legal rules shape which contracts can be offered, how separations occur, how rights are enforced, and how income risk is insured.

This is therefore one of the heavier policy-framework weeks in Labor II. It should feel like the capstone of the policy block rather than a list of statutes. The key move is to replace policy-by-policy memorization with a reusable research framework:

1. classify the regulation;
2. identify the operative labor-market margin;
3. determine which side of the market is directly treated;
4. ask whether enforcement and compliance make the law effective;
5. trace spillovers, uncovered margins, and equilibrium responses;
6. state the welfare benchmark before interpreting the evidence.

The distinctions have to stay explicit from the start.

1. regulation on the books is not the same object as effective regulation;
2. worker-targeted, firm-targeted, and regulator-targeted policies do not operate through the same margins;
3. dismissal costs, labor standards, insurance, and information rules are not interchangeable policy objects;
4. compliance is not the same thing as absence of evasion or informal adjustment;
5. direct effects on covered workers or firms are not the same thing as spillovers to uncovered workers or firms;
6. employment, wages, hours, turnover, search, formality, and price incidence are distinct outcome margins.

```{include} assets/tables/09-regulation-taxonomy-map.md
```

Table {numref}`tbl:regulation-taxonomy-week9` is the opening map for the week. It keeps the lecture focused on analytically distinct families of labor regulation rather than on a long policy inventory.

```{figure} assets/figures/09-regulation-taxonomy-framework.png
:name: fig-lii-w9-taxonomy
Week 9 organizes labor regulation by targeted margin, directly treated side, implementation channel, and equilibrium spillover. The point is to compare heterogeneous policies on common labor-market dimensions.
```

Figure {numref}`fig-lii-w9-taxonomy` is the conceptual front door to the chapter. It makes clear why Week 9 belongs between the bargaining weeks and the aggregate-adjustment weeks: regulations are neither purely contractual nor purely macro, but they shape both.

:::{admonition} Core Material
:class: tip
- labor regulation is easiest to study through wedges, margins, and the directly treated side of the market
- regulation on the books is different from effective regulation once enforcement and compliance matter
- worker-targeted, firm-targeted, and regulator-targeted policies operate through different channels
- spillovers, uncovered sectors, informality, and price incidence are part of the object rather than afterthoughts
- welfare interpretation requires naming the benchmark before reading results
:::

:::{admonition} Optional Extension Block
:class: note
- the Research Lab below extends the chapter toward implementation, equilibrium spillovers, and uncovered-margin questions
:::

## Field Core

### A general framework for labor regulation

The cleanest way to unify the week is to start from wedges. Labor regulations often create a wedge between worker take-home value, firm labor cost, and public or private transfers. Some policies operate by raising firm-side costs. Others insure workers against separation or low pay. Others change information or expected penalties without changing formal transfer schedules. The common object is

```{math}
:label: eq-lii-w9-wedge
w_{it}^{net} = w_{it}^{gross} + b_{it} - \tau_{it}^{worker},
\qquad
c_{it}^{firm} = w_{it}^{gross} + \tau_{it}^{firm} + \kappa_{it}^{comp},
```

where {math}`w_{it}^{net}` is worker-side value, {math}`c_{it}^{firm}` is firm-side labor cost, {math}`b_{it}` is insurance or mandated benefit value, {math}`\tau` terms capture taxes or statutory wedges, and {math}`\kappa_{it}^{comp}` captures compliance, reporting, dismissal, or legal-risk costs. Equation {eq}`eq-lii-w9-wedge` is deliberately broad. A regulation matters when it changes this mapping between what workers receive, what firms pay, and which margins adjust to absorb the wedge.

That framing immediately yields a useful classification. Firm-targeted dismissal protection primarily shifts {math}`\kappa_{it}^{comp}` around separations. Standards enforcement changes the expected penalty for noncompliance and therefore the effective firm-side cost of violating the rule. Worker-targeted insurance changes {math}`b_{it}` and therefore search behavior, reservation wages, and separation dynamics. Information and transparency rules often work by changing beliefs, bargaining, or complaint behavior even when formal wedges barely move. `@macleod2011GreatExpectations` is the right conceptual anchor because the chapter treats law as part of the labor contract environment rather than as an external appendage.

### Worker-side, firm-side, and regulator-side margins

The next step is to make the market two-sided and to bring the regulator inside the analysis. Worker-targeted policies alter search effort, reservation behavior, take-up, complaints, willingness to remain formal, and willingness to separate. Firm-targeted policies alter hiring, firing, contract composition, vacancy posting, outsourcing, capital substitution, and evasion. Regulator-targeted policies alter inspection probability, sanctions, information salience, and the effective return to compliance. Many policies touch all three sides at once.

```{include} assets/tables/09-equilibrium-and-incidence-map.md
```

Table {numref}`tbl:equilibrium-incidence-week9` is the incidence map for the week. It is useful precisely because it forces students to say which adjustment margin they think is first-order before they interpret any coefficient.

```{figure} assets/figures/09-incidence-compliance-and-adjustment.png
:name: fig-lii-w9-incidence
Regulation acts on workers, firms, and regulators simultaneously. Direct treatment is only the first stage; compliance, vacancy adjustment, informal-sector reallocation, and price incidence determine the equilibrium object.
```

Figure {numref}`fig-lii-w9-incidence` highlights why partial-equilibrium reasoning is often incomplete. A direct wage or separation effect may be small while spillovers through vacancies, informality, or prices are large. Conversely, a large treated-worker effect may wash out if firms avoid the regulation through contract redesign or uncovered margins.

### Employment protection and dismissal costs

Dismissal regulation is the cleanest starting point because it puts the contracting margin and the separation margin into one object. A schematic firm problem is

```{math}
:label: eq-lii-w9-dismissal
J_{jt}(s) = p_{jt} - c_{jt}^{firm} - \phi^{D}_{jt}\mathbf{1}\{s=1\},
```

where {math}`J_{jt}(s)` is the value of the match, {math}`p_{jt}` is current productivity, and {math}`\phi^{D}_{jt}` is the dismissal or severance cost triggered when separation {math}`s=1`. Equation {eq}`eq-lii-w9-dismissal` makes the standard point: higher dismissal costs reduce separations on the margin, but the same wedge can also reduce hiring, encourage temporary contracts, or shift firms toward capital, outsourcing, or lower-turnover production techniques.

`@autorDonohueSchwab2006` is the first empirical anchor. The identifying variation is staggered adoption of wrongful-discharge doctrines across U.S. states. The unit of observation is the state labor market, often at the state-year or worker-state-year level. The observed margins are employment-to-population rates, employment, and wages. The key unobserved object is the untreated path of state labor markets absent the doctrine, including other legal or compositional changes. The main lesson is not that every dismissal protection law has one effect. It is that dismissal-cost estimates are design- and doctrine-specific.

`@autorKerrKugler2007` pushes the same logic into establishment outcomes. The identifying variation is again adoption of wrongful-discharge protections across U.S. states, but the unit of observation is the establishment or plant in Census data. The observed margins are employment flows, firm entry, capital deepening, and productivity. The key unobserved object is the counterfactual production technique and composition of plants absent the legal change. This is exactly why Week 9 must emphasize more than employment levels. Dismissal protection can operate through turnover, entry, and technology choice even if net employment is ambiguous.

`@kugler2004JobSecurity` is the reform-based bridge to higher-turnover environments. The identifying variation comes from a labor-market reform that changed job-security regulations in Colombia. The unit is the worker or worker-flow margin. The observed objects are separations, job finding, and unemployment transitions. The key unobserved object is what worker flows would have been under unchanged macro conditions and firm composition. The broader lesson is that dismissal protection is about job-flow dynamics, not just a static headcount effect.

Disagreement in this literature often comes from different policy objects and different equilibrium assumptions. A just-cause rule, severance mandate, and temporary-contract restriction all change the separation margin, but not in identical ways. A paper centered on incumbent jobs may find protection where a paper centered on entrant jobs finds sclerosis. A paper with low observed contract substitution may look different from a setting with a large temporary or informal sector. Those disagreements are substantive rather than pathological.

### Effective regulation: enforcement, compliance, and state capacity

Labor economists learn quickly that the law on the books is an incomplete treatment definition. A more useful schematic object is

```{math}
:label: eq-lii-w9-effective
R_{rt}^{eff} = R_{rt}^{law} \times E_{rt} \times K_{rt} \times P_{rt},
```

where {math}`R_{rt}^{law}` is the formal rule, {math}`E_{rt}` is enforcement capacity, {math}`K_{rt}` is knowledge or salience, and {math}`P_{rt}` is private compliance. Equation {eq}`eq-lii-w9-effective` is intentionally multiplicative: if any component is near zero, measured regulation may bind weakly even when the legal text looks strong.

```{figure} assets/figures/09-enforcement-capacity-to-effective-regulation.png
:name: fig-lii-w9-effective
Effective regulation is the product of the rule, enforcement capacity, worker and firm knowledge, and compliance. The same statute can bind very differently across localities and sectors.
```

Figure {numref}`fig-lii-w9-effective` is the implementation backbone for the week. It is the simplest way to keep students from equating formal law with realized treatment.

`@almeidaCarneiro2012` is the canonical enforcement paper for the chapter and the primary anchor for the lab. The identifying variation is locality-level exposure to labor inspections in Brazil. The unit of observation is the worker, firm, or locality-year depending on the specification. The observed margins are wages, formality, compliance with mandated benefits, and movement between formal and informal work. The key unobserved object is local state capacity and labor-demand conditions that could jointly shape enforcement and outcomes. The economic insight is subtle and central: stronger enforcement raises the effective cost of formal labor, but it can also increase the value of formal employment because mandated benefits become real rather than nominal. Wage rigidity at the bottom then determines whether costs are absorbed in wages or in reallocation across formal and informal jobs.

`@bertrandCrepon2021` complements this by shifting attention from penalties to information. The identifying variation is a randomized information intervention that gave South African firms access to labor-law expertise. The unit of observation is the firm. The observed margins are beliefs about labor regulation, perceived hiring constraints, and employment. The key unobserved object is the longer-run compliance and worker-side response once information diffuses more broadly. The paper is valuable because it shows that perceived regulation can differ from actual regulation. A firm may underhire because it misunderstands the law, which means information itself becomes a regulator-targeted policy.

This section is also where compliance and evasion should be separated. Compliance means the covered margin responds as intended. Evasion means firms redesign behavior to remain outside the intended treatment, perhaps through underreporting hours, using informal labor, outsourcing, or contracting around the rule. In low-enforcement settings, informality can become the main equilibrium escape margin. In high-enforcement settings, price pass-through or job redesign may matter more. The same observed mean employment effect can therefore conceal very different implementation realities.

### Insurance, search, and labor-market equilibrium

Unemployment insurance belongs in this chapter because it is both insurance and labor-market regulation. It changes the value of nonemployment, the timing of separations and recalls, worker search behavior, and sometimes firm layoff incentives. Once vacancies and nonrecipient outcomes move, UI stops being a purely treated-worker object. A compact welfare accounting is

```{math}
:label: eq-lii-w9-ui
\Delta W = MI - BD + EE,
```

where {math}`MI` is the mechanical insurance gain, {math}`BD` is the behavioral distortion cost, and {math}`EE` is the equilibrium externality term capturing effects on nonrecipients, vacancies, queueing, or uncovered sectors. Equation {eq}`eq-lii-w9-ui` is the right organizing object because Week 9 should never discuss insurance design without simultaneously naming the labor-market distortion and equilibrium margins.

```{figure} assets/figures/09-insurance-distortion-equilibrium.png
:name: fig-lii-w9-ui
UI changes search and consumption directly for recipients, but equilibrium interpretation also depends on vacancy responses, nonrecipient outcomes, and uncovered informal margins.
```

Figure {numref}`fig-lii-w9-ui` shows why Week 9 naturally points toward Week 10. Once UI affects vacancies, queueing, and recall dynamics, the policy problem becomes inseparable from aggregate labor-market adjustment.

`@laliveLandaisZweimueller2015` is the non-negotiable equilibrium anchor. The identifying variation is a regional UI extension program in Austria that changed benefit duration for eligible workers in treated regions. The unit of observation is the worker or region-labor-market cell. The observed margins are job-finding rates, unemployment duration, and outcomes for noneligible workers. The key unobserved object is the counterfactual labor-market tightness and spillovers outside treated regions. The central result is exactly what Week 9 needs students to remember: a recipient-level UI estimate can be misleading if nonrecipients also change behavior because vacancies, competition, or queueing move.

`@lindner2020FrontLoading` narrows the object to benefit timing. The identifying variation is a sharp Hungarian reform that front-loaded unemployment benefits while holding total entitlement roughly fixed. The unit of observation is the claimant spell. The observed margins are nonemployment duration and reemployment wages. The key unobserved object is the market-wide response outside the treated cohort. The paper is valuable because it puts the insurance-versus-distortion tradeoff on an operational margin: not just how much UI is paid, but when it is paid.

The Brazil extension `@vanDoornikGerardNaritomi2023` is the bridge to informal and uncovered margins. The identifying variation comes from policy-induced shifts in UI eligibility or timing in a high-informality environment. The unit is the worker spell or local labor market. The observed margins are formal layoffs, recall timing, and transitions into informal work. The key unobserved object is the counterfactual set of informal opportunities and strategic firm-worker behavior absent the UI incentive. This is the right place to say explicitly that worker-targeted insurance can induce firm-targeted responses when the covered margin is formal employment and the uncovered margin is informal work.

### Information, transparency, and rights salience as labor regulation

Information rules look lighter than dismissal law or UI, but they often change behavior on margins that standard contract models take as given. Posted rights, disclosure requirements, labor-law counseling, and pay-transparency mandates can alter complaints, bargaining, search, applications, and employer wage-setting even when the formal underlying right does not change.

`@bertrandCrepon2021` already showed one version of this logic: information about labor law changed firms' beliefs and employment choices. `@cullen2024PayTransparency` broadens the object by synthesizing evidence on horizontal, vertical, and cross-firm pay transparency. The identifying variation in that literature comes from policy rollouts, disclosure mandates, and firm-level changes in pay visibility. The unit of observation varies across workers, vacancies, firms, and worker-firm matches. The observed margins include coworker wage gaps, bargaining, applications, worker beliefs, and wage-setting competition across firms. The key unobserved object is how employers redesign pay systems and job ladders after transparency arrives.

This section matters because it prevents a false dichotomy between "hard" regulation and "soft" information. Rights salience can be the first-order margin in settings where workers do not know the rule, firms overestimate legal risk, or transparency shifts outside options more than formal contract terms do. That is why Week 9 includes information as a genuine labor-market regulation rather than as an afterthought.

### Effectiveness, spillovers, inequality, and welfare

```{include} assets/tables/09-effectiveness-spillovers-and-welfare-map.md
```

Table {numref}`tbl:effectiveness-spillovers-welfare-week9` is the checklist that should follow every empirical estimate in this literature. It makes explicit that effectiveness, spillovers, inequality, and welfare are separate questions.

```{figure} assets/figures/09-regulation-spillovers-inequality-welfare.png
:name: fig-lii-w9-welfare
The direct treated margin is only one welfare input. Regulations also redistribute across covered and uncovered workers, across firms, and across time through insurance, search, prices, and fiscal incidence.
```

Figure {numref}`fig-lii-w9-welfare` is the distributional map for the second half of the lecture. It is the quickest way to show why "no effect on employment" is not the same thing as "no effect."

The welfare question changes across policy families. Dismissal protection may insure incumbent matches, preserve firm-specific capital, and compress layoff risk, but it may also reduce hiring or reallocation. Standards enforcement may raise compliance and worker protection but also shift costs into wages, prices, exit, or informality. UI may smooth consumption and improve matching, but it can also distort search or create strategic separations. Transparency may narrow discriminatory gaps or improve search, but it can also induce compression, strategic disclosure, or countervailing employer bargaining.

Different papers can therefore disagree for at least five coherent reasons.

1. They study different regulations rather than one generic "labor policy" object.
2. They operate under different enforcement regimes, so law on the books and effective treatment differ.
3. They face different uncovered margins such as informal work, temporary contracts, or untreated regions.
4. They embed different equilibrium assumptions about vacancies, spillovers, or price pass-through.
5. They adopt different welfare criteria, such as worker surplus, redistribution, insurance value, productivity, or fiscal cost.

Week 9 should make students comfortable with the possibility that a regulation can reduce turnover, compress risk, and raise welfare even if mean employment barely moves, and equally comfortable with the possibility that a regulation can look successful on the covered margin while generating costly avoidance elsewhere.

### Empirical designs and what they identify

The empirical-design section of the week should read like a map from variation to object.

Legal reform and event-study designs use sharp timing in statutes or court doctrines. The variation is policy adoption or repeal. The unit is usually the state-year, country-year, or worker-region-year cell. The observed margins are employment, wages, job flows, or productivity. The key unobserved object is the untreated institutional trend and any bundled reform package. `@autorDonohueSchwab2006` and `@autorKerrKugler2007` fit here.

Threshold and coverage-discontinuity designs use eligibility cutoffs, benefit schedules, or tenure-based rules. The variation is a statutory threshold or kink. The unit is the worker spell or claimant. The observed margins are duration, recalls, reemployment wages, and sometimes layoffs. The key unobserved object is behavior away from the cutoff and any equilibrium response outside the locally identified margin. `@lindner2020FrontLoading` is the cleanest Week 9 example because it isolates timing while leaving the broader labor-market response only partially observed.

Enforcement-shock designs use inspector assignment, inspection intensity, audit probability, or administrative capacity. The variation is enforcement exposure rather than nominal law. The unit is the firm, locality, or worker-location cell. The observed margins are compliance, wages, formality, and survival. The key unobserved object is why enforcement intensity differs across places in the first place. `@almeidaCarneiro2012` is central because it teaches that enforcement itself can be endogenous.

Information interventions use randomized or quasi-random disclosure of legal or wage information. The variation is exposure to rights information or wage visibility. The unit is the firm, worker, or vacancy. The observed margins are beliefs, complaints, bargaining, applications, and employment. The key unobserved object is what the same actors would have done with full knowledge under unchanged formal law. `@bertrandCrepon2021` is the clean randomized example; the transparency literature summarized by `@cullen2024PayTransparency` broadens the set of settings.

Equilibrium and spillover designs trace untreated-market responses. The variation is large-scale program exposure across regions or groups. The unit is the region, market, or treated-versus-untreated worker cell. The observed margins are vacancies, nonrecipient job finding, unemployment duration, and nearby labor-market outcomes. The key unobserved object is the full market counterfactual absent the policy. `@laliveLandaisZweimueller2015` is the template because it explicitly separates recipient and nonrecipient effects.

Formal-informal transition designs are essential when uncovered work is a live escape margin. The variation is often a policy threshold, benefit rule, or enforcement difference in a setting with substantial informality. The unit is the worker spell, firm, or local labor market. The observed margins are formal layoffs, recall timing, informal transitions, and benefit take-up. The key unobserved object is the value of uncovered work opportunities and strategic avoidance by firms and workers. That is the reason the Brazil UI and informality paper `@vanDoornikGerardNaritomi2023` belongs in Week 9 rather than only in a development field course.

## Research Lab

The optional 60--90 minute extension block should feel like a research workshop on implementation and equilibrium rather than a miscellaneous appendix. The bounded lab follows `Reproduce -> Diagnose -> Transfer`. The reproduction anchor is `@almeidaCarneiro2012`, where the central object is effective enforcement rather than nominal labor law. The diagnose anchor is `@laliveLandaisZweimueller2015`, where the central object is equilibrium spillovers rather than only recipient behavior. The optional extension anchor is the Brazil UI and informality paper `@vanDoornikGerardNaritomi2023`, where the uncovered margin is explicit. The lab handout lives at [labs/09-labor-regulation-enforcement-and-insurance/lab.md](labs/09-labor-regulation-enforcement-and-insurance/lab.md).

The research extension should push students to ask six questions of any Week 9 paper.

1. What regulation is actually being studied?
2. Is the key issue dismissal, standards, enforcement, insurance, or information?
3. Which side of the market is directly treated?
4. What spillover or uncovered margin is likely to matter?
5. What welfare tradeoff is the paper implicitly using?
6. What empirical channel remains latent even after the main design is executed?

This is also the right place to bridge forward. Week 10 will scale up exactly these mechanisms. UI affects vacancies and unemployment dynamics. Dismissal protection affects layoffs and recalls. Enforcement capacity affects cyclical reallocation between formal and informal sectors. Information affects search and wage competition. The aggregate-adjustment week is therefore not a topic shift; it is the next level of the same framework.

## Methods Box

Week 9 only works if the objects stay separate.

1. Regulation on the books is not the same thing as effective regulation.
2. Worker-targeted, firm-targeted, and regulator-targeted policies should not be collapsed into one treatment category.
3. Dismissal protection, labor standards, insurance, and information rules change different labor-market margins.
4. Compliance must be separated from evasion, informal adjustment, and contract redesign.
5. Direct treated-worker or treated-firm effects are not the same thing as spillovers to uncovered workers, firms, or regions.
6. Employment, wages, hours, turnover, search, formality, and prices are different outcome margins and should be named separately.
7. Every empirical result should identify the variation, unit of observation, observed margin, and key unobserved equilibrium or compliance object.
8. Disagreement across papers often reflects different regulations, enforcement regimes, uncovered margins, equilibrium assumptions, and welfare criteria rather than simple contradiction.
9. Welfare evaluation should never be reduced to a single employment coefficient.

## Reading ladder

### Ladder A. Framework and classification

- `@macleod2011GreatExpectations` for the contract-and-law framework that organizes the week.
- `@autorDonohueSchwab2006` for wrongful-discharge doctrines as a tractable dismissal-cost object.
- `@autorKerrKugler2007` for the productivity, entry, and reallocation consequences of employment protection.

### Ladder B. Enforcement, compliance, and effective regulation

- `@almeidaCarneiro2012` for the core distinction between formal law and effective enforcement in a setting with informality.
- `@bertrandCrepon2021` for rights knowledge, firm beliefs, and information as labor-market regulation.

### Ladder C. Insurance, search, and equilibrium effects

- `@laliveLandaisZweimueller2015` for market externalities of UI and why untreated workers matter.
- `@lindner2020FrontLoading` for benefit timing, behavioral response, and welfare accounting.
- `@vanDoornikGerardNaritomi2023` for UI incentives once formal and informal labor markets interact.

### Ladder D. Information, transparency, and frontier directions

- `@cullen2024PayTransparency` for information-based regulation and the wage-setting consequences of transparency.
- Return to `@macleod2011GreatExpectations` after the empirical papers to reconnect evidence to contract theory.

## Exercises / discussion prompts

1. Use Equation {eq}`eq-lii-w9-wedge` to explain how the same regulation can lower wages, raise firm costs, and still increase worker welfare.
2. Why does Equation {eq}`eq-lii-w9-effective` imply that two regions with the same labor law can have different treatment effects?
3. Compare Equation {eq}`eq-lii-w9-dismissal` and Equation {eq}`eq-lii-w9-ui`. Which one acts primarily on separations, which one on search, and where do equilibrium effects enter each?
4. Take one paper from Week 9 and name its identifying variation, unit of observation, observed margin, and key unobserved object.
5. Explain how disagreement across `@almeidaCarneiro2012`, `@laliveLandaisZweimueller2015`, and `@cullen2024PayTransparency` could arise even if all three papers are internally correct.

## Reproducibility or code lab note

The bounded Week 9 lab is intentionally local and synthetic. Students reproduce an Almeida-Carneiro style enforcement panel, diagnose the difference between effective regulation and equilibrium insurance effects, and transfer the design to synthetic UI and formality-margin data. The lab is designed to run without confidential microdata while preserving the key Week 9 objects: enforcement, spillovers, uncovered margins, and welfare tradeoffs.

## Slide companion note

The Week 9 slide deck lives at [slides/week9/09-labor-regulation-enforcement-and-insurance.tex](slides/week9/09-labor-regulation-enforcement-and-insurance.tex). It is slightly longer than a standard week because this lecture is the capstone of the policy block, but it is structured tightly around the taxonomy, implementation, equilibrium, empirical-design, and welfare questions introduced here.
