# Designs and Corrections Toolkit

| Design / tool | Best scenario | What it identifies | Key implementation details | Main caveat |
|---|---|---|---|---|
| Conley spatial HAC | Residual correlation decays with distance | More credible variance estimates under spatial dependence | Choose radius, decay/kernel, and coordinates transparently | Does not solve spillover or sorting bias |
| Exposure mapping | Spillovers can be summarized by neighbors’ treatment/exposure | Effects of own treatment and local exposure under a specified mapping | Justify weights `w_{ij}` and spillover radius/network | Mapping choice is part of the estimand |
| Border comparison / contiguous pairs | Nearby units differ by policy or institution | Local treatment effect across a border | Show border sample, local balance, and trend plausibility | Border may proxy for hidden geography |
| Spatial RD / boundary discontinuity | Signed distance to a meaningful boundary provides local variation | Local discontinuity at the boundary | Use signed distance, local polynomials, and boundary checks | Multi-dimensional boundaries complicate implementation |
| Shift-share / Bartik | Places differ in pre-period composition and face common shocks | Exposure-weighted local effect under share/shock assumptions | Inspect share endogeneity, effective shock variation, and leave-one-out variants | Can hide endogeneity in the shares |
| Place-based policy design | Area-targeted interventions reshape local outcomes | Policy incidence on treated places/workers/firms | Define exposure geography, untreated comparison, and spillovers | Treated and nearby untreated areas may interact |
| Movers / mobility designs | Selection into place is the main threat | Effect of exposure conditional on mover timing/assignment | Align timing, exposure duration, and destination choice | Strong data and dynamic-selection assumptions |
