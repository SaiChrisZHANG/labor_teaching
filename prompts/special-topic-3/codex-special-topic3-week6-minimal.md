Read @AGENTS.md, @docs/repo-workflow.md, @docs/special-topics-roadmap.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, and the week inputs:
- @prompt/codex-special-topic3-week6-minimal.md
- @source/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.md
- @bibliography/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.bib
- @tables/06-policy-to-margin-incidence-map.md
- @tables/06-firm-response-and-welfare-map.md
- @tables/06-policy-as-identification-device-map.md
- @tables/06-frontier-and-reading-map.md

Goal: turn Gender Study Week 6 into a polished long-form chapter package while keeping the editable inputs minimal.

Week identity:
- Course: special-topic3-gender
- Week: 6
- Canonical chapter path:
  `books/special-topic3-gender/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.md`
- Canonical slide path:
  `books/special-topic3-gender/slides/week6/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.tex`
- Canonical lab path:
  `books/special-topic3-gender/labs/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from the week bibliography into `books/special-topic3-gender/references.bib`.
2. Deduplicate repeated BibTeX entries; keep only one canonical entry per cite key.
3. Do not change citation keys.

Required outputs:
1. `books/special-topic3-gender/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.md`
2. `books/special-topic3-gender/slides/week6/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.tex`
3. `books/special-topic3-gender/labs/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection/lab.md`
4. `books/special-topic3-gender/labs/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 6 into the book

Special-topics conventions:
- Every chapter must begin with a short orientation and a clearly visible **Core points** box.
- Do not create a default Extension box.
- Frontier material can live inside Field Core or Research Lab.
- Use linked citation syntax in prose markdown: `[@citekey]`.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use the course-local bibliography only.
- Slides must live only under `books/special-topic3-gender/slides/week6/`.
- Slide compilation outputs should live alongside the `.tex` source.
- Use the `research` conda environment for local commands.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- This week must be a **framework for researching gender-based policies**, not a policy shop.
- The organizing question is: which labor-market margins move, who bears incidence, how do firms respond, and when does welfare improve?
- Use policies as examples of labor-market mechanisms, and also as shocks that identify deeper gender-related labor questions.
- Keep the lecture long and substantial.

Non-negotiable lecture architecture:
1. Opening orientation:
   - why a policy week belongs in a labor course
   - why incidence and margins matter more than simple “gap closed / not closed” narratives

2. Core points box:
   - policies move different margins
   - incidence can fall on workers, firms, coworkers, households, or future careers
   - firm response is central
   - welfare is not the same as gap reduction
   - policy variation can identify underlying gender mechanisms

3. Bridge:
   - connect back to Weeks 2–5:
     - household constraints
     - early choices and sorting
     - firm-side gaps
     - norms and bargaining
   - show how Week 6 uses policies to stress-test those mechanisms

4. Field Core:
   Organize by margins and incidence, not by policy shopping.
   A strong structure is:
   A. A policy-incidence framework:
      - participation / hours / attachment
      - wages / pay-setting / bonuses
      - promotion / authority / leadership
      - occupational sorting / firm sorting
      - fertility / care allocation / household bargaining
      - welfare / autonomy / child outcomes / firm outcomes
   B. Childcare and care-support policies
   C. Parental leave and return-to-work policies
   D. Taxation / transfers / second-earner incentives
   E. Quotas / representation / pipeline interventions
   F. Transparency / equal-pay / anti-discrimination / protection rules
   G. Flexible scheduling / workplace protections / implementation and compliance
   For each block:
      - identify the main margin moved
      - identify likely firm response
      - identify who bears incidence
      - identify what labor question the policy helps reveal

5. Research Lab:
   - use policy variation as an empirical device
   - separate reduced-form policy effects from underlying mechanisms
   - include a practical “policy-as-identification-device” section
   - end with student project ideas

Formal requirements:
- Include at least one compact policy-incidence framework in math or structured notation.
- Include at least one explicit welfare object.
- Clearly separate:
  - average treatment effects on outcomes
  - incidence
  - equilibrium / firm response
  - welfare
- Make clear that policy evaluation is not identical to mechanism identification.

Empirical/literature requirements:
- This is a reading-heavy frontier week.
- Use the week bibliography seriously; do not collapse the week to 4–5 papers.
- The chapter should clearly discuss a broad, high-quality set of papers spanning:
  - childcare
  - parental leave
  - taxation / second-earner incentives
  - quotas
  - pay transparency / equal-pay rules
  - gendered laws / legal protections
  - workplace protections / reporting / safety where relevant
- Use both classic and recent papers where appropriate.
- Make the paper discussion concrete enough that students can see how researchers actually answer the questions.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@blundellDuchiniSimionTurrell2025`.
- Secondary / challenge anchor: `@gentilePassaroKojimaPakzadHurson2026`.
- Optional extension anchors: `@baileyBykerPatelRamnath2025`, `@bertrandBlackJensenLlerasMuney2019`, `@bjorvatnFerrisGulesciNasgowitzSomvilleVandewalle2025`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- It should include, at minimum:
  1. central question and why policy incidence is a labor object
  2. bridge from Weeks 2–5
  3. policy-to-margin framework
  4. childcare / care-support evidence
  5. leave and return-to-work evidence
  6. taxation and second-earner incentives
  7. quotas, transparency, equal-pay, and protection
  8. firm response, incidence, and welfare
  9. policy as identification device
  10. bridge to Week 7

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 6 slides compile from the canonical path.
4. Week 6 lab smoke test passes.

Important implementation notes:
- If you add Week 6 to `index.md` or `myst.yml`, do so in the same style as earlier weeks.
- If you create a new smoke script, keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Keep edits minimal and reviewable.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
