Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/sources/10-synthesis-welfare-and-student-research-designs.md, @books/special-topic1-behavioral/assets/tables/10-research-design-template.md, @books/special-topic1-behavioral/assets/tables/10-welfare-and-evidence-map.md, and @books/special-topic1-behavioral/assets/tables/10-frontier-project-opportunities-map.md.

Goal: turn the Behavioral Labor Week 10 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 10
- Canonical chapter path: `books/special-topic1-behavioral/10-synthesis-welfare-and-student-research-designs.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week10/10-synthesis-welfare-and-student-research-designs.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/10-synthesis-welfare-and-student-research-designs/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/10-synthesis-welfare-and-student-research-designs.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/10-synthesis-welfare-and-student-research-designs.md`
2. `books/special-topic1-behavioral/slides/week10/10-synthesis-welfare-and-student-research-designs.tex`
3. `books/special-topic1-behavioral/labs/10-synthesis-welfare-and-student-research-designs/lab.md`
4. `books/special-topic1-behavioral/labs/10-synthesis-welfare-and-student-research-designs/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 10 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@dellaVigna2009]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week10/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week10/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This is the capstone week of Behavioral Labor.
- It should not be a generic review lecture.
- It should synthesize the course through three lenses:
  1. welfare and interpretation,
  2. research design and identification,
  3. frontier project development.
- The chapter should leave students ready to formulate an original behavioral-labor research project.
- It should explicitly connect worker-side frictions, workplace behavior, firm and market responses, and policy design.

Central organizing question:
How do we translate behavioral labor ideas into welfare-relevant, empirically credible, frontier research projects?

Required organizing logic:
The chapter should be built around a practical project-building framework.
At minimum, students should learn how to move from:
1. a labor-market fact or puzzle,
2. to a behavioral wedge,
3. to an institution or market setting,
4. to an identifying variation,
5. to an econometric method,
6. to a welfare interpretation,
7. to a contribution relative to the frontier.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- The chapter should feel like a capstone research studio, not a loose recap.
- It should use examples from earlier weeks, but it should not merely repeat them.
- It should make students feel that there are still many open questions in behavioral labor.

Formal / conceptual requirements:
Include at least:

1. one general behavioral-labor research mapping object:
```{math}
:label: eq:research-map-week10
Y = g(B, I, M, P, X; \theta)
```
where `{math}`B`` is the behavioral wedge or mechanism, `{math}`I`` is the institution or environment, `{math}`M`` is firm/market response, `{math}`P`` is policy or program design, and `{math}`Y`` is the observed labor-market outcome.

2. one estimand/design object:
```{math}
:label: eq:estimand-week10
\tau = \mathbb{E}[Y_i(1)-Y_i(0) \mid S_i=1]
```
and explain that the econometric problem is rarely just estimating `{math}`\tau``; it is deciding whether the design identifies a treatment effect, a behavioral parameter, a welfare-relevant wedge, or an equilibrium-adjusted response.

3. one welfare object:
```{math}
:label: eq:welfare-week10
W = \int \Psi_i\big(a_i, a_i^\star, M, P\big)\, dF(i)
```
Make explicit that behavioral labor projects need to decide whether welfare is evaluated using observed choice, an internally valid benchmark, long-run learning, or some other normative criterion.

4. one research-idea decomposition:
```{math}
:label: eq:project-week10
Contribution = Question + Mechanism + Data + Design + Interpretation
```
Use this to structure the final project-development section.

Field Core requirements:
Organize the lecture into clearly named subsections on:
- what a behavioral labor contribution looks like
- welfare and normative interpretation in behavioral labor
- mapping topic to behavioral wedge to labor setting
- mapping empirical setting to identification strategy and econometric method
- when reduced-form evidence is enough and when structural work is needed
- equilibrium and external-validity considerations
- frontier project opportunities in behavioral labor
- how to build a credible student project in this field

Substantive requirements:
- make clear that behavioral labor sits at the intersection of labor economics, behavioral economics, policy design, and market response
- explain that many good projects fail because they identify a treatment effect but not the behavioral object, or identify a behavioral object but not a labor-market margin, or estimate a margin without a welfare interpretation
- explicitly connect earlier weeks to possible project families:
  - labor supply / savings / training
  - job search and beliefs
  - attention / salience / learning
  - incentives / monitoring / workplace behavior
  - identity / norms / firm culture
  - behavioral policy design
  - firm and equilibrium responses
- make the chapter research-heavy: students should come away with open questions, not closure

Empirical / conceptual anchors to use:
- broad framing:
  - `[@dellaVigna2009]`
  - `[@chetty2015]`
  - `[@bernheimTaubinsky2018]`
- worker-side / labor-supply anchor:
  - `[@kaurKremerMullainathan2015]`
- workplace / contract / social-preference anchor:
  - `[@dellaVignaListMalmendierRao2022]`
- beliefs / job-search anchor:
  - `[@muellerSpinnewijnTopa2021]`
- take-up / implementation anchor:
  - `[@bhargavaManoli2015]`
- retirement/defaults / welfare anchor:
  - `[@bernheimFradkinPopov2015]`
- methods / information design anchor:
  - `[@haalandRothWohlfart2023]`
- frontier welfare anchor:
  - `[@allcott2025]`

Methods requirements:
- Include an explicit practical bridge between empirical setting and econometric method.
- Students should see, in one section or one substantial table, how the field commonly maps:
  - labor-supply schedule or commitment setting -> field experiment / reduced-form treatment comparison / structural estimation
  - repeated beliefs in job search -> panel FE / forecast-error analysis / hazard models
  - nonlinear schedules and knowledge frictions -> bunching / local elasticity / dynamic learning analysis
  - workplace incentives and reciprocity -> field experiments / heterogeneity analysis / contract design inference
  - implementation and take-up -> randomized encouragement / hazard models / administrative-data treatment analysis
  - welfare and targeting -> sufficient-statistics, calibrated welfare, or structural approaches
- No need to teach the estimators in detail, but the methods should be concrete rather than generic.

Research Lab requirements:
- This week should function as a proposal studio more than a standard single-paper lab.
- Keep the Reproduce -> Diagnose -> Transfer logic, but adapt it:
  - Reproduce: reverse-engineer one or two anchor papers' question/design logic
  - Diagnose: identify the behavioral object, the labor margin, the design, and the welfare claim
  - Transfer: develop a mini-project memo applying that logic to a new setting
- Use an anchor menu rather than a single anchor:
  - `[@muellerSpinnewijnTopa2021]`
  - `[@dellaVignaListMalmendierRao2022]`
  - `[@bhargavaManoli2015]`
  - `[@bernheimFradkinPopov2015]`
- The bounded student path should produce a concise research-design memo template that runs locally and does not require confidential data.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. why a capstone behavioral-labor week matters
  2. the course architecture in one map
  3. what counts as a behavioral-labor contribution
  4. welfare and interpretation
  5. mapping setting -> behavioral wedge -> design -> method
  6. when reduced-form is enough and when structure is needed
  7. frontier project families
  8. common failure modes in project design
  9. a research memo template
  10. bridge outward to dissertation-quality work and related special topics

Validation requirements:
1. strict book build:
   `cd books/special-topic1-behavioral && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic1-behavioral && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 10 slides compile from the canonical path
4. Week 10 lab smoke test passes

Important implementation notes:
- If you add Week 10 to `index.md` or `myst.yml`, do so in the same style that earlier weeks use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Preserve the special-topics conventions established after the audits: Core points box required, no default Extension box, linked citations only.
- This week should push students toward actual project generation, so err on the side of practical research guidance rather than summary prose.
