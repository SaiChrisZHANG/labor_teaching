# Source notes

The reproduce exercise is a deterministic synthetic teaching path inspired by spatial-equilibrium work on housing constraints and spatial misallocation.

The primary paper anchor is Hsieh and Moretti. Their published paper studies a real equilibrium counterfactual in which housing constraints in high-productivity cities affect population allocation and aggregate output. This lab does not use their data, does not use an official replication package, and does not reproduce published estimates.

The teaching data contain:

- city-level productivity;
- housing capacity;
- housing-supply elasticity;
- amenity values;
- baseline equilibrium wages, rents, population, and output;
- a housing-constraint index used for the counterfactual relaxation.

The reproduce script estimates no frontier model. It solves a compact spatial fixed point, reports equilibrium incidence, and asks students to diagnose which objects are observed, which are calibrated, and which are closure assumptions.
