# Disability, Chronic Conditions, Labor Supply, And Job Choice

## Learning Objectives

By the end of Week 2, students should be able to:

1. explain how disability and chronic conditions reshape labor-force attachment, hours, occupation, accommodations, job amenities, and exit;
2. separate direct work-capacity effects from disability-program incentives, employer accommodation, local labor-demand conditions, and selection into disability status or benefit receipt;
3. distinguish short-run disruption from long-run labor-market scarring after disability onset, chronic-condition diagnosis, or acute health shocks;
4. evaluate whether treatment, workplace accommodation, and return-to-work investments change labor-market decisions;
5. explain how job lock, accommodation dependence, local scarcity of feasible jobs, switching costs, and employer information advantages can make labor supply more inelastic;
6. design a credible disability or chronic-condition labor-market study using event studies, program rules, family comparisons, genetic designs, matched employer-employee designs, or treatment-access reforms.

The central question is this: how do disability and chronic conditions reshape labor-force attachment, hours, occupation, accommodations, and exit?

## Opening Orientation

Disability and chronic conditions are labor-market constraints that unfold over time. A new limitation can immediately reduce stamina, task capacity, commuting tolerance, or schedule feasibility. It can also trigger slower adjustments: workplace accommodation, occupational downgrading, hours reductions, insurance and benefit calculations, treatment investments, employer reassignment, or eventual exit from employment. The same condition can therefore produce a small short-run employment effect but a large long-run earnings, job-quality, or welfare effect.

This is a labor-economics lecture, not a generic disability-policy survey. The organizing objects are employment, hours, wages, occupation, job amenities, search, mobility, employer response, and worker welfare. Disability insurance and accommodation law matter here because they change labor-market choices and firm behavior. Medical diagnosis matters because it changes the feasible set for work. But the empirical question is always: which labor margin moved, on what horizon, through which mechanism, and relative to what counterfactual?

:::{admonition} Core points
:class: important

- Disability and chronic conditions reshape labor outcomes through work capacity, reservation wages, job feasibility, accommodations, and program incentives [@meyerMok2019; @collischonHiesingerPohlan2023].
- Short-run and long-run effects can differ sharply. Acute shocks may cause immediate disruption, while chronic conditions can accumulate through persistent job loss, occupational downgrading, and welfare losses [@dobkinFinkelsteinKluenderNotowidigdo2018hospital; @garciaGomezJonesRice2013].
- Treatment, accommodation, and return-to-work investments can change labor-market decisions, so reduced-form disability effects do not reveal immutable health constraints [@hillMaestasMullen2016; @zaresani2018].
- Disability and chronic conditions may generate monopsony power through job lock, accommodation dependence, local scarcity of feasible jobs, switching costs, stigma, and employer information advantages [@madrian1994; @ameriSchurAdyaBentleyEtAl2018].
- Credible causal work separates work-capacity effects, program incentives, employer treatment, local labor demand, and selection into disability status or program use [@bound1991; @frenchSong2014; @maestasMullenStrand2013ssdi].

:::

## Bridge

Week 1 established health as work capacity, risk, and a measurement problem. Week 2 applies that discipline to disability and chronic conditions, where observed labor outcomes are especially likely to mix several objects. A worker may have a real functional limitation, a stronger demand for health insurance, a better or worse employer response, a benefit-application option, a local labor market with few feasible jobs, and private information about future decline. A single employment coefficient can bundle all of these.

The first task is to keep five mechanisms separate:

1. **Direct work-capacity effects:** the condition limits tasks, stamina, cognition, pain tolerance, commuting, or scheduling.
2. **Program incentives and benefit receipt:** disability insurance, eligibility rules, waiting periods, reassessments, and return-to-work rules alter the payoff to employment.
3. **Employer accommodation and workplace treatment:** firms can redesign tasks, schedules, technology, leave, supervision, and retention, or they can screen, stigmatize, or fail to accommodate.
4. **Local labor-demand conditions:** workers with limitations need feasible jobs; weak demand, inaccessible transportation, or a narrow local occupation mix can turn a health constraint into nonemployment.
5. **Selection into disability status and program use:** disability status is partly a health object and partly an endogenous outcome of severity, work history, knowledge, application costs, and expected benefits.

## Field Core

### Disability And Chronic Conditions As Dynamic Labor-Market Constraints

Disability and chronic conditions affect labor-market behavior through several margins at once. They can reduce productivity or hours directly, change the set of feasible jobs, raise the value of flexible schedules or safer tasks, increase the value of employer-provided insurance, and alter the expected value of remaining employed versus applying for benefits. Chronic conditions are especially dynamic: workers may remain attached initially but gradually shift occupation, reduce hours, change employers, or exit employment as symptoms, treatment needs, and employer responses evolve [@currieMadrian1999; @meyerMok2019].

```{include} assets/tables/02-disability-and-chronic-conditions-map.md
```

The labor-market object is therefore not "disabled versus not disabled." It is a vector of constraints and responses. A worker with chronic pain may remain employed but move away from physically demanding work. A worker with a condition requiring predictable treatment may value schedule control more than wage growth. A worker whose current employer has already installed an accommodation may face a high switching cost even if measured employment is unchanged.

```{include} assets/tables/02-disability-chronic-mechanisms-map.md
```

This distinction matters for welfare. Wages and employment can understate the cost of disability if workers stay employed by accepting pain, risk, stigma, poorer schedules, lower promotion chances, or narrower outside options. Conversely, employment losses can overstate pure work-capacity effects if the observed margin is driven by benefit rules, poor local demand, or employer failure to accommodate.

### Direct Capacity Effects Versus Program Incentives

A clean lecture in this area must separate health constraints from institutional incentives. Direct capacity effects operate through the production and feasible-set side of labor supply: the worker cannot perform certain tasks, cannot sustain previous hours, or cannot tolerate the commute, schedule, cognitive load, or physical demand. Program effects operate through eligibility rules, benefit generosity, earnings tests, waiting periods, medical reviews, and the risk of losing benefits after returning to work [@autorDuggan2003disabilityRolls; @frenchSong2014; @lowPistaferri2015disability].

A compact way to write the employment decision is:

```{math}
:label: eq:st6-w2-work-program-value
V^W_{it}(H_{it}, A_{it}, D_{mt}) \geq V^B_{it}(H_{it}, R_{it}, B_{it}),
```

where {math}`V^W` is the value of work, {math}`H_{it}` is health or functional capacity, {math}`A_{it}` is accommodation or job amenities, {math}`D_{mt}` is local labor demand, {math}`V^B` is the value of benefit receipt or nonemployment, {math}`R_{it}` is program eligibility or reassessment risk, and {math}`B_{it}` is benefit generosity. A decline in health can move both sides of this inequality. That is why disability-program status is not a pure health measure.

Examiner-assignment, award-threshold, and reassessment designs are useful because they can isolate program receipt or rules from underlying impairment for marginal applicants [@maestasMullenStrand2013ssdi; @frenchSong2014]. But they answer a narrow question: how program treatment changes labor supply for people near a decision margin. They do not estimate the full work-capacity cost of disability onset for all workers with chronic conditions.

### Short-Term Versus Long-Term Labor-Market Effects

Short-run effects capture immediate disruption: missed work, lower hours, reduced earnings, urgent medical spending, liquidity stress, employer leave decisions, and temporary accommodation. Long-run effects capture scarring: persistent exit, occupation change, reduced career progression, lower income and consumption, weaker mobility, benefit dependence, and changes in household labor supply.

```{include} assets/tables/02-short-vs-long-term-and-treatment-map.md
```

Acute health-shock studies are powerful because timing is sharp. Hospital admissions or severe health events can be placed in event time, letting researchers inspect pre-trends and post-shock trajectories [@dobkinFinkelsteinKluenderNotowidigdo2018hospital; @garciaGomez2013]. But acute-shock evidence does not automatically reveal chronic-condition incidence. A sudden hospitalization can identify disruption and recovery; a chronic disease can produce gradual fatigue, repeated absences, occupational sorting, and slowly worsening outside options.

The long-run disability literature is valuable because it makes persistence visible. Meyer and Mok show that severe and chronic disability can have large effects on earnings, income, and consumption over long horizons [@meyerMok2019]. The lesson for students is not only that the effects are large. It is that horizon choice changes the estimand. A one-year employment estimate, a five-year earnings estimate, and a ten-year consumption estimate are different labor-market objects.

### Treatment, Accommodation, And Return-To-Work Investments

Treatment, accommodation, and return-to-work investments are not afterthoughts. They are part of the labor-market response. Treatment can improve capacity, stabilize symptoms, reduce pain, or make hours feasible. Accommodation can redesign tasks, schedules, remote-work options, assistive technology, leave, commuting requirements, or supervision. Return-to-work policy can alter the costs and risks of testing employment after benefit receipt.

Hill, Maestas, and Mullen show why accommodation is central: employer accommodation can affect labor supply, delayed exit, and SSDI claiming [@hillMaestasMullen2016]. Return-to-work reforms matter for the same reason: they change the value of remaining attached or reentering employment after disability-program interaction [@zaresani2018]. These margins complicate causal interpretation because accommodation and treatment are endogenous. Workers with better jobs, more information, stronger bargaining power, or higher expected productivity may receive more accommodation.

A labor-focused interpretation asks four questions:

1. Does the intervention improve actual work capacity?
2. Does it expand the feasible set of jobs or hours?
3. Does it change program incentives or the risk of losing benefits?
4. Does it change firm behavior, retention, screening, or task assignment?

The same observed employment gain can mean recovery, improved match quality, stronger employer retention, reduced stigma, or altered benefit incentives. A strong design has to name which channel is identified and which remains bundled.

### Local Labor Demand, Employer Response, And Selection

Disability and chronic conditions interact with labor demand. A health limitation becomes more costly when local employers offer few flexible jobs, transportation is inaccessible, occupation mix is physically demanding, or the worker has limited bargaining power. Conversely, a strong labor market with many feasible jobs may absorb the same limitation through sorting, accommodation, or schedule adjustment.

Employer response is a separate mechanism. Firms may accommodate because turnover is costly, because worker-specific human capital is valuable, because legal or internal policy requires it, or because supervisors have discretion. They may also screen workers, assign them to lower-return tasks, reduce promotion opportunities, or avoid hiring under uncertainty. Audit evidence on disability-related hiring barriers is useful here because it shows that employer beliefs and discrimination can alter outside offers, not just current-job outcomes [@ameriSchurAdyaBentleyEtAl2018].

Selection is the constant empirical hazard. Disability status and benefit receipt are selected outcomes. People apply when health, job loss, local demand, information, wealth, and program expectations make application attractive. People with severe but accommodated limitations may remain employed and never appear as benefit recipients. People in weak labor markets may apply at lower measured health severity. This is why the field needs designs that separate onset, severity, program receipt, employer response, and local opportunity.

### Disability, Chronic Conditions, And Monopsony / Inelastic Labor Supply

Disability and chronic conditions can make labor supply to the current employer or local labor market more inelastic. This is a monopsony mechanism, not merely a legal or human-resources issue. The worker's outside option shrinks when feasible jobs are scarce, commuting is difficult, employer-provided insurance is valuable, accommodation is employer-specific, search is costly, or prospective employers hold private information advantages about whether they will accommodate.

```{include} assets/tables/02-monopsony-accommodation-job-lock-map.md
```

Job lock is the canonical example. Employer-provided health insurance can reduce mobility because leaving the job may mean losing coverage, provider networks, or treatment continuity [@madrian1994]. Accommodation lock is parallel: leaving may mean losing a customized schedule, modified tasks, remote-work arrangement, equipment, or supervisor knowledge. Local scarcity compounds both channels when only a small set of firms can offer compatible tasks.

The monopsony interpretation changes what students should look for empirically. Wage losses may reflect lower productivity, occupational downgrading, compensating differentials for flexibility, or employer wage-setting power over workers with weaker outside options. Lower quit rates among workers with chronic conditions need not reveal satisfaction; they may reveal job lock. Better accommodation at the current employer can raise retention and welfare while also increasing employer-specific dependence. The welfare question must therefore include wages, hours, pain, risk, amenities, mobility, and bargaining power.

### Frontier Methods And Identification

Causal identification is difficult because health, work, program use, treatment, and employer response are jointly determined. The methods frontier is best taught as a set of design families, each identifying a different object.

```{include} assets/tables/02-frontier-methods-box.md
```

Acute health-shock event studies use sharp timing around hospitalization or severe events. They are strong for short-run disruption and recovery but must distinguish severity, treatment, liquidity, insurance, and employer retention [@dobkinFinkelsteinKluenderNotowidigdo2018hospital; @garciaGomez2013].

Disability-onset administrative event studies follow workers around newly observed disability status or certification. They can reveal dynamic labor-market paths, but disability onset is often institutional as well as medical [@collischonHiesingerPohlan2023].

Threshold and program-rule designs exploit award decisions, examiner assignment, reassessment rules, earnings tests, or return-to-work reforms. They are powerful for program incentives, but often estimate local effects for marginal applicants [@maestasMullenStrand2013ssdi; @frenchSong2014; @zaresani2018].

Twin and sibling comparisons can reduce family-background confounding in health-labor settings, though they do not automatically solve measurement error or within-family selection. Genetic and Mendelian-randomization-style designs can help study chronic-condition channels such as obesity or health risks, but they require strong exclusion restrictions and careful handling of population structure [@bockermanCawley2018; @vonHinkeKesslerScholder2016].

Matched employer-employee and firm-heterogeneity designs are increasingly important because they ask whether some firms buffer health shocks better than others. They can connect accommodation, retention, and firm policy to worker outcomes, but sorting into firms and endogenous accommodation remain central threats [@hillMaestasMullen2016; @biroGerardGyetvaiPapp2024].

Treatment-access and reform designs ask whether care, accommodations, or return-to-work investments change labor-market behavior. They are useful precisely because they test whether disability effects are technologically fixed or institutionally mediated.

## Research Lab

The Week 2 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Meyer and Mok on disability, earnings, income, and consumption because it makes long-run disability incidence visible [@meyerMok2019]. The challenge anchor is Hill, Maestas, and Mullen because accommodation directly sharpens the treatment, employer-response, and identification discussion [@hillMaestasMullen2016].

The lab is not an official replication package for either paper. It uses deterministic synthetic data to practice the logic of a disability-onset event study, diagnose competing mechanisms, and transfer the design to accommodation or treatment access.

**Reproduce.** Students recover a bounded event-study profile around synthetic disability onset. Outcomes include employment, hours, earnings, occupation feasibility, accommodation receipt, benefit receipt, and job mobility. The goal is to reproduce the structure of long-run incidence, not official estimates.

**Diagnose.** Students classify each post-onset change into direct capacity, program incentives, accommodation or workplace treatment, local labor demand, or selection. They also compare short-run disruption with long-run scarring.

**Transfer.** Students redesign the exercise for one alternative setting: acute hospitalization, employer accommodation access, treatment expansion, disability-program threshold, or matched firm retention design. The transfer task keeps the labor outcome visible while changing the identification strategy.

## Methods Box

:::{admonition} Methods Box: Credible Causal Identification For Disability And Chronic Conditions
:class: note

**Name the health object.** Acute shock, diagnosis, functional limitation, chronic burden, disability certification, and benefit receipt are different empirical objects.

**Name the labor margin.** Employment, hours, earnings, occupation, job amenities, mobility, accommodation, benefit claiming, productivity, and welfare need not move together.

**Separate capacity from institutions.** Direct work-capacity effects differ from program incentives, treatment access, accommodation, local demand, and selection into application or receipt.

**Use timing aggressively.** Event studies around acute shocks or disability onset should show pre-trends, immediate disruption, medium-run adjustment, and long-run scarring.

**Use rules when the estimand is program response.** Examiner assignment, award thresholds, reassessments, earnings tests, and return-to-work reforms identify benefit or rule effects, not the total health cost for all impaired workers.

**Bring firms into the design.** Accommodation and retention are firm-side treatments. Matched employer-employee data can reveal heterogeneity that worker-only designs miss.

**Treat genetic and family designs as complements.** Twin, sibling, and Mendelian-randomization-style approaches help with endowments and chronic-condition channels, but they do not remove the need to interpret labor-market mechanisms.

:::

## Reading Ladder And References

**Core dynamic outcomes.** Start with Meyer and Mok for long-run disability effects on earnings, income, and consumption [@meyerMok2019].

**Accommodation and return-to-work.** Read Hill, Maestas, and Mullen on accommodation and labor supply, then use Zaresani for return-to-work policy and disability-program labor supply [@hillMaestasMullen2016; @zaresani2018].

**Program incentives.** Read Autor and Duggan for disability-roll growth and labor-market interaction, Maestas, Mullen, and Strand for SSDI receipt effects using examiner assignment, French and Song for DI receipt and labor supply, and Low and Pistaferri for the insurance-incentive tradeoff [@autorDuggan2003disabilityRolls; @maestasMullenStrand2013ssdi; @frenchSong2014; @lowPistaferri2015disability].

**Health shocks and timing.** Use Dobkin et al. and Garcia-Gomez et al. for severe health shocks, hospitalization, and dynamic labor-market consequences [@dobkinFinkelsteinKluenderNotowidigdo2018hospital; @garciaGomez2013; @garciaGomezJonesRice2013].

**Employer response, job lock, and monopsony mechanisms.** Use Madrian for health-insurance job lock, Ameri et al. for hiring barriers, and Biro et al. for firm-side buffering of health shocks [@madrian1994; @ameriSchurAdyaBentleyEtAl2018; @biroGerardGyetvaiPapp2024].

**Frontier methods.** Use Bound's measurement critique, Collischon-Hiesinger-Pohlan for administrative onset evidence, and Bockerman-Cawley plus von Hinke and Kessler Scholder for genetic and MR-style designs [@bound1991; @collischonHiesingerPohlan2023; @bockermanCawley2018; @vonHinkeKesslerScholder2016].

## Exercises And Discussion Prompts

1. Why can the same chronic condition have small short-run employment effects but large long-run earnings or welfare losses?
2. Pick one disability measure. What part is direct work capacity, what part is program interaction, and what part is selection?
3. In what sense are accommodation, treatment, and return-to-work policy part of labor-market adjustment rather than outside interventions?
4. How can disability or chronic illness create monopsony power even when local employer concentration is low?
5. Compare an acute health-shock event study with a disability-program threshold design. What does each identify, and what does each miss?
6. Design a matched employer-employee study of accommodations. What worker sorting and firm-selection threats would remain?
7. Why might a lower quit rate among workers with chronic conditions be a warning sign rather than evidence of better job matches?

## Reproducibility And Code Lab Note

The Week 2 code lab lives at `labs/02-disability-chronic-conditions-labor-supply-and-job-choice/`. It is a bounded synthetic teaching path, not an official replication of Meyer and Mok or Hill, Maestas, and Mullen. The smoke path creates deterministic worker-event data; estimates a compact disability-onset event-study profile; diagnoses capacity, program, accommodation, demand, and selection channels; and transfers the design logic to acute shocks, treatment access, program thresholds, and matched-firm accommodation settings.

The lab is conservative by design. It does not claim access to official administrative records, survey panels, disability-program files, or employer accommodation records.

## Slide Companion Note

The Week 2 slide deck lives at `slides/week2/02-disability-chronic-conditions-labor-supply-and-job-choice.tex`. The deck mirrors the chapter logic without duplicating the prose: it defines disability and chronic conditions as dynamic labor-market constraints; separates direct capacity effects from program incentives; contrasts short-run and long-run effects; highlights treatment, accommodation, and return-to-work investments; frames monopsony and job lock as labor-market mechanisms; introduces frontier methods; and closes with the Research Lab workflow.

## Bridge Forward

Week 3 moves from working-age disability and chronic conditions to fertility, mortality, caregiving, and lifecycle labor allocation. The transition broadens the unit of analysis from the worker-employer match to household timing, family shocks, caregiving burdens, and demographic structure. The Week 2 lesson carries forward: health and population events matter for labor economics when they change feasible work, job choice, hours, mobility, wages, firm response, and worker welfare over time.
