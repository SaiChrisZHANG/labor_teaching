# Frontier Methods, New Data, And Evolving Measurement Of Gender In Labor Research

New data are changing gender-and-labor research because they make previously hidden margins visible: applications before matches, firms before wages, supervisors before promotions, time use before hours, climate before quits, and identity before administrative categories. The central question for Week 9 is: **How are new data, designs, and measurement choices changing gender-and-labor research, and where are the main empirical shortfalls in the existing literature?**

This week is designed to kick-start research careers. Students should leave with a practical research map: start from a labor object, choose the data family that can see the relevant margin, state the identifying variation, diagnose what remains unobserved, and then turn the shortfall into a feasible project. The lecture is methodological, but it is not generic econometrics. Every method appears because it helps answer a gender-and-labor question about jobs, firms, hours, authority, safety, identity, sorting, policy incidence, or welfare.

:::{admonition} Core points
:class: important

- Better data do not automatically solve identification. A strong paper still needs a labor margin, a credible comparison, and a clear counterfactual.
- Descriptive gap measurement asks where gender differences appear. Causal identification asks what mechanism generated them and what would change under a counterfactual.
- Matched employer-employee data, administrative panels, audits, surveys, time-use data, job postings, platform data, and climate or identity measures reveal different margins.
- Gender research often turns on four distinctions: worker sorting versus firm treatment, within-firm versus between-firm gaps, incidence versus hidden harms, and direct outcomes versus welfare objects.
- The frontier is especially open where legal categories do not match lived treatment, small cells make intersectional evidence difficult, firm adjustment is undermeasured, and hidden harms are absent from wage and employment data.

:::

## Learning Objectives

By the end of Week 9, students should be able to:

1. classify the main data families used in modern gender-and-labor research and state which labor margins each family observes well;
2. distinguish descriptive gap measurement from causal identification;
3. map empirical settings to practical econometric tools, including event studies, dynamic treatment effects, worker and firm fixed-effects decompositions, audit designs, application decompositions, time-budget decompositions, text-as-data methods, and platform-data decompositions;
4. separate worker sorting from firm treatment and within-firm gaps from between-firm gaps;
5. diagnose empirical shortfalls in the existing literature and link them to earlier weeks in the course;
6. evaluate measurement choices around legal sex, self-identified gender, perceived gender, workplace climate, privacy, small cells, and intersectionality;
7. convert a methodological gap into a research-design pitch for Week 10.

## Bridge

Weeks 2 through 8 built the substantive objects. Week 2 studied care, fertility, household allocation, and child penalties. Week 3 studied education, aspirations, skills, and occupational sorting. Week 4 moved inside firms to hiring, promotion, pay-setting, authority, and retention. Week 5 studied norms, bargaining, and institutions. Week 6 treated policy as a shock to labor-market margins and to firm behavior. Week 7 made safety, violence, mobility, and reproductive autonomy part of the worker feasible set. Week 8 asked which mechanisms travel across countries and which depend on institutions, development, informality, care regimes, and norms.

Week 9 changes the question from "what are the mechanisms?" to "what can researchers actually see and identify?" That shift matters because the same substantive mechanism can require very different data. A child penalty can be studied with administrative event studies, time-use diaries, childcare policy reforms, employer records, or surveys of expectations. Firm-side discrimination can be studied with matched employer-employee data, internal personnel records, audits, job-posting designs, or worker climate surveys. Safety can be studied with complaints, anonymous surveys, administrative violence reports, mobility data, or exits from firms. The empirical setting is not a detail after the theory; it determines which margin is observed.

The forward bridge is Week 10. The final week asks students to write a credible research design. Week 9 supplies the translation layer: labor object -> data family -> observed margin -> identifying variation -> threats -> welfare interpretation -> research contribution.

## Field Core

### Descriptive Gaps Versus Causal Identification

A descriptive gender gap is a measured difference in an outcome:

```{math}
:label: eq-week9-descriptive-gap
\Delta^Y
=
E[Y_i \mid G_i = 1] - E[Y_i \mid G_i = 0].
```

The outcome {math}`Y_i` might be employment, hours, earnings, wages, applications, callbacks, promotion, retention, exposure to risk, reported harassment, or workplace climate. The indicator {math}`G_i` is whatever gender object the dataset measures. The gap is useful because it says where inequality appears. It is not yet a mechanism.

Causal identification asks a different question. It asks how a change in a mechanism {math}`D_i` would change the outcome for a relevant population:

```{math}
:label: eq-week9-causal-object
\tau
=
E[Y_i(1)-Y_i(0) \mid i \in \mathcal{P}].
```

The treatment {math}`D_i` could be childbirth, access to a job posting, exposure to a blind screen, a pay-transparency rule, a supervisor assignment, a commuting intervention, a workplace climate shock, or a change in legal protection. The population {math}`\mathcal{P}` matters. An estimate among employed workers, applicants, platform drivers, public-sector employees, or workers in large firms may not describe those deterred from entering the setting in the first place.

This distinction prevents three common mistakes. First, do not interpret an adjusted wage gap as a causal effect of gender. Controls can be mechanisms: occupation, firm, hours, tenure, and promotion are themselves outcomes of gendered choices and constraints. Second, do not treat a clean causal estimate on one margin as a complete welfare statement. A policy may raise wages but increase sorting, reporting costs, or hidden harms. Third, do not assume that a rich dataset sees the relevant counterfactual. Matched employer-employee data can see firm sorting and wage premiums, but not necessarily nonapplications, unpaid care, harassment exposure, or gender identity.

### A Taxonomy Of Data Families

Modern gender-and-labor research is expanding because researchers can observe more of the labor-market process. The right data family depends on the object.

```{include} assets/tables/09-data-design-toolkit-map.md
```

**Matched employer-employee data** observe workers and firms together. They are powerful when the question is whether gender gaps come from workers sorting into different firms, jobs, supervisors, teams, or wage-premium environments, or from treatment within those environments. Card, Cardoso, and Kline use matched Portuguese data to quantify how firms shape the relative pay of women [@cardCardosoKline2016]. The observed margin is wages and worker-firm matches. The identifying variation comes from comparisons across firms and especially from movers whose pay changes when they move across firms. The design can separate firm premiums and sorting, but it does not by itself reveal why workers sort or how nonemployed workers are excluded.

**Administrative panels** observe individuals over time, often with earnings, employment, childbirth, education, policy exposure, and sometimes employers. They are the natural setting for event studies and dynamic treatment effects. Kleven, Landais, and Sogaard use Danish administrative data to study child penalties over event time [@klevenLandaisSogaard2019]. The observed margins are earnings, wages, hours, employment, and occupation before and after childbirth. The identifying variation is timing around childbirth, interpreted with care because fertility timing, anticipation, and household choices are not random. Administrative panels are excellent for long-run dynamics, but weak on unpaid work, expectations, and workplace climate unless linked to surveys.

**Audits and field experiments** directly manipulate signals or information in hiring, evaluation, or recruitment. Blind auditions study screening when evaluators cannot observe gender-relevant cues [@goldinRouse2000]. Resume audits randomize names or applicant attributes to identify differential callbacks [@bertrandMullainathan2004]. Recent field experiments can vary recruiting messages, job content, or gendered signals [@delfino2024; @eames2025]. The observed margin is usually callback, interview, application, or offer. The identifying variation is randomized. The limitation is that audits often see a narrow stage of the match and may not reveal long-run careers, equilibrium responses, or actual workplace treatment.

**Surveys and expectations data** measure beliefs, aspirations, anticipated discrimination, bargaining expectations, reservation wages, and norms. These data are not second-best when the object is subjective belief or anticipated treatment. Bursztyn, Fujiwara, and Pallais show how marriage-market incentives can affect labor-market investments [@bursztynFujiwaraPallais2017]. Lepage, Li, and Zafar study anticipated discrimination and educational choices [@lepageLiZafar2024]. The observed margin is belief, expectation, stated choice, or reported behavior. The identifying variation can come from survey experiments, vignettes, information treatments, or panel belief updates. The main threats are measurement error, experimenter demand, limited persistence, and selection into survey response.

**Time-use data** observe unpaid work, care, multitasking, scheduling, and nonmarket time. They are essential for Week 2 mechanisms because wages and hours do not fully measure household production. Cortes and Pan review the importance of children and remaining gender gaps [@cortesPan2024]. Time-use designs often use diary aggregation, time-budget decompositions, pre/post comparisons, or linkages to labor outcomes. The observed margin is minutes or hours allocated across market work, care, housework, leisure, commuting, and sleep. The limitation is that time-use data often lack rich firm information and may be cross-sectional.

**Job postings and text-as-data** observe employer demand before hiring. Kuhn and Shen study what happens when employers can no longer discriminate in job ads [@kuhnShen2023]. The observed margin includes stated gender preferences, required hours, flexibility, tasks, pay information, occupational language, and applications or callbacks when linked. The identifying variation can come from a posting ban, platform rule change, ad-level quasi-experiment, or classifier that measures language at scale. The risk is conceptual: text features must be tied to a labor mechanism rather than treated as decorative predictors.

**Platform and transaction data** observe high-frequency labor supply, task choice, acceptance, pricing, experience, and earnings. Cook, Diamond, Hall, List, and Oyer decompose the gender earnings gap among rideshare drivers [@cookDiamondHallListOyer2021]. The observed margins include hours, timing, location, speed, task choice, and experience. The identifying variation is often within-worker or within-platform: compare workers over time, decompose earnings into operational margins, and ask which margins generate gaps. The limitation is that platform workers are selected, platforms have unusual rules, and broader careers are often invisible.

**Gender identity and workplace climate measures** expand the object from legal sex to lived treatment, perceived gender, disclosure, belonging, harassment, and cultural fit. Eames studies hiring discrimination at the intersection of sex and nonbinary gender identity [@eames2025]. Folke and Rickne connect sexual harassment to labor-market inequality [@folkeRickne2022]. The observed margin may be identity, perceived identity, climate, reported exposure, retention, or exit. The central challenge is that small cells, privacy, nonresponse, and changing categories are not nuisances; they define what can be responsibly measured.

### Mapping Settings To Econometric Tools

Students often know the substantive setting before they know the practical method. The following map is the bridge from empirical environment to toolkit.

```{include} assets/tables/09-setting-to-methods-map.md
```

The mapping is not mechanical. Each method needs an observed margin and a source of identifying variation.

**Childbirth and lifecycle shocks.** The observed margins are earnings, employment, hours, occupation, firm, and sometimes time use. The common tools are event studies, stacked event studies, dynamic treatment effects, and decompositions by outcome. The identifying variation is timing around childbirth or a policy shock that changes fertility, leave, childcare, or job protection. The main threat is anticipation: workers may change jobs, hours, marriage, fertility timing, and care arrangements before the event. A good design states which pre-trends matter and whether the estimate is a child effect, a timing effect, a policy effect, or a selected-parent effect.

**Matched worker-firm panels.** The observed margins are wages, firm identifiers, worker moves, tenure, occupation, and sometimes establishment, manager, or team. Tools include worker and firm fixed effects, AKM-style decompositions, mover designs, event studies around job transitions, and within-firm versus between-firm decompositions. The identifying variation comes from worker mobility across firms and changes in pay when workers enter firms with different wage premiums. A basic decomposition is:

```{math}
:label: eq-week9-within-between
\bar w_m-\bar w_f
=
\sum_j (s_{mj}-s_{fj})\bar w_j
+
\sum_j s_{fj}(\bar w_{mj}-\bar w_{fj}),
```

where the first term captures between-firm sorting and the second term captures within-firm gender gaps. The equation is descriptive unless the sorting or treatment component is tied to credible variation. A worker fixed effect can absorb stable worker differences; it cannot explain why workers entered different firms or why some left employment.

**Hiring audits and field experiments.** The observed margins are callbacks, interviews, offers, responses to job ads, or evaluator scores. Tools include randomized resume signals, randomized applicant names, randomized identity signals, treatment-effect heterogeneity, and callback-rate comparisons. The identifying variation is random assignment. The observed margin is usually a direct screening outcome, not long-run productivity or welfare. This is why audits are sharp for discrimination at the studied stage and weaker for internal careers or equilibrium adjustment.

**Applications, search, and job-board settings.** The observed margins are vacancies viewed, applications submitted, callbacks, match composition, search radius, reservation wages, and job characteristics. Tools include application decompositions, directed-search models, difference-in-differences around platform or posting rules, event studies, and ad-level quasi-experiments. Fluchtmann, Glenny, Harmon, and Maibom study the gender application gap using administrative application data [@fluchtmannGlennyHarmonMaibom2024]. The observed margin is pre-match search and applications. The identifying variation can come from job characteristics, platform choice sets, policy changes, or within-worker comparisons. The contribution is to observe the application margin directly rather than infer it from accepted jobs.

**Time-use and care allocation.** The observed margins are care minutes, household production, market hours, multitasking, commute time, and scheduling. Tools include time-budget decompositions, diary aggregation, panel regressions, and pre/post designs around childbirth, care shocks, school schedules, or policy reforms. The identifying variation is often timing or policy-induced change in care constraints. The threat is that time-use categories are coarse and cannot always distinguish choice, constraint, and bargaining.

**Text, postings, and employer demand.** The observed margins are ad language, stated gender preferences, wage posting, flexibility, required hours, seniority, task descriptions, and application responses. Tools include dictionaries, supervised text classification, embeddings or topic models when validated, ad-level fixed effects, and quasi-experiments around rule changes. The identifying variation can be a platform ban on discriminatory ads, an employer-level change in posting policy, or randomized ad text. The key research habit is validation: the text measure must predict or represent a labor object such as demand, flexibility, exclusion, or culture.

**Platform and transaction panels.** The observed margins are hours, task choice, acceptance, location, timing, speed, customer ratings, experience, and pay. Tools include within-worker decompositions, high-frequency fixed effects, dynamic learning designs, and decomposition of earnings into hours, task selection, speed, tenure, and scheduling. The identifying variation is often within-worker variation across times, tasks, or locations. The strength is high-frequency behavior; the limitation is selected platform participation and weak visibility of outside options.

**Climate, harassment, and hidden harms.** The observed margins may be complaints, survey-reported exposure, climate measures, exits, turnover, sick leave, earnings, or job moves. Tools include linked survey-administrative analysis, hazard models, event studies around reported incidents, selection corrections, and designs that distinguish reporting from prevalence. The identifying variation is hard: a reported incident is not random exposure. The right question is often whether the design identifies the effect of exposure, the effect of reporting, or the effect of a workplace environment that generated both.

### Worker Sorting Versus Firm Treatment

Week 4 introduced the firm as a labor-market institution. Week 9 makes the empirical distinction sharper.

Worker sorting means that women and men enter different firms, teams, occupations, supervisors, schedules, or jobs. Firm treatment means that conditional on the relevant position in the firm, workers receive different pay, evaluation, tasks, authority, flexibility, exposure, or promotion. Both can be present. Both can be endogenous. Both can be welfare-relevant.

Matched employer-employee designs help because they observe worker-firm matches. The Card, Cardoso, and Kline logic asks how much of the wage gap reflects sorting into firms with different wage premiums and how much reflects bargaining or treatment within firms [@cardCardosoKline2016]. Cullen and Perez-Truglia show how workplace interactions and informal networks can shape the gender gap inside firms [@cullenPerezTruglia2023]. These papers push students to ask: is the relevant variation across firms, within firms, across managers, across teams, or across informal access to information?

The empirical danger is to call every residual firm gap "treatment." A within-firm gap may still reflect job assignment, occupation, hours, tenure, remote-work eligibility, promotion track, or unmeasured tasks. Conversely, sorting is not necessarily preference. It may reflect care constraints, search frictions, safety, anticipated discrimination, or prior treatment. The best papers avoid moral shortcuts and name the observed margin precisely.

### Incidence, Hidden Harms, And Welfare Objects

Policy incidence and hidden harms require different measurement. Incidence asks who bears the effect of a policy or institutional change: workers, firms, coworkers, consumers, households, applicants, or nonemployed workers. Hidden harms ask what standard outcomes miss: fear, harassment, coercion, retaliation, risk, stigma, identity concealment, mobility avoidance, or dignity at work.

Baker, Halberstam, Kroft, Mas, and Messacar study pay transparency and gender equality [@bakerHalberstamKroftMasMessacar2023]. The observed margins include wages and employer response. The identifying variation is policy exposure. The incidence question is not only whether the gender gap narrows; it is whether firms compress pay, change hiring, reorganize jobs, or shift bargaining. Folke and Rickne show why hidden harms belong in labor economics: harassment can shape sorting, retention, wage interpretation, and welfare even when standard wage gaps are incomplete [@folkeRickne2022].

The direct outcome is what the data measure. The welfare object is what the worker values. A direct outcome might be earnings. A welfare object might include earnings, hours, risk, dignity, flexibility, safety, option value, and future authority:

```{math}
:label: eq-week9-welfare-object
V_{it}
=
E_t\sum_{\tau=t}^{T}\beta^{\tau-t}
\left[
c_{i\tau}
- \phi h_{i\tau}
- \rho r_{i\tau}
- \psi H_{i\tau}
+ A_{i\tau}
+ \Omega_{i\tau}
\right].
```

Here {math}`r` is risk, {math}`H` is hidden harm, {math}`A` is amenity or authority, and {math}`\Omega` is option value over future work, care, mobility, identity disclosure, or fertility timing. A paper does not need to estimate every component. It does need to say which component is observed and which interpretation would be overclaiming.

### Empirical Challenges And Shortfalls In The Existing Literature

The existing literature is strong enough to be cumulative, but many core margins remain fragile. These shortfalls are not reasons to give up. They are research openings.

```{include} assets/tables/09-empirical-challenges-and-shortfalls-map.md
```

**Household allocation and fertility.** Week 2 evidence often uses childbirth event studies or policy reforms. The challenge is that fertility timing, marriage, childcare, job choice, and labor supply co-evolve. Anticipatory behavior can begin before childbirth, and observed parents are selected. New contributions can link administrative panels to time-use, childcare availability, job flexibility, and welfare measures beyond earnings.

**Education and occupational sorting.** Week 3 showed that early choices embed expectations, peer effects, teacher treatment, role models, social norms, and anticipated discrimination. The shortfall is that many papers observe realized major or occupation but not the beliefs and constraints that generated the choice. Better expectation panels, application data, and experiments around information or role models can distinguish preference, constraint, and anticipation of treatment.

**Firm-side gender gaps.** Week 4 evidence has improved through matched employer-employee and personnel data, but many studies still stop at wages or promotions. The frontier is to observe tasks, supervisors, evaluation language, job ladders, schedules, informal networks, and outside offers. The key identification problem is worker sorting versus firm treatment. A design should state whether the variation is worker mobility, manager assignment, policy rollout, vacancy posting, or randomized evaluation.

**Norms and bargaining.** Week 5 warned that norms are often inferred from outcomes. A paper that says "norms" after observing a gap has not measured a norm. Better designs measure norm content, belief distributions, perceived sanctions, and bargaining expectations, ideally repeatedly or with experiments that shift information. The observed margin should be labor supply, search, bargaining, promotion, retention, or household allocation, not a vague cultural residual.

**Policy incidence.** Week 6 emphasized that policies move multiple margins. Transparency, quotas, childcare, leave, tax rules, and protections can alter wages, hiring, compliance, sorting, hours, firm organization, and reporting. Existing evidence can be weak when it reports one outcome and calls it the policy effect. Stronger papers decompose incidence across workers, firms, households, applicants, and coworkers.

**Safety, violence, and reproductive autonomy.** Week 7 showed that hidden harms are often invisible in wage and employment data. Complaint data measure reported incidents, not prevalence. Wage premiums may compensate risk or reflect constrained sorting. Strong designs link surveys, administrative reports, exits, mobility, and job quality while separating exposure from reporting and response.

**Comparative and global evidence.** Week 8 argued for mechanism-first comparative work. The shortfall is portability. A country-specific policy design may identify a mechanism internally but say little about another setting unless the paper states transportability conditions: care infrastructure, informality, enforcement, sectoral composition, mobility, law, and norms.

**Identity and workplace climate.** Standard administrative data often record legal sex but not gender identity, perceived gender, disclosure, nonbinary identity, sexual orientation, or workplace climate. The shortfall is conceptual as well as statistical. Legal categories may be the available measure; lived treatment may be the mechanism. Frontier work must protect privacy while being honest about small cells and category changes.

### Measurement Of Gender, Identity, Climate, And Intersectionality

The object "gender" is not a single variable. Researchers must say which gender concept the dataset measures and which concept the mechanism requires.

```{include} assets/tables/09-gender-measurement-and-identity-map.md
```

**Legal sex or administrative category.** This is often what tax, employer, education, or social-insurance data contain. It can be useful for long panels and linkage, but it may not match identity, presentation, or workplace treatment. A paper using legal sex should not claim to measure all gendered experience.

**Self-identified gender.** This is closer to lived identity, including nonbinary and transgender identities when measured well. It can be central for LGBTQ+ labor research, disclosure, belonging, and workplace climate. The problems are small cells, nonresponse, confidentiality, and category changes over time. These are not merely technical; they affect what can be published responsibly.

**Perceived gender by employers or coworkers.** This may be the actual treatment variable in hiring, promotion, harassment, or customer-facing work. It is rarely observed directly. Audit designs can manipulate signals; linked surveys can ask about perception; text or names can proxy perceived categories, but the paper must state the limits.

**Workplace climate and culture.** Climate can affect retention, authority, voice, mental health, and willingness to report harm. It should not be treated only as a control. If climate is the mechanism, the data need to measure it as an object: survey modules, complaints, internal reports, language in reviews, coworker composition, or turnover patterns.

**Intersectionality.** Gender interacts with race, ethnicity, class, migration status, disability, age, parenthood, sexuality, gender identity, and local institutions. Intersectional analysis is necessary because average gender gaps can hide who bears the constraint. But richer cells create precision and disclosure problems. Good practice means pre-specifying aggregation rules, reporting honest uncertainty, and protecting privacy.

**Legal categories versus lived treatment.** A dataset may observe "female" and "male" because the law or administrative form requires those categories. A workplace may treat workers based on perceived gender presentation, pregnancy, parental status, race-gender stereotypes, nonbinary identity, or sexuality. The empirical question should determine the measurement strategy. When the available category and the mechanism differ, the paper should say so plainly.

### Research Opportunities

The most promising research openings sit where data, methods, and substantive gaps meet.

```{include} assets/tables/09-research-opportunities-map.md
```

**Hidden harms beyond wages and employment.** Use climate surveys, anonymous reporting, administrative violence records, complaint systems, text in reviews, or turnover to study safety, dignity, retaliation, and welfare. The contribution is strongest when hidden harms are tied to labor-market behavior.

**Better firm-side gender measurement.** Link personnel records, payroll, job ladders, manager assignment, evaluation language, schedules, and internal vacancies. The contribution is to separate evaluation, task assignment, informal networks, promotion, and pay-setting rather than call all firm gaps residual discrimination.

**Identity and treatment mismatch.** Build designs where legal category, self-identity, perceived identity, and workplace treatment can be distinguished. This can include audit designs, carefully protected surveys, or climate modules linked to outcomes.

**Search and application behavior.** Application data and platform data let researchers observe the pre-match process. The contribution is to distinguish nonapplication, employer screening, callback, match, and retention.

**Comparative portability.** Use multi-country or multi-institution settings to ask whether a mechanism travels. The contribution is not another country fact; it is a mechanism-first transportability design.

**Intersectional gender research.** Design privacy-safe aggregation and interpretation rules before estimating. The contribution is to show which average effects hide heterogeneity and why that heterogeneity changes labor-market interpretation.

**Policy as identification of deeper mechanisms.** Policies can reveal constraints, bargaining, search frictions, discrimination, or firm organization. The contribution is to decompose which margin moves and what that says about the mechanism.

## Research Lab

### Reproduce -> Diagnose -> Transfer

The Week 9 lab is built around a bounded synthetic-data path. It is a teaching analog, not an official replication, and it does not require confidential microdata.

**Reproduce.** The primary anchor is Fluchtmann, Glenny, Harmon, and Maibom on the gender application gap [@fluchtmannGlennyHarmonMaibom2024]. Students use synthetic job-application data to reproduce compact application-gap decompositions. The observed margins are applications, job attributes, worker constraints, and callbacks. The method separates descriptive gender gaps in applications from observable job-attribute and search-intensity margins.

**Diagnose.** Students classify what the design learns well and what it cannot see. The design observes applications but not every job viewed, every nonapplication, workplace climate after hiring, or long-run firm treatment. Students compare the application setting to matched employer-employee evidence from Card, Cardoso, and Kline [@cardCardosoKline2016] and job-ad evidence from Kuhn and Shen [@kuhnShen2023].

**Transfer.** Students transfer the logic to two nearby settings: matched worker-firm decompositions inspired by Card, Cardoso, and Kline [@cardCardosoKline2016] and job-posting policy variation inspired by Kuhn and Shen [@kuhnShen2023]. Optional frontier memos ask how pay transparency reveals firm response [@bakerHalberstamKroftMasMessacar2023], how platform data support within-worker decompositions [@cookDiamondHallListOyer2021], and how evolving identity measurement changes audit or application designs [@eames2025].

### Research-Design Checklist

A Week 9 project pitch should answer seven questions:

1. **Labor object.** Is the paper about employment, hours, applications, wages, firms, promotions, retention, safety, climate, identity, mobility, or welfare?
2. **Observed margin.** What exactly does the data observe: accepted jobs, posted jobs, applications, callbacks, internal evaluations, time use, transactions, complaints, or beliefs?
3. **Gender measure.** Is gender observed as legal sex, self-identified gender, perceived gender, identity signal, parental status, or workplace treatment?
4. **Identification.** What is the source of variation: event timing, policy rollout, random assignment, mover variation, platform rule change, text variation, or linked survey-admin timing?
5. **Sorting versus treatment.** Does the design observe who enters the setting and how the setting treats them once there?
6. **Hidden margins.** Which harms, constraints, nonapplications, outside options, or welfare components are not observed?
7. **Contribution.** What should readers update: a mechanism, a measurement practice, an econometric design, a policy interpretation, or a welfare claim?

## Methods Box

:::{admonition} Methods Box: Matching Gender Questions To Tools
:class: note

**Descriptive gap measurement.** Use when the goal is to locate where gender differences appear. Report the measured gender object, population, outcome, and conditioning variables. Do not call controls "explained" unless they are conceptually exogenous.

**Event studies and dynamic treatment effects.** Use when the question is how outcomes evolve around childbirth, policy exposure, job transition, reporting, or another timed event. State the observed event, the pre-trend logic, anticipation risks, and whether the event is selected.

**Worker and firm fixed-effects decompositions.** Use matched employer-employee data to separate worker heterogeneity, firm premiums, mover patterns, within-firm gaps, and between-firm sorting. State what mobility identifies and what nonemployment or nonapplication remains unseen.

**Audit and field experiment designs.** Use when the relevant margin is screening, callback, evaluation, or treatment of otherwise comparable signals. Randomization identifies differential treatment at the studied stage, not necessarily long-run careers.

**Application and search decompositions.** Use when data observe applications, vacancies, choice sets, or job-board behavior. State whether the design observes jobs viewed, jobs not applied to, employer callbacks, and realized matches.

**Time-budget decompositions.** Use when unpaid work, care, scheduling, and invisible labor are central. Link time categories to labor outcomes and avoid interpreting time allocation as unconstrained preference without evidence.

**Text-classification and text-as-data approaches.** Use when postings, evaluations, reviews, or communications reveal employer demand, culture, task content, or stated restrictions. Validate the text measure against a labor object.

**Platform-data within-worker decompositions.** Use when high-frequency data observe hours, task choice, timing, location, speed, ratings, and earnings. Separate within-worker margins from selection into the platform.

:::

## Reading Ladder And References

**Start with field framing.** Goldin gives the grand gender-convergence frame [@goldin2014]. Blau and Kahn summarize the evolution of the gender wage gap [@blauKahn2017]. Olivetti and Petrongolo give the cross-country evolution of gender gaps in industrialized countries [@olivettiPetrongolo2016].

**Add firm and matched-data methods.** Card, Cardoso, and Kline are the central matched employer-employee anchor for firm sorting, bargaining, and gender wage gaps [@cardCardosoKline2016]. Cullen and Perez-Truglia add informal networks and gender gaps inside firms [@cullenPerezTruglia2023].

**Add administrative panels and event studies.** Kleven, Landais, and Sogaard are the canonical child-penalty event-study anchor [@klevenLandaisSogaard2019]. Cortes and Pan provide a current synthesis of children and remaining labor-market gender gaps [@cortesPan2024].

**Add audits, experiments, and hiring designs.** Goldin and Rouse show how blind screening can change gendered evaluation [@goldinRouse2000]. Bertrand and Mullainathan provide a classic resume-audit design [@bertrandMullainathan2004]. Delfino shows experimental evidence on gender barriers in pink-collar jobs [@delfino2024]. Eames opens the frontier on sex and nonbinary gender identity in hiring discrimination [@eames2025].

**Add expectations, applications, postings, and text.** Bursztyn, Fujiwara, and Pallais show how marriage-market incentives can affect labor-market investments [@bursztynFujiwaraPallais2017]. Lepage, Li, and Zafar study anticipated discrimination and educational choices [@lepageLiZafar2024]. Fluchtmann, Glenny, Harmon, and Maibom anchor application data and search/sorting methods [@fluchtmannGlennyHarmonMaibom2024]. Kuhn and Shen anchor job postings and ad-level quasi-experimental evidence [@kuhnShen2023].

**Add platforms, transparency, and hidden harms.** Cook, Diamond, Hall, List, and Oyer show how platform data can decompose a gig-economy gender earnings gap [@cookDiamondHallListOyer2021]. Baker, Halberstam, Kroft, Mas, and Messacar study pay transparency and gender equality [@bakerHalberstamKroftMasMessacar2023]. Folke and Rickne connect sexual harassment to labor-market inequality and hidden harms [@folkeRickne2022].

## Exercises And Discussion Prompts

1. Choose one earlier week and rewrite its central question as a data-design problem. State the observed margin, the missing margin, and the identifying variation.
2. Take an adjusted gender wage gap from a paper you know. Which controls are mechanisms? Which are plausibly pre-determined? What interpretation survives?
3. Design a study that separates worker sorting from firm treatment. State whether the key variation is mover variation, manager assignment, policy rollout, audit randomization, or application behavior.
4. Pick a hidden harm from Week 7. Propose two measures: one direct but selected, and one indirect but scalable. Explain what each measure misses.
5. Write a Week 10 proposal paragraph that begins with a labor object, not a dataset. Then add the dataset and method only after the object is clear.

## Reproducibility And Code Lab Note

The Week 9 lab lives at `labs/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research/`. It uses deterministic synthetic data to practice application-gap decompositions, design diagnosis, and transfer to platform and job-posting settings. The smoke test runs only the bounded pedagogical path and does not require restricted administrative, firm, platform, or job-board data.

## Slide Companion Note

The slide deck lives at `slides/week9/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.tex`. The deck should not duplicate the chapter. It should give students a research map: why methods matter, how Weeks 2 through 8 connect, how data families differ, how settings map to econometric tools, where measurement is fragile, and how Week 10 turns those gaps into research designs.

## Forward Bridge To Week 10

Week 10 asks students to synthesize the course into credible research designs. Week 9 gives the discipline needed to do that. A good final project will not say "I have data on gender." It will say: here is the labor object, here is the gender concept, here is the observed margin, here is the identifying variation, here is the selection problem, here is the hidden welfare margin, and here is what readers should update. That is the path from a course topic to a research career.
