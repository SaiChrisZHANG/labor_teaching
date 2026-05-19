:::{table} Bandwidth, weighting, covariates, and practical implementation
:label: tbl:rd-implementation
| Decision | Default logic | When it helps | Main caveat |
| --- | --- | --- | --- |
| Bandwidth choice | Start with data-driven bandwidths, then check nearby alternatives | Balances variance and local bias | Different bandwidths imply different effective estimands |
| Weighting / kernel | Triangular kernel is a strong default near boundaries | Concentrates weight near the cutoff | Kernel choice matters less than bandwidth, but still changes effective comparison |
| Polynomial order | Local linear or local quadratic | Captures local curvature without unstable extrapolation | High-order global polynomials can create misleading boundary behavior |
| Robust bias correction (`rdrobust`) | Modern default for local-polynomial inference | Corrects leading bias when using practical bandwidths | Still depends on smoothness and local-polynomial structure |
| Honest inference (`rdhonest`) | Useful when worst-case bias under a smoothness class is central | Makes smoothness assumptions explicit and conservative | Intervals can be wider and require discipline about the smoothness bound |
| Covariates | Precision enhancement only | Helpful when pre-treatment and balanced across the cutoff | They do not rescue a weak design or create identification |
| Manipulation checks | Density tests, heaping checks, institutional diagnostics | Helps evaluate sorting around the cutoff | Formal tests are informative but not sufficient without institutional reasoning |
| Clustering / dependence | Match inference to the design environment | Essential in time RD, grouped forcing variables, or spatial contexts | Under-clustering can sharply overstate precision |
:::
