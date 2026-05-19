# Source Notes

The reproduction path is a pedagogical design exercise inspired by Angrist and Krueger's quarter-of-birth / compulsory-schooling design and Oreopoulos's work on compulsory schooling.

The data are synthetic because the course lab is meant to run without external downloads. The simulation intentionally includes:

- a rule-based instrument, `compulsory_exposure`;
- an endogenous treatment, `stayed_in_school`;
- unobserved ability that affects both schooling and earnings;
- a known synthetic compliance type for teaching diagnostics;
- controls that mimic birth cohort, state, and family background information.

The purpose is to reproduce the design logic: first stage, reduced form, Wald ratio, 2SLS, weak-IV diagnostics, balance checks, and complier interpretation.
