factor good_bad large_small beautiful_ugly yellow_blue hard_soft sweet_sour strong_weak clean_dirty high_low calm_agitated tasty_distasteful valuable_worthless red_green young_old kind_cruel loud_soft deep_shallow pleasant_unpleasant black_white bitter_sweet happy_sad sharp_dull empty_full ferocious_peaceful heavy_light wet_dry sacred_profane relaxed_tense brave_cowardly long_short rich_poor clear_hazy hot_cold thick_thin nice_awful bright_dark bass_treble angular_rounded fragrant_foul honest_dishonest active_passive rough_smooth fresh_stale fast_slow fair_unfair rugged_delicate near_far pungent_bland healthy_sick wide_narrow,pf

********************************* SEM model **********************************
**** Confirmatory factor analyis ****
** Evaluation
sem ( pleasant_unpleasant good_bad nice_awful beautiful_ugly tasty_distasteful healthy_sick sweet_sour fair_unfair clean_dirty strong_weak happy_sad honest_dishonest fresh_stale relaxed_tense kind_cruel valuable_worthless brave_cowardly bright_dark calm_agitated rich_poor fragrant_foul active_passive fast_slow <- Evaluation) //factor1
** Evaluation - Reduction
sem ( pleasant_unpleasant good_bad nice_awful beautiful_ugly tasty_distasteful healthy_sick sweet_sour fair_unfair clean_dirty strong_weak happy_sad honest_dishonest fresh_stale relaxed_tense kind_cruel  <- Evaluation)
** Evaluation - Osgood
sem (good_bad beautiful_ugly sweet_sour clean_dirty tasty_distasteful valuable_worthless kind_cruel pleasant_unpleasant bitter_sweet happy_sad sacred_profane nice_awful fragrant_foul honest_dishonest fair_unfair <- Evaluation)



** Potency
sem (bitter_sweet ferocious_peaceful strong_weak deep_shallow hard_soft pungent_bland high_low sharp_dull active_passive valuable_worthless loud_soft thick_thin <- Factor2 ) // >0.3

** Potency - Reduction
sem (strong_weak deep_shallow hard_soft pungent_bland high_low sharp_dull active_passive valuable_worthless loud_soft thick_thin <- Factor2 )

** Potency - Osgood
sem (large_small strong_weak heavy_light thick_thin <- Factor2)
** Potency - Osgood (add evaluation related)
sem (large_small strong_weak heavy_light thick_thin hard_soft loud_soft deep_shallow brave_cowardly bass_treble rough_smooth rugged_delicate wide_narrow <- Factor2)
sem, standardized
estat gof,stats(all)
estat eqgof
estat mindices

** Factor3
sem (sweet_sour fast_slow wet_dry beautiful_ugly loud_soft angular_rounded bass_treble high_low rich_poor ferocious_peaceful <- Factor3) // > 0.2
** Factor3 - Reduction
sem (sweet_sour fast_slow  beautiful_ugly rich_poor <- Factor3)

** Factor3 - Osgood
sem(fast_slow active_passive hot_cold sharp_dull angular_rounded <- Factor3) 


** Factor4 // > 0,2
sem ( sharp_dull wet_dry ferocious_peaceful bright_dark relaxed_tense rough_smooth happy_sad rugged_delicate  <- Factor4)
sem ( sharp_dull  ferocious_peaceful bright_dark relaxed_tense rough_smooth happy_sad   <- Factor4)
sem, standardized
estat gof,stats(all)
estat eqgof
estat mindices
** Factor4 - Reduction
sem ( sharp_dull   bright_dark relaxed_tense rough_smooth happy_sad   <- Factor4)


** Factor5 - convergence not achieved
sem (loud_soft hard_soft honest_dishonest rugged_delicate pleasant_unpleasant kind_cruel <- Factor5) // >0.2


sem, standardized
estat gof,stats(all)
estat eqgof
estat mindices

