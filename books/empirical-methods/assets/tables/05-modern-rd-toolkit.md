:::{admonition} Modern RD diagnostics
:class: note

Use this as a practical checklist before claiming an RD design is persuasive.

1. **Threshold discipline**
   - Is the cutoff substantively central to assignment or incentives?
   - Can units manipulate the running variable?
   - Is there evidence of sorting / heaping / strategic timing near the cutoff?

2. **Local comparison quality**
   - Why should potential outcomes be smooth at the cutoff?
   - Are observable covariates continuous at the threshold?
   - Does the institutional setting make local continuity believable?

3. **Estimator choice**
   - Prefer local linear / local quadratic over high-order global polynomials.
   - Default to triangular weights unless there is a clear reason otherwise.
   - Treat bandwidth as part of the design, not a hidden implementation choice.

4. **Inference choice**
   - Use robust bias-corrected inference (`rdrobust`) as a baseline modern implementation.
   - Consider honest intervals (`rdhonest`) when smoothness assumptions and worst-case bias are first-order concerns.
   - Report sensitivity to bandwidth and polynomial order.

5. **Interpretation**
   - Is the effect local but substantively important?
   - Is the paper over-claiming a global policy effect from a local design?
   - Does the threshold identify a level shift, a first-stage jump, a slope change, or a bunching response?

6. **Design-specific threats**
   - **Time RD:** seasonality, serial correlation, anticipation, concurrent shocks.
   - **Spatial RD:** geographic sorting, multidimensional boundaries, confounding border changes.
   - **Bunching:** salience, optimization frictions, counterfactual density specification.
:::
