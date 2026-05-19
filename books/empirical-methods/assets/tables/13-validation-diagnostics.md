## Validation Diagnostics

| Diagnostic | Question it answers | When it matters most | Main caveat |
|---|---|---|---|
| Precision | Of predicted positives, how many are truly positive? | costly false positives | can hide poor recall |
| Recall | Of true positives, how many are recovered? | costly false negatives | can hide noisy positives |
| F1 | How balanced are precision and recall? | balanced classification settings | may not reflect policy loss |
| Calibration | Do predicted probabilities correspond to realized frequencies? | thresholding, targeting, value estimation | can look good overall but fail by subgroup |
| Subgroup performance | Does the measure work similarly across groups? | fairness, heterogeneity, portability | requires adequate subgroup sample size |
| Drift checks | Does performance survive across time/domain? | transportability, repeated use | benchmark may itself become outdated |
| Human review | Does manual inspection confirm interpretation? | embeddings, similarity, multimodal measures | expensive and subjective if not protocolized |
