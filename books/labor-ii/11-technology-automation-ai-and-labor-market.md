---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Technology, Automation, AI, and Labor Market

## Learning objectives

By the end of Week 11, students should be able to:

1. distinguish automation, augmentation, new-task creation, and organizational redesign as separate channels of technological change;
2. explain why technology affects labor supply, labor demand, and market-level equilibrium at the same time;
3. use a task-based framework to organize historical ICT, robot, and contemporary AI evidence;
4. separate direct displacement from indirect productivity, reinstatement, and reallocation effects;
5. distinguish tasks from occupations, exposure from adoption, and within-firm effects from local-labor-market equilibrium effects;
6. evaluate worker adjustment through learning, retraining, occupational switching, and skill obsolescence;
7. interpret empirical designs by naming the identifying variation, unit of observation, observed margin, and key equilibrium margin left offstage;
8. connect Week 10 aggregate adjustment to Week 11 structural adjustment and bridge forward to Week 12 trade and offshoring.

The economic question for Week 11 is explicit: how do technology, automation, and AI reshape work through worker adaptation, firm labor demand, and market-level reallocation?

## Bridge

Week 10 studied cyclical adjustment. The core objects were unemployment, vacancies, separations, job-to-job mobility, wages, and match quality. Week 11 keeps those labor-market objects onstage but changes the shock. Instead of a business-cycle disturbance, the shock now comes from technology adoption, automation, software, robots, and AI. The lecture therefore remains a labor-economics week rather than drifting into a general technology survey.

The first discipline for the week is to organize technology around three linked objects.

1. Supply-side adjustment: worker learning, retraining, search/application technology, occupational switching, and skill obsolescence.
2. Demand-side adjustment: task substitution, task complementarity, automation, augmentation, hiring redesign, and within-firm labor demand.
3. Market-level adjustment: local labor-market reallocation, wage and employment incidence, labor-share changes, concentration, and cross-place equilibrium spillovers.

```{include} assets/tables/11-technology-margins-map.md
```

Table {numref}`tbl:technology-margins-map` is the opening map for the week. It keeps the lecture centered on labor-market margins rather than collapsing robots, ICT, and AI into one undifferentiated shock.

```{figure} assets/figures/11-supply-demand-market-effects.png
:name: fig-lii-w11-supply-demand-market
Week 11 links worker adaptation, firm-side labor demand, and market-level equilibrium. The same technology can change all three margins at once, so neither pure labor-demand language nor pure “AI future of work” language is enough.
```

Figure {numref}`fig-lii-w11-supply-demand-market` previews the lecture structure. The important move is to treat technology as a shock that propagates through feedback loops rather than only through a single firm labor-demand curve.

:::{admonition} Core Material
:class: tip
- technology shocks propagate through worker adjustment, firm labor demand, and market-level reallocation
- tasks, occupations, exposure, and adoption are distinct objects
- displacement, augmentation, new-task creation, and organizational redesign can coexist
- within-firm evidence and local-labor-market evidence identify different margins
- AI evidence should be kept analytically distinct from earlier ICT and robot evidence unless the object is explicit
:::

:::{admonition} Optional Extension Block
:class: note
- frontier questions on AI adoption, organizational complements, and transition policy are surfaced later in the chapter under `Research frontier and extension block`
:::

## Field Core

### Technology as a labor-market shock

It helps to classify technologies before classifying effects. The relevant categories for Labor II are ICT and software, industrial robots, prediction/classification systems, generative AI tools, and broader general-purpose technologies [@autor2015WhyStillManyJobs; @autor2022LaborMarketImpactsTechChange]. These technologies differ in capital embodiment, diffusion speed, observability, and which margins are directly measurable, but they share one labor-economics feature: they change the mapping from tasks to workers, firms, and markets.

The same technology can generate displacement, augmentation, output expansion, new tasks, and organizational redesign at the same time [@acemogluRestrepo2019AutomationNewTasks]. That is why this week must keep explicit distinctions in view.

1. Tasks are units of activity; occupations are bundles of tasks.
2. Exposure is a predicted susceptibility measure; adoption is realized technology use.
3. Within-firm evidence captures partial-equilibrium labor-demand responses more cleanly than market-level equilibrium incidence.
4. Historical ICT and robot evidence should not be read as if it were already evidence about very recent AI.

```{figure} assets/figures/11-task-based-technology-framework.png
:name: fig-lii-w11-task-framework
A task-based framework turns technology into a labor-market mapping problem. Technologies shift the boundary between tasks done by workers, tasks automated by capital or software, and tasks newly created or reorganized inside firms.
```

Figure {numref}`fig-lii-w11-task-framework` is the conceptual anchor. Labor outcomes depend on which tasks move across the automation boundary, which tasks become more productive when paired with workers, and which tasks are newly created.

### Formal core: tasks, automation boundaries, and worker adjustment

The smallest aggregate task-based production object is

```{math}
:label: eq:w11-task-aggregator
Y_t = \left[\int_0^1 y_t(i)^{\frac{\sigma-1}{\sigma}} \, di\right]^{\frac{\sigma}{\sigma-1}},
```

where task {math}`i` contributes to final output and {math}`\sigma` governs substitution across tasks [@acemogluAutor2011SkillsTasksTechnologies]. This object is useful because it makes technological change a statement about task productivity, task assignment, and the elasticity with which firms can reorganize activity across tasks.

Let labor complete task {math}`i` with unit cost {math}`w_t / a_t(i)` and capital, robots, or AI systems complete task {math}`i` with unit cost {math}`c_t^{T} / b_t(i)`. Then the automation boundary {math}`i_t^\ast` solves

```{math}
:label: eq:w11-automation-boundary
\frac{w_t}{a_t(i_t^\ast)} = \frac{c_t^{T}}{b_t(i_t^\ast)},
\qquad
\mathcal{A}_t = \left\{i : \frac{c_t^{T}}{b_t(i)} \le \frac{w_t}{a_t(i)} \right\}.
```

Equation {eq}`eq:w11-automation-boundary` is the task-allocation object for the week. A fall in technology cost {math}`c_t^{T}` or a rise in machine productivity {math}`b_t(i)` expands the set of automated tasks {math}`\mathcal{A}_t`, but that does not by itself tell us whether total labor demand rises or falls. That depends on productivity gains, output expansion, and whether new tasks or complementary tasks appear elsewhere in the system [@acemogluRestrepo2019AutomationNewTasks].

The lecture therefore needs a decomposition that separates direct displacement from indirect offsets:

```{math}
:label: eq:w11-displacement-decomp
\Delta \log L_t =
\underbrace{\Delta \log L_t^{disp}}_{\text{direct displacement}}
+
\underbrace{\Delta \log L_t^{prod}}_{\text{productivity and output expansion}}
+
\underbrace{\Delta \log L_t^{new}}_{\text{reinstatement and new tasks}}.
```

Equation {eq}`eq:w11-displacement-decomp` is deliberately schematic. It does not claim those terms are directly observed in every paper. It clarifies the empirical question students should ask whenever they see a technology coefficient: which part looks like direct substitution, which part looks like output expansion, and which part looks like new-task or reinstatement effects?

Supply-side adjustment belongs in the formal core too. Let worker human capital evolve according to

```{math}
:label: eq:w11-human-capital
H_{t+1} = (1-\delta_t)H_t + I_t,
```

where {math}`I_t` is new investment in skills and {math}`\delta_t` is technology-dependent obsolescence. Rapid technical change raises {math}`\delta_t` for some workers and lowers the value of old experience even when it raises productivity for others [@bartelSicherman1998TechnologicalChangeSkillAcquisition; @demingNoray2020EarningsDynamicsChangingJobSkills]. This is the supply-side object that keeps skill acquisition and skill obsolescence in the same frame.

The reduced-form exposure equation that organizes much of the empirical literature is

```{math}
:label: eq:w11-exposure-rf
\Delta Y_{mt} = \beta \, TechExposure_{mt} + X_{mt}'\Gamma + \varepsilon_{mt},
```

where {math}`m` may be a commuting zone, occupation, industry, firm, or worker-time cell. Equation {eq}`eq:w11-exposure-rf` is intentionally broad because the literature uses different units. The crucial question is whether {math}`TechExposure_{mt}` measures predicted exposure or realized adoption, and whether {math}`\Delta Y_{mt}` is a demand-side, supply-side, or market-level outcome.

### Historical perspective: why labor demand did not simply disappear

The long-run perspective matters because fears of labor-saving technology predate AI by centuries. Autor's central argument is that aggregate labor demand did not collapse because automation eliminated some tasks while raising demand for other tasks, new goods, and complementary capabilities [@autor2015WhyStillManyJobs]. Acemoglu and Restrepo formalize the same point with displacement and reinstatement: automation can reduce demand for labor in automated tasks even as new tasks later pull labor back into production [@acemogluRestrepo2019AutomationNewTasks].

The historical lesson is not that technology is always benign. It is that labor-market effects are mediated by task structure, product demand, institutions, and the speed of worker adjustment. Acemoglu and Autor's task framework turned this into a precise distinction between occupations and the tasks inside them [@acemogluAutor2011SkillsTasksTechnologies]. Michaels, Natraj, and Van Reenen then show how ICT adoption was associated with rising demand for high-skill tasks and declining routine middle-skill work across countries [@michaelsNatrajVanReenen2014ICTPolarizedSkillDemand].

```{include} assets/tables/11-evidence-by-margin-and-era.md
```

Table {numref}`tbl:evidence-margin-era` keeps the historical, robot, and AI eras comparable by margin rather than by hype cycle. That is a better discipline than treating all technology episodes as identical.

```{figure} assets/figures/11-historical-global-technology-evidence.png
:name: fig-lii-w11-historical-global
Historical and global evidence should be read as a sequence of technology waves, design choices, and institutional environments. The relevant comparison is not “old technology versus AI” in the abstract, but which margins are observed in each era and setting.
```

### Demand-side evidence: robots, ICT, AI adoption, and vacancies

Demand-side evidence asks how technology changes hiring, employment, occupational mix, wage bills, and vacancy content inside firms and across local labor markets. The most important discipline is to distinguish direct substitution inside exposed tasks from equilibrium effects operating through productivity, output, entry, and reallocation.

Acemoglu and Restrepo's robot paper uses differential industry robot adoption mapped into local labor-market exposure across U.S. commuting zones [@acemogluRestrepo2020RobotsJobs]. The identifying variation is shift-share exposure. The unit of observation is the commuting-zone-by-period cell. The observed margins are employment-to-population ratios and wages. The key offstage equilibrium margin is broader national product-demand and price adjustment, which the local design does not fully recover. This is the canonical market-level displacement benchmark.

Graetz and Michaels study industrial robots in a seventeen-country industry panel [@graetzMichaels2018RobotsWork]. Their identifying variation comes from cross-country, cross-industry robot penetration over time. The unit is industry-country-year. The observed margins are productivity, hours, and wage-bill components. The offstage margin is worker-level reallocation inside countries. The design is strongest for comparative broad patterns, not for within-market worker transitions.

Contemporary AI evidence often sits closer to the firm and vacancy margin. Acemoglu, Autor, Hazell, and Restrepo use online vacancies to measure how AI exposure maps into hiring intentions and skill demand [@acemogluAutorHazellRestrepo2020AIJobsVacancies]. The identifying variation comes from exposure across occupations and local labor markets. The unit is a vacancy or posting cell. The observed margin is job requirements and vacancy content, not realized employment. That distinction matters because postings tell us what firms seek, not whether staffing or wages ultimately change.

### Worker adaptation and labor supply: learning, obsolescence, and search

Week 11 should not treat worker adjustment as a side note. Bartel and Sicherman show that technological change increases the return to skill acquisition and can alter training patterns for young workers [@bartelSicherman1998TechnologicalChangeSkillAcquisition]. The identifying variation in that literature comes from industry or workplace technological change. The unit is typically the worker or worker-job match. The observed margins are training or earnings trajectories. The offstage margin is the longer-run general-equilibrium diffusion of the technology itself.

Deming and Noray make the obsolescence margin concrete by showing that workers in fast-changing STEM occupations experience steep early-career rewards but faster depreciation of accumulated job-specific knowledge [@demingNoray2020EarningsDynamicsChangingJobSkills]. The unit is the worker-career spell. The observed margin is earnings dynamics by occupational technological intensity. The key distinction is between skill acquisition and skill obsolescence: the same environment can raise the payoff to learning and shorten the half-life of old expertise at the same time.

Generative AI sharpens the supply-side question because it may change onboarding, supervision, and who can perform high-value tasks soon after entry. Brynjolfsson, Li, and Raymond study worker productivity under generative AI assistance [@brynjolfssonLiRaymond2025GenerativeAIWork]. The identifying variation comes from tool access inside a firm setting. The unit is worker-task or worker-shift output. The observed margin is productivity, especially heterogeneity by prior experience. The offstage margin is market-level wage incidence and longer-run job redesign. This is why worker productivity is not the same object as worker welfare.

AI may also change labor supply through application and search technology, but that literature is still thinner than the displacement and vacancy literature. That should be stated plainly. The frontier question is whether AI-assisted job search improves matching quality, changes search intensity, or simply redistributes who wins search tournaments.

### Market-level equilibrium and distribution: reallocation, incidence, and labor share

Once supply and demand interact, technology becomes a market-level incidence problem. Acemoglu and Restrepo's local robot design is again helpful because it captures wage and employment incidence across places rather than only inside firms [@acemogluRestrepo2020RobotsJobs]. Dauth, Findeisen, Suedekum, and Woessner show that the German response to robots combined manufacturing losses with offsets elsewhere in the economy, making reallocation central to the interpretation [@dauthFindeisenSuedekumWoessner2021AdjustmentRobots]. The identifying variation is again exposure, but the institutional environment differs and so does the equilibrium adjustment path.

This is also where labor-share and inequality questions belong. Technology can raise productivity and still worsen labor-market outcomes for some groups if rents shift toward capital, superstar firms, or already-advantaged workers [@autor2022LaborMarketImpactsTechChange]. The relevant distinctions are direct displacement versus indirect output effects, and average productivity versus distributional incidence. A productivity gain observed at the firm level does not by itself tell us who captures the surplus.

```{figure} assets/figures/11-technology-adjustment-and-reallocation.png
:name: fig-lii-w11-adjustment
Technology shocks propagate from task reallocation inside firms to retraining, mobility, and local-market incidence. The longer-run outcome depends on output expansion, sectoral offsets, and how quickly workers and places can adjust.
```

Figure {numref}`fig-lii-w11-adjustment` is the week's equilibrium reminder. Displacement is often the most visible short-run effect, but service offsets, occupational restructuring, and worker mobility determine medium-run incidence.

### Contemporary AI evidence: exposure, adoption, and realized labor demand

Recent AI evidence is distinctive because measurement has moved faster than long-run outcome data. Felten, Raj, and Seamans create an occupation-level AI exposure metric by mapping AI capabilities to occupational abilities [@feltenRajSeamans2018MethodAIAbilities]. The identifying object is descriptive exposure, not treatment. The unit is the occupation. The observed margin is predicted susceptibility. The offstage margin is actual firm adoption and realized worker impact. Exposure measures are useful, but they are not outcomes.

Aghion et al. provide a cleaner adoption-based benchmark by distinguishing different uses of AI in French firms [@aghionEtAl2025HowDifferentUsesAI]. The identifying variation comes from realized adoption categories rather than exposure alone. The unit is the firm. The observed margins are labor-demand responses such as employment growth, vacancies, and workforce composition. The key labor insight is that different uses of the same general technology can have different demand effects: automation-style uses can crowd out some hiring while augmentation or complementary uses can expand it.

Labaschin et al. push the measurement frontier by extending exposure ideas from occupations to firms [@labaschinEtAl2025ExtendingGPTsFirms]. This helps bridge the gap between public task-based exposure measures and actual firm organization, but it still does not eliminate the selection problem in adoption. Firms choose technologies endogenously, and the most adoption-rich data are often the least publicly reproducible.

### AI data and measurement: what each source can and cannot identify

```{include} assets/tables/11-data-design-and-research-opportunities.md
```

Table {numref}`tbl:technology-data-design-map` is the methods map for the second half of the lecture. Students should read it with four questions in mind: what is the technology object, what is the unit of observation, what margin is observed, and what equilibrium margin remains offstage?

```{figure} assets/figures/11-ai-data-and-labor-market-measurement.png
:name: fig-lii-w11-ai-measurement
AI measurement sits on a ladder from descriptive exposure to realized adoption to operational productivity logs and finally to market-level incidence. Moving down that ladder usually improves treatment measurement but narrows the equilibrium object that is directly observed.
```

The cleanest measurement distinction is between public occupation exposure measures and actual use. Public exposure measures scale well and are easy to merge with labor data, but they remain descriptive mappings from task content to predicted technological relevance [@feltenRajSeamans2018MethodAIAbilities]. Firm adoption data measure realized treatment more directly, but selection into adoption becomes central [@aghionEtAl2025HowDifferentUsesAI]. Vacancy data reveal changing labor demand and job design, but postings are not employment [@acemogluAutorHazellRestrepo2020AIJobsVacancies]. Worker-level field or operational data identify heterogeneity in productivity or learning, but they are often narrow in setting and weak on general equilibrium [@brynjolfssonLiRaymond2025GenerativeAIWork].

### Global and comparative evidence

Week 11 should be explicitly comparative. Michaels, Natraj, and Van Reenen show ICT-related skill-demand shifts across eleven countries [@michaelsNatrajVanReenen2014ICTPolarizedSkillDemand]. Graetz and Michaels show robot-associated productivity and labor-market patterns across seventeen countries [@graetzMichaels2018RobotsWork]. Dauth et al. study German labor-market adjustment to robots with strong worker and regional detail [@dauthFindeisenSuedekumWoessner2021AdjustmentRobots]. Aghion et al. add contemporary French firm evidence on how different uses of AI shape labor demand [@aghionEtAl2025HowDifferentUsesAI].

The reason to keep these settings together is not to produce a country catalog. It is to show that institutions, training systems, bargaining structures, sector mix, and mobility shape equilibrium adjustment. Cross-country evidence therefore helps with external validity, but it also warns against taking one design as universal.

### Research frontier and extension block

The optional ninety-minute extension block should be longer than usual because this is one of the major shock-and-adjustment weeks in Labor II. A useful frontier map includes at least six open questions.

1. How much of measured AI exposure predicts realized adoption, and how much remains a descriptive forecast?
2. When does AI complement weaker or less experienced workers, and when does it mainly increase scale for already-strong workers?
3. How much technology adjustment runs through wage-setting and rent sharing rather than headcount alone?
4. Which organizational complements determine whether AI is labor-saving, labor-using, or primarily redistributive inside firms?
5. What is genuinely new about contemporary AI relative to earlier ICT and robot waves [@liuPapanikolaouSchmidtSeegmiller2025TechnologyLaborMarkets]?
6. Which policies matter most for worker transition support: training subsidies, diffusion policy, wage insurance, or mobility support?

The discipline for frontier work is the same as for canonical papers. Name the identifying variation, the unit of observation, the observed margin, and the equilibrium object that still sits offstage.

### Bridge to Week 12

Week 11 studied technology as a shock generated inside production, task choice, and organizational redesign. Week 12 will study trade and offshoring as shocks generated through global goods and production integration. Both weeks are about labor-market adjustment, but the mapping from exposure to incidence differs. Technology shocks often begin with task assignment and adoption inside firms; trade shocks often begin with product-market integration and import or export exposure across firms, industries, and places.

## Research Lab

The Week 11 lab follows the standard `Reproduce -> Diagnose -> Transfer` structure and keeps the bounded student path fully local. The primary anchor is `@aghionEtAl2025HowDifferentUsesAI`, where the core teaching object is realized AI adoption by use type inside firms. The challenge anchor is `@acemogluRestrepo2020RobotsJobs`, where the contrast is a local-labor-market exposure design rather than a within-firm adoption design. The optional extension anchor is `@brynjolfssonLiRaymond2025GenerativeAIWork`, which helps students connect worker-level productivity and learning evidence to the broader demand-side and equilibrium framework.

The local handout lives at [labs/11-technology-automation-ai-and-labor-market/lab.md](labs/11-technology-automation-ai-and-labor-market/lab.md). The point of the lab is not to turn students loose on a vague “AI and jobs” exercise. It is to force them to state whether the object is supply-side, demand-side, or market-level; whether the technology measure is exposure or adoption; what the unit of observation is; which labor margin is observed; and which equilibrium margin remains offstage.

## Methods Box

Keep these distinctions explicit throughout the week.

1. Tasks versus occupations: tasks are the economically primitive object in the theory, while occupations are observed bundles that mix many tasks [@acemogluAutor2011SkillsTasksTechnologies].
2. Exposure versus adoption: exposure measures predicted susceptibility; adoption measures realized use, usually with more selection concerns [@feltenRajSeamans2018MethodAIAbilities; @aghionEtAl2025HowDifferentUsesAI].
3. Within-firm versus market-level evidence: firm evidence is strongest on direct labor-demand responses, while local-market designs are stronger on equilibrium incidence across places [@aghionEtAl2025HowDifferentUsesAI; @acemogluRestrepo2020RobotsJobs].
4. Direct displacement versus indirect productivity and output effects: a negative coefficient on an exposed task margin is not the whole labor-demand effect [@acemogluRestrepo2019AutomationNewTasks].
5. Historical ICT and robot evidence versus very recent AI evidence: the underlying technologies, diffusion speeds, and observable margins differ [@michaelsNatrajVanReenen2014ICTPolarizedSkillDemand; @brynjolfssonLiRaymond2025GenerativeAIWork].
6. Skill obsolescence versus skill acquisition: technology can raise the return to learning while making prior task-specific knowledge depreciate faster [@bartelSicherman1998TechnologicalChangeSkillAcquisition; @demingNoray2020EarningsDynamicsChangingJobSkills].
7. Public occupation exposure maps versus actual use: descriptive exposure should not be narrated as realized treatment [@feltenRajSeamans2018MethodAIAbilities].
8. Descriptive exposure correlations versus causal adoption evidence: each tells a different part of the labor-market story and neither replaces the other [@acemogluAutorHazellRestrepo2020AIJobsVacancies; @aghionEtAl2025HowDifferentUsesAI].

## Reading ladder

### Ladder A. Core framework

- @autor2015WhyStillManyJobs
- @acemogluRestrepo2019AutomationNewTasks
- @acemogluAutor2011SkillsTasksTechnologies

### Ladder B. Historical and global evidence

- @michaelsNatrajVanReenen2014ICTPolarizedSkillDemand
- @graetzMichaels2018RobotsWork
- @dauthFindeisenSuedekumWoessner2021AdjustmentRobots
- @acemogluRestrepo2020RobotsJobs

### Ladder C. Worker adaptation and labor supply

- @bartelSicherman1998TechnologicalChangeSkillAcquisition
- @demingNoray2020EarningsDynamicsChangingJobSkills
- @brynjolfssonLiRaymond2025GenerativeAIWork

### Ladder D. Contemporary AI, measurement, and frontier directions

- @acemogluAutorHazellRestrepo2020AIJobsVacancies
- @feltenRajSeamans2018MethodAIAbilities
- @aghionEtAl2025HowDifferentUsesAI
- @labaschinEtAl2025ExtendingGPTsFirms
- Optional frontier extension: @liuPapanikolaouSchmidtSeegmiller2025TechnologyLaborMarkets

## Exercises / discussion prompts

1. Pick one paper from the week and name the identifying variation, unit of observation, observed margin, and key equilibrium margin left offstage.
2. Suppose a new AI system raises output per worker in a call-center setting. List at least four labor-market objects that could still move in opposite directions: employment, wage inequality, vacancy content, and worker progression are good starting candidates.
3. Compare `@acemogluRestrepo2020RobotsJobs` with `@aghionEtAl2025HowDifferentUsesAI`. Which one is closer to exposure, which one is closer to adoption, and which one is closer to market-level equilibrium incidence?
4. Design a bounded empirical exercise that distinguishes skill obsolescence from skill acquisition using either public occupation cells or a synthetic worker panel.

## Reproducibility or code lab note

The bounded pedagogical path lives in [labs/11-technology-automation-ai-and-labor-market/lab.md](labs/11-technology-automation-ai-and-labor-market/lab.md). It is intentionally local and synthetic. Students reproduce a firm-level AI-use design, diagnose the difference between adoption and exposure, and then transfer one exposure idea to a small market-level setting. The smoke test runs only that bounded path.

## Slide companion note

The canonical Week 11 slide source is [slides/week11/11-technology-automation-ai-and-labor-market.tex](slides/week11/11-technology-automation-ai-and-labor-market.tex). The deck is designed to mirror the chapter's logic without duplicating it: question first, task framework next, then supply-side adjustment, demand-side evidence, equilibrium incidence, measurement, frontier questions, and the bridge to Week 12 trade and offshoring.
