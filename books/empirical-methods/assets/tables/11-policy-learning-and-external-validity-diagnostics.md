**Causal ML, policy learning, and external validity diagnostics**

| Dimension | Key question | Strong case | Warning sign | Practical implication |
|---|---|---|---|---|
| Heterogeneity object | Is the goal CATE estimation or policy choice? | Policy object is explicit | Heterogeneity is estimated but no decision problem is defined | Do not confuse subgroup estimates with treatment rules |
| Policy class | What set of rules is allowed? | Feasible and interpretable class | Flexible rule unconstrained by implementation | Constrain by budget, fairness, and deployability |
| Overlap | Are treated and untreated units comparable where the rule assigns treatment? | Good support in targeted regions | Extreme targeting where overlap is weak | Trim or restrict the policy class |
| Value estimation | How is policy performance evaluated? | Honest out-of-sample or cross-fit evaluation | In-sample policy value | Report value and regret using held-out data |
| External validity | Will the rule travel? | Clear source-target comparison | Different institutions, prices, or take-up conditions | Treat portability as an empirical question |
| Fairness and constraints | Can the rule be implemented legally and ethically? | Feasibility is explicit | Model-optimized rule ignores protected groups or legality | Separate statistical from institutional optimality |
