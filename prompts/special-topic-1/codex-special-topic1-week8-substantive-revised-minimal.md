Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, and the current live week files around Weeks 5–9 if they exist.

Goal: replace the current Behavioral Labor Week 8 materials with a more substantive and research-heavy equilibrium lecture.

Week identity:
- Course: Behavioral Labor
- Canonical chapter path: `books/special-topic1-behavioral/08-firm-market-and-equilibrium-responses-to-behavioral-frictions.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week8/08-firm-market-and-equilibrium-responses-to-behavioral-frictions.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/08-firm-market-and-equilibrium-responses-to-behavioral-frictions/`
- Local conda environment: `research`

Important sequencing instruction:
- The behavioral public policy lecture is canonical Week 9 material.
- Do not overwrite existing policy materials or recreate them under Week 8 paths.
- The Week 8 package should be the equilibrium-response lecture.

Before drafting:
1. Merge any missing entries from `bibliography/08-firm-market-and-equilibrium-responses-to-behavioral-frictions.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in the course-local bibliography.
3. Do not duplicate citation keys.

Non-negotiable special-topics conventions:
- Include a visible **Core points** box near the top.
- Do NOT create a default Extension box.
- Use linked citations in prose, e.g. `[@bernheimFradkinPopov2015]`.
- Do not use bare `@key` or backticked `` `@key` `` citations in prose.
- Use valid MyST markdown.

What this week is and is not:
- This is NOT a reprise of Week 5 (incentives/monitoring/reciprocity) or Week 6 (identity/norms/culture).
- Behavioral frictions, monitoring, and culture may be mentioned only in passing if needed for context, but they should NOT structure the lecture.
- The week must instead ask the next-level question:
  **once worker-level behavioral wedges exist, how do firms and markets respond, and what survives in equilibrium?**

Required structure:
1. opening orientation
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references

Required conceptual arc:
1. Why worker-level wedges do not map one-for-one into observed market outcomes.
2. A taxonomy of firm responses:
   - exploit
   - accommodate
   - insure
   - screen / sort / segment
3. Market conditions that govern whether behavioral wedges survive:
   - competition
   - transparency
   - switching costs / inertia
   - search frictions
   - worker heterogeneity
   - labor market power
4. Welfare and interpretation:
   - attenuation vs amplification of wedges
   - partial vs equilibrium effects
   - what this implies for the policy lecture

Substance requirement:
- The previous version was too thin.
- This revised week must be anchored to a real literature spine.
- Students should come away seeing how researchers actually study these questions.

Required paper spine:
At minimum, the chapter should substantially engage with the following types of papers and use them in the lecture logic, not just in a reading list:

A. Employer-sponsored benefits / savings / plan-design markets
- `[@bernheimFradkinPopov2015]`
- `[@handelKolstad2015]`
- `[@duarteHastings2012]`
- `[@hastingsHortacsuSyverson2017]`

B. Worker beliefs, search, and equilibrium/segmentation
- `[@jagerRothRoussilleSchoefer2022]`
- `[@menzio2022]`

C. Sorting / signaling / market communication
- `[@hortonKuchlerStanton2021]`

D. Broad conceptual equilibrium framing
- `[@gabaixLaibson2006]`
- `[@spiegler2015]`

You may add more references if they strengthen the lecture, but do not thin this list out.

Content requirements:
- The chapter must contain a substantial Field Core, not just conceptual bullets.
- Include at least:
  - one taxonomy figure/table of firm responses,
  - one figure/table of market conditions under which wedges survive,
  - one section on employer-sponsored benefits / savings markets,
  - one section on search/bargaining/segmentation under distorted worker beliefs,
  - one section on sorting / information / market communication,
  - one section on welfare interpretation and empirical pitfalls,
  - a concrete bridge to Week 9 policy.

Methods requirements:
- Students must see how these papers are actually identified.
- For each empirical block, name the identifying variation and observed margin.
- Explicitly distinguish:
  - worker-level reduced-form effects,
  - firm response margins,
  - market/equilibrium outcomes.
- The chapter should surface where the frontier is:
  - equilibrium measurement,
  - external validity of nudges,
  - welfare under endogenous firm response,
  - segmentation and behavioral monopsony / search.

Research Lab requirements:
- Build the lab around a clear Reproduce -> Diagnose -> Transfer structure.
- Primary anchor: `[@bernheimFradkinPopov2015]`
- Challenge anchor: `[@jagerRothRoussilleSchoefer2022]`
- Optional extension: `[@duarteHastings2012]` or `[@hastingsHortacsuSyverson2017]`
- The lab section should explain what can be diagnosed or extended:
  - menu design and defaults
  - demand elasticity / switching-cost interpretation
  - belief distortions and market segmentation
  - equilibrium interpretation limits

Slide requirements:
The slide deck should be more substantial than the previous thin version.
At minimum include:
1. central question and why Week 8 follows Weeks 1–7
2. why worker-level behavioral wedges are not enough
3. taxonomy: exploit / accommodate / insure / screen-sort
4. employer-sponsored benefits / savings as a market-response domain
5. plan choice, inertia, and welfare
6. distorted outside-option beliefs and segmentation
7. firm messages / sorting / search direction
8. competition, transparency, search frictions, and persistence
9. partial vs equilibrium welfare interpretation
10. bridge to Week 9 policy design

Implementation notes:
- Keep overlap with Weeks 5 and 6 minimal.
- Do not use monitoring, reciprocity, or culture as one of the main empirical blocks.
- If policy materials appear under noncanonical paths, keep them under the Week 9 policy package and make the smallest clean renumbering/wiring fix.
- Keep edits minimal and reviewable beyond the intended week replacement.

Validation requirements:
1. strict book build:
   `cd books/special-topic1-behavioral && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic1-behavioral && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 8 slides compile from the canonical path
4. Week 8 lab smoke test passes

At the end, report:
- files changed
- whether Week 8/Week 9 renumbering was needed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
