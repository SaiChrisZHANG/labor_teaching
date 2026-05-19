# Spatial Identification Problems Map

| Identification issue | Why it matters | Typical design response | Anchor paper | Main caveat |
|---|---|---|---|---|
| Spatially correlated shocks | Nearby units share unobservables, so conventional SEs can understate uncertainty | Conley-style or other spatially robust inference | [@conley1999] | Fixes inference, not bias |
| Spillovers / interference | One unit’s treatment affects nearby units’ outcomes | Exposure mappings, partial-interference designs, explicit spillover estimands | [@miguelKremer2004] | SUTVA no longer literal |
| Endogenous boundaries | Policy or institutional borders may coincide with latent sorting or geography | Boundary continuity checks, signed-distance designs, narrow samples | [@black1999; @dell2010] | Border may carry more than treatment |
| Correlated local shocks in border comparisons | Neighboring places can still differ in trends or local shocks | Contiguous-pair designs with local controls and spatial inference | [@dubeLesterReich2010] | Border does not guarantee comparability |
| Shift-share exposure endogeneity | Shares may embed endogenous historical structure | Shock-share decomposition, modern diagnostics, leave-one-out logic | [@goldsmithPinkhamSorkinSwift2020; @borusyakHullJaravel2025] | Shares are not automatically predetermined |
| Neighborhood sorting | Place effects can be confounded by who selects into place | Movers, lotteries, mobility experiments | [@chettyHendrenKatz2016] | Strong data and timing demands |
| MAUP / geography choice | Changing units changes the estimand and mechanism | Mechanism-first geography choice, robustness across spatial units | [@bussoGregoryKline2013] | Robustness may still be hard to interpret |
