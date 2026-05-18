# Education, Skills, Aspirations, And Occupational Sorting

## Learning Objectives

By the end of Week 3, students should be able to:

1. distinguish early-choice channels from later-adjustment and inertia channels in gendered sorting;
2. explain why observed occupational sorting is neither pure preference nor pure constraint;
3. map role models, competitiveness, teacher bias, information, aspirations, and anticipated discrimination to education and field-choice margins;
4. represent sorting as a dynamic sequence from skills and beliefs to entry placement and later mobility;
5. identify what reduced-form education interventions, teacher-bias designs, survey-expectations designs, early-career quasi-experiments, and long-panel lifecycle designs can and cannot show;
6. connect Week 3 backward to care and household expectations from Week 2 and forward to firm-side mechanisms in Week 4 and norms in Week 5.

## Opening Orientation

Week 3 asks how education, skills, aspirations, and early occupational choices generate later gendered labor-market outcomes. The central labor object is sorting: who accumulates which skills, enters which fields, begins on which career ladder, and can later adjust away from early placements. The point is not to say that women and men choose different jobs. The point is to ask how those choices are formed, what constraints surround them, and why early differences can persist.

Sorting matters because it links pre-market decisions to wages, authority, job quality, promotion, safety, flexibility, and welfare. A major or occupation is not a taste parameter. It is an equilibrium object shaped by expected returns, information, self-beliefs, stereotypes, role-model exposure, competitive environments, anticipated discrimination, family expectations, and the organization of jobs. It is also not the end of the story. After entry, workers face switching costs, career ladders, early job matches, timing constraints, promotion bottlenecks, and direct barriers that can make adjustment costly.

:::{admonition} Core points
:class: important

- Gendered occupational sorting has two main channels: early choices before or at labor-market entry, and later adjustment or inertia after early choices are made.
- Early choices can move through aspirations, competitiveness, information, teacher signals, stereotypes, role models, mentors, and anticipated discrimination.
- Later outcomes can persist because first placements, career ladders, switching costs, flexibility constraints, and promotion systems make adjustment costly.
- Observed sorting should not be read as either pure preference or pure constraint; credible evidence names the margin, the identifying variation, and the mechanism.
- Domestic and workplace norms help shape what fields and jobs feel feasible or desirable, but Week 3 uses norms only as a bridge. Week 5 studies norms directly.

:::

## Bridge

Week 2 placed paid work inside household allocation, fertility timing, care constraints, and bargaining. Week 3 moves one step earlier in the lifecycle and one step outward into the labor market. The same expectations about care, family timing, mobility, and job flexibility that mattered in Week 2 can affect course choices, majors, internships, first jobs, and willingness to enter demanding or high-variance career paths before a child penalty is visible in the data.

That backward bridge matters for interpretation. If a student avoids a field because she expects future care responsibilities to conflict with the field's hours, travel, or promotion norms, the early-choice margin already contains anticipated household constraints. If a worker starts in a flexible but lower-growth job because of expected family timing, the later wage path may reflect both early sorting and the organization of career ladders. This is why Week 3 must separate two channels while also allowing them to interact.

```{figure} assets/figures/03-week-bridges.svg
:name: fig-week3-course-bridge
:alt: Conceptual bridge from Week 2 household allocation through Week 3 sorting to Week 4 firms and Week 5 norms.

Week 3 connects household expectations to education, skills, aspirations, and sorting, then points forward to firm-side allocation and norms.
```

## Field Core

### Why Sorting Is Not One Mechanism

Occupational sorting is a sequence. Gender may affect human-capital investments and beliefs before labor-market entry. It may affect first assignment into fields, firms, sectors, occupations, or tasks. It may also affect whether workers can later move across tracks, preserve career momentum, or recover from early mismatches.

```{figure} assets/figures/03-two-channel-decomposition.svg
:name: fig-week3-two-channel-decomposition
:alt: Conceptual decomposition of early-choice, entry-sorting, and later-adjustment channels.

The early-choice and later-adjustment channels are distinct, but they can reinforce each other through feedback.
```

The conceptual decomposition is:

```{math}
:label: eq-week3-sequence-decomposition
G_Y
=
\Delta^{early}_Y
+
\Delta^{entry}_Y
+
\Delta^{adjust}_Y
+
\Delta^{returns}_Y
+
\Delta^{interactions}_Y .
```

Here {math}`G_Y` is a gender-associated gap in a later labor outcome {math}`Y`, such as earnings, wages, authority, promotion, hours, job quality, or occupational status. The term {math}`\Delta^{early}_Y` captures differences produced through skills, schooling, field of study, aspirations, beliefs, and information. The term {math}`\Delta^{entry}_Y` captures first labor-market assignment. The term {math}`\Delta^{adjust}_Y` captures persistence, switching costs, flexibility constraints, and barriers to later movement. The term {math}`\Delta^{returns}_Y` captures differential returns to the same skills, occupations, firms, or tasks. The interaction term is not decorative: anticipated future constraints may change early choices, and early choices may make later adjustment harder.

This is a conceptual decomposition, not an estimator by itself. A paper that decomposes wage gaps by occupation may describe allocation. A paper that randomly varies role-model exposure may estimate an early-choice intervention. A paper that uses quasi-random early placement and long follow-up may identify later inertia. Those are different empirical objects.

```{include} assets/tables/03-early-choices-vs-later-adjustment-map.md
```

### A Dynamic Sorting Object

A compact way to write the worker problem is to let initial sorting depend on skills, beliefs, expected returns, and expected constraints:

```{math}
:label: eq-week3-initial-sorting
o_i^0
=
\arg\max_{o \in \mathcal{O}}
\left\{
\mathbb{E}_{i0}\left[\sum_{t=0}^{T}\beta^t w_{ot}(H_{it})\right]
+ A_{io}
- C_{io}
- D^e_{io}
- \kappa^e_{io}
\right\}.
```

The initial field or occupation {math}`o_i^0` is chosen from the feasible set {math}`\mathcal{O}`. Expected wages depend on skills {math}`H_{it}`. The term {math}`A_{io}` captures aspirations, identity fit, and perceived belonging. The term {math}`C_{io}` captures monetary and nonmonetary costs of preparation and entry. The term {math}`D^e_{io}` captures expected discrimination or expected exclusion. The term {math}`\kappa^e_{io}` captures expected future adjustment costs, such as flexibility constraints, family timing, commuting limits, or promotion systems.

After entry, the dynamic problem changes:

```{math}
:label: eq-week3-dynamic-career
V_{it}(o)
=
\max
\left\{
u_{it}(o) + \beta V_{i,t+1}(o),
\max_{o' \neq o}\left[u_{it}(o') - K_{i,t}(o,o') + \beta V_{i,t+1}(o')\right]
\right\}.
```

The switching cost {math}`K_{i,t}(o,o')` can include lost occupation-specific human capital, credential requirements, weakened networks, lost seniority, relocation costs, schedule constraints, employer discrimination, or promotion bottlenecks. If {math}`K_{i,t}` differs by gender or rises at family-sensitive career stages, early occupational choices can have long-run effects even when two workers started with similar skills.

### Early-Choice Channel

The early-choice channel asks why workers enter different educational, skill, and occupational pipelines. It includes major choice, course taking, track choice, internships, training, early search behavior, and first occupation. The key empirical discipline is to name the observed margin. A role-model intervention may identify major choice. A teacher-bias design may identify course taking or field selection. A survey-expectations design may identify intended major, expected treatment, or mediated choice. These are related margins, not interchangeable ones.

```{figure} assets/figures/03-early-choice-mechanisms.svg
:name: fig-week3-early-choice-mechanisms
:alt: Mechanisms linking role models, competition, teacher signals, information, aspirations, and anticipated discrimination to early choices.

Early choices can shift because the perceived returns, costs, risks, and identity value of a field change.
```

Role models and mentors are early-choice mechanisms because they can change information and perceived belonging before career paths are locked in. Porter and Serra use a role-model intervention in economics classes and observe changes in female students' major choice, which makes the paper a clean anchor for reduced-form field interventions [@porterSerra2020femaleRoleModelsMajor]. The identifying variation is classroom exposure to female role models; the observed margin is subsequent economics major choice. The result should not be described as a direct estimate of labor-market discrimination or later wage growth. It is evidence that information and identity-relevant exposure can move an early education margin.

Competitiveness and aspirations enter through willingness to choose high-variance, high-status, or tournament-like paths. Buser, Niederle, and Oosterbeek connect measured competitiveness to later educational track choice [@buserNiederleOosterbeek2014genderCompetitivenessCareerChoices]. The identifying object is not a firm promotion tournament. It is an experimentally measured behavioral margin linked to later track selection. The labor-economics interpretation is that preferences over competition, beliefs about performance, and risk over rewards can shape entry into career ladders where returns are steep.

Teacher bias and stereotypes are early-choice mechanisms because students use grades, feedback, and teacher signals to infer comparative advantage. Lavy and Sand study teachers' stereotypical biases and subsequent human-capital choices [@lavySand2018teacherBiasHumanCapital]. Card, Domnisoru, Sanders, and Taylor provide related evidence on female teachers and female students' later outcomes [@cardDomnisoruSandersTaylor2022femaleTeachers]. The observed margins are school achievement, field choice, and later education or welfare outcomes, depending on the setting. The identifying variation comes from the school or teacher environment, not from a generic taste difference.

Anticipated discrimination is especially important because it links demand-side expectations to supply-side choices. Lepage, Li, and Zafar study anticipated discrimination and major choice [@lepageLiZafar2025anticipatedDiscrimination]. The key point is conceptual as much as empirical: if students expect worse treatment in a field, their major choice may respond before they ever encounter the relevant employer. A later researcher observing fewer women in the field should not infer that the field was simply less preferred. The preference may already incorporate expected barriers.

```{include} assets/tables/03-mechanisms-and-evidence-map.md
```

### Later-Adjustment And Inertia Channel

The later-adjustment channel begins after early choices are made. It asks whether workers can revise their path when new information arrives, when family timing changes, when the first job is a poor match, or when they face direct barriers in promotion, mobility, or switching. This channel is analytically separate from early choices. Conditional on the same major or first job, gender can still alter wage growth, task assignment, promotion, hours, retention, occupational persistence, and the cost of moving to a different ladder.

```{figure} assets/figures/03-dynamic-career-inertia.svg
:name: fig-week3-dynamic-career-inertia
:alt: Dynamic career paths showing high-growth, persistent early-track, and late-switch trajectories.

Later adjustment can be costly when first placements determine seniority, networks, promotion gates, schedules, and occupation-specific human capital.
```

Early-career setbacks provide a clean way to see the channel. Fadlon, Lyngse, and Nielsen study early-career setbacks and women's career-family tradeoffs [@fadlonLyngseNielsen2022earlyCareerSetbacks]. The identifying variation is an early-career shock or quasi-experimental placement environment; the observed margins include labor outcomes, family timing, and career trajectories. The interpretation is not only that women selected differently at entry. It is that early shocks can change later adjustment and family-career tradeoffs.

Career ladders can also create inertia without a single discrete shock. Bertrand, Goldin, and Katz study young professionals in financial and corporate sectors and show how hours, interruptions, and dynamic career structure are tied to gender gaps [@bertrandGoldinKatz2010dynamicsGenderGap]. The setting matters because high-skill professional careers often have nonlinear rewards, early promotion races, and penalties for temporary reductions in availability. The observed margins include earnings, hours, family status, and career progression. The identifying variation is not a randomized education intervention; the paper maps dynamic career divergence in a setting where early path choices and later job design interact.

The later-adjustment channel also includes direct barriers to moving out of early tracks. Some barriers are formal: credentials, licensing, tenure clocks, seniority rules, or firm-specific promotion gates. Others are informal: networks, mentorship, client assignment, travel expectations, harassment risk, biased evaluation, or expectations about availability. Flexibility constraints sit between household and firm mechanisms. A worker may be willing to switch fields but unable to absorb retraining, relocation, hours volatility, or lower short-run earnings at the exact stage when family and career demands collide.

### How The Channels Interact

The two channels are distinct, but they are not independent. Anticipated future constraints can enter Equation {eq}`eq-week3-initial-sorting` through {math}`\kappa^e_{io}` and {math}`D^e_{io}`. A student may choose a field partly because she expects later discrimination, inflexible hours, weaker promotion access, or family-incompatible job design. That is an early choice shaped by expected later frictions.

The reverse interaction is equally important. Early choices can change later adjustment costs in Equation {eq}`eq-week3-dynamic-career`. A first occupation builds occupation-specific skills, networks, credentials, and reputation. Moving later may require a wage cut, retraining, relocation, or loss of seniority. If the costs of switching rise when care demands rise, early sorting and household timing interact. If firms use early assignments to ration training or client exposure, early sorting and firm behavior interact. Week 4 will unpack those firm-side mechanisms.

The empirical payoff is that papers must be precise. A reduced-form major-choice intervention can show that early choices moved, but it rarely proves that later labor-market gaps would disappear. A long-panel administrative design can show persistence after early placement, but it may not identify the belief or aspiration process that generated the initial placement. A decomposition can show how much of a gap is between occupations, but it does not by itself reveal whether the allocation came from preferences, constraints, discrimination, information, or adjustment costs.

### Short Bridge To Week 5 Norms

Norms enter Week 3 because aspirations, self-promotion, mobility, field identity, and perceived job feasibility are socially mediated. Domestic norms can shape expected care responsibility. Workplace norms can shape who is seen as belonging in technical, competitive, authority-bearing, or travel-intensive roles. These beliefs can affect education and sorting long before a formal employer decision appears in the data.

But norms are not the main object of Week 3. The object here is the labor allocation sequence: skill formation, field choice, first job, occupational persistence, and later adjustment. Week 5 returns to norms, bargaining, identity, and institutions directly. Week 3's job is to show where norms enter the sorting problem without making every sorting fact a norms fact.

```{include} assets/tables/03-norms-bridge-map.md
```

### Methods And Evidence

A useful rule for this literature is: do not present a result without naming the identifying variation and the observed margin. The same phrase, "gendered sorting," can refer to a randomized role-model intervention, a teacher-bias design, a beliefs survey, a field-choice model, a decomposition, a quasi-random early-career assignment, or a long lifecycle panel.

Reduced-form field or education interventions identify whether an exposure changes a schooling or field margin. Porter and Serra identify the effect of female role-model exposure on economics major choice [@porterSerra2020femaleRoleModelsMajor]. The strength is clean intervention variation; the limitation is that later career outcomes may be outside the design.

Teacher-bias and role-model designs identify distorted signals, information, or identity-relevant exposure. Lavy and Sand use teacher-bias variation to study later human-capital choices [@lavySand2018teacherBiasHumanCapital]. The observed margin must be named: course performance, field selection, applications, major choice, or later outcomes.

Survey-expectations and beliefs designs identify perceived returns, expected treatment, and anticipated discrimination. Lepage, Li, and Zafar focus on anticipated discrimination and major choice [@lepageLiZafar2025anticipatedDiscrimination]. The method is strongest when beliefs are measured before choices or when designs can shift beliefs; it is weaker when expected treatment and unobserved preferences are hard to separate.

Early-career quasi-experiments identify later adjustment when an early placement, shock, or assignment changes career paths. Fadlon, Lyngse, and Nielsen provide the anchor for early-career setbacks [@fadlonLyngseNielsen2022earlyCareerSetbacks]. The observed margin is not a major declaration. It is persistence, switching, earnings, family timing, or career adjustment after entry.

Long-panel lifecycle administrative designs map the dynamic path from entry to later outcomes. Bertrand, Goldin, and Katz are useful because the observed margins include earnings, hours, family status, and career progression in a high-skill labor market [@bertrandGoldinKatz2010dynamicsGenderGap]. These designs are often strong on dynamics and heterogeneity but require care in causal interpretation.

Decomposition and causal designs answer different questions. A decomposition can say how much of a wage gap is associated with field or occupation. A causal design can say whether a particular intervention or shock changed a margin. The decomposition is useful for accounting; the design is useful for counterfactuals. Neither should be made to do the other's job.

```{include} assets/tables/03-data-and-methods-map.md
```

## Research Lab

The Week 3 research lab is organized as **Reproduce -> Diagnose -> Transfer**. Its purpose is to train students to see whether a paper identifies an early-choice mechanism, a later-adjustment mechanism, or a bundled sequence.

**Reproduce.** The primary lab anchor is Porter and Serra on female role models and major choice [@porterSerra2020femaleRoleModelsMajor]. Students use deterministic synthetic course-level data to reproduce a reduced-form field-intervention exercise. The observed margin is economics major choice. The identifying variation is role-model exposure. The lesson is that a clean intervention can move a pre-market choice margin without directly estimating later wages.

**Diagnose.** Students classify each mechanism in the synthetic outputs: role-model exposure, baseline preparation, beliefs about belonging, expected returns, and major choice. They write a short design memo stating the treatment, outcome, comparison group, identifying variation, and what the reduced form does not prove.

**Transfer.** The challenge anchor is Buser, Niederle, and Oosterbeek on competitiveness and career choices [@buserNiederleOosterbeek2014genderCompetitivenessCareerChoices]. Students transfer the same discipline to a synthetic competitiveness exercise that links a behavioral measure to later track choice. They diagnose why the object is different from the role-model intervention: it connects a measured trait and track choice rather than randomly shifting field information.

**Optional frontier prompt.** Students can extend the memo to either early-career setbacks [@fadlonLyngseNielsen2022earlyCareerSetbacks] or anticipated discrimination and major choice [@lepageLiZafar2025anticipatedDiscrimination]. The prompt asks them to state whether the design is mainly about later adjustment or expected treatment before entry, which margin is observed, and what counterfactual is credible.

Open research questions for the lab:

1. Which early-choice interventions produce durable changes in career outcomes rather than only field declarations?
2. When do role models change information, identity, beliefs about returns, or expectations about discrimination?
3. How can researchers distinguish competitiveness from beliefs about success, risk, or expected treatment?
4. Which early-career shocks reveal true adjustment frictions rather than prior sorting?
5. What data would connect field choice, first job, firm assignment, promotion, and family timing in one lifecycle design?

## Methods Box

:::{admonition} Methods Box: Match The Sorting Claim To The Design
:class: note

**Reduced-form field and education interventions.** Use randomized or quasi-random exposure to role models, information, advising, or field content. Name the observed margin: course taking, major declaration, applications, internships, or first occupation.

**Teacher-bias and role-model designs.** Use teacher assignment, grading environments, classroom exposure, or mentor presence. Name the variation and the signal being shifted.

**Survey-expectations and beliefs designs.** Measure expected returns, expected treatment, discrimination expectations, belonging, or perceived fit before choices. Be explicit about whether the design shifts beliefs or only observes them.

**Early-career quasi-experiments.** Use early placement, lottery, shock, or assignment variation. These designs speak to persistence, switching, wage growth, family timing, and later adjustment rather than initial preferences alone.

**Long-panel and lifecycle administrative designs.** Follow workers from education or entry through careers. Strong for timing and persistence; causal interpretation depends on the source of variation.

**Decomposition versus causal evidence.** Decompositions allocate gaps across fields, occupations, firms, hours, or returns. Causal designs estimate the effect of a specified intervention or shock on a specified margin.

:::

## Reading Ladder And References

**Start with the sorting map.** Use Goldin's discussion of the grand gender convergence and high-skill career structure as broad background on why occupational and temporal organization matter [@goldin2014grandGenderConvergence].

**Early choices and field interventions.** Porter and Serra are the primary reading for role models and economics major choice [@porterSerra2020femaleRoleModelsMajor].

**Competition, aspirations, and track choice.** Buser, Niederle, and Oosterbeek provide the anchor for competitiveness and later educational or career choices [@buserNiederleOosterbeek2014genderCompetitivenessCareerChoices].

**Teacher signals and stereotypes.** Lavy and Sand show how stereotypical bias in school environments can affect human-capital choices, with Card, Domnisoru, Sanders, and Taylor as a related teacher-exposure reading [@lavySand2018teacherBiasHumanCapital; @cardDomnisoruSandersTaylor2022femaleTeachers].

**Anticipated discrimination.** Lepage, Li, and Zafar are the frontier anchor for expected discrimination and major choice [@lepageLiZafar2025anticipatedDiscrimination].

**Later adjustment and career inertia.** Fadlon, Lyngse, and Nielsen anchor early-career setbacks; Bertrand, Goldin, and Katz anchor dynamic high-skill career divergence [@fadlonLyngseNielsen2022earlyCareerSetbacks; @bertrandGoldinKatz2010dynamicsGenderGap].

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week3-sequence-decomposition` to classify a gender gap in earnings into early-choice, entry-sorting, later-adjustment, returns, and interaction components. Which terms are accounting objects, and which require causal variation?
2. In Equation {eq}`eq-week3-initial-sorting`, explain how anticipated discrimination {math}`D^e_{io}` can change field choice before a worker meets an employer.
3. In Equation {eq}`eq-week3-dynamic-career`, give two examples of switching costs {math}`K_{i,t}(o,o')` that could differ by gender after labor-market entry.
4. Compare Porter and Serra with Buser, Niederle, and Oosterbeek. What is the identifying variation in each? What is the observed margin?
5. Compare an occupation decomposition with an early-career quasi-experiment. Which is better for describing the size of between-occupation sorting? Which is better for identifying adjustment frictions?
6. Give one reason Week 3 must mention norms and one reason Week 5 should carry the main norms analysis.

## Reproducibility And Code Lab Note

The Week 3 code lab lives at `labs/03-education-skills-aspirations-and-occupational-sorting/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates local synthetic data, reproduces a reduced-form role-model intervention exercise, and transfers the same diagnostic logic to a competitiveness and track-choice exercise. It runs without confidential microdata.

## Slide Companion Note

The Week 3 slide deck lives at `slides/week3/03-education-skills-aspirations-and-occupational-sorting.tex`. The deck is a conceptual map rather than a duplicate of the chapter. It defines the central question, bridges from Week 2, separates early-choice and later-adjustment channels, maps role models, competition, information, teacher signals, anticipated discrimination, early-career inertia, the Week 5 norms bridge, and the Week 4 firm-side transition.

## Bridge Forward

Week 4 moves inside firms. Week 3 explains who enters which fields and early career ladders; Week 4 asks how firms hire, evaluate, pay, promote, allocate authority, and retain workers once they arrive. Week 5 then returns to norms, bargaining, and institutions directly. Together, the three weeks separate worker-side sorting, firm-side allocation, and norm/institution channels without pretending they are independent in real careers.
