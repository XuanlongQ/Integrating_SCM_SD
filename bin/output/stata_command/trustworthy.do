factor honest_dishonest authentic_unreliable credible_manipulative dependable_cunning ethical_sneaky sincere_fraudulent trustable_sneering steadfast_unscrupulous consistent_scheming loyal_corrupt genuine_duplicitous principled_treacherous upstanding_disloyal truthful_insincere unimpeachable_deceptive faithful_greedy veracious_opportunistic,pf


****** Confirmatory ******

sem (honest_dishonest authentic_unreliable credible_manipulative dependable_cunning ethical_sneaky sincere_fraudulent trustable_sneering steadfast_unscrupulous consistent_scheming loyal_corrupt genuine_duplicitous principled_treacherous upstanding_disloyal truthful_insincere unimpeachable_deceptive faithful_greedy veracious_opportunistic <- Factor1)

**** Reduction ****
sem ( steadfast_unscrupulous honest_dishonest credible_manipulative consistent_scheming faithful_greedy dependable_cunning genuine_duplicitous loyal_corrupt sincere_fraudulent unimpeachable_deceptive <- Factor1)
sem, standardized
estat gof,stats(all)
estat eqgof
estat mindices
