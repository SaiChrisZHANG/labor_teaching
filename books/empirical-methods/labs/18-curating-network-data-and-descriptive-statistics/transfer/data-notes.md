# Transfer Data Notes

The transfer data are a deterministic synthetic referral-program log inspired by referral research in labor economics [@beamanMagruderWhoGetsJob2012; @barwickReferralsInequalityLabor2024; @friebelWhatDoEmployee2020].

Each row is a directed edge from an employee referrer to an applicant:

- `referrer_worker_id`: employee who made the referral;
- `applicant_id`: applicant receiving the referral;
- `referrer_group` and `applicant_group`: synthetic group labels for access diagnostics;
- `firm_id`: firm receiving the referral;
- `referral_month`: timing of the edge;
- `tie_strength`: synthetic relationship strength;
- `hired`: whether the referral resulted in a hire in the teaching data.

The data are designed for curation and descriptive diagnostics only. They do not identify the causal effect of receiving a referral. A causal design would need exogenous referral variation, randomized incentives, or another strategy that separates referral access from worker selection and employer screening.
