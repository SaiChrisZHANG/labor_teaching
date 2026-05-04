# Portfolio Charter

## Purpose

This document governs the public teaching platform in labor economics and applied methods. It defines the portfolio mission, course set, teaching model, production rules, completion standards, and build order for repository work.

## Portfolio Mission

The portfolio exists to build a durable public teaching platform that demonstrates:
- labor-economics depth
- empirical and methodological breadth
- pedagogical clarity across audience levels
- technically modern and reproducible teaching practice
- a coherent public-facing academic identity

The platform should produce reusable teaching assets rather than isolated course notes. Books, slides, code labs, and shared methods materials should reinforce one another and follow a common structure.

## Public-Facing Courses

The primary public-facing courses are:
1. Labor I: Workers, Human Capital, and Inequality
2. Labor II: Firms, Frictions, and Institutions
3. Empirical Methods for Applied Economics
4. Behavioral Labor

These courses are the main book-level products of the repository and should eventually support public landing pages, syllabi, module maps, notes, slides, exercises, and selected code labs.

## Incubator Courses

The incubator course is:
1. Labor Markets and Political/Cultural Institutions

Incubator courses do not need full-book buildout in the first release. Their role is to:
- preserve space for distinctive future teaching directions
- host polished syllabi and a small number of showcase modules
- test framing, scope, and audience fit before expansion into a full course

Incubator work should stay selective and should not displace completion of the core public-facing courses.

## Teaching-Layer Model

Every teaching module must serve three layers:
- Bridge: advanced undergraduate and master's students who need intuition, framing, and core empirical patterns
- Field Core: PhD students who need the canonical models, identification logic, evidence base, and debates
- Research Lab: students and researchers who need frontier questions, open problems, and extension paths

This three-layer model is mandatory across the portfolio. Modules should be structured so the economic question is stated early and the movement from intuition to formal analysis is explicit.

## Code Policy

Python is the backbone language for public code labs, reproducible examples, and shared utilities.

R is allowed when a package ecosystem or literature makes it pedagogically superior for a specific task. Stata is allowed for selected applied-economics workflows and replication-oriented snippets. R and Stata should be used as selective companions, not as default parallel implementations.

Repository code policy should therefore follow these rules:
- prefer one primary Python workflow
- add R or Stata only when they create clear teaching value
- avoid maintaining the same lab in Python, R, and Stata by default
- keep reusable code in shared locations when it supports more than one course

## Slide Policy

Slides are a parallel teaching product, not a duplication of the written notes.

Each slide deck should:
- define the economic question
- present the conceptual map
- include only the essential equations, figures, or identification diagrams
- isolate the main logic of theory or empirical design
- end with takeaways and open questions

Slide decks should remain concise and presentation-oriented. Full exposition belongs in the book modules, not in the slides.

## Definition of Done

### Module done

A module is done only when it includes:
- a title and clear learning objectives
- the full Bridge / Field Core / Research Lab structure
- a Methods Box
- a reading ladder
- at least one exercise or discussion block
- an explicit reproducibility, code lab, or replication note
- a slide companion note or completed slide deck

A module is not done if it lacks the required structure, mixes audience layers unclearly, invents citations, or leaves notation inconsistent with shared standards.

### Course done

A course is done only when it has:
- a clear course outline
- a coherent set of module pages following the portfolio template
- a syllabus
- matching slide coverage for the completed modules
- exercises or discussion prompts across modules
- selected code labs where appropriate
- internal consistency in notation, headings, links, and references

A course does not need every possible interactive or computational extension before release. The standard is a coherent, reusable, public-facing teaching product.

## Build Priority Order

The build priority order for the platform is:
1. repository scaffold and shared conventions
2. shared toolkit shells, beginning with labor market facts and datasets, identification primer, and reproducibility workflow
3. Labor I
4. Empirical Methods for Applied Economics
5. Labor II
6. Behavioral Labor
7. Institutions incubator

Within the first sprint, priority should remain on establishing conventions and shipping one complete showcase sequence: one full module, one matching slide deck, and one executable Python lab.
