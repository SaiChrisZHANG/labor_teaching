# Fertility, Mortality, Caregiving, And Lifecycle Labor Allocation

## Learning Objectives

By the end of Week 3, students should be able to:

1. describe lifecycle labor allocation as a dynamic worker and household problem involving work, care, savings, health, fertility, aging, and retirement;
2. explain how fertility timing and child penalties affect current labor supply, future wages, occupations, promotion paths, mobility, and household specialization;
3. distinguish short-run and medium-run family labor-supply responses to severe illness, mortality risk, death, and other household health shocks;
4. analyze informal caregiving as a labor-market force that changes hours, participation, retirement timing, job choice, geographic mobility, and demand for flexibility;
5. evaluate how pension rules, retirement savings, health, and employer job design shape retirement timing, bridge jobs, rehiring, part-time transitions, and post-retirement work;
6. connect global aging evidence to labor-market institutions without turning demographic change into a purely macro population-aging discussion;
7. design a lifecycle labor-allocation study that names the shock, the labor margin, the horizon, the household or firm unit, and the relevant policy or institutional object.

The central question is this: how do fertility timing, mortality risk, aging, and caregiving burdens reshape labor allocation over the life cycle?

## Opening Orientation

Week 3 starts from a simple labor-economics premise: demographic and family-health events are not background characteristics. They arrive at particular ages, interact with job ladders and household resources, and can shift the whole path of work, care, savings, mobility, retirement, and welfare. A birth, a spouse's illness, a parent's care need, a pension eligibility threshold, or a late-life health decline can change current hours today and also change future wages, occupation, retirement resources, and household specialization.

The lecture is therefore not a generic demography, family, or retirement lecture. Fertility matters here because it changes labor allocation and career dynamics. Mortality risk matters because families adjust work and savings when severe health shocks change resources, time needs, and expected horizons. Caregiving matters because unpaid family care competes with market work and raises the value of job flexibility. Aging and retirement matter because pension rules, savings, health, and employer job design determine whether older workers exit, reduce hours, bridge into different jobs, return to work, or remain attached in flexible arrangements.

:::{admonition} Core points
:class: important

- Lifecycle labor allocation is a dynamic household problem: work, care, savings, health, fertility timing, aging, and retirement decisions are jointly linked over time [@macurdy1981; @becker1965allocation].
- Fertility timing and children can generate both immediate labor-supply responses and persistent career effects through experience accumulation, occupation choice, promotion timing, and household specialization [@addaDustmannStevens2017; @klevenLandaisSogaard2019; @lundborgPlugRasmussen2017].
- Severe illness, mortality risk, and death create family labor-supply responses because they change income, time needs, care responsibilities, insurance value, and expected horizons [@fadlonNielsen2021; @garciaGomezJonesRice2013].
- Informal caregiving is a labor-market margin, not only a household chore: it changes hours, participation, retirement timing, mobility, and demand for flexible jobs or paid leave [@vanHoutvenCoeSkira2013informalCare; @maestasMullenPowell2023; @coileRossinSlaterSu2022].
- Aging societies make pension design, retirement savings, post-retirement work, bridge jobs, rehiring, and older-worker flexibility central labor-market objects [@ameriksBriggsCaplin2020; @biZubairy2023; @coileMilliganWise2018].

:::

## Bridge

Week 2 studied disability and chronic conditions as direct work-capacity constraints, program interactions, and employer-response problems. Week 3 broadens the unit of analysis. The worker is still central, but the relevant state variables now include children, spouses, parents, care needs, pension eligibility, assets, survival risk, and the job arrangements available late in life.

This shift changes the empirical discipline. Many Week 3 events are predictable in broad outline but uncertain in timing, severity, and persistence. Children may be anticipated, but childbirth still arrives at a specific point in a career. Parents may age gradually, but care needs can become acute. Retirement is often planned, but health shocks, spouse shocks, pension rules, and employer flexibility can move the actual exit date. Students should therefore ask not only whether labor supply changes, but when the event arrives, how long the effect persists, and which future margins are altered.

## Field Core

### A Brief Lifecycle Labor-Allocation Framework

A compact lifecycle framework keeps the week organized. A worker or household chooses market work, care time, job type, mobility, savings, and retirement over a finite horizon. The state vector includes age, health, children and their ages, spouse or parent health, assets, pension eligibility, job type, accumulated experience, and local care arrangements. Choices today affect both current utility and future states: hours build experience, job changes alter wage growth, informal care changes time available for work, savings determine retirement resources, and retirement or part-time work changes future attachment.

A stripped-down representation is:

```{math}
:label: eq:st6-w3-lifecycle-value
V_t(s_t) =
\max_{h_t, c_t, j_t, a_{t+1}, r_t}
u(C_t, L_t, q_t, \ell_t)
+ \beta E_t[V_{t+1}(s_{t+1})],
```

where {math}`h_t` is market work, {math}`c_t` is informal care time, {math}`j_t` is job type or occupation, {math}`a_{t+1}` is saving, {math}`r_t` is retirement or late-life work status, {math}`q_t` captures job amenities and flexibility, and {math}`s_t` contains health, family structure, assets, pension rules, wages, care needs, and age. Fertility, severe health shocks, mortality risk, caregiving onset, pension eligibility, and aging enter as changes in the state vector or transition process.

```{include} assets/tables/03-lifecycle-framework-map.md
```

The framework is not here to derive a full structural model. It disciplines interpretation. Fertility timing is about when a care and time-allocation shock arrives relative to school, tenure, promotion windows, and human-capital accumulation. Severe illness and mortality risk are shocks to resources, time, insurance needs, and expected horizons. Caregiving is a competing use of time and attention that can change job feasibility. Aging changes work capacity and the value of flexibility. Pension rules and savings shift the budget set, but retirement is still a labor-allocation margin rather than only a benefit-claiming decision.

### Fertility Timing, Children, And Dynamic Career Effects

Children affect labor allocation immediately through time demands, leave, hours, childcare costs, and household specialization. They can also affect the dynamic career path through experience accumulation, occupational sorting, promotion timing, employer attachment, wage growth, mobility, and job amenities. The same birth can therefore produce a short-run participation response and a much longer-run earnings or occupation response.

Child penalties are useful because they make these dynamics visible. Event-study evidence around childbirth shows that earnings and labor supply can diverge sharply by gender after children arrive, with persistent effects that are not reducible to one-period hours changes [@klevenLandaisSogaard2019]. Dynamic career models emphasize that the cost of children depends on the timing of fertility relative to human-capital accumulation, occupation choice, and career ladders [@addaDustmannStevens2017]. Fertility-treatment evidence helps separate timing and family-size variation from some of the selection that makes ordinary fertility choices hard to interpret [@lundborgPlugRasmussen2017].

The key distinction is between timing effects and persistent specialization effects. A timing effect arises because childbirth arrives before or after a promotion window, training investment, tenure threshold, job search spell, or occupational transition. A persistent specialization effect arises when the household reallocates market work and care in ways that change future experience, outside offers, skills, employer attachment, or job amenities. Both are labor-market effects, but they imply different counterfactuals and policy interpretations.

Family-size instruments and fertility-timing designs can help, but they identify different objects. Angrist and Evans use variation in family size to study parental labor supply, while modern child-penalty and career-cost studies focus on dynamic trajectories around births [@angristEvans1998childrenLaborSupply; @klevenLandaisSogaard2019; @addaDustmannStevens2017]. A good Week 3 paper should therefore say whether it is studying the effect of an additional child, the timing of a birth, the arrival of first parenthood, the household specialization response, or the cumulative career cost.

### Severe Health Shocks, Mortality Risk, And Family Labor Supply

Severe illness, mortality risk, and death affect labor allocation because households insure each other through work, care, savings, and transfers. When a spouse becomes severely ill, the healthy spouse may increase work to replace income, reduce work to provide care, switch jobs for flexibility, draw down savings, or alter retirement timing. When a household member dies, the surviving family faces resource changes, grief, changes in time needs, and a different expected horizon. The sign of the labor response is therefore not predetermined.

Fadlon and Nielsen are a natural anchor because they study family labor-supply responses to severe health shocks in an administrative setting and make the household response dynamic [@fadlonNielsen2021]. The lesson is not simply that families respond. It is that severe shocks can reveal the household's insurance technology: whose labor supply moves, on what horizon, and whether the response reflects income replacement, caregiving time, anticipation, or changes in expected resources. Related health-shock evidence shows that sharp illness events can have persistent effects on employment and income, but the interpretation depends on whether the event primarily changes own capacity, family resources, or care needs [@garciaGomezJonesRice2013; @dobkinFinkelsteinKluenderNotowidigdo2018hospital].

Short-run and medium-run responses should be separated. In the short run, households may use leave, savings, temporary hours changes, or urgent care arrangements. In the medium run, they may change jobs, alter retirement plans, move geographically, shift household specialization, or adjust savings and benefit claiming. Anticipated mortality risk can also change behavior before death, so event-time designs must distinguish surprise shocks from predictable decline and must check for pre-trends.

### Caregiving And Household Reallocation

Informal caregiving is a labor-market force because care time competes with market work and changes which jobs are feasible. Parent care, spouse care, and elder care differ in intensity, predictability, co-residence, geographic distance, formal-care substitutes, and emotional cost. They also differ in how much the labor-market response is observed. A worker may stay employed but reject promotion, reduce travel, stop searching, decline overtime, switch to a flexible job, or retire earlier.

Evidence on informal care and work shows that care responsibilities can reduce work and wages, though the size and margin depend on intensity, relationship, and institutional setting [@vanHoutvenCoeSkira2013informalCare]. Administrative evidence on caregiving is valuable because it can link care needs to employment histories and benefits more cleanly than many survey measures [@maestasMullenPowell2023]. Paid family leave and care arrangements matter because they shift the time cost and insurance value of staying attached to work during family health shocks [@coileRossinSlaterSu2022]. Long-term care insurance and family insurance models sharpen the distinction between formal care markets and household self-insurance [@mommaerts2018].

Caregiving also interacts with retirement. A worker near retirement age may respond to a parent's or spouse's care needs by claiming benefits earlier, reducing hours, taking a bridge job, or leaving a career job for flexible work. A younger worker may instead preserve labor-force attachment but accept slower wage growth or narrower mobility. These differences are why lifecycle timing is central: the same care shock has different labor consequences at ages 30, 50, and 65.

### Aging, Pensions, Retirement Timing, And Late-Life Work

Aging and retirement are major Week 3 objects, not a coda. Older-worker labor supply is shaped by health, pension rules, retirement savings, employer demand, job flexibility, family care needs, and expectations about longevity. Retirement is not merely an absorbing exit. Many workers transition through partial retirement, bridge jobs, consulting, rehiring by previous employers, self-employment, part-time work, or post-retirement work after a spell out of the labor force.

Pension rules and retirement savings shift the late-life budget set. Eligibility ages, benefit accrual, earnings tests, tax treatment, employer pensions, and public pension reforms change the payoff to continued work and benefit claiming. French and Jones show how health insurance and self-insurance can affect retirement behavior, while public pension reform evidence highlights how policy incentives alter retirement decisions and aggregate labor supply [@frenchJones2011retirement; @biZubairy2023]. Cross-country retirement work is useful because it shows how institutions make similar aging processes produce different labor-force outcomes [@coileMilliganWise2018].

Flexibility is the bridge between retirement incentives and job design. Ameriks and coauthors show that many older workers place high value on flexible work, which means nonemployment at older ages may reflect job-design constraints as well as preferences for leisure or pension incentives [@ameriksBriggsCaplin2020]. Employment protection, mandatory retirement rules, and older-worker labor-market institutions add the demand-side piece: employers decide whether late-career workers can remain, return, or shift into less demanding roles [@saezSeimSchoefer2024].

```{include} assets/tables/03-global-aging-and-retirement-map.md
```

The welfare interpretation depends on the margin. Earlier retirement may be welfare-improving if work is painful, risky, or inflexible. It may be welfare-reducing if workers leave because employers do not offer feasible hours, schedules, or tasks. Post-retirement work may indicate inadequate savings, weak pensions, preferences for work, demand for social connection, or an unmet market for flexible late-life jobs. A labor economist should not collapse all of these into "retirement."

### Global Aging And Comparative Evidence

Global aging matters for labor economics because it changes the distribution of workers across ages, the demand for care, the fiscal and incentive structure of pensions, and the design of jobs for older workers. The labor-market question is not only whether population aging reduces aggregate growth. It is how aging changes labor-force attachment, retirement timing, care burdens, older-worker job quality, firm adaptation, and the incidence of demographic adjustment.

Cross-country retirement evidence helps separate health, preferences, and institutions because public pension systems, eligibility ages, disability programs, employment protection, and care systems vary across settings [@coileMilliganWise2018]. Comparative aging work can also show how older-worker participation, care demand, and demographic composition interact with productivity and labor-market adjustment [@bloomCanningFink2010populationAgeing; @maestasMullenPowell2023aging]. Kotschy and Bloom are useful as comparative background when used carefully: the labor point is not demographic drag in the abstract, but the worker, firm, pension, and care margins through which aging societies adjust [@kotschyBloom2023].

The course will return to aggregate demographic change in Week 5. Week 3's role is narrower and deeper: aging societies make lifecycle labor allocation more important because more workers face late-life health risk, pension incentives, care responsibilities, and flexible-work decisions at the same time.

### Research Architecture For Lifecycle Labor Papers

A strong lifecycle labor-allocation paper names five objects:

1. the event or state transition: birth, child age, severe illness, death, caregiving onset, pension eligibility, retirement-age reform, aging threshold, or late-life health decline;
2. the labor margin: hours, participation, earnings, occupation, mobility, savings, benefit claiming, retirement, bridge job, rehire, or post-retirement work;
3. the dynamic horizon: immediate disruption, medium-run reallocation, long-run career path, or late-life welfare;
4. the unit of adjustment: worker, spouse, household, extended family, employer, or local labor market;
5. the institutional object: leave, childcare, elder care, pension rules, disability program, health insurance, employment protection, or flexible job design.

```{include} assets/tables/03-methods-and-data-map.md
```

The main identification problems are timing endogeneity, anticipation, selective survival, selection into treatment or care, endogenous benefit claiming, confounding labor-demand shifts, and mismeasurement of informal care or post-retirement work. Event studies are powerful when timing is sharp, but pre-trends are especially important because many lifecycle events are partly anticipated. Policy reforms are powerful when the institutional object is clear, but they may move several margins at once.

## Research Lab

The Week 3 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Fadlon and Nielsen on family labor-supply responses to severe health shocks because it is a labor-focused lifecycle paper with a clear dynamic household response [@fadlonNielsen2021]. The challenge anchor is Ameriks and coauthors on older-worker flexibility because it pushes the lab toward aging, retirement, bridge jobs, and late-life job design [@ameriksBriggsCaplin2020].

The lab is not an official replication package for either paper. It uses deterministic synthetic data to practice the logic of an event-time family health-shock design and then transfers the lifecycle logic to fertility timing, caregiving onset, pension reform, and flexible late-life work.

**Reproduce.** Students recover a bounded event-study profile around a severe family health shock. Outcomes include own hours, spouse hours, household earnings, care hours, savings drawdown, job flexibility, retirement claiming, and post-retirement work. The object is to reproduce the structure of dynamic household adjustment, not official administrative estimates.

**Diagnose.** Students classify each movement as income replacement, care-time demand, own work-capacity loss, pension or benefit incentive, flexibility response, or dynamic selection. They compare short-run disruption with medium-run reallocation.

**Transfer.** Students redesign the same logic for one alternative lifecycle setting: first birth and child penalties, caregiving onset, pension eligibility reform, or bridge-job and rehire transitions among older workers. The transfer task keeps the labor margin visible while changing the event, horizon, and institutional object.

```{include} assets/tables/03-reading-and-lab-map.md
```

## Methods Box

:::{admonition} Methods Box: Dynamic Lifecycle Labor Designs
:class: note

**Start from the event and the age.** A fertility shock at age 28, a parent-care shock at age 52, and a pension eligibility threshold at age 62 move different future states.

**Separate timing from specialization.** Child penalties can reflect immediate leave and hours changes, but also persistent changes in experience, occupation, promotion, mobility, and household specialization.

**Separate income replacement from care demand.** Severe illness can make family members work more to replace income or work less to provide care. The observed sign is not mechanically determined.

**Treat caregiving intensity as a hidden state.** Survey or administrative care measures may miss emotional load, scheduling constraints, co-residence, travel time, and forgone promotions.

**Do not make retirement absorbing by assumption.** Partial retirement, bridge jobs, rehiring, part-time transitions, self-employment, and post-retirement work are labor margins.

**Use institutions carefully.** Leave rules, childcare, elder care, pensions, disability programs, health insurance, and employment protection identify specific margins, not a universal lifecycle effect.

**Keep welfare visible.** Wages and employment can miss pain, stress, flexibility, family insurance, retirement adequacy, and the value of care.

:::

## Reading Ladder And References

**Core lifecycle framing.** Start with MaCurdy for lifecycle labor supply and Becker for time allocation, then use Currie and Madrian to connect health, insurance, and labor-market behavior [@macurdy1981; @becker1965allocation; @currieMadrian1999].

**Fertility timing and child penalties.** Read Adda, Dustmann, and Stevens on career costs, Kleven, Landais, and Sogaard on child penalties, Lundborg, Plug, and Rasmussen on fertility-treatment variation, and Cortes and Pan for a recent synthesis of children and gender gaps [@addaDustmannStevens2017; @klevenLandaisSogaard2019; @lundborgPlugRasmussen2017; @cortesPan2023children].

**Severe health shocks and family labor supply.** Use Fadlon and Nielsen as the primary household-response anchor, then pair it with Garcia-Gomez, Jones, and Rice and Dobkin and coauthors for dynamic labor-market consequences of severe health events [@fadlonNielsen2021; @garciaGomezJonesRice2013; @dobkinFinkelsteinKluenderNotowidigdo2018hospital].

**Caregiving and household reallocation.** Use Van Houtven, Coe, and Skira for informal care and work, Maestas, Mullen, and Powell for administrative caregiving evidence, Coile, Rossin-Slater, and Su for paid leave around family health shocks, and Mommaerts for long-term care and family insurance [@vanHoutvenCoeSkira2013informalCare; @maestasMullenPowell2023; @coileRossinSlaterSu2022; @mommaerts2018].

**Aging, pensions, and late-life work.** Read Ameriks and coauthors on older-worker flexibility, Bi and Zubairy on public pension reforms, Coile, Milligan, and Wise on retirement around the world, French and Jones on health insurance and retirement, and Saez, Seim, and Schoefer on older-worker employment protection [@ameriksBriggsCaplin2020; @biZubairy2023; @coileMilliganWise2018; @frenchJones2011retirement; @saezSeimSchoefer2024].

**Global aging and comparative evidence.** Use Bloom, Canning, and Fink, Maestas, Mullen, and Powell, and Kotschy and Bloom as comparative background, while keeping the labor margins of retirement, care demand, older-worker jobs, productivity, and firm adjustment in view [@bloomCanningFink2010populationAgeing; @maestasMullenPowell2023aging; @kotschyBloom2023].

## Exercises And Discussion Prompts

1. In a lifecycle labor-allocation problem, how do fertility timing and severe health shocks differ as labor-market events?
2. Why can a child penalty reflect both a timing effect and a persistent specialization effect?
3. A spouse has a severe health shock. What would make the healthy spouse work more, and what would make the healthy spouse work less?
4. Pick a caregiving measure. What care intensity, emotional burden, scheduling constraint, or geographic constraint might remain unobserved?
5. When does post-retirement work indicate inadequate retirement resources, and when does it indicate unmet demand for flexible jobs?
6. Why can pension eligibility identify an incentive effect without identifying the total welfare value of retirement?
7. Choose one country facing population aging. Which labor margin should a labor economist study first: older-worker participation, retirement timing, care work, firm job design, migration, or automation?

## Reproducibility And Code Lab Note

The Week 3 code lab lives at `labs/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation/`. It is a bounded synthetic teaching path, not an official replication of Fadlon and Nielsen or Ameriks and coauthors. The smoke path creates deterministic household-event data; estimates a compact family health-shock event profile; diagnoses income replacement, care demand, work-capacity, pension, flexibility, and selection channels; and transfers the design logic to fertility timing, caregiving onset, pension reform, and bridge-job or rehire margins.

The lab is conservative by design. It does not claim access to official Danish administrative records, health registers, pension records, older-worker survey modules, or employer rehiring data.

## Slide Companion Note

The Week 3 slide deck lives at `slides/week3/03-fertility-mortality-caregiving-and-lifecycle-labor-allocation.tex`. The deck mirrors the chapter logic without duplicating the prose: it opens with the lifecycle labor-allocation framework; covers fertility timing and child penalties; separates family responses to severe health shocks from caregiving reallocation; makes aging, pensions, retirement timing, and post-retirement work central; includes global aging evidence; and closes with the Research Lab design.

## Bridge Forward

Week 4 moves from household lifecycle allocation to mental health, stress, workplace productivity, and worker welfare. The unit of analysis shifts from family timing, care burdens, and retirement margins toward workplace functioning, absenteeism, presenteeism, supervision, job quality, and the welfare cost of work under psychological strain. The Week 3 lesson carries forward: labor outcomes are dynamic, and a current shock can change future wages, jobs, flexibility, mobility, and welfare.
