Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic4-urban/index.md, @books/special-topic4-urban/OUTLINE.md, @books/special-topic4-urban/myst.yml, @books/special-topic4-urban/README.md, @books/special-topic4-urban/references.bib, and these week-specific inputs:

- @special_topic4_urban_week4_edit_pack/source/04-crime-safety-environment-and-the-urban-feasible-set-for-work.md
- @special_topic4_urban_week4_edit_pack/bibliography/04-crime-safety-environment-and-the-urban-feasible-set-for-work.bib
- @special_topic4_urban_week4_edit_pack/tables/04-risk-and-feasible-set-map.md
- @special_topic4_urban_week4_edit_pack/tables/04-two-sided-equilibrium-map.md
- @special_topic4_urban_week4_edit_pack/tables/04-data-and-methods-map.md
- @special_topic4_urban_week4_edit_pack/tables/04-welfare-and-hidden-harms-map.md

Goal: draft Week 4 of special-topic4-urban as a polished chapter, slide deck, and lab package.

Target chapter:
- `books/special-topic4-urban/04-crime-safety-environment-and-the-urban-feasible-set-for-work.md`

Target slides:
- `books/special-topic4-urban/slides/week4/04-crime-safety-environment-and-the-urban-feasible-set-for-work.tex`

Target lab folder:
- `books/special-topic4-urban/labs/04-crime-safety-environment-and-the-urban-feasible-set-for-work/`

This is a content-drafting task, but it must preserve the existing special-topics workflow.

Non-negotiable conventions:
1. Use the special-topics chapter structure:
   - opening orientation
   - Core points box
   - Bridge
   - Field Core
   - Research Lab
   - reading ladder / references if appropriate
2. Core points box is required.
3. Do NOT add a default extension box.
4. Linked citations only in prose markdown:
   - use `[@citekey]`
   - do not use bare `@citekey`
   - do not use backticked prose citations
5. Use only the course-local bibliography as the destination bibliography:
   - `books/special-topic4-urban/references.bib`
6. Merge any missing entries from the week-specific `.bib` into the course-local bibliography and deduplicate repeated entries.
7. Use the local conda environment `research` for validation.
8. Slides must live only in:
   - `books/special-topic4-urban/slides/week4/`

Substantive requirements for this week:
- Keep the week labor-focused.
- This is not just a “crime and environment” lecture.
- The key framing is two-sided:
  1. crime/safety/environment as labor-market constraints that change the feasible set for work
  2. labor-market opportunity, job loss, and earnings prospects as determinants of crime and risky activity
- The chapter should therefore provide an equilibrium-style framework that tells both sides of the story.
- The environment section should include pollution/heat/noise/productivity/labor-supply margins.
- The crime/safety section should include workplace harassment/violence and commuting/public-space risk where relevant.
- The chapter should emphasize why wages alone can be a poor welfare statistic when risk and exposure differ across workers and places.

Paper and literature use:
- Build the narrative around a compact but serious research spine drawn from the supplied bibliography.
- Make the empirical mechanisms concrete.
- Do not let the chapter become a loose list of papers.
- Keep the focus on mechanisms, identification, and welfare interpretation.

Required tables:
- include and use the supplied tables in the chapter where appropriate
- if a table needs light polishing for formatting when inserted, that is acceptable

Slide requirements:
- produce a concise Beamer deck in the repo’s standard style
- slides should reflect the chapter’s structure
- include a slide that explicitly lays out the two-sided equilibrium framework
- include a slide on empirical designs/data
- keep slide filenames and week-folder conventions clean

Research Lab requirements:
- create a lab handout and structure that follows the repo’s standard lab workflow
- anchor the lab to one main empirical paper/design
- include a bounded extension idea
- include a smoke-test path if the current workflow expects one
- keep it realistic and research-oriented

Implementation notes:
- If any local references to Week 4 paths need to be added to `myst.yml` or `index.md`, do so minimally.
- Do not modify other weeks except for tiny cross-links if absolutely necessary.
- Do not rewrite course-level scaffolding beyond the smallest needed integration edits.

Validation:
1. run a strict build:
   `cd books/special-topic4-urban && conda run -n research jupyter book build --html --strict`
2. compile the Week 4 slides from the canonical path
3. if the lab has a smoke path, run it
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created or changed
2. whether the week bibliography was merged/deduplicated into the course-local bibliography
3. pass/fail for the strict build
4. pass/fail for slide compilation
5. pass/fail for lab smoke test if applicable
6. any remaining manual follow-up items
