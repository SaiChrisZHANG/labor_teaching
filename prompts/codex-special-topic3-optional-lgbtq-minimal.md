Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/sources/10-lgbtq-identities-work-discrimination-and-labor-market-institutions.md, @books/special-topic3-gender/assets/tables/10-lgbtq-measurement-and-core-outcomes-map.md, @books/special-topic3-gender/assets/tables/10-hiring-climate-benefits-and-law-map.md, @books/special-topic3-gender/assets/tables/10-empirical-challenges-and-research-opportunities-map.md, and @books/special-topic3-gender/assets/tables/10-reading-and-lab-map.md.

Goal: turn the optional LGBTQ+ Gender Study source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Gender Study
- Module: Optional long lecture inserted after Week 9 and before the final synthesis lecture
- Canonical chapter path: `books/special-topic3-gender/10-lgbtq-identities-work-discrimination-and-labor-market-institutions.md`
- Canonical slide path: `books/special-topic3-gender/slides/week10/10-lgbtq-identities-work-discrimination-and-labor-market-institutions.tex`
- Canonical lab path: `books/special-topic3-gender/labs/10-lgbtq-identities-work-discrimination-and-labor-market-institutions/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/10-lgbtq-identities-work-discrimination-and-labor-market-institutions.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.
4. If the live book sequence currently ends at Week 9, wire this module in as an optional long lecture after Week 9. Do not overwrite any existing final synthesis lecture; if a final synthesis chapter already exists as Week 10, preserve it and report the smallest clean way to place this optional module before it.

Required outputs:
1. `books/special-topic3-gender/10-lgbtq-identities-work-discrimination-and-labor-market-institutions.md`
2. `books/special-topic3-gender/slides/week10/10-lgbtq-identities-work-discrimination-and-labor-market-institutions.tex`
3. `books/special-topic3-gender/labs/10-lgbtq-identities-work-discrimination-and-labor-market-institutions/lab.md`
4. `books/special-topic3-gender/labs/10-lgbtq-identities-work-discrimination-and-labor-market-institutions/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire the optional lecture into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use linked citations only in prose markdown: `[@citekey]`.
- Special-topic convention: include a clearly visible **Core points** box near the top.
- Do not add a default Extension box.
- Slides must live only under `books/special-topic3-gender/slides/week10/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week10/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established opening orientation -> Core points -> Bridge -> Field Core -> Research Lab structure.
- Keep the lecture labor-focused. Do not drift into generic sexuality studies, public-health survey tours, or abstract identity theory without a clear labor-market object.
- Treat LGBTQ+ labor research as a substantial labor-economics field, not a token add-on.
- Include enough high-quality papers so students have a real reading ladder and can see multiple research designs.
- Include a dedicated section on **research opportunities / frontier gaps**.

At minimum, the final chapter should include:
1. a measurement section on sexual orientation, gender identity, disclosure, legal categories, and sample-definition problems
2. a labor-outcomes section covering employment, earnings, occupation, benefits, and firm-side treatment
3. a hiring-discrimination section with audit / field-experiment evidence
4. a workplace-climate / disclosure / harassment section
5. a legal-institutions section covering anti-discrimination law, marriage/family recognition, and benefit design
6. a specific section on transgender and nonbinary labor-market measurement and evidence
7. a research-opportunities section that identifies the most promising contribution margins
8. a real reading ladder with citations
9. a clear bridge to the final synthesis lecture

Methods requirements:
- Explicitly distinguish:
  - sexual orientation vs gender identity as empirical objects
  - disclosure/visibility vs underlying population membership
  - hiring discrimination vs within-job treatment vs selection into jobs/firms
  - legal recognition / protection vs actual workplace treatment
  - outcomes visible in wages/employment vs hidden harms in climate, safety, and welfare
- Name actual empirical designs where appropriate, including:
  - correspondence / audit studies
  - large-employer audit platforms
  - administrative identity-linkage designs
  - policy/event-study designs around marriage equality or anti-discrimination protection
  - survey/list experiments for stigma and support measurement
- Do not discuss empirical settings without saying what the identifying variation is and what the observed margin is.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@tilcsik2011prideprejudice]`
- Secondary / challenge anchors: `[@granbergAnderssonAhmed2020transhiring]`, `[@sansone2019pinkwork]`
- Optional extension anchors: `[@carpenterLee2024transgenderearnings]`, `[@klineRoseWalters2021systemic]`, `[@carpenterPostolekWarman2024sameSexBenefits]`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why LGBTQ+ labor research belongs in labor economics,
  2. bridge from Weeks 1–9 of the gender course,
  3. measurement and definitional challenges,
  4. earnings/employment/benefits patterns,
  5. hiring discrimination evidence,
  6. workplace climate / disclosure / harassment,
  7. law, family recognition, and benefit design,
  8. transgender and nonbinary measurement frontier,
  9. research opportunities,
  10. bridge to the final synthesis lecture.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 10 slides compile from the canonical path
4. Week 10 lab smoke test passes

Important implementation notes:
- If you add the optional lecture to `index.md` or `myst.yml`, do so in the same style used elsewhere in the special-topic books, but clearly mark it as optional.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
