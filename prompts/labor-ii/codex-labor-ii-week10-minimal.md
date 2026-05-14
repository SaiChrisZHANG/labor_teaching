Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/10-aggregate-fluctuations-and-labor-market-adjustment.md, @books/labor-ii/assets/tables/10-cyclical-margins-map.md, @books/labor-ii/assets/tables/10-theory-to-evidence-map.md, @books/labor-ii/assets/tables/10-measurement-and-identification-map.md, and any existing Week 10 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 10 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 10
- Canonical chapter path: `books/labor-ii/10-aggregate-fluctuations-and-labor-market-adjustment.md`
- Canonical slide path: `books/labor-ii/slides/week10/10-aggregate-fluctuations-and-labor-market-adjustment.tex`
- Canonical lab path: `books/labor-ii/labs/10-aggregate-fluctuations-and-labor-market-adjustment/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/10-aggregate-fluctuations-and-labor-market-adjustment.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/10-aggregate-fluctuations-and-labor-market-adjustment.md`
2. `books/labor-ii/slides/week10/10-aggregate-fluctuations-and-labor-market-adjustment.tex`
3. `books/labor-ii/labs/10-aggregate-fluctuations-and-labor-market-adjustment/lab.md`
4. `books/labor-ii/labs/10-aggregate-fluctuations-and-labor-market-adjustment/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 10 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week10/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week10/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on aggregate fluctuations and labor market adjustment as a labor-market lecture; do not let it drift into a general monetary-macro or Phillips-curve lecture.
- This should be one of the heavier Labor II weeks: a full 3-hour core chapter with a substantial optional 60–90 minute extension block.
- Move cleanly from theoretical/conceptual framework to empirical evidence.
- Include, in explicit mathematical form, all of the following core objects:
  1. a law of motion for unemployment,
  2. a steady-state unemployment expression,
  3. a matching function,
  4. job-finding and vacancy-filling rates,
  5. a free-entry / vacancy-posting condition,
  6. a match-surplus object,
  7. a matching-efficiency residual,
  8. an endogenous-separation condition,
  9. one on-the-job-search or job-to-job transition object,
  10. one wage-cyclicality / composition decomposition.
- At minimum the chapter must contain equations or labeled formal objects corresponding to:
  - `\dot u_t = s_t(1-u_t) - f_t u_t`
  - `u_t^* = s_t/(s_t+f_t)`
  - `m_t = \mu_t u_t^\alpha v_t^{1-\alpha}`
  - `f_t = m_t/u_t`, `q_t = m_t/v_t`
  - `\kappa = q_t E_t[J_{t+1}]` or an equivalent free-entry expression
  - `S_t = J_t + W_t - U_t`
  - `\mu_t = m_t/(u_t^\alpha v_t^{1-\alpha})`
  - `s_t = Pr(S_t(z)<0)` or an equivalent threshold formulation
  - a reduced-form `EE_t` or on-the-job-search object
  - a wage-cyclicality equation that distinguishes incumbents, movers, and composition/sorting
- In addition, include:
  - one Beveridge-curve interpretation section,
  - one unemployment stock-flow decomposition,
  - one separations / endogenous-separation section,
  - one job-to-job / on-the-job-search / churning section,
  - one wage-cyclicality and match-quality section,
  - one empirical-design and measurement section,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 9 and forward to Week 11.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- The lecture should not become a bag of macro facts.

Methods requirements:
- Explicitly distinguish:
  - unemployment as a stock vs worker flows as hazards,
  - job finding vs separation vs job-to-job transitions vs participation margins,
  - matching efficiency residuals vs heterogeneity/composition accounts of Beveridge-curve shifts,
  - cross-sectional reallocation vs aggregate unemployment dynamics,
  - wage cyclicality for incumbents vs job changers,
  - measured wage cyclicality vs cyclicality driven by sorting or match quality,
  - national time-series identification vs state/local cyclical variation vs matched employer-employee flow evidence.
- Do not present empirical results without naming:
  - the identifying variation,
  - the unit of observation,
  - the observed margin,
  - and the relevant hidden margin that remains offstage.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@barnichonFigura2015AggregateMatching`.
- Secondary / challenge anchor: `@elsbyMichaelsSolon2009InsOuts`.
- Optional extension anchor: `@karahanMichaelsPugsleySahinSchuh2017JobToJob`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be explicit about:
  1. what aggregate labor-market object is being measured,
  2. whether the design is about stocks, flows, efficiency, wages, or job ladders,
  3. what margin is observed and what margin is inferred,
  4. what cyclical comparison is being made,
  5. what transfer exercise students should implement on a small public, synthetic, or aggregate dataset.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and week repositioning,
  2. Week 9 to Week 10 bridge,
  3. labor-market stocks, flows, and the law of motion for unemployment,
  4. matching, tightness, and the Beveridge curve,
  5. free entry, surplus, and the Shimer/Hall logic,
  6. unemployment inflows, outflows, and separations,
  7. on-the-job search, job-to-job transitions, and churning,
  8. wage cyclicality, sorting, and match quality,
  9. empirical designs and what they identify,
  10. recent Beveridge-curve-shift evidence and open questions,
  11. bridge to Week 11 technology shocks and adjustment.
- The deck can be slightly longer than a standard week if needed, but it must remain cleanly structured.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 10 slides compile from the canonical path
4. Week 10 lab smoke test passes

Important implementation notes:
- If you add Week 10 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1–9 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/10-aggregate-flows-and-margins.png`
  - `assets/figures/10-beveridge-curve-and-matching-efficiency.png`
  - `assets/figures/10-separations-jobfinding-unemployment.png`
  - `assets/figures/10-job-to-job-wage-cyclicality.png`
  - `assets/figures/10-match-quality-and-reallocation.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
