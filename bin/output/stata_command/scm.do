factor sociable_unsociable friendliness_unfriendliness friendly_unfriendly warm_cold warmth_coldness likable_unlikable pleasant_unpleasant liked_disliked outgoing_shy sensitive_insensitive affectionate_unaffectionate caring_uncaring sympathetic_unsympathetic helpful_unhelpful supportive_unsupportive polite_impolite social_antisocial funny_boring popular_unpopular nice_nasty agreeable_disagreeable hospitable_inhospitable thoughtful_inconsiderate moral_immoral trustworthy_trustworthiness sincere_insincere honest_dishonest egoistic_altruistic selfless_selfish benevolent_threat softhearted_hardhearted loyal_disloyal fair_unfair tolerant_intolerant tolerance_intolerance good_bad kind_unkind right_wrong kindness_mean honorable_dishonorable incorrupt_corrupt innocent_criminal amicable_hostile genuine_fake truthful_untruthful cooperative_uncooperative responsible_irresponsible unprejudiced_prejudiced,pf

******* Warmth *******
sem ( supportive_unsupportive friendly_unfriendly caring_uncaring good_bad pleasant_unpleasant thoughtful_inconsiderate sincere_insincere honest_dishonest helpful_unhelpful fair_unfair tolerant_intolerant liked_disliked honorable_dishonorable sympathetic_unsympathetic sociable_unsociable loyal_disloyal truthful_untruthful nice_nasty likable_unlikable cooperative_uncooperative warmth_coldness polite_impolite hospitable_inhospitable selfless_selfish <- Factor1)

*** Reduction - no need
sem ( supportive_unsupportive friendly_unfriendly caring_uncaring good_bad pleasant_unpleasant thoughtful_inconsiderate sincere_insincere honest_dishonest helpful_unhelpful fair_unfair tolerant_intolerant liked_disliked honorable_dishonorable sympathetic_unsympathetic sociable_unsociable loyal_disloyal  <- Factor1)

sem, standardized
estat gof,stats(all)
estat eqgof
estat mindices

**********************************************
factor competent_incompetent competitive_uncompetitive intelligent_unintelligent intelligence_stupid able_unable educated_uneducated rational_irrational creative_uncreative capable_incapable practical_impractical imaginative_unimaginative shrewd_foolish undiscriminating_discriminating clever_maladroit folly_wisdom wise_unwise efficient_inefficient effective_ineffective logical_illogical ability_inability fearlessness_fear assertive_unassertive secure_insecure striver_lazy active_inactive determined_doubtful independent_dependent persistent_sporadic energetic_lethargic ambitious_unambitious dedicated_undedicated motivated_unmotivated dominant_submissive dominance_submission competence_incompetence skill_dumb skillfull_dumbness critical_naive brilliant_inept confidence_diffident striving_apathy aggressive_negligent cautious_impulsive unwavering_wavering daring_unadventurous conscientious_careless untroubled_troubled,pf

******* Competent *******
sem ( efficient_inefficient competent_incompetent effective_ineffective capable_incapable intelligent_unintelligent creative_uncreative imaginative_unimaginative competitive_uncompetitive brilliant_inept able_unable motivated_unmotivated energetic_lethargic educated_uneducated ability_inability competence_incompetence logical_illogical ambitious_unambitious practical_impractical rational_irrational active_inactive conscientious_careless striving_apathy dedicated_undedicated <- Factor1)

sem, standardized
estat gof,stats(all)
estat eqgof
estat mindices

