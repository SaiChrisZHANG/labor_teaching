Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/sources/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.md, @books/special-topic3-gender/assets/tables/04-firm-side-gap-mechanisms-map.md, @books/special-topic3-gender/assets/tables/04-hiring-promotion-and-pay-setting-map.md, @books/special-topic3-gender/assets/tables/04-data-and-identification-map.md, and @books/special-topic3-gender/assets/tables/04-frontier-and-reading-map.md.

Goal: turn the Gender Study Week 4 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: special-topic3-gender
- Week: 4
- Canonical chapter path: `books/special-topic3-gender/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.md`
- Canonical slide path: `books/special-topic3-gender/slides/week4/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.tex`
- Canonical lab path: `books/special-topic3-gender/labs/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic3-gender/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.md`
2. `books/special-topic3-gender/slides/week4/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.tex`
3. `books/special-topic3-gender/labs/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps/lab.md`
4. `books/special-topic3-gender/labs/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 4 into the book

Special-topic conventions to preserve:
- include a clearly visible **Core points** box near the top
- do **not** add a default Extension box
- use linked citations only in prose markdown
- use the course-local bibliography
- keep edits minimal and reviewable

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `books/special-topic3-gender/references.bib`.
- Slides must live only under `books/special-topic3-gender/slides/week4/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week4/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established structure:
  1. short opening orientation,
  2. Core points box,
  3. Bridge,
  4. Field Core,
  5. Research Lab,
  6. reading ladder / references block.
- Keep the week focused on firms and internal labor markets as generators of gender gaps in hiring, evaluation, promotion, authority, pay-setting, and retention.
- The chapter must distinguish three broad channels:
  1. **sorting into firms and jobs**;
  2. **within-firm personnel processes** (screening, evaluation, promotion, supervision, task allocation, networks);
  3. **firm-level pay-setting rules and bargaining institutions**.
- Explicitly separate worker sorting from firm behavior.
- Treat firms as labor-market institutions that allocate authority, rents, schedules, performance metrics, promotion opportunities, and wage premiums.
- Include at least:
  - one hiring/screening object or audit-style contrast,
  - one promotion/leadership-pipeline object,
  - one firm-pay-premium / pay-setting decomposition,
  - one low-promotability-task or informal-network mechanism,
  - one policy/design subsection on pay transparency, equal-pay rules, or similar firm-facing regulation,
  - four tables,
  - a real reading ladder with citations,
  - a clear backward bridge to Week 3 and forward bridge to Weeks 5 and 6.

Substantive emphasis:
- This should be one of the most literature-rich weeks in the course.
- Include a mix of classic and frontier personnel-economics papers.
- Students should see how gender gaps emerge from:
  - hiring screens and referrals,
  - social interactions with managers,
  - subjective potential ratings,
  - low-promotability tasks,
  - firm-specific pay premiums,
  - bargaining / ask salaries / pay transparency,
  - workplace conditions that affect retention and authority.
- Make clear which papers are about **hiring**, which are about **promotion/authority**, which are about **pay-setting**, and which are about **retention or exit**.

Methods requirements:
- Explicitly distinguish:
  - audit / screening designs,
  - personnel records and promotion models,
  - manager rotation or quasi-random assignment,
  - matched employer-employee wage decompositions,
  - firm-policy reforms (e.g. pay transparency / equal-pay rules),
  - survey-linked administrative evidence,
  - reduced-form designs vs within-firm mechanism measurement.
- Do not present empirical results without naming the identifying variation and the observed margin.

Empirical anchors to use:
- classic hiring:
  - `[@goldinRouse2000blindAuditions]`
- firm-side pay-setting / sorting:
  - `[@cardCardosoKline2016bargainingSortingGender]`
- networks / authority / promotion:
  - `[@cullenPerezTruglia2023oldBoysClub]`
  - `[@bensonLiShue2026potentialPromotionGap]`
- tasks and internal allocation:
  - `[@babcockRecaldeVesterlundWeingart2017lowPromotabilityTasks]`
- firm-facing policy / pay-setting frontier:
  - `[@blundellDuchiniSimionTurrell2025payTransparency]`
  - `[@gentilePassaroKojimaPakzadHurson2026equalPaySimilarWork]`
- workplace retention / exit / conditions:
  - `[@folkeRickne2022sexualHarassment]`

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@cullenPerezTruglia2023oldBoysClub]`
- Secondary / challenge anchor: `[@goldinRouse2000blindAuditions]`
- Optional extension anchor: `[@blundellDuchiniSimionTurrell2025payTransparency]` or `[@bensonLiShue2026potentialPromotionGap]`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- It should include, at minimum:
  1. central question and why firms are labor-market institutions,
  2. Week 3 -> Week 4 bridge,
  3. sorting into firms/jobs vs within-firm treatment,
  4. hiring and screening,
  5. promotions, authority, and leadership pipelines,
  6. social networks, mentoring, and old-boy channels,
  7. task allocation and low-promotability work,
  8. firm-specific pay premiums, bargaining, and pay-setting,
  9. pay transparency / equal-pay policy frontier,
  10. bridge to Weeks 5 and 6.

Implementation notes:
- If you add Week 4 to `index.md` or `myst.yml`, do so in the same style as the existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If any prose markdown still contains bare or backticked citations, normalize them to linked citations.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 4 slides compile from the canonical path.
4. Week 4 lab smoke test passes.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
