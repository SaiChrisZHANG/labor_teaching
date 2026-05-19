# Transfer Data Notes

The default transfer dataset is synthetic. It models workers who may enter a workplace training program. The observed pre-treatment variables are:

- prior wage;
- tenure;
- baseline performance;
- supervisor referral;
- schedule flexibility;
- distance to the training site;
- high-skill job indicator.

The treatment variable is `training`. The outcome is `next_wage`. The main omitted-variable threat is latent motivation or manager private information. A real-data transfer version should add richer pre-treatment performance histories, manager assignment rules, eligibility criteria, and worker application records.
