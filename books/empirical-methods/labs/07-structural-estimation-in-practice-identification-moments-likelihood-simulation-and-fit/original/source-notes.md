# Source notes

The replacement exercise is a deterministic synthetic teaching path inspired by dynamic discrete-choice estimation. The data contain unit histories, mileage states, replacement decisions, next states, operating costs, and downtime. The econometrician observes state-specific replacement behavior and transitions but does not observe the latent replacement cost, maintenance-cost slope, shocks, or continuation values.

The reproduce script estimates:

- a likelihood-style dynamic replacement model;
- identity-weighted and diagonally weighted moment estimators;
- a simulated-moments analogue;
- targeted and untargeted fit diagnostics;
- a cluster bootstrap over units;
- a delta-method approximation for a replacement-cost counterfactual.

The exercise does not use official Rust data or reproduce published magnitudes. It reproduces the implementation logic at teaching scale.
