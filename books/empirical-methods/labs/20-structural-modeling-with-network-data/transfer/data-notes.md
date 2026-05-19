# Transfer Data Notes

## Transfer Anchor

The transfer exercise is inspired by labor-market referral models and evidence, especially Galenianos [@galenianos2021referral] and Dustmann, Glitz, Schonberg, and Bruderl [@dustmann2016referral].

## Synthetic Referral Opportunity Set

The generated data contain referral opportunities between synthetic referrers and applicants. Each row includes:

- referrer and applicant identifiers;
- referrer and applicant groups;
- whether the pair is same-group or cross-group;
- whether a network link already exists;
- tie strength;
- signal quality;
- referrer access;
- applicant skill;
- observed referral status;
- synthetic callback outcome for observed referrals.

## Policy Scenarios

The transfer script compares three scenarios:

1. baseline observed referrals;
2. better information quality on existing referrals;
3. an endogenous cross-group referral policy that turns selected cross-group opportunities into observed referrals.

## Interpretation Limits

The generated policy effects are not empirical estimates. They are meant to show how the counterfactual changes when policy affects link formation rather than only outcomes conditional on existing links.
