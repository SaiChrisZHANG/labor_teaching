# Worker Adjustment, Skills, Training, And Career Transitions

## Learning Objectives

By the end of Week 3, students should be able to:

1. explain why technology shocks are worker-adjustment problems, not only labor-demand shocks;
2. distinguish early skill and field choices, within-firm retraining, between-job mobility, and later-career exit as separate adjustment margins;
3. explain how aggregate labor-market adaptation can coexist with persistent earnings, employment, and welfare losses for particular workers;
4. evaluate training, retraining, and skill accumulation evidence while recognizing selection, measurement, and dynamic-outcome problems;
5. compare frontier empirical designs for studying worker adjustment, including admissions cutoffs, centralized assignment, matched employer-worker event studies, local exposure designs, worker-level patent or task exposure, and training evaluations;
6. analyze how distrust, inertia, present bias, limited memory, information frictions, switching costs, and unequal access to training can amplify inequality after technological change.

The central supply-side question is this: when technology changes task prices and career risk, which workers can adjust through skills, training, mobility, or job redesign, and which workers bear persistent losses?

## Opening Orientation

Week 2 studied automation and AI as labor-demand shocks. It asked which tasks are displaced, which workers are augmented, and how employment and wages move when firms adopt new technologies. Week 3 turns to the other side of the same market. Once task demand moves, workers have to decide whether to learn, retrain, search, switch occupations, move employers, relocate, bargain over a redesigned job, or exit work.

The main lesson is that aggregate adjustment is not the same as worker welfare. A local labor market can recover employment, firms can fill new vacancies, and the wage distribution can re-sort while displaced workers still suffer long earnings losses, skill depreciation, nonemployment, lost firm-specific rents, or costly transitions. This distinction is central for labor economics because the relevant object is not only whether the economy eventually reallocates labor. It is who pays the adjustment cost along the way.

This week separates three worker-side margins. First, workers make **early skill choices** through majors, fields, vocational tracks, and occupational entry. Second, incumbents face **within-firm adaptation** through retraining, task reassignment, and learning around new tools. Third, workers face **later-career transitions** through employer switching, occupational mobility, geographic movement, unemployment, disability, or retirement. Technology can change all three, but each margin requires different data and a different empirical design.

:::{admonition} Core points
:class: important

- Worker adjustment is central because technology changes the return to existing skills, the value of new skills, and the risk attached to particular careers.
- Aggregate labor-market adjustment and individual incidence are different objects. A market can reallocate while exposed workers experience persistent earnings and welfare losses.
- Early field choice, within-firm retraining, occupational switching, and retirement are separate margins. Treating them as one generic "reskilling" response hides the economics.
- Training and skill accumulation are hard to measure. Strong designs need credible exposure, clear adjustment margins, dynamic worker outcomes, and attention to selection.
- Frictions such as distrust, skepticism, inertia, present bias, limited memory, information failures, liquidity constraints, and switching costs can slow adjustment and widen inequality.

:::

## Bridge

The course now moves from demand incidence to supply response. Week 1 gave the general map: technology changes tasks, tasks change skill demand and organization, and workers and firms adjust before equilibrium outcomes appear. Week 2 concentrated on the labor-demand side of that map. Week 3 asks what happens after exposed workers confront a new task frontier.

This is not a generic education lecture. Education, training, and human capital matter here because they shape workers' exposure to technological change and their capacity to move when old tasks lose value. The relevant labor objects are skill portability, task-specific human capital, training access, occupational mobility, job ladders, employer attachment, search costs, earnings losses, and welfare. The literature is especially challenging because many adjustment margins are private, dynamic, and partly unobserved. A worker who does not enroll in training may be uninformed, liquidity constrained, skeptical of the program, near retirement, attached to a local labor market, or rationally responding to low expected returns.

The week also adds a methodological discipline that students will need for the rest of the course. A strong worker-adjustment paper must state the technology shock, define the exposed workers, identify the adjustment margin, observe outcomes over time, and say whether the estimate captures causal adjustment or selection into better fields, firms, or training opportunities.

## Field Core

### A Worker-Adjustment Framework

Start with a technology shock that changes the value of tasks. Let worker {math}`i` have a current task bundle, skill vector, employer match, and local labor-market environment. A technology can lower the price of some tasks, raise the productivity of other tasks, or create demand for new tasks. The worker's adjustment problem can be written as:

```{math}
:label: eq:st5-w3-worker-value
V_{it}
=
w_{it}(s_{it}, o_{it}, f_{it}, \tau_t)
- c_i(a_{it})
- \kappa_i(m_{it})
+ E_t \sum_{r=t+1}^{T} \beta^{r-t} u_{ir},
```

where {math}`s_{it}` denotes skills, {math}`o_{it}` occupation, {math}`f_{it}` employer, {math}`\tau_t` the technology environment, {math}`a_{it}` adjustment effort such as training or learning, and {math}`m_{it}` mobility such as employer, occupation, sector, or location switching. The terms {math}`c_i(a_{it})` and {math}`\kappa_i(m_{it})` are central: adjustment can be costly even when the destination job is better.

Equation {eq}`eq:st5-w3-worker-value` is not meant to be estimated directly. It organizes the margins that empirical work has to observe. Technology changes current wages, the expected value of future skills, the probability of remaining employed, the option value of training, and the cost of switching. The worker may adjust through one of several channels:

1. **early skill choice**, including field of study, major, vocational track, or initial occupation;
2. **within-job adaptation**, including employer-provided training, learning by doing, task reassignment, or tool adoption;
3. **between-job mobility**, including employer switching, occupational switching, sectoral reallocation, or migration;
4. **labor-force exit**, including unemployment, disability, early retirement, or delayed reentry.

```{include} assets/tables/03-adjustment-margins-map.md
```

The object of interest is not simply whether workers move. Mobility can be evidence of successful adjustment, but it can also be evidence of displacement. Staying can mean adaptation inside a productive firm, but it can also mean being trapped in declining work. A worker-adjustment design has to interpret movement, nonmovement, and exit together.

### Skill Specificity, Portability, And Career Risk

Technology makes some skills more portable and others more fragile. A portable skill is valuable across firms, occupations, or technologies: analytical reasoning, social coordination, troubleshooting, quantitative problem solving, or the ability to learn new tools. A specific skill is valuable inside a narrower task bundle, employer, occupation, software environment, or production technology. Specific skills can have high returns before a shock and sharp losses afterward.

Deming and Noray frame STEM careers as a setting where the skill frontier moves quickly [@demingNoray2020]. The point is not that STEM is bad or that non-STEM is safe. The point is that returns to a field can depend on continual updating. Entry into a technology-intensive occupation may raise early earnings but also expose workers to faster skill obsolescence if tasks, tools, or programming languages change.

This logic generalizes beyond STEM. Production workers can have machine-specific skills. Clerical workers can have software-specific routines. Health workers can have workflow-specific administrative knowledge. Platform workers can have system-specific ratings and search knowledge. When technology changes the task environment, workers lose not only a wage in the current job. They can lose the value of accumulated knowledge, the option value of staying with an employer, and the credibility of their experience in a new labor market.

This is why the course separates **task exposure** from **skill portability**. A task exposure measure predicts which work can be automated or augmented. A skill-portability measure asks whether the worker can redeploy existing human capital when tasks move. Two workers with the same exposure can face very different welfare costs if one has portable skills and the other has highly specific skills.

### Early Choices: Fields, Majors, And Vocational Tracks

Early choices shape later technology exposure. Field of study, college major, vocational track, apprenticeship, and first occupation all influence the task bundles workers enter and the skills they accumulate. The empirical challenge is that students select into fields based on ability, preferences, information, family resources, local institutions, and expectations. Observed earnings differences across majors or vocational tracks are therefore not enough.

One frontier design family uses cutoffs and centralized assignment. Kirkeboen, Leuven, and Mogstad use discontinuities in field assignment to estimate long-run returns to fields of study in secondary school [@kirkeboenLeuvenMogstad2021]. Silliman uses centralized vocational secondary admissions to study labor-market returns to vocational education [@silliman2022]. Bleemer and Mehta use a college-major regression discontinuity to estimate how access to economics changes major choice and earnings [@bleemerMehta2022].

These papers are not all narrow technology-adoption papers. They matter this week because they show what credible evidence on skill pathways can look like. If technology changes returns across tasks, then field access and major assignment can affect future exposure, occupational options, and resilience. A cutoff design is powerful because it compares students near an admission threshold who are plausibly similar but enter different training paths. Its limitation is equally important: the estimand is local to applicants near the cutoff and captures an early-choice margin, not the later-career worker who is displaced after twenty years in a specific occupation.

### Training And Retraining As Adjustment Margins

Training is the adjustment margin students often name first and measure last. It can occur through formal programs, community colleges, vocational providers, apprenticeships, employer courses, peer learning, online tools, or informal learning by doing. It can be worker-financed, firm-financed, publicly subsidized, or embedded in job redesign. It can help incumbents adapt, or it can screen workers who were already likely to succeed.

The empirical problem is that training take-up is selected. Workers who enroll may have stronger motivation, better information, more time, better credit access, higher expected returns, or employers willing to invest in them. Firms that train may be higher-productivity firms with better management and lower separation risk. A before-after comparison of trained workers therefore confounds training with selection unless the design has credible assignment, policy variation, eligibility rules, or linked administrative histories.

Bertermann's work is useful because it treats training and retirement as explicit responses to trade and technology shocks in local labor markets [@bertermann2025]. The key idea is that adjustment can occur through human-capital investment or through withdrawal from the labor force. Muehlemann studies AI adoption and workplace training, showing why incumbent training, new-hire training, and firm reorganization have to be separated [@muehlemann2024]. If AI adoption leads firms to train new hires but not exposed incumbents, aggregate skill upgrading can coexist with worker-level displacement.

The policy implication is subtle. "More training" is not a complete answer unless the design tells us who receives it, what skill is produced, whether the skill is portable, whether earnings recover, and whether nonparticipants are left worse off. Training can reduce inequality if it reaches exposed workers with high adjustment costs. It can widen inequality if high-skill workers, young workers, or workers at productive firms capture most of the opportunity.

### Within-Firm Adaptation And Matched Employer-Worker Evidence

Many technology shocks are implemented inside firms. Workers do not simply meet an abstract market price; they meet a manager, a new software system, a robot cell, an AI tool, a redesigned workflow, or a new promotion ladder. Matched employer-worker data are therefore central for this week because they let researchers observe workers before and after adoption while tracking whether they stay, move, or exit.

Genz studies worker adjustment when firms adopt new technologies, using matched employer-worker evidence to separate within-firm adaptation from worker exits and selection [@genz2021]. Kogan, Papanikolaou, Schmidt, and Seegmiller link labor-displacing technology exposure from patents to worker outcomes, showing how exposure can be measured closer to the worker rather than only at the occupation or place level [@koganPapanikolaouSchmidtSeegmiller2021]. These designs move the field beyond repeated cross-sections because they can ask who was exposed before the shock, who remained attached to an adopting firm, and how earnings evolved afterward.

The main identification challenge is adoption timing. Firms do not adopt technology randomly. Early adopters can be more productive, better managed, more skill-intensive, and already on a different growth path. Workers at adopters can also differ from workers at nonadopters. A credible event-study design therefore needs pre-trend checks, worker and firm histories, attention to composition, and a clear distinction between the effect of adoption on incumbents and the selection of workers into adopting firms.

### Later-Career Mobility, Displacement, And Welfare Costs

Later-career adjustment is often the hardest and most welfare-relevant margin. Older workers may have more occupation-specific or firm-specific human capital, shorter horizons over which to recover training investments, stronger family and housing ties, and weaker incentives for firms to retrain them. Displacement can therefore generate persistent losses even if the market eventually creates replacement jobs.

The welfare cost of technology-induced displacement is broader than the first lost paycheck. Workers can lose firm wage premia, seniority, health insurance, predictable schedules, commute routines, occupational identity, and the option value of future promotions. They may reenter at lower wages, cycle through unstable jobs, accept poorer amenities, or leave the labor force. The market-level employment rate can recover while the original exposed workers remain below their counterfactual earnings path.

A simple dynamic incidence object is:

```{math}
:label: eq:st5-w3-displacement-loss
Loss_i(H)
=
\sum_{h=0}^{H} \beta^h
\left[
Y_{i,t+h}^{0} - Y_{i,t+h}^{1}
\right],
```

where {math}`Y^0` is the worker's counterfactual outcome without the technology shock or displacement event and {math}`Y^1` is the observed outcome after exposure. The outcome can be earnings, employment, hours, job quality, or a welfare index. The equation highlights why short-run estimates can understate or misstate the object of interest. A worker may find a job quickly but lose earnings for years. Another may remain employed but lose task autonomy, promotion prospects, or bargaining power.

This distinction also disciplines the aggregate story. Reallocation can be efficient in the long run and still impose concentrated transition costs. A labor economist should therefore ask two questions at once: what is the new allocation of work, and who bears the cost of moving there?

### Frictions In Worker Adjustment And Inequality

Technology adjustment is often narrated as if workers see a new skill price, invest, and move. The empirical literature is more complicated. Workers can fail to adjust even when a simple earnings comparison suggests they should. The reasons include information, behavior, finance, institutions, and identity.

```{include} assets/tables/03-adjustment-frictions-and-inequality-map.md
```

**Distrust and skepticism.** Workers may distrust new technologies, training providers, employers, platforms, or public programs. Skepticism can be rational if workers have seen low-quality programs, unstable tools, biased algorithms, or firms use training rhetoric while replacing incumbents. It can also slow beneficial adjustment if workers underweight credible opportunities.

**Inertia, present bias, and limited memory.** Adjustment has immediate costs and delayed benefits. Workers may postpone training, fail to complete programs, or avoid learning new tools because current work and family demands dominate a future return. Evidence on inertia, limited memory, and distrust in technology adoption provides a useful behavioral lens, even when the exact empirical setting is managerial rather than worker retraining [@gertlerJohnsonVillarreal2025].

**Information frictions.** Workers may not know which skills are becoming valuable, which programs are credible, which employers reward new skills, or how exposed their current tasks are. Better-connected workers and workers in high-information firms may adjust earlier, while isolated workers discover the shock after demand has already moved.

**Adjustment costs and switching frictions.** Training takes time, money, attention, and risk. Switching occupations can require credentialing, search, references, geographic mobility, or a temporary wage cut. Moving places can require housing liquidity, spousal employment, school changes, and social-network losses. These costs are not incidental. They determine whether theoretical reallocation becomes feasible for actual workers.

**Inequality implications.** Adjustment frictions are stratified. Younger, wealthier, higher-educated, and better-connected workers often have more time, liquidity, information, and employer support. Older workers, workers in highly specific occupations, workers in declining local labor markets, and workers with care responsibilities may face higher costs and shorter payoff horizons. Technology can therefore widen inequality not only by changing task demand, but by making adjustment easier for already advantaged workers.

### Research Architecture: From Technology Shock To Worker Incidence

A disciplined worker-adjustment study names six objects:

1. **Technology shock.** Is the relevant shock robots, AI, software, digital tools, patents, task automation, or a broader local technology exposure?
2. **Exposed worker group.** Are workers exposed through occupation, firm, industry, local labor market, field of study, or observed tasks?
3. **Adjustment margin.** Is the response training, retraining, major choice, employer switching, occupational mobility, within-firm reassignment, migration, retirement, or nonemployment?
4. **Outcome horizon.** Are outcomes measured immediately, over several years, or over a career?
5. **Counterfactual.** What would have happened to the same workers without exposure, without training, or without access to the field?
6. **Welfare object.** Does the design measure earnings, employment, hours, job quality, amenities, uncertainty, identity, or a broader welfare cost?

This architecture keeps the week labor-focused. The point is not to declare that technology requires more education in general. It is to ask which skills are becoming more valuable, which workers can acquire or redeploy them, which institutions lower adjustment costs, and which workers remain exposed to persistent losses.

## Research Lab

The Week 3 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Kogan, Papanikolaou, Schmidt, and Seegmiller's worker-level exposure logic linking labor-displacing technologies from patents to worker outcomes [@koganPapanikolaouSchmidtSeegmiller2021]. The challenge transfer uses training and retirement responses inspired by Bertermann [@bertermann2025] and AI-related training differences inspired by Muehlemann [@muehlemann2024].

The lab is not an official replication of any paper. No official replication package, patent-worker microdata, German administrative data, or firm training microdata are bundled locally. The teaching path uses deterministic synthetic data to practice the design logic: constructing worker exposure, diagnosing worker incidence, and transferring the framework to training and retirement margins.

**Reproduce.** Students construct a worker-level technology exposure measure by combining worker task shares with technology weights inspired by patent/task exposure logic. They estimate how exposure relates to earnings change, employment stability, and occupational switching in a synthetic worker panel. The goal is to reproduce the structure of a worker-level exposure design, not official estimates.

**Diagnose.** Students classify whether each exposed worker appears to adjust through staying, training, switching, unemployment, or exit. They compare worker-level exposure with firm-level adoption and local adjustment capacity. The diagnosis asks whether an observed earnings loss is best interpreted as direct displacement, low skill portability, weak training access, or selection into exposed firms.

**Transfer.** Students move the logic to two related settings. First, they compare training and early-retirement responses under local technology exposure. Second, they compare incumbent training and new-hire training under AI adoption. The transfer exercise asks when aggregate skill upgrading can hide persistent losses for exposed incumbents.

## Methods Box

Worker adjustment is difficult to study because skills are multidimensional, training is selected, technologies are partially observed, and outcomes are dynamic. Strong designs in this literature do not treat "reskilling" as a black box. They identify a specific margin and make the counterfactual visible.

```{include} assets/tables/03-frontier-methods-box.md
```

:::{admonition} Methods Box: What Strong Designs Look Like
:class: note

**College, major, and track cutoff RD.** Cutoff and centralized-assignment designs use discontinuities in access to fields, majors, or vocational tracks. They are strongest for causal returns to early skill pathways and weaker for later-career displacement unless linked to later technology exposure [@kirkeboenLeuvenMogstad2021; @silliman2022; @bleemerMehta2022].

**Training and retraining evaluations.** Strong evaluations use randomized offers, eligibility thresholds, policy rollouts, or administrative assignment rules. They should measure take-up, completion, employment, earnings, job quality, and persistence. The central threat is that motivated workers and better firms select into training.

**Matched employer-worker event studies around technology adoption.** These designs observe incumbent workers before and after firm adoption. They can separate retention, exit, wage growth, occupational mobility, and internal task reassignment, but they must address adopter selection and differential pre-trends [@genz2021].

**Local exposure designs linked to training or retirement.** These designs combine local technology, trade, or task exposure with administrative records on training, unemployment, retirement, or mobility. They identify equilibrium adjustment in places, not pure individual treatment effects, and should be interpreted accordingly [@bertermann2025].

**Worker-level patent, task, or exposure measures.** These measures attach technology exposure to workers using patents, tasks, occupations, firms, or skill histories. They are valuable because they move incidence closer to the worker, but the exposure mapping must be transparent and validated [@koganPapanikolaouSchmidtSeegmiller2021; @almeidaDixCarneiro2025].

**Firm AI adoption and task-content panels.** Recent data on AI adoption, vacancy text, surveys, and task content can distinguish incumbent retraining, new-hire skill demand, and job redesign. The advantage is proximity to implementation; the risk is short horizons, measurement noise, and selection into early adoption [@muehlemann2024; @babinaFedykHeHodson2024].

:::

The design lesson is simple but demanding. A good worker-adjustment paper must say whether it identifies access to a skill pathway, exposure to a technology, take-up of training, adoption by a firm, equilibrium adjustment in a place, or realized use by a worker. These are different treatments.

## Reading Ladder And References

```{include} assets/tables/03-reading-and-lab-map.md
```

**Core framing.** Start with Autor's automation overview and Deming and Noray on STEM careers and technological change to see why task change creates dynamic career risk [@autor2015; @demingNoray2020].

**Worker-level incidence.** Read Kogan, Papanikolaou, Schmidt, and Seegmiller as the primary worker-exposure anchor [@koganPapanikolaouSchmidtSeegmiller2021].

**Within-firm adaptation.** Use Genz to study how matched employer-worker data can reveal retention, exits, and earnings after firm technology adoption [@genz2021].

**Training, retirement, and AI adoption.** Read Bertermann for training and retirement as alternative adjustment margins, and Muehlemann for contemporary AI adoption and workplace training [@bertermann2025; @muehlemann2024].

**Early skill pathways.** Use Kirkeboen-Leuven-Mogstad, Silliman, and Bleemer-Mehta to understand strong field, track, and major designs [@kirkeboenLeuvenMogstad2021; @silliman2022; @bleemerMehta2022].

**Frontier measurement and frictions.** Use Almeida and Dix-Carneiro for digital task change, Smeets for skill specificity and disruption, and Gertler-Johnson-Villarreal for behavioral frictions around technology adoption [@almeidaDixCarneiro2025; @smeets2025; @gertlerJohnsonVillarreal2025].

## Exercises And Discussion Prompts

1. Explain how a labor market can adjust in aggregate while displaced workers experience persistent welfare losses. Name at least three margins that would be missed by an employment-only outcome.
2. Compare a centralized admissions RD with a matched employer-worker adoption event study. What adjustment margin does each identify well, and what does each leave offstage?
3. Design a training evaluation for workers exposed to AI-driven task change. What is the treatment, who is eligible, what is the counterfactual, and what dynamic outcomes would you measure?
4. Suppose a firm adopts AI and reports higher average wages two years later. Give three reasons this may not imply incumbent workers benefited.
5. Choose an occupation exposed to automation or AI. Separate early skill choices, within-firm adaptation, and later-career mobility responses for workers in that occupation.
6. How can distrust, present bias, limited memory, or information frictions make adjustment policy less effective? What design would let you distinguish low returns from low take-up?

## Reproducibility And Code Lab Note

The Week 3 code lab lives at `labs/03-worker-adjustment-skills-training-and-career-transitions/`. It is a bounded synthetic teaching path. The smoke path constructs worker-level task exposure, writes a compact exposure-outcome table, diagnoses adjustment margins, and transfers the logic to training, retirement, and AI adoption settings. It requires no external downloads, confidential worker records, patent microdata, administrative training files, or official replication materials.

## Slide Companion Note

The Week 3 slide deck lives at `slides/week3/03-worker-adjustment-skills-training-and-career-transitions.tex`. The deck presents the chapter logic without duplicating the prose: it starts from the supply-side question, separates adjustment margins, emphasizes aggregate adjustment versus worker losses, includes a methods/design slide, includes a worker-frictions slide, and closes with the Reproduce -> Diagnose -> Transfer lab design.

## Bridge Forward

Week 4 moves inside firms. Week 3 treated workers as the unit that must adjust through skills, training, mobility, and career transitions. Week 4 asks how firms shape those possibilities through adoption decisions, hiring, management, internal labor markets, job redesign, monitoring, and organizational complements. The worker-side lesson carries forward: technology adoption is not complete when the tool arrives. It becomes a labor-market event when firms decide which workers to retrain, which tasks to reorganize, which workers to hire, and which workers to leave behind.
