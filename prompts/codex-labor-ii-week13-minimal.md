Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/13-synthesis-and-student-research-designs.md, @books/labor-ii/assets/tables/13-labor-ii-architecture-map.md, @books/labor-ii/assets/tables/13-research-design-template.md, @books/labor-ii/assets/tables/13-frontier-and-bridge-map.md, and any existing Week 13 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 13 source pack into a polished capstone chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 13
- Canonical chapter path: `books/labor-ii/13-synthesis-and-student-research-designs.md`
- Canonical slide path: `books/labor-ii/slides/week13/13-synthesis-and-student-research-designs.tex`
- Canonical lab path: `books/labor-ii/labs/13-synthesis-and-student-research-designs/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/13-synthesis-and-student-research-designs.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/13-synthesis-and-student-research-designs.md`
2. `books/labor-ii/slides/week13/13-synthesis-and-student-research-designs.tex`
3. `books/labor-ii/labs/13-synthesis-and-student-research-designs/lab.md`
4. `books/labor-ii/labs/13-synthesis-and-student-research-designs/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 13 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week13/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week13/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Use the exact week title: `Synthesis and Student Research Designs`.
- Treat this as a true capstone week, not a perfunctory recap.
- The chapter should do four things clearly:
  1. synthesize the main conceptual blocks of Labor II,
  2. show how Labor I and Labor II fit together in modern labor economics,
  3. teach students how to turn a labor-market mechanism into a research design,
  4. bridge from this sequence to dissertation topics and later special-topics courses.
- This should be a full 3-hour core chapter with a substantial workshop-style extension block.
- Include all of the following:
  - one integrative labor-market architecture object linking workers, firms, frictions, institutions, and shocks,
  - one explicit framework for choosing units of analysis (worker, firm, establishment, occupation/task, region, market),
  - one explicit framework for choosing between descriptive, reduced-form, and structural approaches,
  - one policy-vs-shock comparison section,
  - one section that integrates wage-setting and labor market power,
  - one section that integrates labor-market institutions and regulation,
  - one section that integrates macro, technology, and trade shocks,
  - one section on partial-equilibrium versus equilibrium reasoning,
  - one section on how to build a research idea from question -> mechanism -> unit -> data -> design -> contribution,
  - one section on frontier directions and open gaps,
  - four figures minimum,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Labor I and outward to Behavioral Labor, Labor Markets and Political/Cultural Institutions, and dissertation questions.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.

Methods requirements:
- Explicitly distinguish:
  - worker-level, firm-level, place-level, and market-level objects,
  - policies versus shocks,
  - partial-equilibrium versus equilibrium effects,
  - short-run versus long-run adjustment,
  - descriptive decomposition versus causal reduced-form identification versus structural counterfactual analysis,
  - outcome variables versus welfare objects.
- Do not let the chapter make broad claims without clarifying:
  - what the unit of treatment is,
  - what margin is observed,
  - what equilibrium channels are offstage,
  - and what kind of counterfactual claim is actually justified.
- The capstone should help students understand when a design is “enough” and when a more structural or equilibrium framework is needed.

Lab requirements:
- This week’s lab is a capstone research-design studio rather than a standard single-paper replication.
- The logic should be: Diagnose -> Compare -> Design.
- Provide an anchor-paper menu spanning major Labor II blocks.
- The anchor menu must include at least:
  - `@saezSchoeferSeim2019`
  - `@yehMacalusoHershbein2022`
  - `@cengizDubeLindnerZipperer2019`
  - `@jagerNaiduSchoefer2024`
  - `@acemogluRestrepo2020RobotsJobs`
  - `@autorDornHanson2013ChinaSyndrome`
- The lab handout should require students to choose one anchor paper (or one tightly related pair), identify:
  1. the central labor-market mechanism,
  2. the unit of treatment and observation,
  3. the observed margin,
  4. the key equilibrium concern,
  5. a plausible extension or transfer design.
- The bounded student path can be memo-first rather than estimation-heavy, but it must still run locally and produce a concrete artifact.
- The smoke test should only validate the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why a synthesis week matters,
  2. Labor I -> Labor II bridge,
  3. Labor II architecture map: firms, frictions, institutions, shocks,
  4. choosing units of analysis,
  5. descriptive vs reduced-form vs structural approaches,
  6. comparative synthesis: wage-setting and labor market power,
  7. comparative synthesis: regulation and institutions,
  8. comparative synthesis: macro, technology, and trade adjustment,
  9. research idea template and common failure modes,
  10. frontier directions and bridge beyond Labor II.
- The deck can be longer than a standard week if needed, but it must remain tightly structured.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 13 slides compile from the canonical path
4. Week 13 lab smoke test passes

Important implementation notes:
- If you add Week 13 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1–12 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/13-labor-ii-architecture-map.png`
  - `assets/figures/13-question-mechanism-unit-design.png`
  - `assets/figures/13-policy-vs-shock-comparison.png`
  - `assets/figures/13-frontier-and-dissertation-bridge.png`
  - `assets/figures/13-common-failure-modes.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
