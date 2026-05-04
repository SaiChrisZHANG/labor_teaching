# Code Policy

## Primary language

Python is the default language for all public labs, executable notes, and shared utilities.

## Secondary languages

Use R when:
- the teaching value of an R package is high
- the literature convention strongly leans R
- visualization or causal-inference tooling is materially easier in R

Use Stata when:
- a canonical empirical workflow is traditionally taught in Stata
- a replication snippet is valuable for labor/applied micro students
- package parity in Python/R is weak for the specific task

## Default rule

Do not build three fully parallel code paths by default.
Prefer:
- one complete Python implementation
- optional short R translation or note
- optional short Stata translation or do-file skeleton

## Public code expectations

All code examples should:
- run from a clearly stated environment
- use relative paths where possible
- state input and output files
- avoid hidden state
- include short comments for teaching value
- separate teaching notebooks from utility scripts

## Teaching expectations

Every code lab should say:
- what students are estimating or simulating
- why that method is being used
- what output they should reproduce
- one extension exercise

## Language balance by course

- Labor I / II: mostly Python, selective Stata/R sidecars
- Empirical Methods: Python backbone, explicit R/Stata bridges where pedagogically useful
- Behavioral Labor: Python-first, experiments and data tasks
- Institutions incubator: selective code, more figure/data construction and archival or text workflows
