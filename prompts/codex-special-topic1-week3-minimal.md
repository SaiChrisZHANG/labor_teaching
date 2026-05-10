Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/sources/03-beliefs-expectations-and-job-search.md, @books/special-topic1-behavioral/assets/tables/03-beliefs-and-search-map.md, @books/special-topic1-behavioral/assets/tables/03-job-search-margins-map.md, and @books/special-topic1-behavioral/assets/tables/03-identification-and-design-map.md.

Goal: turn the Behavioral Labor Week 3 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 3
- Canonical chapter path: `books/special-topic1-behavioral/03-beliefs-expectations-and-job-search.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week3/03-beliefs-expectations-and-job-search.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/03-beliefs-expectations-and-job-search/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/03-beliefs-expectations-and-job-search.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/03-beliefs-expectations-and-job-search.md`
2. `books/special-topic1-behavioral/slides/week3/03-beliefs-expectations-and-job-search.tex`
3. `books/special-topic1-behavioral/labs/03-beliefs-expectations-and-job-search/lab.md`
4. `books/special-topic1-behavioral/labs/03-beliefs-expectations-and-job-search/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 3 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@dellaVigna2009]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week3/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week3/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic-boundary requirement:
- This week must stay focused on **job search**.
- The organizing object is how behavioral elements affect beliefs, expectations, attention, perceived competition, search effort, applications, reservation behavior, duration dependence, and employer-worker information frictions in job search.
- Do not let the chapter drift into a generic search-theory lecture, generic labor-market discrimination, or broad market-design material.
- It is fine to mention adjacent issues like wage posting, skill certification, or hiring frictions, but only insofar as they shape the job-search problem behaviorally.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- Keep the week anchored to DellaVigna’s taxonomy, but make clear that job search is the natural domain where **beliefs, expectations, perception, and limited information** are often most visible.
- The chapter should show students that behavioral job search is not one thing. It includes:
  - biased or sticky beliefs about job-finding probabilities,
  - misperception of wages or competitiveness,
  - limited information about one’s own skills or fit,
  - application costs and procrastination in search effort,
  - weak updating during unemployment spells,
  - two-sided informational frictions between workers and firms.
- Keep the chapter behavioral and labor-specific: show how labor economists turn these wedges into empirical questions.

Formal / conceptual requirements:
Include at least:
1. one benchmark search-choice object, such as:
```{math}
:label: eq:search-choice-week3
\max_{s_t,\bar{w}_t}\; p_t(s_t)\mathbb{E}\left[V^E(w)\mid w\ge \bar{w}_t\right] + \left(1-p_t(s_t)\right)V^U - c(s_t),
```
with text explaining search effort {math}`s_t`, reservation wage {math}`\bar{w}_t`, and perceived job-finding probability {math}`p_t(s_t)`;

2. one behavioral search object with subjective beliefs or misperceived probabilities, e.g.
```{math}
:label: eq:subjective-search-week3
\max_{s_t,\bar{w}_t}\; p_t^{b}(s_t)\mathbb{E}^{b}\left[V^E(w)\mid w\ge \bar{w}_t\right] + \left(1-p_t^{b}(s_t)\right)V^U - c(s_t),
```
and a clear explanation that the behavioral wedge can enter through beliefs, perceived wage offers, or perceived competitiveness rather than preferences alone;

3. one discussion of duration dependence and belief updating:
   - why job seekers' beliefs can be predictive yet insufficiently updated during unemployment;
   - why this matters for reservation behavior, effort, and welfare;

4. one two-sided information subsection:
   - workers lack information about wages, fit, or prospects;
   - firms lack information about worker skills;
   - job search is therefore a behavioral-information environment, not just a frictionless application problem;

5. one subsection on perceived competition / wage announcements:
   - posted wages affect search, but workers may also infer competitiveness from wages, altering applications;

6. one subsection on policy / information interventions:
   - brochures, advice, skills signals, or information provision can alter search strategies and employment outcomes.

Methods requirements:
- Explicitly distinguish:
  - elicited beliefs,
  - survey-measured expectations,
  - field experiments on information provision,
  - field experiments on job-posting content or application incentives,
  - certification / skill-signaling experiments,
  - structural job-search estimation with subjective beliefs.
- Make clear what each design identifies and what it does not.
- Show students how behavioral objects in job search are empirically separated from pure search frictions, unobserved heterogeneity, or standard rational learning.

Suggested empirical anchors:
- beliefs and duration dependence: `[@muellerSpinnewijnTopa2021]`
- information provision to job seekers: `[@altmannFalkJaegerZimmermann2018]`
- two-sided limited information and skill certification: `[@carranzaGarlickOrkinRankin2022]`
- perceived competition from posted wages: `[@belotKircherMuller2022]`
- job-search impatience / effort margin: `[@dellaVignaPaserman2005]`
- application costs and talent selection: `[@abebeCariaOrtizOspina2021]`

Field Core requirements:
- This should be one of the more material-heavy weeks in the course.
- It should move cleanly from:
  1. benchmark search problem,
  2. behavioral wedges in beliefs and expectations,
  3. duration dependence and weak updating,
  4. information provision and search strategy,
  5. two-sided information and certification,
  6. perceived competition / wage postings,
  7. welfare and policy implications.
- Do not turn this into a generic job-search-theory survey.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@muellerSpinnewijnTopa2021]`
- Secondary / challenge anchor: `[@carranzaGarlickOrkinRankin2022]`
- Optional extension anchor: `[@belotKircherMuller2022]`
- The lab should teach students how to diagnose:
  - what belief or information object is measured,
  - how duration dependence is interpreted,
  - how a design separates beliefs from pure heterogeneity,
  - how to transfer the logic to another search setting.
- Bounded transfer ideas:
  - apply belief-elicitation logic to another search margin,
  - adapt a certification/information design to another hiring context,
  - study how wage/quality signals alter application behavior in a new dataset or reduced pedagogical simulation.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and bridge from Week 2
  2. why job search is behaviorally rich
  3. benchmark search problem
  4. subjective beliefs and search effort
  5. unemployment duration and belief updating
  6. information provision to job seekers
  7. two-sided limited information / certification
  8. wage announcements and perceived competition
  9. methods / identification map
  10. research frontier and bridge to Week 4

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 3 slides compile from the canonical path
4. Week 3 lab smoke test passes

Important implementation notes:
- If you add Week 3 to `index.md` or `myst.yml`, do so in the same style that earlier weeks use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Keep the chapter labor-focused and research-facing rather than generic.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
