Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/sources/07-experiments-measurement-and-behavioral-identification-in-labor.md, @books/special-topic1-behavioral/assets/tables/07-behavioral-object-data-and-design-map.md, @books/special-topic1-behavioral/assets/tables/07-empirical-setting-to-econometric-methods-map.md, and @books/special-topic1-behavioral/assets/tables/07-identification-diagnostics-and-common-failures.md.

Goal: turn the Behavioral Labor Week 7 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 7
- Canonical chapter path: `books/special-topic1-behavioral/07-experiments-measurement-and-behavioral-identification-in-labor.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week7/07-experiments-measurement-and-behavioral-identification-in-labor.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/07-experiments-measurement-and-behavioral-identification-in-labor/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/07-experiments-measurement-and-behavioral-identification-in-labor.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/07-experiments-measurement-and-behavioral-identification-in-labor.md`
2. `books/special-topic1-behavioral/slides/week7/07-experiments-measurement-and-behavioral-identification-in-labor.tex`
3. `books/special-topic1-behavioral/labs/07-experiments-measurement-and-behavioral-identification-in-labor/lab.md`
4. `books/special-topic1-behavioral/labs/07-experiments-measurement-and-behavioral-identification-in-labor/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 7 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@dellaVigna2009]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week7/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week7/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This week is the empirical toolkit lecture for Behavioral Labor.
- It should remain labor-focused and should not become a generic econometrics course or a generic methodology survey.
- The purpose is to teach students how behavioral labor economists move from:
  - a behavioral object,
  - to a labor-market setting,
  - to a data design,
  - to an actual econometric method,
  - to interpretation and welfare.
- The chapter should bridge the gap between empirical settings and the actual methods commonly used in applied work.
- Students should leave the week understanding not just that a certain empirical setting is useful, but also which econometric tools are typically used and why.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- The chapter should be organized around a practical arc:
  - what counts as behavioral identification in labor,
  - measuring behavioral objects,
  - experiments and information interventions,
  - job-search duration and hazard settings,
  - nonlinear incentives, salience, and bunching,
  - structural behavioral estimation,
  - a practical methods bridge that maps empirical settings to econometric tools,
  - common failure modes, diagnostics, and interpretation.
- The chapter should feel like a toolkit lecture inside a labor course, not an econometrics textbook chapter.

Formal / conceptual requirements:
Include at least:

1. one measurement equation for a latent behavioral object:
```{math}
:label: eq:measurement-week7
z_{ij} = \theta_i + \eta_{ij}
```
where `{math}`\theta_i`` is a latent behavioral object (belief, preference parameter, norm sensitivity, etc.) and `{math}`\eta_{ij}`` is measurement noise.

2. one canonical randomized-treatment estimating equation:
```{math}
:label: eq:rct-week7
Y_i = \alpha + \beta T_i + X_i'\gamma + \varepsilon_i
```
with a discussion of when OLS/ANCOVA is the right practical estimator and when randomization inference or treatment-effect heterogeneity should be added.

3. one search-duration / hazard object:
```{math}
:label: eq:hazard-week7
h_{it} = \Pr(U_{i,t+1}=0 \mid U_{it}=1,\, X_{it}, B_{it})
```
and a discussion of discrete-time logit/probit or Cox-style hazard implementations for behavioral search settings.

4. one nonlinear-schedule / bunching object:
```{math}
:label: eq:bunching-week7
\hat e = \frac{\Delta b / b}{\Delta (1-\tau)/(1-\tau)}
```
or an equivalent local elasticity object, together with a discussion of bunching estimators and what they do and do not identify when salience or knowledge frictions matter.

5. one structural-estimation object:
```{math}
:label: eq:structural-week7
\hat \psi \in \arg\min_{\psi \in \Psi}
\left[m^{data}-m^{model}(\psi)\right]'W\left[m^{data}-m^{model}(\psi)\right]
```
where `{math}`\psi`` denotes behavioral parameters and the text should explain when MLE, SMM, or related structural tools are useful in behavioral labor.

Field Core requirements:
- Make the chapter explicitly practical.
- Add a named subsection or table-level synthesis that answers:
  **Given this empirical setting, what methods do behavioral labor economists actually use?**
- Cover at least these method families in a labor-focused way:
  - randomized field experiments and ANCOVA-style estimators,
  - survey elicitation / repeated subjective expectations data,
  - duration / hazard models for search and unemployment,
  - bunching / kink / notch methods under salience or information frictions,
  - IV / RD / DiD / event-study style quasi-experiments where behavior is shifted by policy or information shocks,
  - structural estimation (MLE / SMM / dynamic discrete choice or closely related approaches),
  - heterogeneity analysis using interactions, random coefficients, or related tools.
- No need to teach the methods in technical detail, but the chapter must connect settings to actual econometric practice.
- The methods bridge should be explicit enough that a student can say:
  - “this is a belief-elicitation panel, so fixed effects, validation, and measurement-error concerns matter,” or
  - “this is a job-search duration design, so hazard methods are natural,” or
  - “this is a nonlinear-schedule setting, so bunching and local elasticity tools are relevant,” or
  - “this is a behavioral parameter-recovery problem, so structural estimation may be the right tool.”

Empirical anchors to use:
- framing / course methods anchors:
  - `[@dellaVigna2009]`
  - `[@dellaVigna2018]`
  - `[@listRasul2011]`
- information / experiment design:
  - `[@haalandRothWohlfart2023]`
  - `[@altmannFalkJaegerZimmermann2018]`
  - `[@bhargavaManoli2015]`
- beliefs / expectations measurement:
  - `[@muellerSpinnewijnTopa2021]`
- structural and parameter-recovery examples:
  - `[@kaurKremerMullainathan2015]`
  - `[@dellaVignaListMalmendierRao2022]`
- salience / nonlinear incentives / knowledge frictions:
  - `[@chettyFriedmanSaez2013]`
- effort / real-effort design benchmark:
  - `[@dellaVignaPope2018]`

Methods requirements:
- Explicitly distinguish:
  - the behavioral object,
  - the labor margin,
  - the identifying variation,
  - the estimand,
  - the actual econometric method,
  - and the interpretation/welfare limits.
- Include a compact “methods cheat sheet” either as a separate subsection or by leaning heavily on the dedicated table.
- The chapter should make clear that in applied work, there is often no single “behavioral method”; rather, researchers combine labor settings with standard econometric tools plus behavioral measurement or modeling.
- The text should mention common practical choices such as:
  - OLS/ANCOVA in experiments,
  - discrete-time hazard models,
  - bunching estimators,
  - panel fixed-effects models with elicited beliefs,
  - IV/RD/DiD/event-study designs,
  - structural MLE/SMM.
- Do not turn this into a generic methods-course chapter; every method should be illustrated through a labor application.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@altmannFalkJaegerZimmermann2018]`
- Secondary / challenge anchor: `[@dellaVignaListMalmendierRao2022]`
- Optional extension anchor: `[@chettyFriedmanSaez2013]` or `[@kaurKremerMullainathan2015]`
- The lab should train students to diagnose:
  - what the behavioral object is,
  - which margin is observed,
  - which econometric method is natural,
  - what the identifying assumptions are,
  - what alternative method could have been used,
  - and how a design could be transferred to a nearby labor setting.
- The bounded student path must run locally without confidential data.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and bridge from Weeks 1–6
  2. what counts as behavioral identification in labor
  3. measuring preferences, beliefs, attention, and norms
  4. field experiments and labor settings
  5. information interventions and survey/expectations data
  6. hazard models for job-search and duration outcomes
  7. bunching, salience, and nonlinear schedules
  8. structural estimation in behavioral labor
  9. practical econometric methods cheat sheet
  10. common failure modes and interpretation
  11. bridge to Week 8

Validation requirements:
1. strict book build:
   `cd books/special-topic1-behavioral && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic1-behavioral && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 7 slides compile from the canonical path
4. Week 7 lab smoke test passes

Important implementation notes:
- If you add Week 7 to `index.md` or `myst.yml`, do so in the same style that earlier weeks use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Preserve the special-topics conventions established after the audits: Core points box required, no default Extension box, linked citations only.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
