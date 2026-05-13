# Automation, AI, And Labor Demand

## Learning Objectives

By the end of Week 2, students should be able to:

1. separate displacement, augmentation, output-demand effects, and new-task creation as labor-demand channels;
2. explain why automation and AI can affect employment, wages, vacancies, and worker mobility differently;
3. identify the relevant unit of incidence: occupations, establishments, firms, industries, and local labor markets;
4. compare modern AI and robotics evidence with earlier literatures on mechanization, electrification, computerization, and occupational churn;
5. evaluate robot exposure, task exposure, AI exposure, patent or text exposure, firm adoption, vacancy text, and worker-use data as distinct empirical objects;
6. design a bounded labor-demand replication or transfer exercise that names the technology margin, exposure mapping, outcome, and equilibrium channel.

The core labor-demand question is this: when automation or AI changes production, which tasks and workers are displaced, which are augmented, when do productivity and output effects offset displacement, and when does new-task creation move labor demand into different work?

## Opening Orientation

Week 1 established the course's discipline: technology becomes a labor-economics object when it changes task content, skill demand, firm organization, wages, employment, mobility, or worker welfare. Week 2 applies that discipline to automation and AI as labor-demand shocks. The lecture is not about whether "AI" is good or bad in the abstract. It is about the incidence of changing task demand across workers, occupations, establishments, firms, industries, and local labor markets.

Modern AI research should be read inside a longer labor-demand literature. Mechanization changed the demand for human and machine power; electrification changed production organization; computerization changed routine cognitive and clerical work; robotics made embodied automation measurable; generative AI now reaches some cognitive and language tasks with unusually granular usage data. The novelty is real, but it does not erase the older logic: displacement, productivity, scale, reorganization, and new work have always had to be separated [@autorLevyMurnane2003SkillContent; @goldinKatz1998origins; @autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks].

:::{admonition} Core points
:class: important

- Automation and AI affect labor demand through four linked channels: displacement, augmentation, output-demand expansion, and new-task creation.
- Employment and wages can move differently because technology changes task composition, worker bargaining positions, firm growth, vacancies, and local adjustment at the same time.
- The unit of incidence matters. A technology can reduce demand for a task, raise employment at adopting firms, and lower wages in exposed local labor markets.
- Historical comparison disciplines the AI debate. Mechanization, electrification, computerization, robotics, and generative AI differ in measurement and speed, but all require the same labor-demand accounting.
- Measurement is first order. Robots, tasks, AI exposure, patents, firm adoption, job postings, and worker-use data identify different margins and should not be interpreted as interchangeable treatments.

:::

## Bridge

The Week 1 task framework ran from technology to task content, then to skill demand and organization, then to worker and firm adjustment, and finally to equilibrium outcomes. Week 2 zooms in on the first major substantive application: labor demand. The question is not only whether a technology "substitutes" for labor. It is where substitution occurs, whether other tasks become more valuable, whether productivity raises product demand, whether firms reorganize, and whether new tasks expand the domain of work [@autorLevyMurnane2003SkillContent; @acemogluAutor2011SkillsTasks; @autor2015Jobs].

This focus keeps the lecture labor-centered. Robots, software, and AI are important here because they change the marginal value of tasks, the composition of vacancies, the demand for skills, the organization of firms, and the distribution of wages and employment. Macro forecasts, technology taxonomies, and industry narratives enter only when they help explain labor-demand incidence.

## Field Core

### A Compact Theoretical Backbone

Start from a task production view. Output uses a set of tasks {math}`k \in K`. Some tasks are performed by labor, some by capital, software, robots, or AI systems, and some by teams that combine workers with technology. Let {math}`s_{ok}` denote the share of task {math}`k` in occupation {math}`o`, and let {math}`\theta_k` denote how much a technology changes the cost or productivity of performing task {math}`k`. A simple exposure object is:

```{math}
:label: eq:st5-w2-task-exposure
Exposure_o = \sum_{k \in K} s_{ok} \theta_k.
```

Equation {eq}`eq:st5-w2-task-exposure` is not a treatment effect. It is a mapping from task content to predicted exposure. A labor-demand effect requires an outcome, a counterfactual, and an adjustment horizon.

A useful demand accounting decomposition separates four channels:

```{math}
:label: eq:st5-w2-demand-decomposition
\Delta L =
\underbrace{\Delta L^{disp}}_{\text{tasks substituted away}}
+
\underbrace{\Delta L^{aug}}_{\text{workers more productive in remaining tasks}}
+
\underbrace{\Delta L^{scale}}_{\text{output demand and firm growth}}
+
\underbrace{\Delta L^{new}}_{\text{new tasks and occupations}}.
```

The terms in equation {eq}`eq:st5-w2-demand-decomposition` can have different signs. Displacement reduces labor demand in tasks that become automated. Augmentation can raise the marginal product of workers in tasks that remain human-performed. Scale effects depend on whether productivity gains lower prices, expand output, and increase demand for complementary labor. New-task creation reinstates labor demand in activities that did not previously exist or did not previously have economic value [@autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks; @autorChinSalomonsSeegmiller2024NewWork].

```{include} assets/tables/02-demand-channels-map.md
```

This backbone turns a broad automation question into concrete labor-demand questions:

1. Which tasks are directly displaced?
2. Which tasks are complemented or augmented?
3. Which firms or industries expand output enough to hire more workers?
4. Which new tasks, occupations, or job designs appear?
5. Which workers bear transition costs before the new allocation is reached?

### Labor-Demand Incidence Across Units

Automation and AI are not single-level treatments. They can appear at one level and produce outcomes at another.

At the **occupation** level, exposure depends on task content. Routine production, routine clerical, prediction, classification, language drafting, coding, and customer support tasks can be exposed in very different ways. The task approach of Autor, Levy, and Murnane remains the central bridge from technology to occupation-level labor demand [@autorLevyMurnane2003SkillContent].

At the **establishment or firm** level, adoption is an organizational choice. Firms decide whether to install robots, buy software, deploy AI tools, redesign jobs, train workers, change hiring, or expand output. Firm-level evidence can therefore show employment gains at adopters even when a local-market exposure design shows displacement for some workers [@acemogluLelargeRestrepo2020competingRobots; @aghionBergeaudBoppartKlenowLi2025differentUsesAI].

At the **industry** level, automation can shift input mix, productivity, output prices, and product demand. Graetz and Michaels use cross-country industry robot adoption to study how robots affect productivity, wages, and labor shares at a sectoral scale [@graetzMichaels2018Robots].

At the **local labor-market** level, exposure aggregates industry and occupation composition into commuting-zone incidence. Local designs ask whether workers in exposed places experience lower employment, wages, or labor-force participation after technology shocks [@acemogluRestrepo2020Robots; @dauthFindeisenSuedekumWoessner2021Robots].

The interpretation rule is that these units answer different questions. An occupation exposure measure asks which job bundles are technically susceptible. A firm adoption measure asks what adopters do. An industry measure asks how a production sector changes. A local exposure measure asks who is exposed in equilibrium through the regional structure of work.

### Causal Incidence: Why Employment And Wages Can Move Differently

Employment and wages do not have to move in the same direction after a technology shock. A technology can reduce employment in exposed tasks while raising wages for complementary workers. It can raise productivity and sales at adopting firms while lowering demand for routine tasks in the local labor market. It can increase vacancies for AI-complementary skills while weakening the bargaining position of workers whose old tasks have become easier to substitute.

A reduced-form design often has the form:

```{math}
:label: eq:st5-w2-incidence-design
\Delta Y_{g t}
=
\beta Exposure_{g t}
+ X_{g t}'\Gamma
+ \delta_t
+ \alpha_g
+ \varepsilon_{g t},
```

where {math}`g` can be an occupation, firm, industry, or local labor market, and {math}`Y` can be employment, wages, vacancies, occupational shares, sales, training, or mobility. The coefficient {math}`\beta` is only interpretable after the exposure object and unit are named.

There are at least five reasons employment and wage estimates can diverge.

First, **task displacement** can lower employment in exposed tasks while wages among remaining workers rise if surviving jobs are more skill-intensive. Second, **augmentation** can raise worker productivity without creating many new jobs if output demand is inelastic. Third, **scale effects** can expand employment at firms or industries even when the directly automated task shrinks. Fourth, **composition effects** can raise average wages because low-wage jobs disappear or high-wage complementary jobs grow. Fifth, **bargaining and rent-sharing** can shift wages even when employment changes are modest [@acemogluRestrepo2020Robots; @hampoleMontesOberfield2025].

This is why "AI raises productivity" is not yet a labor-demand conclusion. A productivity gain can become higher wages, higher profits, lower prices, more output, less employment, more employment in complementary tasks, or a changed job ladder. The empirical design has to say which margin is visible.

### Measurement: Technology Proxies Identify Different Margins

Measurement is one of the central research problems in this lecture. "Technology" is almost never observed as a clean treatment. Researchers instead observe proxies that sit at different points between invention, exposure, adoption, use, and reorganization.

```{include} assets/tables/02-technology-measurement-and-identification-map.md
```

**Robot exposure** is concrete and interpretable. It measures embodied automation capital and is especially useful for production and manufacturing tasks. Its limitation is scope: robot data miss software, AI, and many forms of workplace reorganization [@acemogluRestrepo2020Robots; @graetzMichaels2018Robots].

**Task exposure** links theory to occupation content. It asks whether the tasks inside an occupation are susceptible to substitution or augmentation. Its limitation is that exposure is not adoption; a task can be technically exposed without a firm actually changing production [@autorLevyMurnane2003SkillContent; @feltenRajSeamans2021AIExposure].

**AI exposure** measures, including task-based and capability-based indices, often ask whether AI can perform, assist, or transform the tasks workers do. These measures are valuable before broad adoption is visible, but they can overstate realized labor-market change if firms face adoption costs, legal constraints, data limits, or organizational frictions [@webb2020; @agrawalGansGoldfarb2019].

**Patent and text-based exposure** measures are close to the innovation frontier. They can connect technical content to occupations or workers, but they often identify the direction of invention rather than realized workplace use [@koganPapanikolaouSchmidtSeegmiller2023].

**Firm adoption** measures are closer to treatment because they observe implementation. They make selection into adoption central: early adopters may already be larger, faster-growing, better managed, or more skill-intensive [@babinaFedykHe2024; @aghionBergeaudBoppartKlenowLi2025differentUsesAI].

**Job-posting and vacancy measures** reveal desired skill demand and job redesign intentions. They are useful for studying early changes in labor demand, but postings are not employment, realized wages, or worker welfare [@acemogluAutorHazellRestrepo2022AIJobs; @huiReshefZhou2025shortTermGenAI].

**Worker-level productivity or use data** move closest to realized AI use inside jobs. They can reveal who is augmented and in which tasks, but they often come from narrow settings and short horizons [@brynjolfssonLiRaymond2025GenerativeAI; @noyZhang2023GenerativeAI; @dellAcquaEtAl2026JaggedFrontier].

The same occupation can look highly exposed in a patent-text measure, modestly exposed in a robot measure, and rapidly changing in vacancy data. That disagreement is not necessarily a problem. It can reveal that invention, embodied adoption, desired hiring, and realized use are moving at different speeds.

### Historical Comparison: AI Inside The Longer Labor-Demand Literature

Modern AI and robotics research is not outside the older technology-and-labor literature. It is the newest part of it. The comparison matters because it clarifies which claims are recurring features of technological change and which may be distinctive to AI.

```{include} assets/tables/02-historical-comparison-map.md
```

#### Mechanization, Steam Power, And Industrial Labor Demand

Steam-era and mechanization evidence shows the old version of the displacement/productivity problem. Inanimate power substituted for human and animal effort in some production tasks, but it also raised output capacity, changed plant size, and reorganized manufacturing work. The labor-demand question was never simply whether machines replaced workers. It was which manual tasks became less valuable, which supervisory and maintenance tasks became more valuable, which industries expanded, and which workers could move [@atackBatemanMargo2020inanimatePower; @mokyrVickersZiebarth2015historyAnxiety].

The lesson for AI is that automation anxiety is recurrent, but so is the need for a task-level accounting. Mechanization changed physical power and routinized production. AI changes some prediction, classification, language, coding, and coordination tasks. Both require asking where direct substitution is offset by output expansion and new work.

#### Electrification And Organizational Change

Electrification is a strong historical comparison because it was a general-purpose technology whose effects depended on complementary reorganization. Electric power did not simply replace steam power one machine at a time. It changed factory layout, workflow, capital use, and the timing of productivity gains. Labor demand shifted through organizational redesign, not only through the installation of a new input [@fiszbeinLafortuneVamplew2020electrification].

The AI analogy is direct. A firm does not obtain the full labor-demand effect of AI by subscribing to a model. It has to decide which tasks to automate, which workers to augment, how to change review and supervision, what data to expose to the system, which job ladders to redesign, and how to manage risk. This is why firm-level adoption evidence may look different from occupation exposure indices: the technology becomes economically relevant through organization.

#### Computerization, ICT, And Skill Demand

Computerization and ICT provide the direct parent literature for modern AI work. The routine-task framework showed that computers substitute for routine codifiable tasks while complementing abstract, analytical, and problem-solving work [@autorLevyMurnane2003SkillContent]. Goldin and Katz show that technology-skill complementarity has a longer historical arc in which education, capital, and production methods jointly shape wage structure [@goldinKatz1998origins].

This comparison is important because AI is often described as if it begins a wholly new labor-economics problem. It does not. AI changes the boundary of what is codifiable and automatable, especially in some cognitive and language tasks, but it still operates through task content, skill demand, organizational complements, and worker adjustment.

#### Robotics, Local Exposure, And Firm Heterogeneity

Robotics is the modern benchmark for concrete automation evidence. Robot data are not vague exposure measures; they observe a specific form of embodied automation. Local exposure designs show how industry composition translates robot adoption into regional employment and wage incidence [@acemogluRestrepo2020Robots]. Cross-country industry evidence connects robot adoption to productivity and labor outcomes [@graetzMichaels2018Robots]. Firm-level robot evidence then shows that adoption can interact with productivity, market share, and employment composition inside firms [@acemogluLelargeRestrepo2020competingRobots].

The AI comparison is that many AI measures are less physical and more text-based, posting-based, or usage-based. That can make AI evidence faster and more granular, but it also makes measurement harder. A robot installation is a clearer treatment than a vacancy asking for machine learning skills; a worker using generative AI is closer to realized use than an occupation-level exposure score.

#### Long-Run Occupational Churn And Technological Disruption

Long-run work on occupational change reminds us that technology changes the content of work over decades, not only in short event windows. New tasks and new occupations are a major part of labor-demand adjustment [@autorChinSalomonsSeegmiller2024NewWork]. Deming's work on technological disruption emphasizes that workers experience technology through changing tasks, shifting skill demand, and adjustment costs across cohorts and occupations [@deming2025technologicalDisruption].

The lesson for AI is humility about horizons. Short-run productivity studies can reveal augmentation. Vacancy data can reveal early demand signals. Local labor-market designs can reveal displacement. But the new-task margin may be slow, uneven, and difficult to observe until job titles, occupational classifications, and firm organization catch up.

### What Is Distinctive About AI, And What Is Not

AI may be distinctive in five ways.

First, it reaches some **cognitive and language tasks** that older automation measures did not capture well. Second, some AI tools have **low marginal deployment costs**, so diffusion may be faster in occupations where data, workflow, and governance barriers are low. Third, AI often works through **firm-level reorganization** rather than direct one-for-one machine substitution. Fourth, AI produces unusually rich **digital traces**: prompts, usage logs, vacancy text, software adoption, and worker-level productivity measures. Fifth, general-equilibrium effects are especially uncertain because the technology can change task boundaries in many sectors at once [@brynjolfssonLiRaymond2025GenerativeAI; @aghionBergeaudBoppartKlenowLi2025differentUsesAI; @huiReshefZhou2025shortTermGenAI].

But several features are not new. Technologies have long generated displacement fears, adoption lags, organizational complements, uneven incidence, skill-biased effects, and new tasks [@mokyrVickersZiebarth2015historyAnxiety; @autor2015Jobs; @deming2025technologicalDisruption]. The proper conclusion is not that AI is "just like" past technologies or that it is completely unprecedented. The correct labor-economics move is to locate the technology in a demand-channel map, choose the right measurement object, and state the incidence unit.

### Research Architecture For This Literature

A strong automation or AI labor-demand paper names five objects:

1. **Technology object.** Is the paper about robots, software, AI capabilities, generative AI use, patents, vacancies, or firm adoption?
2. **Exposure mapping.** How does the technology variable attach to tasks, occupations, firms, industries, or places?
3. **Outcome margin.** Is the outcome employment, wages, vacancies, task mix, productivity, sales, mobility, or job quality?
4. **Adjustment horizon.** Is the paper estimating immediate use, short-run adoption, medium-run local adjustment, or long-run occupational change?
5. **Equilibrium channel.** Which channels are inside the estimate and which are offstage?

```{include} assets/tables/02-frontier-and-reading-map.md
```

The empirical contribution is strongest when the paper does not overclaim. A local robot-exposure estimate is not a firm adoption effect. A firm AI-adoption estimate is not the general-equilibrium effect of AI. A worker productivity experiment is not a long-run wage incidence estimate. Each design is valuable because it illuminates a specific part of the labor-demand mechanism.

## Research Lab

The Week 2 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Acemoglu and Restrepo's robot exposure design for local labor markets [@acemogluRestrepo2020Robots]. The challenge paper is Aghion, Bergeaud, Boppart, Klenow, and Li's firm-level evidence on different uses of AI and labor demand in France [@aghionBergeaudBoppartKlenowLi2025differentUsesAI].

The lab is not an official replication of either paper. No official replication package or confidential microdata are bundled locally. The teaching path uses deterministic synthetic data to reproduce the logic of a shift-share local exposure design, diagnose incidence across employment and wages, and transfer the design logic to firm-level AI adoption.

**Reproduce.** Students construct a local robot exposure measure by combining synthetic commuting-zone industry shares with industry robot adoption intensity. They estimate and interpret a simple exposure-outcome relationship for employment and wages. The goal is to reproduce the structure of a local exposure design, not the official estimates.

**Diagnose.** Students classify why employment and wage effects differ across local labor markets. They separate direct displacement, wage pressure, composition, output-demand offsets, and local reallocation. They then explain why a commuting-zone coefficient is an equilibrium incidence object rather than a direct task-level treatment.

**Transfer.** Students move the same logic to firm AI adoption. They compare a firm adoption/use measure with an occupation-exposure measure and a vacancy AI-demand measure. The transfer exercise asks when firm-level AI adoption could raise employment even if task exposure predicts displacement for some workers.

## Methods Box

:::{admonition} Methods Box: Reading Automation And AI Labor-Demand Estimates
:class: note

**Exposure is not adoption.** Exposure predicts susceptibility. Adoption observes use. A design can be excellent while answering only one of these questions.

**Direct task effects are not equilibrium effects.** Automation can displace tasks while scale effects, new tasks, or local reallocation change aggregate employment.

**Wages and employment answer different incidence questions.** Employment tracks quantities; wages also reflect composition, productivity, bargaining, rents, and selection into surviving jobs.

**The unit changes the estimand.** Occupation, firm, industry, and local-market designs are not substitutes. They locate different adjustment margins.

**Historical comparison is a design tool.** Earlier technologies help identify which AI claims are new measurement opportunities and which are familiar demand-channel problems.

:::

## Reading Ladder And References

**Core task and demand framework.** Start with Autor, Levy, and Murnane, then read Autor and Acemoglu-Restrepo to separate task substitution, augmentation, productivity, and reinstatement [@autorLevyMurnane2003SkillContent; @autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks].

**Canonical robotics evidence.** Read Acemoglu and Restrepo for local labor-market incidence, Graetz and Michaels for industry-level robot adoption, and Acemoglu, Lelarge, and Restrepo for firm-level robot adoption in France [@acemogluRestrepo2020Robots; @graetzMichaels2018Robots; @acemogluLelargeRestrepo2020competingRobots].

**AI, adoption, and worker use.** Read Brynjolfsson, Li, and Raymond for worker-level productivity and Aghion et al. for firm-level AI adoption and labor demand [@brynjolfssonLiRaymond2025GenerativeAI; @aghionBergeaudBoppartKlenowLi2025differentUsesAI].

**Measurement frontier.** Use Webb, Felten-Raj-Seamans, vacancy evidence, and patent-worker exposure work to compare capability exposure, task exposure, desired demand, and worker-level exposure [@webb2020; @feltenRajSeamans2021AIExposure; @acemogluAutorHazellRestrepo2022AIJobs; @koganPapanikolaouSchmidtSeegmiller2023].

**Historical comparison.** Use Goldin and Katz for technology-skill complementarity, Atack-Bateman-Margo for mechanization, Fiszbein-Lafortune-Vamplew for electrification, Mokyr-Vickers-Ziebarth for technological anxiety, and Deming for long-run disruption [@goldinKatz1998origins; @atackBatemanMargo2020inanimatePower; @fiszbeinLafortuneVamplew2020electrification; @mokyrVickersZiebarth2015historyAnxiety; @deming2025technologicalDisruption].

## Exercises And Discussion Prompts

1. Pick an occupation and list four tasks inside it. Which task is most likely to be displaced by AI or automation? Which is most likely to be augmented?
2. Explain how employment can fall while wages rise after automation. Then explain how employment can rise while wages stagnate.
3. Compare a robot exposure design with a firm AI adoption design. What is the treatment in each case? What is the main selection or interpretation problem?
4. Which historical comparison is most useful for modern AI: mechanization, electrification, computerization, or robotics? Defend the comparison using labor-demand channels.
5. Design a vacancy-based AI labor-demand study. What does a posting reveal? What does it fail to reveal?
6. Choose one technology proxy and one outcome. State whether your design identifies invention, exposure, adoption, usage, or equilibrium incidence.

## Reproducibility And Code Lab Note

The Week 2 code lab lives at `labs/02-automation-ai-and-labor-demand/`. It is a bounded synthetic teaching path. The smoke path constructs a local robot exposure measure, writes a compact exposure-outcome table, diagnoses employment-wage incidence patterns, and transfers the logic to firm AI adoption. It requires no external downloads, confidential firm data, official robot microdata, or proprietary vacancy records.

## Slide Companion Note

The Week 2 slide deck lives at `slides/week2/02-automation-ai-and-labor-demand.tex`. The deck presents the lecture logic rather than duplicating the chapter: it starts from the labor-demand question, separates the four demand channels, shows why unit and measurement choices change the estimand, includes a structured historical-comparison block, and closes with the Reproduce -> Diagnose -> Transfer lab design.

## Bridge Forward

Week 3 moves from labor-demand incidence to worker adjustment. Week 2 asks which tasks, workers, firms, industries, and places are exposed when technology changes demand. Week 3 asks how workers respond through skills, training, mobility, career transitions, bargaining, and labor-force attachment once those demand shocks arrive.
