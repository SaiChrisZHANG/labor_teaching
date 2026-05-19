## Modern DID Estimator Choice Guide

| Setting | Best default choice | What it identifies | Main problem it fixes | Main caveat |
|---|---|---|---|---|
| Two groups, two periods | Standard DID / TWFE | ATT under parallel trends | None needed if design is simple | Parallel trends still has to be argued |
| Staggered timing, dynamic effects, heterogeneous treatment effects | Sun-Abraham | Cohort-relative event-time effects | Contamination from already-treated controls in TWFE event studies | Requires care in aggregation and interpretation |
| Staggered timing, transparent group-time effects | Callaway-Sant'Anna | Group-time ATT and flexible aggregations | Bad comparison sets in staggered adoption | Users must choose the aggregation that matches the research question |
| Need to diagnose a TWFE estimate | Goodman-Bacon decomposition | Weighted 2x2 decomposition of TWFE | Reveals hidden comparison structure | Diagnostic only, not the final estimator |
| Small number of treated aggregate units, strong pre-treatment path information | Synthetic control / synthetic DID | Treated-minus-weighted-donor path gap | Weak untreated-average comparisons | Requires good donor pool and convincing pre-treatment fit |
| Heterogeneous timing with concern about forbidden comparisons and weighting | de Chaisemartin-D'Haultf\oeuille family | Alternative corrected ATT logic | Negative/contaminated comparison weights | Choice among variants requires care |
