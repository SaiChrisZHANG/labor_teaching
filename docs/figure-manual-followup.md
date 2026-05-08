# Figure Manual Follow-Up

This inventory lists figures that were explicitly excluded from the Phase 1 script-based restyling pass.

## Exclusion rules

- figures with no matching source script in the audited script folders were not redrawn
- the FRED-linked Labor I dashboard was not regenerated because that would refresh live data rather than perform a pure style-only update
- chapter markdown was not edited unless a figure-path issue created a build problem

## Labor I deferred figures

| Figure path | Likely issue type | Why excluded from Phase 1 |
| --- | --- | --- |
| `books/labor-i/assets/figures/01-labor-market-status-dashboard.png` | data-sensitive live-series styling refresh | Source script exists, but regenerating would pull live FRED data unless data are frozen locally first |
| `books/labor-i/assets/figures/01-labor-market-status-dashboard-teaching-data.png` | alternate dashboard styling and labeling consistency | No matching audited source script |
| `books/labor-i/assets/figures/10-employer-mobility-measurement-correction.png` | chart styling, annotation spacing | No matching audited source script |
| `books/labor-i/assets/figures/10-employer-mobility-transition-heatmap.png` | heatmap typography and spacing | No matching audited source script |
| `books/labor-i/assets/figures/10-migration-selection-schematic.png` | diagram spacing and arrow alignment | No matching audited source script |
| `books/labor-i/assets/figures/10-rank-rank-transmission-schematic.png` | panel balance and typography consistency | No matching audited source script |
| `books/labor-i/assets/figures/12-behavioral-labor-design-map.png` | diagram box hierarchy and spacing | No matching audited source script |
| `books/labor-i/assets/figures/12-benchmark-vs-behavioral-wedges.png` | diagram style consistency | No matching audited source script |
| `books/labor-i/assets/figures/12-dellavigna-taxonomy-to-labor.png` | dense conceptual map layout | No matching audited source script |
| `books/labor-i/assets/figures/12-market-responses-and-welfare.png` | quadrant spacing and line hierarchy | No matching audited source script |

## Labor II deferred figures

| Figure path | Likely issue type | Why excluded from Phase 1 |
| --- | --- | --- |
| `books/labor-ii/assets/figures/03-data-design-frontier-map.png` | diagram spacing and title scale | No matching audited source script |
| `books/labor-ii/assets/figures/03-incentives-assignment-promotion.png` | arrow alignment and box spacing | No matching audited source script |
| `books/labor-ii/assets/figures/03-managers-peers-teams.png` | line hierarchy and label spacing | No matching audited source script |
| `books/labor-ii/assets/figures/03-personnel-economics-in-course-map.png` | course-map style consistency | No matching audited source script |
| `books/labor-ii/assets/figures/03-research-opportunities-landscape.png` | bubble-map spacing and typography | No matching audited source script |
| `books/labor-ii/assets/figures/07-adjustment-margins-under-wage-floors.png` | conceptual diagram cleanup | No matching audited source script |
| `books/labor-ii/assets/figures/07-competitive-vs-monopsony-minimum-wage.png` | panel style consistency | No matching audited source script |
| `books/labor-ii/assets/figures/07-employment-debate-landscape.png` | label density and box alignment | No matching audited source script |
| `books/labor-ii/assets/figures/07-global-minimum-wage-evidence-map.png` | map layout and visual hierarchy | No matching audited source script |
| `books/labor-ii/assets/figures/07-wage-law-toolkit.png` | node spacing and line hierarchy | No matching audited source script |
| `books/labor-ii/assets/figures/08-certification-to-coverage-pipeline.png` | oversized title and clipped layout risk | No matching audited source script |
| `books/labor-ii/assets/figures/08-collective-bargaining-regimes.png` | text density and box balance | No matching audited source script |
| `books/labor-ii/assets/figures/08-membership-vs-coverage-distinction.png` | large whitespace and title dominance | No matching audited source script |
| `books/labor-ii/assets/figures/08-political-economy-bridge.png` | title clipping and label congestion | No matching audited source script |
| `books/labor-ii/assets/figures/08-union-wage-compression-and-spillovers.png` | multi-panel style consistency | No matching audited source script |
| `books/labor-ii/assets/figures/09-enforcement-capacity-to-effective-regulation.png` | diagram scale and arrow geometry | No matching audited source script |
| `books/labor-ii/assets/figures/09-incidence-compliance-and-adjustment.png` | dense conceptual diagram cleanup | No matching audited source script |
| `books/labor-ii/assets/figures/09-insurance-distortion-equilibrium.png` | node spacing and connection routing | No matching audited source script |
| `books/labor-ii/assets/figures/09-regulation-spillovers-inequality-welfare.png` | title scale and cluster balance | No matching audited source script |
| `books/labor-ii/assets/figures/09-regulation-taxonomy-framework.png` | many-node diagram alignment | No matching audited source script |
| `books/labor-ii/assets/figures/10-aggregate-flows-and-margins.png` | diagram layout and arrow hierarchy | No matching audited source script |
| `books/labor-ii/assets/figures/10-beveridge-curve-and-matching-efficiency.png` | chart style consistency and annotation cleanup | No matching audited source script |
| `books/labor-ii/assets/figures/10-job-to-job-wage-cyclicality.png` | multi-axis chart styling | No matching audited source script |
| `books/labor-ii/assets/figures/10-match-quality-and-reallocation.png` | conceptual diagram spacing | No matching audited source script |
| `books/labor-ii/assets/figures/10-separations-jobfinding-unemployment.png` | stacked-panel chart styling | No matching audited source script |
| `books/labor-ii/assets/figures/11-ai-data-and-labor-market-measurement.png` | box layout and text density | No matching audited source script |
| `books/labor-ii/assets/figures/11-historical-global-technology-evidence.png` | timeline spacing and label scale | No matching audited source script |
| `books/labor-ii/assets/figures/11-supply-demand-market-effects.png` | equilibrium diagram hierarchy | No matching audited source script |
| `books/labor-ii/assets/figures/11-task-based-technology-framework.png` | title scale, line weight, and diagram balance | No matching audited source script |
| `books/labor-ii/assets/figures/11-technology-adjustment-and-reallocation.png` | flow-chart spacing and box density | No matching audited source script |
| `books/labor-ii/assets/figures/12-trade-adjustment-worker-vs-place.png` | two-path diagram spacing | No matching audited source script |
| `books/labor-ii/assets/figures/12-trade-channels-framework.png` | many-channel diagram alignment | No matching audited source script |
| `books/labor-ii/assets/figures/12-trade-global-evidence-and-frontiers.png` | large conceptual map cleanup | No matching audited source script |
| `books/labor-ii/assets/figures/12-trade-structural-change-transitions.png` | box alignment and connector geometry | No matching audited source script |
| `books/labor-ii/assets/figures/12-trade-welfare-and-reallocation.png` | stacked welfare map spacing | No matching audited source script |
| `books/labor-ii/assets/figures/13-common-failure-modes.png` | title scale and box spacing | No matching audited source script |
| `books/labor-ii/assets/figures/13-frontier-and-dissertation-bridge.png` | horizontal layout balance | No matching audited source script |
| `books/labor-ii/assets/figures/13-labor-ii-architecture-map.png` | dense architecture diagram cleanup | No matching audited source script |
| `books/labor-ii/assets/figures/13-policy-vs-shock-comparison.png` | two-column conceptual panel spacing | No matching audited source script |
| `books/labor-ii/assets/figures/13-question-mechanism-unit-design.png` | pipeline layout and label density | No matching audited source script |

## Next-step recommendation

The safest Phase 2 path is to locate or reconstruct the true source files for these diagrams before restyling them. If source recovery is not possible, redraw should happen only in a dedicated manual pass with side-by-side visual review to make sure the restyle does not accidentally alter interpretation.
