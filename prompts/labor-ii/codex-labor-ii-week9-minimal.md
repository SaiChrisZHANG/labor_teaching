Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/09-labor-regulation-enforcement-and-insurance.md, @books/labor-ii/assets/tables/09-regulation-taxonomy-map.md, @books/labor-ii/assets/tables/09-equilibrium-and-incidence-map.md, @books/labor-ii/assets/tables/09-effectiveness-spillovers-and-welfare-map.md, and any existing Week 9 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 9 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 9
- Canonical chapter path: `books/labor-ii/09-labor-regulation-enforcement-and-insurance.md`
- Canonical slide path: `books/labor-ii/slides/week9/09-labor-regulation-enforcement-and-insurance.tex`
- Canonical lab path: `books/labor-ii/labs/09-labor-regulation-enforcement-and-insurance/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/09-labor-regulation-enforcement-and-insurance.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/09-labor-regulation-enforcement-and-insurance.md`
2. `books/labor-ii/slides/week9/09-labor-regulation-enforcement-and-insurance.tex`
3. `books/labor-ii/labs/09-labor-regulation-enforcement-and-insurance/lab.md`
4. `books/labor-ii/labs/09-labor-regulation-enforcement-and-insurance/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 9 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week9/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week9/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on labor regulation, enforcement, and insurance as a coherent labor-economics framework; do not turn the lecture into a bucket of unrelated policies.
- This should be one of the heavier policy-framework weeks in Labor II: a full 3-hour core chapter with a substantial optional 60–90 minute extension block.
- In addition to the course outline, the lecture must be organized around these four questions:
  1. What is a useful general framework for understanding different types of labor regulations?
  2. How do regulations affect both sides of the labor market, and what key equilibrium effects matter?
  3. Empirically, how effective are regulations once enforcement, spillovers, and inequality implications are considered?
  4. What are the welfare implications?
- Include at least:
  - one clean general taxonomy of labor regulations,
  - one employment-protection / dismissal-cost framework,
  - one enforcement / compliance framework,
  - one insurance / unemployment-benefit equilibrium framework,
  - one section on information, transparency, or rights salience as a labor-market regulation,
  - one explicit section on effectiveness, spillovers, inequality, and welfare,
  - one empirical-design section,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 8 and forward to Week 10.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- The lecture should feel like a **research framework** for students interested in this area, not a survey list of policies.

Methods requirements:
- Explicitly distinguish:
  - regulation on the books vs effective regulation,
  - worker-targeted vs firm-targeted vs regulator-targeted policies,
  - dismissal costs / employment protection vs labor standards vs insurance vs information/transparency,
  - partial-equilibrium effects vs equilibrium effects,
  - compliance vs evasion / informal-sector adjustment,
  - direct effects on covered workers/firms vs spillovers to uncovered workers/firms,
  - employment, wages, hours, turnover, search, formality, and price incidence as different outcome margins.
- Do not present empirical results without naming:
  - the identifying variation,
  - the unit of observation,
  - the observed margin,
  - and the key unobserved equilibrium or compliance object.
- Be explicit that disagreement in this literature can come from:
  - different regulations,
  - different enforcement regimes,
  - different uncovered margins,
  - different equilibrium assumptions,
  - and different welfare criteria.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@almeidaCarneiro2012`.
- Secondary / challenge anchor: `@laliveLandaisZweimueller2015`.
- Optional extension anchor: `@vanDoornikGerardNaritomi2023`.
- You may use `@bertrandCrepon2021` or `@autorDonohueSchwab2006` as additional references in the lab handout if useful, but do not overload the bounded path.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be explicit about:
  1. what regulation is being studied,
  2. whether the key issue is enforcement, insurance, dismissal, or information,
  3. what side of the market is directly treated,
  4. what spillover or uncovered margin matters,
  5. what the relevant welfare tradeoff is,
  6. how to transfer the design to a small public, synthetic, or aggregate dataset.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and week repositioning,
  2. Week 8 to Week 9 bridge,
  3. general taxonomy of labor regulations,
  4. worker-side, firm-side, and regulator-side margins,
  5. employment protection / dismissal-cost logic,
  6. enforcement, compliance, and effective regulation,
  7. insurance / unemployment-benefit equilibrium effects,
  8. empirical designs and what they identify,
  9. effectiveness, spillovers, inequality, and welfare,
  10. bridge to Week 10 aggregate adjustment.
- The deck should be slightly longer than a standard week if needed, but still cleanly structured.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 9 slides compile from the canonical path
4. Week 9 lab smoke test passes

Important implementation notes:
- If you add Week 9 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1–8 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/09-regulation-taxonomy-framework.png`
  - `assets/figures/09-incidence-compliance-and-adjustment.png`
  - `assets/figures/09-enforcement-capacity-to-effective-regulation.png`
  - `assets/figures/09-insurance-distortion-equilibrium.png`
  - `assets/figures/09-regulation-spillovers-inequality-welfare.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
