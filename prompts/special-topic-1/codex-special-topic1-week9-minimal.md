Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/sources/09-behavioral-public-policy-in-labor-markets.md, @books/special-topic1-behavioral/assets/tables/09-roles-of-behavioral-frictions-in-policy-design.md, @books/special-topic1-behavioral/assets/tables/09-policy-tools-implementation-and-equilibrium-map.md, and @books/special-topic1-behavioral/assets/tables/09-welfare-targeting-and-frontier-map.md.

Goal: turn the Behavioral Labor Week 9 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 9
- Canonical chapter path: `books/special-topic1-behavioral/09-behavioral-public-policy-in-labor-markets.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week9/09-behavioral-public-policy-in-labor-markets.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/09-behavioral-public-policy-in-labor-markets/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/09-behavioral-public-policy-in-labor-markets.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/09-behavioral-public-policy-in-labor-markets.md`
2. `books/special-topic1-behavioral/slides/week9/09-behavioral-public-policy-in-labor-markets.tex`
3. `books/special-topic1-behavioral/labs/09-behavioral-public-policy-in-labor-markets/lab.md`
4. `books/special-topic1-behavioral/labs/09-behavioral-public-policy-in-labor-markets/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 9 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@chettyFriedmanSaez2013]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week9/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week9/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This is the policy-design week of Behavioral Labor.
- The chapter should be organized around the role of behavioral frictions in labor-market policy design.
- It should remain labor-focused. The main policy applications should be:
  - tax credits and labor-supply incentives,
  - benefit claiming and take-up,
  - unemployment insurance and job-search support,
  - training and post-displacement investment,
  - retirement and work-linked saving,
  - disability / claiming / work incentives where useful.
- It should NOT become a generic public economics course or a generic nudges lecture.

Central organizing question:
How do behavioral frictions change the design, implementation, targeting, equilibrium effects, and welfare analysis of labor-market policies?

Required organizing logic:
The chapter should be built around a systematic taxonomy of what behavioral frictions do in labor policy.

At minimum, cover these roles:
1. behavioral frictions as biases or wedges to be corrected
2. behavioral frictions as levers that policy can harness for welfare improvement
3. behavioral frictions as implementation and take-up frictions
4. behavioral frictions as modifiers of who responds, when they respond, and how quickly they learn
5. behavioral frictions as forces that interact with firms, intermediaries, and market equilibrium
6. behavioral frictions as complications for welfare analysis, paternalism, and targeting

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- The chapter should feel like a coherent policy framework, not a bucket of interventions.
- Students should leave with a mental model of how behavioral labor policies differ from standard labor policies.

Formal / conceptual requirements:
Include at least:

1. one generic behavioral-policy environment:
```{math}
:label: eq:policy-environment-week9
p = (\tau, n, s, d)
```
where `{math}`\tau`` denotes financial incentives or budget-set parameters, `{math}`n`` denotes information/salience design, `{math}`s`` denotes simplification / administrative burden / claiming support, and `{math}`d`` denotes defaults / commitment / active-choice architecture.

2. one worker choice object with perceived or behaviorally mediated policy:
```{math}
:label: eq:behavioral-policy-choice-week9
a_i(p) \in \arg\max_{a \in \mathcal{A}} \tilde U_i(a; p, b_i) - K_i(a; p)
```
where `{math}`b_i`` summarizes behavioral frictions or beliefs and `{math}`K_i`` captures procedural or cognitive costs.

3. one take-up / implementation object:
```{math}
:label: eq:takeup-week9
D_i(p) = \mathbf{1}\!\left\{\tilde V_i(p; b_i) - C_i(p) \ge 0\right\}
```
The text should explain that policy can change take-up not only through generosity but also through salience, simplification, trust, reminders, and procedural support.

4. one dynamic learning / information-acquisition object:
```{math}
:label: eq:learning-policy-week9
b_{i,t+1} = B\!\left(b_{it},\, m_{it},\, x_{i,t+1},\, p_t\right)
```
The text should explain that policy effects can be dynamic because people learn schedules, rules, and claiming procedures over time.

5. one welfare object that makes normative ambiguity explicit:
```{math}
:label: eq:welfare-week9
W(p) = \int \Psi_i\!\left(a_i(p), a_i^\star(p), p\right)\, dF(i)
```
where `{math}`a_i^\star(p)`` is a benchmark or welfare-relevant action. The text should explain why welfare analysis is harder when choices may be distorted or when analysts disagree about what counts as welfare-relevant preference.

Field Core requirements:
Organize the lecture around the policy roles above.

At minimum, include named subsections on:
- standard labor policy versus behavioral labor policy
- biases as objects to be corrected
- biases as tools / levers for policy design
- implementation, take-up, salience, and administrative burden
- dynamic learning, endogenous information acquisition, and policy persistence
- firms, intermediaries, and equilibrium responses
- welfare, targeting, and normative ambiguity
- frontier directions in behavioral labor policy

Substantive requirements:
- Make clear that “behavioral labor policy” is not just about nudges.
- Show that behavioral frictions can matter at multiple stages:
  - response to incentives,
  - awareness and claiming,
  - program enrollment,
  - persistence and learning,
  - employer or intermediary response,
  - and welfare evaluation.
- Explain that the same friction can play multiple roles:
  - something to correct,
  - something to harness,
  - something that alters implementation,
  - and something that complicates welfare.

Empirical anchors to use:
- framing / policy logic:
  - `[@chetty2015]`
  - `[@bernheimTaubinsky2018]`
- labor-supply incentives and knowledge:
  - `[@chettyFriedmanSaez2013]`
  - `[@kostolMyhre2021]`
- take-up / implementation:
  - `[@bhargavaManoli2015]`
  - `[@liebmanLuttmer2015]`
- defaults / commitment / retirement saving:
  - `[@madrianShea2001]`
  - `[@bernheimFradkinPopov2015]`
- labor-policy implementation / training example:
  - `[@barrTurner2018]`
- methods / frontier design:
  - `[@haalandRothWohlfart2023]`
  - `[@allcottListTaubinsky2023]`

Methods requirements:
- Explicitly distinguish:
  - information experiments,
  - simplification / procedural redesign,
  - defaults / active choice / commitment designs,
  - policy-learning and dynamic-response designs,
  - local knowledge or peer-information designs,
  - welfare analysis under distorted choice,
  - and equilibrium/intermediary response settings.
- Students should see not just the empirical settings, but also the practical econometric methods that usually go with them.
- Include a compact methods bridge connecting:
  - information / reminder interventions -> randomized field experiments, ANCOVA, heterogeneity analysis
  - learning and repeated response -> panel/event-study / distributed-lag or dynamic-treatment analysis
  - take-up / claiming -> treatment-on-the-extensive-margin / hazard or duration-style take-up analysis where appropriate
  - defaults / policy menus -> bunching, reduced-form treatment comparisons, sufficient-statistics or calibrated welfare methods
  - welfare / targeting -> structural or sufficient-statistics frameworks

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@bhargavaManoli2015]`
- Secondary / challenge anchor: `[@chettyFriedmanSaez2013]`
- Optional extension anchor: `[@bernheimFradkinPopov2015]` or `[@kostolMyhre2021]`
- The lab should train students to diagnose:
  - what friction the policy is targeting,
  - whether the policy is correcting a mistake or harnessing a bias,
  - whether implementation/take-up is the main margin,
  - what the relevant welfare benchmark is,
  - and where equilibrium or intermediary responses may matter.
- The bounded student path must run locally without confidential data.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and bridge from Weeks 1–8
  2. a taxonomy of the roles of behavioral frictions in policy design
  3. standard policy versus behavioral policy
  4. biases as targets of correction
  5. biases as tools/levers for design
  6. implementation, take-up, and administrative burden
  7. dynamic learning and policy persistence
  8. firms/intermediaries/equilibrium responses
  9. welfare, targeting, and normative ambiguity
  10. frontier directions and literature gaps
  11. bridge from Week 8

Validation requirements:
1. strict book build:
   `cd books/special-topic1-behavioral && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic1-behavioral && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 9 slides compile from the canonical path
4. Week 9 lab smoke test passes

Important implementation notes:
- If you add Week 9 to `index.md` or `myst.yml`, do so in the same style that earlier weeks use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Preserve the special-topics conventions established after the audits: Core points box required, no default Extension box, linked citations only.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
