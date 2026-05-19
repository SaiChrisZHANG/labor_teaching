# Source Notes

The source sample is a deterministic synthetic teaching corpus. It is designed to mimic the structure of an LLM-assisted labor-market measurement project without using proprietary data or a live model API.

## Unit Of Observation

Each row is a document bundle indexed by `doc_id`. The bundle combines a job or screening note with information about worker readiness.

## Key Fields

- `source_text`: synthetic raw text given to the prompt workflow.
- `benchmark_mismatch`: benchmark label for whether the record contains a skill, credential, or schedule mismatch.
- `benchmark_type`: benchmark category: `skill_gap`, `credential_gap`, `schedule_gap`, or `none`.
- `sector`, `region`, `occupation_group`, `document_type`: subgroup fields for validation.
- `applicant_interest`: synthetic downstream outcome used to show how generated-variable error changes an applied association.

## Interpretation

The lab is inspired by LLM-assisted labor-market measurement workflows. It is not an official replication and should not be cited as evidence about real labor-market mismatch.
