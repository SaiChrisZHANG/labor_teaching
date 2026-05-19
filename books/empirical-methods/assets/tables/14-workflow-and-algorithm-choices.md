## Workflow and Algorithm Choices

| Task | Typical workflow | Useful methods/resources | Key implementation choice | Main caveat |
|---|---|---|---|---|
| Structured data extraction from documents | prompt templates + schema + post-processing | instruction prompting, JSON/schema outputs, retrieval augmentation | schema design and benchmark set | output can look structured but still be wrong |
| Classification / coding | labeled examples + prompt or fine-tuned classifier | zero/few-shot prompting, supervised fine-tuning, embeddings + classifier | benchmark labels and subgroup evaluation | classifier may inherit benchmark bias |
| Literature / document summarization | chunking + retrieval + constrained summarization | RAG, chunking, citation-aware workflows | citation grounding and context windows | fabricated or weakly grounded summaries |
| Synthetic labels | benchmark creation + model coding + human audit | prompt-based coding, pairwise comparisons, active learning | human review share and disagreement rules | synthetic labels may drift over domains |
| Simulated subjects | scenario design + persona/prompt design + benchmark tasks | LLM-as-subject workflows, survey simulation tools | environment specification and benchmark regularities | responses can reflect prompt artifacts more than human behavior |
| Agent / economy simulation | structured state/action loop + logging | agent frameworks, tool use, iterative environment simulation | state transition logging and reproducibility | simulated equilibrium may not map to empirical behavior |
