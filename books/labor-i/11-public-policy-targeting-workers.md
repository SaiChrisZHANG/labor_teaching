---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Public Policy Targeting Workers

## Learning Objectives

By the end of Week 11, students should be able to:

1. define worker-targeted policy as policy that primarily changes worker-side incentives, constraints, frictions, insurance, or investments rather than directly regulating firms;
2. map Weeks 2--10 into policy-relevant margins such as participation, hours, search, training, care allocation, mobility, and take-up;
3. distinguish statutory generosity from effective policy exposure once enrollment, knowledge, and administrative burden intervene;
4. decompose worker-policy effects into extensive and intensive labor-supply responses;
5. explain why unemployment insurance and related search policies are jointly insurance and incentive objects;
6. interpret training, childcare, disability, and retirement policies as dynamic labor-market interventions rather than one-period employment nudges;
7. state the identifying variation behind kink, bunching, randomized field-experiment, reform-event-study, judge-IV, and knowledge-exposure designs;
8. connect reduced-form policy estimates to welfare, heterogeneity, and external-validity questions;
9. explain why take-up is itself a labor-economics outcome and a bridge into Week 12 frictions;
10. use a practical researcher's checklist for evaluating worker-side policy evidence.

## Opening Orientation

The economic question for the week is cumulative. Weeks 2 through 10 built a worker-side model of labor supply, dynamic adjustment, human-capital investment, household allocation, inequality, discrimination, and mobility. Week 11 asks how public policy enters that architecture and how labor economists learn whether the policy changed worker behavior for reasons of incentives, insurance, or frictions [@eissaLiebman1996; @chettyFriedmanSaez2013; @kolsrudLandaisNilssonSpinnewijn2018].

:::{admonition} Core materials
:class: tip
- worker-targeted policies act through incentives, constraints, frictions, insurance, or investment
- design choice must match the behavioral margin and institutional setting
- eligibility is not treatment if knowledge, filing, or adjudication screens who actually receives the policy
- policy evaluation is incomplete without dynamics, heterogeneity, and welfare interpretation
:::

## Bridge

Week 11 is the worker-side policy capstone for Labor I. It should not feel like a generic public-finance detour. The point is to reinterpret the semester's earlier objects as policy margins. Week 2 gave us nonlinear budget sets and participation choices. Week 3 added timing, duration, and continuation values. Week 4 taught us to see training and skill policy as investment policy. Week 6 showed that childcare, leave, and care costs alter household time allocation rather than only one person's hours. Week 10 made clear that search support and mobility assistance may relax place, credit, and information constraints rather than merely change a tax wedge. Week 12 will ask what happens when these responses are filtered through salience, information, and optimization frictions. Week 11 is therefore the point where the frictionless benchmark meets actual policy delivery.

Worker-targeted policy refers to policies that primarily alter worker-side incentives, constraints, insurance, information, or investments. Examples include in-work tax credits, unemployment insurance, search assistance, training, childcare support, disability-insurance adjudication, retirement earnings tests, and administrative simplification. Firm-targeted regulation, wage-setting institutions, vacancy creation, and labor-demand incidence are not absent from the story, but they become central in Labor II rather than here.

```{figure} assets/figures/11-policy-margins-framework.png
:name: fig-week11-framework
Week 11 maps worker-targeted policies into five transmission channels and six worker-side margins. The empirical problem is to learn which channel actually moved the observed labor outcome.
```

Figure {numref}`fig-week11-framework` is the week's conceptual map. A policy can move participation through a tax schedule, through childcare costs, through search requirements, through benefit timing, or through information about program availability. Those are not the same object. A null employment response to a policy may reflect weak incentives, low take-up, delayed dynamic adjustment, or measurement on the wrong behavioral margin. That is why this lecture synthesizes theory, evidence, and identification instead of just listing program results.


:::{admonition} Optional Extension Block
:class: note
- administrative burden and take-up as frontier design objects in the spirit of [@linosProhofskyRameshRothsteinUnrath2022]
- front-loaded unemployment benefits and dynamic sufficient-statistics logic in the spirit of [@lindnerReizer2020; @kolsrudLandaisNilssonSpinnewijn2018]
- disability, household insurance, and labor-supply spillovers in the spirit of [@autorKostolMogstadSetzler2019]
:::

## Field Core

### A unified worker-policy framework

The cleanest starting point is a policy-adjusted worker choice problem. Let {math}`h_t` denote hours, {math}`a_t` care or search intensity, and {math}`e_t` effective enrollment in the program. Then a compact budget object is

```{math}
:label: eq-week11-budget
c_t = y_t + w_t h_t - T_t(w_t h_t, z_t) + e_t B_t(w_t h_t, z_t) - p_t^a a_t .
```

Equation {eq}`eq-week11-budget` is intentionally broad. Taxes and transfers change the payoff to work. Effective enrollment {math}`e_t` reminds us that statutory benefits matter only when the worker knows about the program, files, qualifies, or is adjudicated in. Childcare prices, transport costs, and search effort appear as worker-side costs. Training policy may raise the future wage path rather than current disposable income. The labor question is therefore not "does the policy increase work?" but "which part of the choice set or continuation value moved, for which workers, and through which margin?"

```{include} assets/tables/11-policy-toolkit-map.md
```

Table {numref}`tbl:week11-policy-toolkit` organizes the policy families around worker-side margins. That table is useful because it prevents three common errors. First, it prevents in-work subsidies and training policies from being treated as the same object. Second, it shows that unemployment insurance is not only about duration; it is also about reemployment wages, take-up, and consumption smoothing. Third, it forces the lecture to remain labor-focused. The target outcomes are participation, hours, search, earnings, mobility, and household allocation.

### Extensive and intensive margins under in-work support

The EITC remains the canonical Week 11 object because it is a nonlinear policy schedule that transparently maps back to Week 2 static labor supply and Week 3 dynamic adjustment [@eissaLiebman1996; @eissaHoynes2004; @bastian2020]. The central decomposition is

```{math}
:label: eq-week11-decomp
\frac{d \mathbb{E}[w h]}{d \theta}
= \bar{h} \frac{d \Pr(h>0)}{d \theta}
+ \Pr(h>0) \frac{d \mathbb{E}[h \mid h>0]}{d \theta},
```

where {math}`\theta` is a policy parameter such as a phase-in rate or credit level. Equation {eq}`eq-week11-decomp` separates the extensive participation response from the intensive hours response. In-work subsidies often raise the participation margin strongly for eligible groups while generating weaker or offsetting hours responses among already-employed workers because the phase-in, plateau, and phase-out regions imply different effective returns to earnings.

```{figure} assets/figures/11-tax-credit-budget-set.png
:name: fig-week11-budget-set
An in-work credit rotates the budget set differently across the phase-in, plateau, and phase-out regions. The same policy can therefore increase entry into work while generating heterogeneous hours responses among workers already in employment.
```

Figure {numref}`fig-week11-budget-set` is why the Week 2 toolkit matters for policy. Eissa and Liebman identify a strong participation response for single mothers after EITC expansions, while Eissa and Hoynes show that married-couple responses require careful attention to secondary-earner incentives and household incidence [@eissaLiebman1996; @eissaHoynes2004]. Bastian shows that the rise of working mothers is partly about the EITC changing labor-force attachment, not only annual tax liabilities [@bastian2020]. None of those findings can be interpreted correctly without distinguishing extensive from intensive margins as in Equation {eq}`eq-week11-decomp`.

Chetty, Friedman, and Saez add the crucial Week 11 twist: even when the statutory schedule is common, effective treatment varies because knowledge differs across neighborhoods [@chettyFriedmanSaez2013]. This shifts the interpretation from "workers facing the same schedule all understand it" to "policy exposure is mediated by information, filing support, and local social learning." That observation is a direct bridge to the take-up section below and to Week 12.

### Unemployment insurance, benefit timing, and search assistance

Unemployment insurance is the cleanest example of a worker policy that is simultaneously an insurance instrument and an incentive instrument. Let {math}`U_t` denote the continuation value of nonemployment and {math}`W_{t+1}` the value of work after a match. A compact timing object is

```{math}
:label: eq-week11-ui
U_t(b_t) = u(c_t, \ell_t) + \beta \left[\lambda_t(b_t) W_{t+1} + \big(1-\lambda_t(b_t)\big) U_{t+1}(b_{t+1})\right],
\qquad
\frac{\partial \lambda_t}{\partial b_t} < 0 .
```

Equation {eq}`eq-week11-ui` says why "does UI reduce work?" is the wrong first question. Benefit generosity and timing change current consumption, search intensity, job acceptance, and possibly the quality of the eventual match. Kolsrud, Landais, Nilsson, and Spinnewijn use this logic to show that the timing of benefits is itself a design variable, because liquidity needs are high early in unemployment while search distortions evolve over the spell [@kolsrudLandaisNilssonSpinnewijn2018]. Lindner and Reizer similarly study front-loading, which moves the same total support across time rather than simply making benefits larger everywhere [@lindnerReizer2020].

The labor evaluation problem therefore has at least four margins: nonemployment duration, job-finding, reemployment wages, and consumption smoothing. Search assistance belongs next to UI rather than in a separate policy silo because it can offset or complement the incentive effects of cash benefits. Wheeler, Garlick, Johnson, Shaw, and Gargano show how job-readiness interventions can work through information, application quality, and search efficiency rather than through direct wage subsidies [@wheelerGarlickJohnsonShawGargano2022]. Verho, Hamalainen, and Kanninen similarly remind us that removing welfare traps is partly about the dynamic interaction between benefits and participation incentives, not only about a one-period replacement rate [@verhoHamalainenKanninen2022].

### Training, job readiness, and dynamic earnings paths

Training policy should be taught as a human-capital intervention, not as a short-run placement contest. Week 4 emphasized that skill investments change future wages, occupational ladders, and the value of search. Week 11 carries that logic into program evaluation. A low immediate employment effect is not decisive if the intervention improves information, occupational upgrading, certification, or later earnings growth. Conversely, a short-run placement gain may be misleading if it pushes workers into low-quality matches that do not persist.

The Week 11 discipline is to specify the behavioral object. Is the program raising job-finding now, increasing future wage growth, changing the set of occupations a worker can access, or altering migration willingness because the worker becomes employable in new places? Wheeler et al. are especially useful here because the intervention is visibly about readiness and application quality, which makes it easier to connect program content to the margin being moved [@wheelerGarlickJohnsonShawGargano2022]. The empirical lesson is that training policies often need horizon-specific outcomes: immediate employment, medium-run earnings, and persistence.

### Family-support, care prices, and household incidence

Week 6 established that household labor supply is a joint allocation problem. Family-support and care policies therefore change labor-market behavior by altering the shadow price of time inside the household, not simply by moving one adult's wage. In the worker-policy framework of Equation {eq}`eq-week11-budget`, childcare subsidies or leave policy reduce the effective cost term {math}`p_t^a a_t` for market work, especially for secondary earners or parents facing tight care constraints.

The labor-economics takeaway is twofold. First, participation effects can be large even when observed wage elasticities are modest because care costs operate as participation wedges. Second, incidence may run through bargaining and substitution inside the household. A policy that raises maternal employment can also change partner hours, home production, fertility timing, and the demand for market care. That is why family-support policy belongs in Week 11 but should not duplicate Week 6. The point here is to show how household structure mediates policy incidence and why reduced-form estimates should state the family margin they identify [@blundellPistaferriSaportaEksten2016].

### Disability and retirement incentives

Disability-insurance and retirement-policy research force Week 11 to be explicit about dynamic incentives, selection, and local treatment effects. Disability receipt changes labor supply, consumption insurance, spousal labor supply, and the value of reapplying or appealing. Retirement rules and earnings tests similarly alter exit timing rather than only current hours.

French and Song use examiner assignment to identify the effect of DI receipt on labor supply, showing why administrative assignment can be a labor-economics instrument rather than a legal detail [@frenchSong2014]. Autor, Kostol, Mogstad, and Setzler push the logic further by showing that disability benefits provide household insurance and shift family labor supply, which means welfare analysis cannot be reduced to the recipient's own employment response [@autorKostolMogstadSetzler2019]. Manoli and Weber show how retirement incentives can be read through nonlinear schedules and bunching-style logic, especially when benefit rules create salient thresholds [@manoliWeber2016].

The unifying Week 11 lesson is that the observed receipt margin often combines adjudication, persistence, and dynamic incentives. That is why judge-IV and threshold designs are so prominent in this literature. The policy object is not only the cash payment. It is also the assignment process that determines who gets treated.

### Take-up, salience, and administrative burden

Take-up is one of the core sections of the chapter because it converts statutory policy into effective exposure. A simple take-up condition is

```{math}
:label: eq-week11-takeup
D_i = \mathbf{1}\left\{\mathbb{E}_i[B_i \mid \mathcal{I}_i] - \kappa_i - \phi_i - s_i > 0\right\},
```

where {math}`\mathcal{I}_i` is information, {math}`\kappa_i` is hassle or filing cost, {math}`\phi_i` is administrative burden, and {math}`s_i` is stigma or psychic cost. Equation {eq}`eq-week11-takeup` matters because it turns nonenrollment into a labor object rather than a nuisance residual. A worker may be eligible but uninformed, informed but unconvinced the gain is worth the burden, or enrolled but unable to claim the full benefit value.

```{figure} assets/figures/11-takeup-salience-funnel.png
:name: fig-week11-takeup
Program reach contracts at each step from eligibility to full-value receipt. The relevant treatment intensity is therefore not the statute alone but the entire delivery funnel.
```

Figure {numref}`fig-week11-takeup` clarifies why null policy estimates can be deeply misleading. If few eligible workers understand, claim, or keep the benefit, then an average earnings or employment estimate combines structural responsiveness with a weak first stage in delivery. Chetty, Friedman, and Saez show that local knowledge conditions EITC responses [@chettyFriedmanSaez2013]. Linos, Prohofsky, Ramesh, Rothstein, and Unrath show experimentally that nudges and simplified communication can increase EITC take-up, which means delivery design changes treatment exposure without changing the statutory schedule [@linosProhofskyRameshRothsteinUnrath2022]. This is the direct conceptual bridge to Week 12: optimization frictions and information frictions shape labor-supply responses by changing whether workers perceive and can act on the policy at all.

### Empirical design: what do the main designs identify?

Week 11 requires unusual design discipline because policies differ so much in margin and institution. A useful generic estimand is the Wald object

```{math}
:label: eq-week11-iv
\tau^{IV} = \frac{\operatorname{Cov}(Z_i, Y_i)}{\operatorname{Cov}(Z_i, D_i)},
```

where {math}`Z_i` may be randomized encouragement, judge stringency, or administrative assignment and {math}`D_i` is actual receipt or take-up. Equation {eq}`eq-week11-iv` is not the answer to every policy question; it is a reminder that identification depends on the source of quasi-random variation.

```{include} assets/tables/11-identification-map.md
```

Table {numref}`tbl:week11-identification` is the empirical spine for this section. Kink and bunching designs are natural when the policy creates clear nonlinear schedules, as with tax credits, retirement earnings tests, or benefit thresholds [@saez2010; @manoliWeber2016]. Randomized field experiments and encouragement designs are well matched to take-up nudges, search help, or job-readiness interventions because the treatment is the policy as delivered rather than an abstract schedule [@linosProhofskyRameshRothsteinUnrath2022; @wheelerGarlickJohnsonShawGargano2022]. Reform-based event studies and difference-in-differences are natural for EITC expansions, UI redesigns, or welfare reforms when exposure varies systematically across places or groups [@eissaLiebman1996; @bastian2020; @verhoHamalainenKanninen2022]. Judge or examiner assignment IV fits disability-insurance receipt when adjudication leniency creates plausibly exogenous variation in receipt [@frenchSong2014].

Difference-in-knowledge or exposure designs are especially important for Week 11 because they sit between policy statutes and worker behavior. Chetty, Friedman, and Saez show that neighborhood knowledge can reveal where the EITC is behaviorally salient [@chettyFriedmanSaez2013]. That design does not identify a generic tax elasticity. It identifies how effective exposure varies when social learning differs across local environments. The design choice must therefore match the institutional channel. If the policy margin is knowledge, we need variation in knowledge. If the margin is timing, we need variation in timing. If the margin is receipt conditional on adjudication, we need variation in adjudication.

```{figure} assets/figures/11-policy-design-toolkit.png
:name: fig-week11-design
Designs differ in how naturally they identify participation, hours, search, take-up, timing, and welfare margins. Week 11 evidence is persuasive only when the identifying variation matches the policy channel.
```

### Welfare and policy-design interpretation

Labor economists care about more than employment effects because worker-targeted policies trade off insurance, redistribution, dynamic earnings, delivery quality, and incentive cost. A compact sufficient-statistics-style welfare object is

```{math}
:label: eq-week11-welfare
\frac{dW}{d\theta}
=
\underbrace{\sum_i \omega_i \frac{\partial c_i}{\partial \theta}}_{\text{insurance and redistribution}}
- \underbrace{\lambda \sum_i \frac{\partial y_i}{\partial \theta}}_{\text{fiscal incentive cost}}
+ \underbrace{\sum_i \eta_i \frac{\partial D_i}{\partial \theta}}_{\text{delivery and take-up gain}} .
```

Equation {eq}`eq-week11-welfare` keeps three Week 11 ideas in one place. First, consumption and insurance matter, not just employment. Second, incentive costs depend on which labor margin adjusts. Third, delivery improvements that raise take-up can generate welfare gains even when the statutory schedule is unchanged. Chetty's friction framework is useful here because optimization frictions imply that observed labor-supply elasticities may understate responses to well-salient policies while overstating the welfare case for leaving delivery complex [@chetty2012].

```{figure} assets/figures/11-insurance-incentive-frontier.png
:name: fig-week11-frontier
Worker-policy design is a frontier problem, not a one-dimensional generosity problem. Delivery reform, front-loading, and search assistance can shift the insurance-distortion trade-off without simply scaling benefits up or down.
```

Figure {numref}`fig-week11-frontier` is a teaching device for policy ranking. Standard UI, front-loaded UI, search assistance, and take-up simplification need not sit on the same point in policy space. The right ranking depends on who is liquidity constrained, who is information constrained, which margin moves, and whether the intervention changes future opportunities as well as current labor supply. This is also where external validity enters. A policy estimated in a high-knowledge environment may behave differently in a low-knowledge one. A UI design estimated in a system with strong search assistance may not transport cleanly to a weaker administrative setting.

### Capstone synthesis: a researcher's checklist

Week 11 should end as a design checklist rather than a loose summary.

1. What is the policy object: a schedule, a timing rule, an administrative process, or an information intervention?
2. Which worker-side margin is supposed to move: participation, hours, search, training, household allocation, mobility, or take-up?
3. Which earlier Labor I tools interpret that margin: Weeks 2 and 3 for labor supply and dynamics, Week 4 for investment, Week 6 for households, Week 10 for mobility?
4. What frictions stand between statutory policy and effective exposure?
5. What identifying variation isolates the relevant channel?
6. Which outcomes are contemporaneous and which are dynamic?
7. What heterogeneity matters for interpretation: liquidity, family structure, health, prior filing, or local knowledge?
8. Can the evidence support a welfare claim, or only a reduced-form statement about one margin?

Those questions also define the bridge to Week 12. If effective exposure depends on knowledge, attention, hassle, and salience, then worker behavior cannot be evaluated with frictionless labor-supply logic alone. Week 11 therefore closes the first part of Labor I by showing that policy evaluation requires both the classical benchmark and a serious account of frictions.

## Research Lab

The bounded Week 11 lab follows the course's standard `Reproduce -> Diagnose -> Transfer` workflow. The reproduction step uses a deterministic synthetic neighborhood panel in the spirit of [@chettyFriedmanSaez2013] to show that higher-knowledge places display stronger earnings, employment, and take-up responses after an EITC-style expansion. The diagnostic step asks students to explain why the key object is effective policy exposure rather than the statutory schedule alone. The transfer step then moves to a synthetic take-up experiment in the spirit of [@linosProhofskyRameshRothsteinUnrath2022], where reminder letters and simplified notices change the delivery funnel without changing the benefit schedule.

The local path is deliberately bounded. Students do not need tax microdata, IRS filing records, or state UI administrative files to learn the research logic of Week 11. The optional challenge block uses [@lindnerReizer2020] conceptually by asking how front-loaded benefits would shift continuation values in Equation {eq}`eq-week11-ui`. Optional frontier extensions connect to [@frenchSong2014], [@autorKostolMogstadSetzler2019], [@manoliWeber2016], [@wheelerGarlickJohnsonShawGargano2022], and [@verhoHamalainenKanninen2022].

The key lab lesson is interpretive. When the treatment is delivered through filing assistance, reminders, or administrative simplification, the reduced-form estimate is partly about program design and partly about labor-supply responsiveness. That is exactly the bridge from Week 11 to Week 12.

```{include} assets/tables/11-research-frontier-map.md
```

Table {numref}`tbl:week11-frontier` keeps the frontier questions visible. The most important are whether small treatment effects reflect weak incentives or weak delivery, when partial-equilibrium evidence is enough for a policy claim, and how dynamic gains should be aggregated into welfare when search, earnings, insurance, and household outcomes move together.

## Methods Box

### Methods Box 1: design must match the policy margin

Equation {eq}`eq-week11-budget` tells us what the policy changes; Table {numref}`tbl:week11-identification` tells us how the field learns about it. Bunching is persuasive for local schedule incentives but weak for broad delivery problems. Judge IV is persuasive for DI receipt among compliers but local by construction. Randomized take-up nudges identify delivered interventions, not generic long-run equilibrium effects. Reform event studies identify regime changes if exposure is well measured and parallel-trends logic is credible. The design question is therefore inseparable from the behavioral question.

### Methods Box 2: effective policy exposure versus statutory generosity

Equation {eq}`eq-week11-takeup` and Figure {numref}`fig-week11-takeup` make a strong methodological point: labor economists should often measure the first stage between statutory policy and actual exposure. Knowledge, administrative burden, and adjudication can attenuate or reallocate treatment. This is why Chetty, Friedman, and Saez, and Linos et al., are central Week 11 papers rather than side notes [@chettyFriedmanSaez2013; @linosProhofskyRameshRothsteinUnrath2022]. They show that delivery technology is part of the labor policy itself.

## Reading Ladder And References

### Canonical worker-policy papers

- Eissa and Liebman on EITC participation responses [@eissaLiebman1996]
- Eissa and Hoynes on family labor-supply incidence under the EITC [@eissaHoynes2004]
- Kolsrud, Landais, Nilsson, and Spinnewijn on the timing of UI benefits [@kolsrudLandaisNilssonSpinnewijn2018]
- French and Song on disability-insurance receipt and labor supply [@frenchSong2014]
- Manoli and Weber on retirement incentives and nonlinear schedule responses [@manoliWeber2016]

### Design-intensive empirical studies

- Chetty, Friedman, and Saez on neighborhood knowledge and effective EITC exposure [@chettyFriedmanSaez2013]
- Lindner and Reizer on front-loaded unemployment benefits [@lindnerReizer2020]
- Linos, Prohofsky, Ramesh, Rothstein, and Unrath on field experiments that raise EITC take-up [@linosProhofskyRameshRothsteinUnrath2022]
- Wheeler, Garlick, Johnson, Shaw, and Gargano on job-readiness training and search outcomes [@wheelerGarlickJohnsonShawGargano2022]
- Verho, Hamalainen, and Kanninen on removing welfare traps in the Finnish basic income experiment [@verhoHamalainenKanninen2022]

### Frontier papers on take-up, heterogeneity, and design interpretation

- Chetty on optimization frictions and elasticities [@chetty2012]
- Autor, Kostol, Mogstad, and Setzler on disability benefits, household insurance, and spillovers [@autorKostolMogstadSetzler2019]
- Bastian on the rise of working mothers and historical EITC incidence [@bastian2020]

## Exercises And Discussion Prompts

1. In Equation {eq}`eq-week11-budget`, which terms would change under an EITC expansion, a childcare subsidy, and a search-assistance intervention?
2. Why does Equation {eq}`eq-week11-decomp` imply that one program can raise participation but reduce hours for some already-employed workers?
3. In Equation {eq}`eq-week11-ui`, what kind of policy change would move current consumption without proportionally changing long-run search incentives?
4. Why is Equation {eq}`eq-week11-takeup` a labor-economics object rather than merely an administrative complication?
5. What identifying variation does Equation {eq}`eq-week11-iv` represent in a disability-insurance judge-IV design?
6. Which design in Table {numref}`tbl:week11-identification` would you trust most for an earnings-test threshold, and why?
7. How would you explain the difference between statutory generosity and effective exposure to a student who only looked at a tax schedule?
8. Why can an experimental take-up nudge have strong policy value even if it barely changes the underlying labor-supply elasticity?
9. What would make a short-run training estimate a poor guide to long-run worker welfare?
10. Which Week 10 mobility frictions can be relaxed by worker-side policy without changing firms' wage-setting directly?
11. How does the Week 11 researcher's checklist change the way you would read a headline result that "policy X increased employment by 2 percentage points"?

## Reproducibility And Code Lab Note

The Week 11 lab uses a bounded local workflow rather than administrative tax or UI microdata. Students first reproduce a synthetic effective-exposure factbook in the spirit of [@chettyFriedmanSaez2013], then diagnose the delivery channel, and finally transfer the workflow to a synthetic take-up field experiment in the spirit of [@linosProhofskyRameshRothsteinUnrath2022]. The student-facing workflow is documented in [labs/11-public-policy-targeting-workers/lab.md](labs/11-public-policy-targeting-workers/lab.md).

## Slide Companion Note

The Week 11 deck should open as the worker-side policy capstone, map Weeks 2--10 into policy margins, then move through a unified framework, EITC and in-work support, UI timing and search assistance, training, family-support policy, disability and retirement incentives, take-up and administrative burden, the empirical design toolkit, welfare interpretation, and a research checklist that points directly to Week 12 frictions. The canonical source is [slides/week11/11-public-policy-targeting-workers.tex](slides/week11/11-public-policy-targeting-workers.tex).

## Bridge Forward

Use this closing bridge to carry the module's labor object, mechanism, and evidence into the next course step or research-design exercise.
