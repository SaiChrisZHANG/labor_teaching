Read @AGENTS.md, @docs/repo-workflow.md, @docs/special-topics-roadmap.md, and these files:

- @books/special-topic3-gender/index.md
- @books/special-topic3-gender/OUTLINE.md
- @books/special-topic3-gender/myst.yml
- @books/special-topic3-gender/README.md
- @books/special-topic3-gender/references.bib

Course context:
- @books/special-topic3-gender/01-why-gender-matters-for-labor-economics.md
- @books/special-topic3-gender/02-labor-supply-care-work-fertility-and-household-allocation.md
- @books/special-topic3-gender/03-education-skills-aspirations-and-occupational-sorting.md
- @books/special-topic3-gender/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.md
- @books/special-topic3-gender/05-social-norms-bargaining-and-institutions-shaping-gendered-work.md
- @books/special-topic3-gender/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.md
- @books/special-topic3-gender/07-violence-safety-mobility-and-labor-market-access.md
- @books/special-topic3-gender/08-comparative-and-global-gender-in-labor-market-development.md
- @books/special-topic3-gender/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.md

Minimal pack inputs:
- @bibliography/10-synthesis-frontier-questions-and-student-research-designs.bib
- @source/10-synthesis-frontier-questions-and-student-research-designs.md
- @tables/10-research-design-template.md
- @tables/10-where-the-literature-is-and-where-it-is-going.md
- @tables/10-interdisciplinary-directions-map.md
- @tables/10-portability-and-relevance-map.md

Goal: turn the Gender Study final-week source pack into a polished chapter package while preserving the course's established conventions.

Week identity:
- Course: special-topic3-gender
- Canonical final lecture path: `books/special-topic3-gender/10-synthesis-frontier-questions-and-student-research-designs.md`
- Canonical slide path: `books/special-topic3-gender/slides/week10/10-synthesis-frontier-questions-and-student-research-designs.tex`
- Canonical lab path: `books/special-topic3-gender/labs/10-synthesis-frontier-questions-and-student-research-designs/`
- Local conda environment: `research`

Important sequencing note:
- There is an OPTIONAL LGBTQ+ lecture that sits immediately before the final synthesis lecture.
- If that optional lecture currently occupies a conflicting `10-...` path, preserve it by renaming/moving it cleanly to an optional-module path rather than overwriting it.
- Preferred optional-module naming:
  - chapter: `books/special-topic3-gender/optional-lgbtq-identities-work-discrimination-and-labor-market-institutions.md`
  - slides: `books/special-topic3-gender/slides/optional-lgbtq/`
  - labs: `books/special-topic3-gender/labs/optional-lgbtq-identities-work-discrimination-and-labor-market-institutions/`
- Update any book wiring needed so the optional lecture remains visible as optional and the final synthesis week remains Week 10.

Before drafting:
1. Merge any missing entries from `bibliography/10-synthesis-frontier-questions-and-student-research-designs.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.
4. If the optional LGBTQ+ lecture needs renaming to avoid conflict with Week 10, perform that cleanup first.

Required outputs:
1. `books/special-topic3-gender/10-synthesis-frontier-questions-and-student-research-designs.md`
2. `books/special-topic3-gender/slides/week10/10-synthesis-frontier-questions-and-student-research-designs.tex`
3. `books/special-topic3-gender/labs/10-synthesis-frontier-questions-and-student-research-designs/lab.md`
4. `books/special-topic3-gender/labs/10-synthesis-frontier-questions-and-student-research-designs/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire the final week correctly and preserve the optional LGBTQ+ lecture

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use linked citation syntax in prose markdown.
- Use real citation keys from `books/special-topic3-gender/references.bib`.
- Special-topics convention: a clearly visible **Core points** box is required.
- Do NOT add a default Extension box.
- Slides must live only under `books/special-topic3-gender/slides/week10/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week10/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established opening orientation / Core points / Bridge / Field Core / Research Lab structure.
- This week is a research-launch capstone, not a recap.
- It must include:
  1. where the gender-and-labor literature currently is,
  2. what major questions have been answered,
  3. what important questions remain open,
  4. how students can move from a gendered labor fact to a credible research design,
  5. why gender-and-labor research is a vibrant field worth investing in,
  6. a section on interdisciplinary directions, including at least:
     - urban
     - political economy / representation / institutions
     - health / reproduction / well-being
     - and any additional frontier directions that fit naturally
- Keep it labor-focused even when discussing interdisciplinary spillovers.

Methods/research-design requirements:
- Explicitly teach students how to move from:
  - labor-market object
  - mechanism
  - comparison group / counterfactual
  - key labor margin
  - data source
  - identification strategy
  - welfare or distributional object
  - contribution
- Include a section on portability / external validity / why a study is broadly relevant.
- Include a frank section on current literature gaps and where contribution margins are largest.
- Include a short section on what “good” gender-and-labor questions look like.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Design.
- This week does not need a heavy replication package.
- The bounded lab can focus on:
  - comparing candidate project ideas,
  - diagnosing identification threats,
  - mapping outcomes to methods,
  - and producing a short research memo.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should include, at minimum:
  1. course recap as a research map
  2. where the literature is now
  3. unresolved core debates / gaps
  4. research-design template
  5. portability / external validity / broad-interest framing
  6. interdisciplinary directions
  7. project-generation guidance
  8. bridge to students’ own research agendas

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 10 slides compile from the canonical path
4. Week 10 lab smoke test passes

Important implementation notes:
- If you add Week 10 to `index.md` or `myst.yml`, do so in the same style already used by this special-topic book.
- If the optional LGBTQ+ lecture had to be renamed/repositioned, keep the smallest clean fix and update references coherently.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- whether the optional LGBTQ+ lecture needed renaming/repositioning
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
