# Week 9. Frontier Methods, New Data, and Evolving Measurement of Gender in Labor Research

## Central question

How are new data, designs, and measurement choices changing gender-and-labor research, and where are the main empirical shortfalls in the existing literature?

## Why this week matters

This week is the methodological capstone of the course. By this point students have seen the main substantive objects in gender and labor: household allocation, education and sorting, firms and internal labor markets, norms and bargaining, policy incidence, safety and reproductive autonomy, and comparative evidence. The next step is to ask what researchers can *actually* learn about these objects with modern data and design choices, where current evidence is strong, and where it is still weak.

The aim is not to turn the course into a generic econometrics lecture. The aim is to help students map gender questions to empirical settings, then map those settings to practical methods, data, measurement choices, and research opportunities.

```{admonition} Core points
:class: important
- New data change what labor economists can see about jobs, firms, hours, authority, safety, sorting, and welfare, but better data do not automatically solve identification problems.
- Matched employer–employee data, administrative panels, audits and field experiments, time-use data, job postings, platform data, and survey/expectations data each illuminate different gender margins.
- In gender research, empirical difficulty often comes from the interaction of **selection**, **measurement**, and **equilibrium response**, not from lack of descriptive patterns.
- A strong gender-and-labor paper usually does three things clearly: define the labor margin, justify the measurement, and explain what counterfactual or identifying variation actually isolates the mechanism.
- Important empirical gaps remain in firm-side measurement, hidden harms, intersectional heterogeneity, evolving identity categories, and portability across institutional settings.
```

## Bridge

Earlier weeks emphasized substantive mechanisms:
- Week 2 focused on household allocation, fertility, and child penalties.
- Week 3 studied education, aspirations, and occupational sorting.
- Week 4 moved inside firms.
- Week 5 studied norms and bargaining.
- Week 6 studied policy incidence.
- Week 7 studied violence, safety, and reproductive autonomy.
- Week 8 asked which mechanisms travel across countries.

This week asks how those literatures are actually identified, measured, and extended. It also prepares students for Week 10, where they will turn substantive puzzles into research designs of their own.

## Field Core

### 1. Data families and what they let researchers see

The first goal of the lecture is to organize the expanding data environment. The key idea is that different data sources do not simply give “more detail”; they reveal different labor margins and create different identification possibilities.

Use `assets/tables/09-data-design-toolkit-map.md` to organize the main families:

- matched employer–employee data for firm-specific pay-setting, promotion, retention, and sorting [@cardCardosoKline2016];
- administrative panels for lifecycle shocks, childbirth, policy reforms, and event-study designs [@klevenLandaisSogaard2019];
- audits and field experiments for hiring, evaluation, screening, and treatment of applicants [@goldinRouse2000; @bertrandMullainathan2004; @delfino2024];
- surveys, expectations data, and vignette designs for aspirations, anticipated discrimination, bargaining beliefs, and norms [@bursztynFujiwaraPallais2017; @lepageLiZafar2024];
- time-use data for unpaid work, scheduling, care, and invisible labor margins [@cortesPan2024];
- job postings and text-as-data for employer demand, job design, stated restrictions, and gendered language [@kuhnShen2023];
- platform and transaction data for high-frequency labor supply, pay, and flexibility choices [@cookDiamondHallListOyer2021];
- new measurement of gender identity, workplace climate, and intersectionality, which expands the object of study but introduces small-cell, privacy, and category-comparability problems [@eames2025].

The lecture should make clear that “best data” depends on the question. Rich firm data are not automatically best for hidden harms; audits are not automatically best for long-run equilibrium effects; surveys are not automatically weak if the object is belief formation.

### 2. Mapping empirical settings to actual econometric methods

Students often understand the *setting* but not the practical econometric toolkit. This week should make that mapping explicit.

Use `assets/tables/09-setting-to-methods-map.md` as a practical bridge. At minimum the chapter should connect these settings to commonly used methods:

- matched employer–employee panels → worker and firm fixed effects, AKM decompositions, event studies around job transitions, between/within-firm decompositions [@cardCardosoKline2016];
- childbirth and lifecycle shocks → stacked event studies, dynamic treatment effects, decomposition of earnings/employment/hours [@klevenLandaisSogaard2019];
- audits and hiring experiments → callback-rate comparisons, randomized resume or signal variation, treatment-effect heterogeneity [@goldinRouse2000; @bertrandMullainathan2004; @eames2025];
- job-search/application data → choice-set measurement, application-demand decompositions, directed-search designs, ban/removal experiments [@fluchtmannGlennyHarmonMaibom2024; @kuhnShen2023];
- time-use / care allocation → diary aggregation, time-budget decompositions, linking unpaid work to labor outcomes [@cortesPan2024];
- platform data → high-frequency fixed-effects designs, within-worker comparisons, decomposition of earnings into hours, task choice, speed, and experience [@cookDiamondHallListOyer2021];
- workplace climate / harassment data → linked survey-admin evidence, reporting vs prevalence distinctions, exit/turnover analysis [@folkeRickne2022];
- text/job-posting data → dictionary/classifier construction, demand-side language measurement, ad-level quasi-experiments [@kuhnShen2023].

The point is not to teach every estimator in detail. The point is to give students a concrete translation layer from empirical environment to feasible tools.

### 3. Empirical challenges and recurring shortfalls in the literature

A dedicated section should diagnose where the literature remains fragile. This is a core part of the week.

Use `assets/tables/09-empirical-challenges-and-shortfalls-map.md` to organize the discussion.

The chapter should highlight at least these recurring problems:

- **selection into observed employment**: many wage-gap and firm-gap studies observe only workers who remain in employment, excluding those deterred from entry or pushed out;
- **sorting vs treatment**: occupational, firm, and policy studies often struggle to separate who selects into a setting from how the setting changes outcomes;
- **timing and anticipation**: childbirth, leave, promotions, and safety-related decisions often have anticipatory responses that complicate event-study interpretation;
- **underreporting and hidden harms**: harassment, violence, coercion, and unsafe conditions are often poorly measured in wage data, complaint data, or reported incidents [@folkeRickne2022];
- **firm adaptation and equilibrium response**: transparency, equal-pay rules, scheduling regulation, and anti-discrimination rules may change hiring, task assignment, or sorting, not just wages [@bakerHalberstamKroftMasMessacar2023];
- **legal categories vs lived treatment**: administrative sex/gender categories may not capture identity, presentation, or treatment in workplaces, especially for LGBTQ+ populations [@eames2025];
- **intersectional small cells**: richer identity measurement creates sparse data, precision problems, and disclosure/privacy constraints;
- **external validity and transportability**: hiring audits, platform settings, and one-country institutional designs may identify a mechanism clearly but say less about broader labor markets unless framed carefully.

This section should be constructive rather than cynical: the message is that these are precisely the places where new contributions are possible.

### 4. Evolving measurement of gender, workplace climate, and identity

This week also needs a dedicated measurement section because the object “gender” itself is evolving in labor research.

Use `assets/tables/09-gender-measurement-and-identity-map.md`.

The chapter should distinguish:
- legal sex categories,
- self-identified gender,
- perceived gender by employers/coworkers,
- workplace climate and culture,
- intersectional identity dimensions.

It should then ask:
- which of these is observed in a given dataset?
- which one is theoretically relevant for the mechanism?
- when does mismeasurement create attenuation vs conceptual misclassification?
- how should researchers think about privacy, disclosure, and comparability over time?

### 5. Why this week can start a research career

This week should end by turning methodological diagnosis into concrete research opportunities.

Use `assets/tables/09-research-opportunities-map.md`.

Good opportunities likely lie where:
- data richness has improved faster than identification strategy,
- a familiar margin is still badly measured,
- firm-side adjustment is missing,
- hidden harms are omitted from standard welfare objects,
- legal categories do not match lived treatment,
- comparative designs have not yet separated mechanism from setting.

## Research Lab

The Research Lab should be practical and explicitly career-starting.

### Suggested lab logic
- **Reproduce** one clean method paper with a transparent design and publicly usable code or bounded pedagogical data.
- **Diagnose** what the design learns well and what it cannot see.
- **Transfer** the design logic to a nearby gender-and-labor setting.

### Recommended anchors
Primary anchor:
- `[@fluchtmannGlennyHarmonMaibom2024]` for administrative application data and search/sorting methods.

Challenge anchors:
- `[@cardCardosoKline2016]` for matched employer–employee methods,
- `[@kuhnShen2023]` for job-posting and ad-level quasi-experimental evidence,
- `[@bakerHalberstamKroftMasMessacar2023]` for transparency and firm response,
- `[@cookDiamondHallListOyer2021]` for platform data decompositions.

Optional frontier anchors:
- `[@eames2025]` for evolving measurement of gender identity in audit designs,
- `[@folkeRickne2022]` for hidden harms and linked survey-admin data.

### Research-design questions students should practice
- What is the labor margin?
- What is observed directly, and what is proxied?
- What selection problem is most severe?
- Where is equilibrium adjustment likely to show up?
- What welfare object is missing from the standard outcome data?
- What new data or linkages would make the question tractable?

## Reading ladder

Foundational framing:
- `[@goldin2014]`
- `[@blauKahn2017]`
- `[@olivettiPetrongolo2016]`

Matched employer–employee and firm methods:
- `[@cardCardosoKline2016]`
- `[@cullenPerezTruglia2023]`

Administrative panels and event studies:
- `[@klevenLandaisSogaard2019]`
- `[@cortesPan2024]`

Audits, field experiments, and hiring designs:
- `[@goldinRouse2000]`
- `[@bertrandMullainathan2004]`
- `[@delfino2024]`
- `[@eames2025]`

Applications, postings, and text:
- `[@fluchtmannGlennyHarmonMaibom2024]`
- `[@kuhnShen2023]`

Platform, transparency, and hidden harms:
- `[@cookDiamondHallListOyer2021]`
- `[@bakerHalberstamKroftMasMessacar2023]`
- `[@folkeRickne2022]`

## Forward bridge

The final lecture should now be able to do more than summarize themes. It should help students move from:
- substantive gender puzzle,
- to labor margin,
- to empirical setting,
- to feasible measurement,
- to identification strategy,
- to portability and welfare interpretation.

That is the main payoff of this methods capstone.
