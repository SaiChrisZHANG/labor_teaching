## Selection, inference, and implementation diagnostics

| Design issue | Core question | Practical diagnostic | Main caveat |
| --- | --- | --- | --- |
| Parallel trends | Would treated and control units have evolved similarly absent treatment? | Plot pre-trends, justify comparison set, use institutional timing knowledge | Flat pre-trends are suggestive, not proof |
| Dynamic effects | Are effects delayed, temporary, or persistent? | Event-study plot with clear reference period | TWFE event studies can be contaminated in staggered settings |
| Timing heterogeneity | Do cohorts receive treatment at different dates? | Tabulate treatment timing and cohort sizes | Already-treated units can be bad controls |
| Inference | Are shocks serially correlated within clusters? | Cluster at treatment level; assess number of clusters | Few clusters can invalidate asymptotics |
| Spillovers | Can untreated units be indirectly affected? | Map geographic / market / firm exposure | Violated SUTVA changes interpretation |
| Synthetic control suitability | Is the treated case too singular for panel DID? | Check donor pool and pre-period fit | Poor pre-fit undermines credibility |
