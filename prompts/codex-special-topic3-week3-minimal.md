Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/sources/03-education-skills-aspirations-and-occupational-sorting.md, @books/special-topic3-gender/assets/tables/03-early-choices-vs-later-adjustment-map.md, @books/special-topic3-gender/assets/tables/03-mechanisms-and-evidence-map.md, @books/special-topic3-gender/assets/tables/03-norms-bridge-map.md, and @books/special-topic3-gender/assets/tables/03-data-and-methods-map.md.

Goal: turn the Gender Study Week 3 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Gender Study
- Week: 3
- Canonical chapter path: `books/special-topic3-gender/03-education-skills-aspirations-and-occupational-sorting.md`
- Canonical slide path: `books/special-topic3-gender/slides/week3/03-education-skills-aspirations-and-occupational-sorting.tex`
- Canonical lab path: `books/special-topic3-gender/labs/03-education-skills-aspirations-and-occupational-sorting/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/03-education-skills-aspirations-and-occupational-sorting.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic3-gender/03-education-skills-aspirations-and-occupational-sorting.md`
2. `books/special-topic3-gender/slides/week3/03-education-skills-aspirations-and-occupational-sorting.tex`
3. `books/special-topic3-gender/labs/03-education-skills-aspirations-and-occupational-sorting/lab.md`
4. `books/special-topic3-gender/labs/03-education-skills-aspirations-and-occupational-sorting/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 3 into the book

Special-topic conventions:
- Every chapter must contain a clearly visible **Core points** box near the top.
- No default Extension / Optional Extension box.
- If there is genuine frontier or optional material, surface it inside Field Core or Research Lab rather than forcing a separate extension box.
- Use linked citations in prose markdown only, e.g. `[@porterSerra2020femaleRoleModelsMajor]`; do not use bare `@key` or backticked citation keys in prose.

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `books/special-topic3-gender/references.bib`.
- Slides must live only under `books/special-topic3-gender/slides/week3/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week3/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established opening orientation -> Core points -> Bridge -> Field Core -> Research Lab structure.
- Keep the week focused on education, skills, aspirations, and occupational sorting.
- The chapter must cleanly separate the **two main channels**:
  1. gender affects early choices (education, major/track, skill accumulation, aspirations, competitiveness, information, role models, anticipated discrimination);
  2. gender directly creates inertia or adjustment frictions after early choices are made (career ladders, early job matches, flexibility constraints, persistence of initial placements, direct barriers to later adjustment).
- Add a short but explicit bridge to Week 5:
  - domestic and workplace gender norms help shape aspirations, educational choices, and what jobs are perceived as feasible or desirable;
  - however, norms are not the main object of Week 3 and should not dominate the lecture.
- Do not treat observed sorting as either pure preference or pure constraint.
- Include at least:
  - one conceptual decomposition distinguishing early-choice vs later-adjustment channels,
  - one formal/object-level representation of sorting or dynamic career evolution,
  - four figures,
  - four tables,
  - a real reading ladder with citations,
  - a clear backward bridge to Week 2 and forward bridge to Weeks 4 and 5.
- Treat this as a full 3-hour core chapter with optional frontier material embedded in Field Core / Research Lab.

Substantive emphasis:
- Early-choice channel should include papers/ideas on:
  - role models and mentors,
  - competitiveness and aspirations,
  - teacher bias / stereotypes / information,
  - anticipated discrimination affecting field choice.
- Later-adjustment / inertia channel should include papers/ideas on:
  - early career sorting and persistent later outcomes,
  - occupational/career path dependence,
  - direct gendered barriers to moving out of early tracks,
  - flexibility constraints / timing / early-career mismatch.
- Make clear that these channels can interact.

Methods requirements:
- Explicitly distinguish:
  - reduced-form field/education interventions,
  - teacher-bias or role-model designs,
  - survey-expectations / beliefs designs,
  - early-career quasi-experiments,
  - long-panel/lifecycle administrative designs,
  - decomposition vs causal designs.
- Do not present empirical results without naming the identifying variation and the observed margin.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@porterSerra2020femaleRoleModelsMajor]`.
- Secondary / challenge anchor: `[@buserNiederleOosterbeek2014genderCompetitivenessCareerChoices]`.
- Optional extension anchor: `[@fadlonLyngseNielsen2022earlyCareerSetbacks]` or `[@lepageLiZafar2025anticipatedDiscrimination]`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course reorientation,
  2. Week 2 -> Week 3 bridge,
  3. why sorting is not a single mechanism,
  4. early choices channel,
  5. aspirations / competition / information / role models,
  6. anticipated discrimination and field choice,
  7. later adjustment / inertia channel,
  8. early-career path dependence and long-run outcomes,
  9. short bridge to Week 5 norms,
  10. research frontier and Week 4 bridge.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 3 slides compile from the canonical path
4. Week 3 lab smoke test passes

Important implementation notes:
- If you add Week 3 to `index.md` or `myst.yml`, do so in the same style used elsewhere in the special-topic books.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
