## Extraction Workflow and Algorithm Choices

| Research goal | Best starting point | Why | Common caveat |
|---|---|---|---|
| Detect explicit rules or mentions | dictionaries / regex | transparent and auditable | brittle to wording changes |
| Recover a stable binary label | supervised classifier | aligns directly with labeled target | target definition dominates everything |
| Measure semantic similarity / exposure | embeddings | robust to synonyms and context | interpretation can drift |
| Build a continuous index | aggregated scores / embeddings / supervised prediction | creates scalable numeric measure | scale may not map cleanly to economics object |
| Use images to proxy environment | transfer learning + supervised fine-tuning | uses pretrained visual representations | learned visual features may not correspond to welfare object |
| Use audio to measure tone/emotion | acoustic features or speech embeddings | captures information beyond transcript | highly sensitive to context and speaker traits |
| Combine multiple modalities | multimodal representation | captures complementary signals | validation burden rises sharply |
