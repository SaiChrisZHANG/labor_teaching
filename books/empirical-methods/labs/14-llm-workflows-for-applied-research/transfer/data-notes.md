# Transfer Data Notes

The transfer sample is a deterministic synthetic teaching corpus of workforce-agency case notes.

## Unit Of Observation

Each row is a case note indexed by `case_id`.

## Key Fields

- `case_text`: synthetic transfer-domain text.
- `benchmark_mismatch`: benchmark label for whether the case contains a skill, credential, or schedule barrier.
- `benchmark_type`: benchmark category: `skill_gap`, `credential_gap`, `schedule_gap`, or `none`.
- `program_area`, `region`: subgroup fields for transfer validation.
- `placement_score`: synthetic downstream outcome.

## Why This Transfer Is Hard

The transfer sample uses terms such as `bridge credential`, `reciprocity unresolved`, `rapid upskilling`, and `wraparound schedule`. These are meaningful for workforce agencies but only partly covered by the source prompt vocabulary. Students should decide whether prompt adaptation improves the same measure or creates a new target construct.
