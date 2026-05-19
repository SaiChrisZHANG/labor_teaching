## LLM Workflow Diagnostics

| Use case | Economic object | What the LLM produces | What must be benchmarked | Main failure mode | When it is strongest |
|---|---|---|---|---|---|
| Research assistant | workflow support | summaries, code drafts, search paths, extraction templates | reproducibility of final workflow | silent prompt drift, undocumented revisions | when the final published object is still researcher-controlled |
| Coder / extractor | measurement variable | labels, fields, scores, structured entries | accuracy vs a human benchmark, subgroup stability | hallucinated structure, nonclassical measurement error | when documents are numerous and the target construct is clearly specified |
| Synthetic coder / annotator | scalable labeling | human-like labels or scores | agreement with gold labels, sensitivity to prompt/model | systematic coding bias, unstable labels | when human annotation is expensive but a benchmark set exists |
| Synthetic subject | simulated responses | choices, survey answers, experimental play | correspondence to human patterns under benchmark tasks | prompt dependence, unrealistic adaptation | for pilot testing or benchmarked exploratory work |
| Simulation engine | environment transitions / agent interactions | generated states, actions, narratives | reproduction of known regularities, scenario stability | overfitting to prompt narratives, ungrounded comparative statics | when used as disciplined exploratory infrastructure rather than final evidence |
