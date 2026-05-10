Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/sources/06-identity-norms-fairness-and-labor-market-allocation.md, @books/special-topic1-behavioral/assets/tables/06-identity-norms-fairness-map.md, @books/special-topic1-behavioral/assets/tables/06-micro-norms-peer-pressure-and-firm-culture-map.md, and @books/special-topic1-behavioral/assets/tables/06-identification-and-frontier-map.md.

Goal: turn the Behavioral Labor Week 6 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 6
- Canonical chapter path: `books/special-topic1-behavioral/06-identity-norms-fairness-and-labor-market-allocation.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week6/06-identity-norms-fairness-and-labor-market-allocation.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/06-identity-norms-fairness-and-labor-market-allocation/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/06-identity-norms-fairness-and-labor-market-allocation.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/06-identity-norms-fairness-and-labor-market-allocation.md`
2. `books/special-topic1-behavioral/slides/week6/06-identity-norms-fairness-and-labor-market-allocation.tex`
3. `books/special-topic1-behavioral/labs/06-identity-norms-fairness-and-labor-market-allocation/lab.md`
4. `books/special-topic1-behavioral/labs/06-identity-norms-fairness-and-labor-market-allocation/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 6 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@akerlofKranton2005]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week6/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week6/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This week is about identity, norms, fairness, and labor-market allocation at the micro level.
- It should focus on how workers and firms respond to:
  - social identity,
  - fairness concerns,
  - pay comparisons,
  - peer pressure,
  - team norms,
  - firm culture,
  - manager-driven cultural transmission,
  - and related within-firm or near-market allocation margins.
- It should NOT become the political/cultural institutions special-topic course.
- That other course should handle:
  - labor law,
  - state capacity,
  - macro cultural persistence,
  - unions and collective political organization,
  - historical institutional change,
  - political conflict over labor-market rules.
- This week should stay at the behavioral-labor / micro-norms level:
  - worker choices,
  - workplace interactions,
  - firm culture,
  - sorting into jobs and firms,
  - pay satisfaction, effort, quits, promotions, and coworker interactions.
- It may mention gender or household norms briefly as one allocation example, but it should not become a gender-course week.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- The arc should be:
  - identity and norms as behavioral objects in labor,
  - fairness and social comparisons,
  - peer pressure and coworker norms,
  - micro-norms inside teams and firms,
  - firm culture as a labor-market object,
  - manager/supervisor transmission of norms,
  - labor-market allocation and sorting implications,
  - frontier directions.

Formal / conceptual requirements:
Include at least:

1. one identity-in-organization object:
```{math}
:label: eq:identity-utility-week6
U_i(a,j) = u\!\left(w_j\right) - c_i(a) + I_i\!\left(a, j, N_j, C_j\right)
```
where `{math}`N_j`` denotes social norms in job or team `{math}`j`` and `{math}`C_j`` denotes firm culture.

2. one fairness / social-comparison object:
```{math}
:label: eq:fairness-comparisons-week6
U_i = u\!\left(w_i\right) - c(e_i) - \phi_i \max\{0, w^{ref}_i - w_i\} - \psi_i \max\{0, w_i - w^{ref}_i\}
```
where `{math}`w_i^{ref}`` or `{math}`w^{ref}_i`` is a peer or manager comparison wage.

3. one peer-pressure / team-norm object:
```{math}
:label: eq:peer-pressure-week6
U_i(e_i) = u\!\left(w_i\right) - c(e_i) - P_i\!\left(e_i,\bar e_{-i},N_g\right)
```
where `{math}`N_g`` is the group norm and `{math}`P_i`` captures social penalties from deviating from coworker behavior.

4. one allocation / sorting object:
```{math}
:label: eq:sorting-culture-week6
j_i^\star \in \arg\max_{j \in \mathcal{J}} \; \mathbb{E}\!\left[U_i(j; X_i, N_j, C_j)\right]
```
This should make clear that identity and firm culture shape job choice and labor-market allocation.

5. one manager-transmission or culture-evolution object:
```{math}
:label: eq:culture-transmission-week6
C_{f,t+1} = \Gamma\!\left(C_{f,t}, M_{f,t}, H_{f,t}, R_{f,t}\right)
```
where culture evolves with managers `{math}`M_{f,t}``, hiring `{math}`H_{f,t}``, and reward systems `{math}`R_{f,t}``.

Field Core requirements:
- Distinguish identity/norms/fairness as behavioral mechanisms from broader institutions.
- Explain clearly how this week differs from the political/cultural institutions special topic:
  - this week is micro and allocation-focused,
  - the institutions course is macro/institutional/political and historically broader.
- Include named subsections on:
  - identity and self-image at work,
  - fairness and pay comparisons,
  - peer pressure and micro norms,
  - firm culture and labor-market sorting,
  - manager and supervisor transmission of norms,
  - frontier questions on micro culture and workplace behavior.
- Add micro-norms explicitly:
  - firm culture,
  - team culture,
  - peer pressure,
  - manager norms,
  - social sanctions and conformity,
  - belief formation about what “people like me” do at work.

Empirical anchors to use:
- theory / framing:
  - `[@akerlofKranton2005]`
- peer pressure / coworker norms:
  - `[@masMoretti2009]`
- fairness / relative pay:
  - `[@brezaKaurShamdasani2018]`
  - `[@cullenPerezTruglia2018]`
- culture communication / sorting:
  - `[@huangPacelliShiZou2024]`
- manager-driven norm transmission / frontier:
  - `[@minniNguyenSarsonsSrebot2026]`
- allocation example (brief, not dominant):
  - `[@bertrandKamenicaPan2015]`

Methods requirements:
- Explicitly distinguish:
  - field experiments on peer effects,
  - experiments or quasi-experiments on pay transparency / social comparisons,
  - survey-plus-admin designs on wage beliefs and morale,
  - firm-postings/text designs for culture communication,
  - manager-rotation or assignment designs for norm transmission,
  - sorting vs treatment vs equilibrium cultural selection.
- Do not present results without naming:
  - the behavioral object,
  - the labor margin,
  - the social/reference group,
  - the identifying variation,
  - and whether the effect is treatment, sorting, or transmission.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@masMoretti2009]`
- Secondary / challenge anchor: `[@brezaKaurShamdasani2018]`
- Optional frontier extension: `[@huangPacelliShiZou2024]` or `[@minniNguyenSarsonsSrebot2026]`
- The lab should train students to diagnose:
  - what the relevant norm or identity object is,
  - who the comparison group is,
  - whether the design identifies peer pressure, fairness, sorting, or norm transmission,
  - how the framework could extend to firm culture, algorithmic teams, or manager rotation settings.
- The bounded student path must run locally without confidential data.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and bridge from Weeks 1–5
  2. why identity/norms/fairness are behavioral labor topics
  3. topic boundary relative to the institutions course
  4. identity and self-image at work
  5. fairness and pay comparisons
  6. peer pressure and coworker norms
  7. firm culture and job sorting
  8. manager-driven norm transmission / micro culture
  9. empirical designs and frontier directions
  10. bridge to Week 7

Validation requirements:
1. strict book build:
   `cd books/special-topic1-behavioral && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic1-behavioral && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 6 slides compile from the canonical path
4. Week 6 lab smoke test passes

Important implementation notes:
- If you add Week 6 to `index.md` or `myst.yml`, do so in the same style already used in the book.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
