## Annotation and Benchmark Design

| Design choice | What to specify | Why it matters for economics |
|---|---|---|
| Unit of labeling | document, sentence, image, clip, frame, response | determines the estimand and the noise structure |
| Label definition | exact conceptual target vs proxy | weak targets create invalid economic measures |
| Labeler type | expert, RA, crowd, subject, mixed | label quality and interpretation may differ |
| Instructions / rubric | decision rules, examples, edge cases | makes disagreement interpretable |
| Adjudication | majority vote, expert override, tie-break | affects benchmark stability |
| Held-out benchmark | clean untouched validation sample | avoids tuning on the benchmark |
| External benchmark | outside dataset or institutional measure | tests transportability and construct validity |
| Subgroup benchmark | labels stratified by group/place/time | reveals differential failure modes |
