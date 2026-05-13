---
title: Technology, Tasks, and Labor-Market Adjustment: Core Frameworks
bibliography:
  - references.bib
---

# Week 1. Technology, Tasks, and Labor-Market Adjustment: Core Frameworks

## Opening Orientation

This opening week gives the course its main research map: labor economists do not study “technology” as a slogan, but as a set of changes in task capability, production organization, information, and adjustment costs that alter labor demand, worker adjustment, and equilibrium outcomes [@autorLevyMurnane2003SkillContent; @acemogluRestrepo2019AutomationNewTasks]. The point of the lecture is not only to introduce task-based and skill-based frameworks, but also to clarify a measurement problem that keeps returning throughout the course: the empirical object called “technology” is never observed directly, and different proxies capture different underlying mechanisms [@webb2020; @koganPapanikolaouSchmidtSeegmiller2023].

```{admonition} Core points
:class: important
- Labor economists should distinguish invention, adoption, and diffusion rather than treating “technology” as a single event.
- The key labor framework runs from technology to tasks, from tasks to skills and organizational choices, and then to wages, employment, inequality, mobility, and worker welfare.
- Automation, augmentation, and new-task creation are distinct channels with different empirical implications [@autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks].
- Measurement is a first-order research question: patents, robots, software adoption, job-posting text, task surveys, and firm-level adoption measures capture different objects and need not agree [@webb2020; @babinaFedykHe2024].
```

## Bridge

The labor sequence has already emphasized that employment and wages are determined through worker choices, firm behavior, institutions, and market adjustment. This course adds a specific class of shocks to that map: technological and innovative change. The key discipline is to avoid treating “new technology” as a black box. Labor research is strongest when it states what changes in production, who adjusts, over what horizon, and how the empirical proxy for technology relates to that mechanism.

## Field Core

### What are technology and innovation in labor economics?

For labor economists, technology is best understood as a change in what can be done, at what cost, with which inputs, under which organizational form. Innovation includes invention, commercial development, adoption, and diffusion. That distinction matters because a patent, a robot installation, a software rollout, a new AI workflow, and a vacancy requesting AI skills are not the same empirical event.

A useful taxonomy separates:
1. **invention**: a new capability is created;
2. **adoption**: a firm or establishment begins using it;
3. **diffusion**: the technology spreads across firms, regions, or workers;
4. **reorganization**: the firm changes task assignment, supervision, hiring, or workflow in response.

The labor consequences depend on which stage is being studied. Invention without adoption need not move labor demand. Adoption without broad diffusion may produce firm-level but not market-level effects. Diffusion without worker adjustment can temporarily widen inequality.

### Core frameworks: skills, tasks, automation, and new tasks

The classic task approach starts from the idea that production requires tasks rather than broad factors alone. Workers differ in comparative advantage across tasks, and technologies change which tasks are assigned to labor versus capital or software [@autorLevyMurnane2003SkillContent; @acemogluAutor2011SkillsTasks]. This is the bridge from technology to labor outcomes.

A minimal conceptual map is:

```{math}
:label: eq:tech-framework
\text{Technology / Innovation}
\;\rightarrow\;
\text{Task content of production}
\;\rightarrow\;
\text{Skill demand and organization}
\;\rightarrow\;
\text{Worker and firm adjustment}
\;\rightarrow\;
\text{Equilibrium wages, employment, and welfare.}
```

This framework immediately separates three channels.

First, **automation** moves tasks away from labor and toward machines or software. Second, **augmentation** raises worker productivity within tasks that remain human-performed. Third, **new-task creation** expands the set of tasks in which labor has comparative advantage [@autor2015Jobs; @acemogluRestrepo2019AutomationNewTasks].

The course will keep returning to the distinction between displacement and productivity effects. The same technology can raise output and yet reduce labor demand in particular tasks or occupations. Conversely, technologies that raise productivity in complementary tasks can increase labor demand even when some tasks are automated.

### A short equilibrium lens

One reason Week 1 must be labor, not generic technology studies, is that the relevant outcome is never just “more automation.” The relevant question is how workers and firms adjust after the change in task content.

Worker adjustment can happen through:
- retraining,
- occupational switching,
- within-firm reassignment,
- migration,
- labor-force exit,
- bargaining over a new task mix.

Firm adjustment can happen through:
- hiring different workers,
- reorganizing production,
- changing supervision or management,
- entering or exiting markets,
- relocating,
- complementing the new technology with organizational capital.

The same direct technology shock can therefore produce different observed outcomes depending on mobility frictions, training technologies, labor-market institutions, and firm organization.

### Measurement as a research problem

Measurement is one of the most important open questions in this field. “Technology” can be proxied in many ways, but each proxy captures a different underlying object.

The literature commonly uses:
- **patents / patent text**, which are closest to invention and technological capability [@koganPapanikolaouSchmidtSeegmiller2023];
- **robot installations**, which are close to embodied automation adoption [@acemogluRestrepo2020Robots];
- **software / IT adoption**, which often captures organizational and skill-complementary technology;
- **task-based exposure measures** using patent text or model capabilities mapped to occupations [@webb2020];
- **job-posting text**, which captures employer demand for technology-related tasks and skills;
- **firm adoption measures** based on worker resumes, internal investment, or product innovation [@babinaFedykHe2024];
- **task surveys and O*NET-style descriptions**, which help connect technology to job content rather than just occupation titles.

The crucial point for students is that these are not substitutes in a mechanical sense. A patent measure may capture new capability before adoption. A job-posting measure may capture employer expectation rather than realized use. A robot measure can identify one narrow but concrete class of automation. A resume-based AI-investment measure may better capture firm adoption and reorganization than invention itself [@babinaFedykHe2024].

So an empirical design should always answer:
1. what technological object am I measuring?
2. at what level do I observe it: task, occupation, firm, establishment, commuting zone, industry?
3. is my proxy closer to invention, adoption, or diffusion?
4. through which labor mechanism should this measure matter?

```{include} assets/tables/01-core-frameworks-map.md
```

```{include} assets/tables/01-technology-and-innovation-measurement-map.md
```

### A guide to interpretation

A common failure in this literature is to move too quickly from an exposure index to a substantive conclusion. Exposure is not effect. A patent-text exposure score, a robot-adoption exposure score, and a job-posting AI score may all rank occupations differently because they capture different technologies and different stages of adjustment [@webb2020; @koganPapanikolaouSchmidtSeegmiller2023].

That means a good paper should be explicit about:
- the technology margin,
- the unit of analysis,
- the adjustment horizon,
- the equilibrium channel,
- and the welfare object.

```{include} assets/tables/01-setting-to-measurement-map.md
```

### Domain preview for the rest of the course

Week 1 is deliberately broad because the rest of the course will unpack this framework in pieces. Later weeks will ask whether technology mostly changes labor demand, worker adaptation, firm organization, inequality, or institutions. But the organizing map remains the same: technology changes task content; workers and firms respond; equilibrium determines who gains, who loses, and which effects persist.

```{include} assets/tables/01-domain-preview-map.md
```

## Research Lab

### Primary anchor

A natural primary anchor for this week is Webb’s measurement framework for technology exposure [@webb2020]. The educational value is that the paper is not only about AI; it is fundamentally about how labor economists map technology descriptions into task exposure scores.

### Reproduce

Students should reproduce a bounded pedagogical version of the exposure-building logic:
- define a small set of technology descriptors,
- map them to task descriptions,
- and generate an exposure score for a toy set of occupations or firms.

The point is not to rebuild the full paper, but to understand how measurement choices create the empirical object.

### Diagnose

Students should then diagnose:
- what exactly the exposure score measures,
- which stage of the technology process it captures,
- what kinds of occupations are likely to be mismeasured,
- and why different proxies might disagree about the same occupation.

A strong diagnosis asks whether the exposure index is identifying automation, augmentation, or a mix.

### Transfer

For transfer, students can apply the same logic to a different measurement setting, such as:
- mapping job-posting text to technology-related task demand,
- comparing robot-style embodied adoption measures to patent-text measures,
- or contrasting patent-based exposure with firm-level AI adoption measures.

The goal is to make students think like labor researchers designing a technology measure, not just consumers of someone else’s index.

## Reading Ladder And References

Start with the conceptual frame: [@autorLevyMurnane2003SkillContent], [@autor2015Jobs], and [@acemogluRestrepo2019AutomationNewTasks]. Then read the measurement-focused papers [@webb2020; @koganPapanikolaouSchmidtSeegmiller2023]. For a contemporary firm-adoption perspective, add [@babinaFedykHe2024]. For AI-specific labor-market framing, [@agrawalGansGoldfarb2019] is a useful complement.

## Exercises And Discussion Prompts

1. When should a patent-based technology measure be preferred to a job-posting-based measure?
2. Give one example of a labor-augmenting technology and one example of an automating technology. How would the empirical designs differ?
3. Why is it misleading to speak about “AI exposure” without specifying the unit of analysis and the margin of adjustment?
4. Design a simple empirical project in which two different technology measures lead to different labor-market conclusions. What would that teach you?

## Reproducibility And Code Lab Note

The Week 1 code lab should be bounded and pedagogical. If full official replication materials are unavailable locally, the lab can still be implemented as a reduced exposure-construction exercise with synthetic or reduced data, as long as the distinction between pedagogical reproduction and full replication is made explicit.

## Slide Companion Note

The slide deck should mirror the chapter logic closely:
1. why technology is a labor object;
2. skills vs tasks;
3. automation vs augmentation vs new tasks;
4. why measurement is hard;
5. the main families of technology measures;
6. research design implications.

## Bridge Forward

Week 2 will take the task framework into automation, AI, and labor demand more directly. The key bridge is that the next lecture will not ask only whether technology displaces labor, but which tasks move first, which workers are exposed, and whether firms adjust through scale, reorganization, or new task creation.
