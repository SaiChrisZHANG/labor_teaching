# Technology, Tasks, And Labor-Market Adjustment: Core Frameworks

## Learning Objectives

By the end of Week 1, students should be able to:

1. define technology and innovation as labor-market objects rather than as broad labels;
2. distinguish invention, adoption, diffusion, and workplace reorganization;
3. separate labor-substituting technologies, labor-augmenting technologies, automation, augmentation, and new-task creation;
4. map technology into tasks, skills, worker and firm adjustment, and equilibrium outcomes;
5. explain why patents, robot data, software adoption, vacancy text, task surveys, firm adoption, and worker-skill measures identify different empirical objects;
6. design a bounded measurement exercise that makes the technology margin, unit of observation, and labor outcome explicit.

The opening question is direct: how should labor economists turn technological change into objects that can explain wages, employment, skills, mobility, organization, inequality, and worker welfare?

## Opening Orientation

This course starts from a discipline that will matter every week: labor economists do not study "technology" as a slogan. They study changes in task capability, production costs, information, organization, and adjustment frictions that alter labor demand, worker adjustment, wage setting, employment, mobility, and welfare. The task-based literature gives the first map from technologies to work [@autorLevyMurnane2003SkillContent; @acemogluAutor2011SkillsTasks]. The automation and new-task literature then asks whether technology shrinks, raises the productivity of, or expands the tasks performed by labor [@autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks].

Week 1 also makes measurement a central research question. Technology is rarely observed directly. A patent, a robot installation, an IT investment, a vacancy requesting AI skills, a task-survey score, and a resume-based skill measure are all empirical proxies, but they sit at different points between invention, adoption, diffusion, and realized workplace use. Students should leave this week understanding that different technology measures can imply different empirical conclusions because they measure different objects.

:::{admonition} Core points
:class: important

- Technology and innovation become labor-economics objects when they change task content, skill demand, firm organization, wages, employment, mobility, inequality, or worker welfare.
- Invention, adoption, diffusion, and reorganization are separate margins. Evidence about one is not automatically evidence about the others.
- Automation, augmentation, and new-task creation are distinct channels. They can coexist inside the same firm, occupation, or technology wave.
- The main framework runs from technology and innovation to tasks, from tasks to skills and organization, from skills and organization to worker and firm adjustment, and from adjustment to equilibrium outcomes.
- Measurement is a frontier problem. Patents, robots, software, vacancy text, task surveys, firm investments, and worker-skill measures capture different empirical objects and should be interpreted accordingly.

:::

## Bridge

Labor I supplies the worker-side foundations: human capital, labor supply, wage determination, mobility, inequality, amenities, and welfare. Labor II supplies the firm and market architecture: labor demand, production, search, wage setting, monopsony, institutions, and adjustment. This course asks what happens when the shock comes from technology and innovation.

The first move is to keep the labor object visible. Technology matters here because it changes what firms want workers to do, what workers can profitably learn, how jobs are designed, which vacancies appear, which firms adopt, and how equilibrium wages and employment adjust. A course on innovation policy might begin from patents, R&D, or productivity. This course begins from work.

The second move is to avoid collapsing all technology into one event. Invention can occur without adoption. Adoption can occur without broad diffusion. Diffusion can occur without equal worker access to retraining. A technology can automate some tasks, augment others, and create new tasks elsewhere. The analytical task is to name the margin before interpreting the evidence.

## Field Core

### Technology And Innovation As Labor-Market Objects

For this course, a **technology** is a change in the feasible way production, matching, information processing, monitoring, or service delivery can be done. It changes which tasks can be completed, at what cost, with which inputs, under which organizational form. An **innovation** is the process by which a new capability becomes economically relevant: invention, development, adoption, diffusion, and reorganization.

Four margins should be separated at the start.

1. **Invention** creates a new capability or technique. Patent data and patent text often sit closest to this margin.
2. **Adoption** occurs when a firm, establishment, worker, or organization begins using the technology. Robot installations, software rollouts, and firm-level AI investments are closer to this margin.
3. **Diffusion** describes how adoption spreads across firms, occupations, industries, regions, workers, or countries.
4. **Reorganization** occurs when firms change task assignment, hiring, training, supervision, promotion, workflow, or job design around the technology.

This distinction is not semantic housekeeping. A patent can signal frontier capability before workers ever encounter the technology. A vacancy can reveal employer demand for a skill before a hire occurs. A robot installation can identify a narrow but concrete form of embodied automation. A resume-based AI measure may capture realized firm reorganization more directly than an invention measure. These proxies should not be narrated as if they were interchangeable.

### Core Frameworks: Skills, Tasks, Automation, And New Tasks

The classic task approach starts from the idea that production uses tasks rather than broad labor categories alone. Occupations are bundles of tasks, and workers differ in comparative advantage across those tasks. Technologies change which tasks are assigned to workers, machines, software, algorithms, or teams [@autorLevyMurnane2003SkillContent; @acemogluAutor2011SkillsTasks].

```{math}
:label: eq:st5-w1-tech-framework
\text{Technology / Innovation}
\rightarrow
\text{Task content}
\rightarrow
\text{Skill demand and organization}
\rightarrow
\text{Worker and firm adjustment}
\rightarrow
\text{Equilibrium outcomes.}
```

Equation {eq}`eq:st5-w1-tech-framework` is the organizing map for the course. Technology first changes what can be done and how tasks are bundled. Firms then decide whether to adopt, how to reorganize production, which workers to hire, and which complementary investments to make. Workers decide whether to learn, switch tasks, move jobs, bargain over new duties, or exit. Wages, employment, skill premia, mobility, firm rents, labor share, job quality, and welfare are equilibrium outcomes of those linked choices.

The task map separates several channels.

**Labor-substituting technologies** reduce the demand for labor in particular tasks, holding output and organization fixed. Industrial robots in routine production tasks are the clean benchmark [@acemogluRestrepo2020Robots; @graetzMichaels2018Robots].

**Labor-augmenting technologies** raise worker productivity in tasks that remain performed by labor. Broadband, IT, software, decision support, and AI tools can be augmenting when they make workers more productive rather than replacing the task entirely [@bresnahanBrynjolfssonHitt2002ITWorkplace; @akermanGaarderMogstad2015Broadband].

**Automation** moves a task from labor toward capital, software, or an algorithmic system. **Augmentation** changes how productive workers are inside tasks that remain human-performed. **New-task creation** expands the set of tasks in which labor has comparative advantage [@autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks; @autorChinSalomonsSeegmiller2024NewWork].

General-purpose technologies and application-specific organizational technologies differ in scope. A general-purpose technology, such as electrification, IT, or AI, can affect many sectors and require complementary changes in organization. An application-specific organizational technology, such as a scheduling algorithm, warehouse scanner, or firm-specific software workflow, may have narrower reach but sharper workplace consequences. Labor researchers should care less about the label and more about which tasks, workers, firms, and markets are affected.

```{include} assets/tables/01-core-frameworks-map.md
```

### A Short Equilibrium Lens

A minimal task-allocation object clarifies why exposure is not the same as effect. Let task {math}`k` be performed by labor with productivity {math}`a_{Lk}` and by technology with productivity {math}`a_{Tk}` and user cost {math}`c_T`. A firm automates task {math}`k` when the technology-adjusted cost is low relative to the labor-adjusted cost:

```{math}
:label: eq:st5-w1-automation-condition
\frac{c_T}{a_{Tk}} \leq \frac{w}{a_{Lk}}.
```

Equation {eq}`eq:st5-w1-automation-condition` is intentionally spare. It says that automation depends on wages, technology costs, task-specific productivity, and organization. A change in {math}`c_T` or {math}`a_{Tk}` may shift the automation boundary, but labor-market outcomes also depend on scale effects, product demand, new tasks, worker retraining, firm entry and exit, and wage setting.

A reduced-form empirical design often looks like this:

```{math}
:label: eq:st5-w1-exposure-design
\Delta Y_{g t} =
\beta \, TechMeasure_{g t}
+ X_{g t}'\Gamma
+ \varepsilon_{g t},
```

where {math}`g` may be a task, occupation, worker group, firm, establishment, industry, commuting zone, or country. The coefficient {math}`\beta` cannot be interpreted until the measure and unit are explicit. Does {math}`TechMeasure_{g t}` capture invention, exposure, adoption, diffusion, or realized use? Is {math}`Y_{g t}` an employment outcome, wage outcome, skill-price outcome, mobility outcome, organizational outcome, or welfare outcome? Which equilibrium margins remain offstage?

Worker adjustment can occur through retraining, occupational mobility, within-firm reassignment, migration, job search, bargaining, or labor-force exit. Firm adjustment can occur through adoption, hiring, training, capital investment, job redesign, supervision, entry, exit, outsourcing, or relocation. Institutions then shape the speed and incidence of adjustment. The same technology can therefore produce different labor outcomes across places, firms, and worker groups.

### Measurement As A Research Problem

Measurement is one of the central open questions in technology-and-labor research. The empirical object called "technology" is almost always constructed. That construction choice determines what the paper can and cannot claim.

Common measurement families include:

- **Patents and patent text.** These are close to invention and capability. Patent text can be mapped to tasks or occupations, but it remains distant from realized use [@webb2020; @koganPapanikolaouSchmidtSeegmiller2023].
- **Robots and industrial adoption.** Robot installations measure a concrete embodied automation margin. The strength is interpretability; the limitation is narrow technological scope [@acemogluRestrepo2020Robots; @graetzMichaels2018Robots].
- **Software, IT, and digital adoption.** These measures often capture organizational complements, skill-biased adoption, and workplace transformation, but the same software label can mean different things across firms [@bresnahanBrynjolfssonHitt2002ITWorkplace; @bloomSadunVanReenen2012AmericansIT].
- **Job-posting and vacancy text.** Vacancy data reveal employer demand for tasks and skills in near real time, including AI-related skill requests, but postings measure desired hiring rather than realized employment [@acemogluAutorHazellRestrepo2022AIJobs].
- **Task surveys and O*NET-style descriptions.** Task descriptions help connect technology to job content rather than occupation names alone. They can be transparent and scalable, but they may lag workplace change [@autorLevyMurnane2003SkillContent; @feltenRajSeamans2021AIExposure].
- **Firm adoption, investment, and worker-skill measures.** Firm investments, worker resumes, and observed skill stocks can move closer to realized use and reorganization, but access, comparability, and selection into adoption become central [@babinaFedykHeHodson2023AIWorkforce; @babinaFedykHe2024].

```{include} assets/tables/01-technology-and-innovation-measurement-map.md
```

The interpretation rule is simple: different measures imply different empirical objects. A patent-based exposure measure may say an occupation is technologically exposed because patented capabilities resemble its tasks. A vacancy measure may say the same occupation is becoming more AI-intensive because employers request AI skills. A robot-adoption measure may show little change because the occupation is not exposed to embodied automation. A resume-based measure may show adoption concentrated in firms with particular worker mixes. Those findings can all be true because they refer to different stages of the technology process.

### From Setting To Measurement Choice

The measurement should follow the labor question. If the question is whether industrial automation reduced local employment, robot exposure is a plausible first-pass measure. If the question is how new capabilities map to occupations before adoption is widespread, patent-text exposure may be appropriate. If the question is whether firms are changing skill demand, vacancy text is closer. If the question is worker career adjustment, the technology measure must be linked to worker histories and occupations.

```{include} assets/tables/01-setting-to-measurement-map.md
```

A good technology-and-labor design states:

1. the technology margin;
2. the measured object;
3. the unit of observation;
4. the adjustment horizon;
5. the outcome and welfare object;
6. the equilibrium channel left outside the design.

The danger is to treat an exposure index as a treatment effect. Exposure says a unit is predicted to be susceptible to a technology margin. Adoption says the technology is used. Diffusion says many units have adopted. Effects require an outcome and a counterfactual.

### Domain Preview For The Course

Week 1 is broad because the rest of the course unpacks this framework one margin at a time. Week 2 moves directly into automation, AI, and labor demand. Week 3 studies worker adjustment, skill portability, training, and career transitions. Week 4 moves inside firms and hiring systems. Week 5 studies inequality, rents, market power, and institutions. Week 6 converts the sequence into research designs.

```{include} assets/tables/01-domain-preview-map.md
```

## Research Lab

The Week 1 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Webb's task and patent-text exposure logic [@webb2020]. The measurement contrast is Kogan, Papanikolaou, Schmidt, and Seegmiller's worker-level technology exposure logic [@koganPapanikolaouSchmidtSeegmiller2023]. The lab is not an official replication of either paper. It is a bounded teaching exercise that helps students see how measurement choices create empirical objects.

**Reproduce.** Students build a small exposure index. The local script defines task descriptions, technology descriptors, and a toy set of occupations. It maps technology descriptors to task weights and then computes occupation-level exposure. This reproduces the logic of constructing a technology-to-task bridge, not the full proprietary data or full paper estimates.

**Diagnose.** Students compare three measures: patent-text-style capability exposure, robot-style embodied automation exposure, and vacancy-style skill-demand exposure. They classify each measure as invention, adoption, desired demand, or realized use. They then explain why occupations rank differently across the measures and what that implies for interpretation.

**Transfer.** Students transfer the same logic to a synthetic firm setting. They compare firms whose workforce task portfolios look exposed to AI capabilities with firms whose measured technology change appears mainly in vacancy text or embodied automation. The deliverable is a short memo explaining how two reasonable measurement choices could produce different conclusions about wages, employment, skill demand, or reorganization.

## Methods Box

:::{admonition} Methods Box: Measurement Discipline For Technology And Labor
:class: note

**Tasks versus occupations.** Tasks are activities; occupations bundle tasks. A technology can affect some tasks inside an occupation while leaving others unchanged.

**Exposure versus adoption.** Exposure measures predicted susceptibility. Adoption measures realized use. They answer different questions and have different selection problems.

**Invention versus diffusion.** Patent data may capture new capabilities before those capabilities are adopted by firms or workers.

**Vacancies versus employment.** Job postings reveal employer demand and job design intentions, not realized employment, wages, or worker welfare.

**Within-firm versus market-level incidence.** Firm adoption evidence is often closer to treatment, while local-market evidence is often closer to equilibrium incidence.

**Technology coefficient versus welfare claim.** A coefficient on a technology measure is not a welfare result unless the design states the affected workers, wage and nonwage margins, adjustment costs, and counterfactual.

:::

## Reading Ladder And References

**Core task framework.** Start with Autor, Levy, and Murnane on task content, then read Acemoglu and Autor for the broader skills-tasks-technologies framework [@autorLevyMurnane2003SkillContent; @acemogluAutor2011SkillsTasks].

**Automation, augmentation, and new tasks.** Use Autor and Acemoglu-Restrepo to separate displacement, productivity, reinstatement, and new-task creation [@autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks].

**Concrete automation and adoption.** Use robot evidence to see a measurable embodied automation margin and its labor-market consequences [@acemogluRestrepo2020Robots; @graetzMichaels2018Robots].

**Measurement frontier.** Use Webb for technology-to-task exposure construction and Kogan et al. for worker-level technology exposure logic [@webb2020; @koganPapanikolaouSchmidtSeegmiller2023].

**Firm adoption and vacancy demand.** Use Babina et al. and Acemoglu et al. to compare realized firm investment and online vacancy measures [@babinaFedykHeHodson2023AIWorkforce; @acemogluAutorHazellRestrepo2022AIJobs].

**AI framing.** Agrawal, Gans, and Goldfarb help students frame prediction as a task-changing technology rather than as a vague AI shock [@agrawalGansGoldfarb2019].

## Exercises And Discussion Prompts

1. Give one example of invention without adoption, adoption without broad diffusion, and diffusion without equal worker adjustment. What labor outcome would you expect each case to affect first?
2. Choose an occupation. List three tasks inside it, then classify whether a new technology would automate, augment, or create tasks around that occupation.
3. When should a patent-text measure be preferred to a vacancy-text measure? When should the reverse be true?
4. Suppose a robot exposure measure and a job-posting AI measure rank the same occupation very differently. Give two substantive reasons why both rankings might be defensible.
5. Design a two-measure empirical project in which one measure is closer to invention and the other is closer to adoption. What would each coefficient mean?

## Reproducibility And Code Lab Note

The Week 1 code lab lives at `labs/01-technology-tasks-and-labor-market-adjustment-core-frameworks/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates deterministic task, technology, occupation, and firm data; computes exposure scores under multiple measurement choices; writes compact reproduce, diagnose, and transfer outputs; and requires no confidential data or external downloads.

## Slide Companion Note

The Week 1 slide deck lives at `slides/week1/01-technology-tasks-and-labor-market-adjustment-core-frameworks.tex`. The deck mirrors the chapter logic without duplicating the prose: it defines the labor question, introduces the task framework, separates automation, augmentation, and new-task creation, centers the measurement problem, maps the main literature, and closes with the lab logic.

## Bridge Forward

Week 2 takes this framework into automation, AI, and labor demand. The next lecture asks which tasks are displaced, complemented, or newly created when robots, software, and AI diffuse through firms and markets. The Week 1 lesson carries forward: before asking whether technology raises or lowers employment, students must ask what technology object is measured, which tasks are exposed, which workers and firms adjust, and which equilibrium margin is visible.
