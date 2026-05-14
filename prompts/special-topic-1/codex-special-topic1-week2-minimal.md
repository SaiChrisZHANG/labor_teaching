Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/sources/02-nonstandard-preferences-in-labor.md, @books/special-topic1-behavioral/assets/tables/02-preference-taxonomy-map.md, @books/special-topic1-behavioral/assets/tables/02-labor-applications-map.md, and @books/special-topic1-behavioral/assets/tables/02-identification-and-welfare-map.md.

Goal: turn the Behavioral Labor Week 2 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 2
- Canonical chapter path: `books/special-topic1-behavioral/02-nonstandard-preferences-in-labor.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week2/02-nonstandard-preferences-in-labor.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/02-nonstandard-preferences-in-labor/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/02-nonstandard-preferences-in-labor.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/02-nonstandard-preferences-in-labor.md`
2. `books/special-topic1-behavioral/slides/week2/02-nonstandard-preferences-in-labor.tex`
3. `books/special-topic1-behavioral/labs/02-nonstandard-preferences-in-labor/lab.md`
4. `books/special-topic1-behavioral/labs/02-nonstandard-preferences-in-labor/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 2 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@dellaVigna2009]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week2/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week2/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic-boundary requirement:
- This week must stay primarily in the worker-side topic family of **labor supply, effort, savings, and training**.
- Do not let the chapter drift into broader market design, occupational sorting, generic household finance, or generic behavioral economics.
- If other applications are mentioned, they should only be brief side remarks and not the organizing focus of the chapter.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- Keep the week anchored to DellaVigna’s taxonomy of behavioral economics, but isolate the focus to **nonstandard preferences** rather than beliefs or decision-making.
- Cover several key preference types, including but not limited to:
  - present bias / self-control problems
  - commitment demand
  - risk aversion as it matters for savings or effort-related choices
  - loss aversion / reference dependence
  - social preferences / reciprocity / fairness
- For each preference type, briefly show:
  - what the preference object is,
  - how labor economists operationalize it,
  - what kinds of labor outcomes it changes,
  - what an applied empirical design looks like.
- Keep the applications concentrated on:
  - labor supply timing and intertemporal effort
  - workplace effort and performance
  - savings behavior in work-linked settings (especially retirement or payroll-linked savings)
  - training / self-investment / completion problems

Formal / conceptual requirements:
- Include at least:
  - one DellaVigna-style taxonomy paragraph situating nonstandard preferences within Behavioral Labor
  - one quasi-hyperbolic / present-bias object
  - one commitment-demand interpretation
  - one reference-dependent or loss-aversion object
  - one social-preference / gift-exchange object
  - one welfare paragraph explaining why preference-based departures complicate labor-policy evaluation
- Use equations selectively but clearly.
- Keep the theory disciplined and connected to empirical margins.

Applied / empirical requirements:
- Explicitly distinguish which worker-side margin each preference maps onto:
  - labor supply timing
  - effort intensity
  - savings / retirement saving / payroll-linked saving behavior
  - training / self-investment / completion
- Do not present empirical results without naming the identifying variation and the observed margin.
- Use the provided tables if they fit; improve captions/labels if needed while keeping paths stable.
- If a paper is not mainly about labor supply, effort, savings, or training, keep it peripheral.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@kaurKremerMullainathan2010]` and/or `[@kaurKremerMullainathan2015]`.
- Savings-side auxiliary anchor: `[@madrianShea2001]` or `[@dufloGaleLiebmanOrszagSaez2006]` if useful for a bounded extension.
- Challenge anchor: `[@mas2006]`.
- Optional extension anchor: `[@dellaVignaListMalmendierRao2022]`.
- The bounded student path must run locally without proprietary or confidential data.
- The smoke test should only run the bounded pedagogical path.
- The lab handout should help students see how an abstract preference object becomes an applied labor design.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and bridge from Week 1,
  2. DellaVigna taxonomy with Week 2 highlighted,
  3. present bias and commitment demand in labor supply / effort,
  4. savings and self-control in work-linked environments,
  5. loss aversion / reference dependence in labor supply or performance,
  6. social preferences and workplace effort,
  7. empirical designs and what they identify,
  8. welfare and policy interpretation,
  9. bridge to Week 3 on beliefs / expectations / search.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 2 slides compile from the canonical path
4. Week 2 lab smoke test passes

Important implementation notes:
- If you add Week 2 to `index.md` or `myst.yml`, do so in the same style that the course already uses.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
