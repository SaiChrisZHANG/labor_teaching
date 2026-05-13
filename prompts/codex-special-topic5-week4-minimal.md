Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic5-technology/index.md
- @books/special-topic5-technology/OUTLINE.md
- @books/special-topic5-technology/references.bib
- @books/special-topic5-technology/03-worker-adjustment-skills-training-and-career-transitions.md if it exists
- @books/special-topic5-technology/04-firms-hiring-management-and-organizational-response-to-new-technology.md if it exists

If helpful, also inspect:
- the Week 4 slide file if it exists
- the Week 4 lab folder if it exists
- the Week 4 source pack if it exists in the repo

Goal: create or refresh Week 4 of the Technology, Innovation, and Labor course as a concrete labor-economics lecture on firm adoption, organizational response, and AI attitudes.

Canonical chapter target:
- `books/special-topic5-technology/04-firms-hiring-management-and-organizational-response-to-new-technology.md`

This is a week-drafting task using the special-topics conventions already established.

Non-negotiable Week 4 identity:
- The week must remain a labor-economics lecture, not a generic management or innovation lecture.
- The focus is on how firms adopt technology and reorganize labor demand, hiring, supervision, internal labor markets, and job design around it.
- AI should be treated as:
  1. a labor-demand shock inside firms,
  2. a productivity/augmentation technology,
  3. an organizational and principal-agent problem.
- A key added theme is that employees’ and managers’ attitudes toward AI can affect adoption, delegation, redesign, and resistance.
- The week must include a dedicated methods box on frontier methods for measuring and identifying AI-adoption attitudes.

Special-topics defaults to enforce:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown
- use the course-local bibliography only
- if you merge week-specific bibliography entries into `references.bib`, deduplicate repeated BibTeX entries

Required structure:
1. Opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Reading Ladder And References
7. Exercises And Discussion Prompts
8. Reproducibility And Code Lab Note
9. Slide Companion Note
10. Bridge Forward

Required Week 4 content:

A. Firm adoption and organizational response
The Field Core should clearly cover:
- complementary investments and adoption costs
- job redesign and task reassignment
- hiring/screening for new tasks
- training and internal reallocation
- supervision/monitoring changes
- promotion and internal labor-market implications
- algorithmic management / platform-style control where relevant

B. AI as both substitution and augmentation
Make clear that AI can:
- substitute for specific tasks or roles
- augment worker productivity
- change who is supervised, who is delegated to, and how performance is evaluated
- create principal-agent tensions because firms and workers may value adoption differently

C. Attitudes toward AI adoption
Add a substantive section inside Field Core on:
- employee acceptance, distrust, and adoption resistance
- manager beliefs and delegation choices
- perceived fairness / transparency / control
- algorithm aversion and acceptance in hiring/evaluation contexts
- how these attitudes may affect both measured adoption and actual productivity gains
- how such frictions can contribute to inequality within and across firms

D. Methods box
Add a dedicated methods box or clearly labeled methods subsection covering frontier designs for measuring AI-adoption attitudes, such as:
- surveys linked to worker or firm outcomes
- management surveys linked to firm administrative data
- randomized pilots / staggered rollouts inside firms
- survey experiments / vignette experiments / conjoint designs
- lab or online experiments eliciting delegation to algorithms
- matched employer–employee panels around adoption timing
- job-posting / vacancy text linked to firm adoption
- worker-level usage logs or software telemetry if available
- other strong designs you judge relevant

This methods box should answer:
- what the design identifies
- what the design cannot identify
- where attitudes can be confounded with actual productivity effects
- how a good empirical design should separate technology adoption from technology sentiment

E. Research lab
The Research Lab should use actual papers and the standard:
- Reproduce
- Diagnose
- Transfer

It should point to one primary anchor paper and one challenge/extension paper if useful.

Paper-selection principle:
- use high-quality labor or labor-adjacent frontier papers
- include some recent AI-adoption evidence
- include at least one paper or design that gets at worker/manager attitudes or algorithm aversion/acceptance
- do not invent replication packages
- be conservative if replication availability is uncertain

Required tone:
- research-facing
- concrete
- labor-focused
- oriented toward mechanisms and identification

Allowed changes:
- create or refresh the Week 4 chapter
- add a methods box
- add or revise the Research Lab
- merge week bibliography entries into the course bibliography and deduplicate
- make tiny chapter cross-links if needed

Forbidden changes:
- do not rewrite the rest of the course
- do not change bibliography keys unnecessarily
- do not use the labor-series shared bibliography as the primary bibliography
- do not create a default Extension box
- do not drift into generic AI commentary without a labor-market mechanism

Validation:
1. run a strict build for:
   `cd books/special-topic5-technology && conda run -n research jupyter book build --html --strict`
2. if the chapter references a new Week 4 slide path, ensure the path is consistent
3. fix the smallest issue and rerun if needed

At the end, report:
1. files changed
2. which paper(s) anchor the Research Lab
3. what the methods box covers
4. whether worker/manager attitudes toward AI are now explicit in the chapter
5. whether bibliography entries were merged/deduplicated
6. pass/fail for the strict build
7. any small manual-review items