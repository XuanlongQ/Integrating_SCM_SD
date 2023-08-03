factor good_bad large_small beautiful_ugly yellow_blue hard_soft sweet_sour strong_weak clean_dirty high_low calm_agitated tasty_distasteful valuable_worthless red_green young_old kind_cruel loud_soft deep_shallow pleasant_unpleasant black_white bitter_sweet happy_sad sharp_dull empty_full ferocious_peaceful heavy_light wet_dry sacred_profane relaxed_tense brave_cowardly long_short rich_poor clear_hazy hot_cold thick_thin nice_awful bright_dark bass_treble angular_rounded fragrant_foul honest_dishonest active_passive rough_smooth fresh_stale fast_slow fair_unfair rugged_delicate near_far pungent_bland healthy_sick wide_narrow,pf

********************************* SEM model **********************************
//alpha good_bad beautiful_ugly sweet_sour strong_weak clean_dirty tasty_distasteful pleasant_unpleasant happy_sad nice_awful honest_dishonest fresh_stale fair_unfair healthy_sick,std gen(Evaluation) //0.4
//alpha hard_soft strong_weak deep_shallow high_low valuable_worthless loud_soft bitter_sweet sharp_dull ferocious_peaceful thick_thin active_passive pungent_bland,std gen(Potency) // 0.3
//alpha sweet_sour beautiful_ugly high_low loud_soft ferocious_peaceful wet_dry rich_poor bass_treble angular_rounded fast_slow,std gen(Activity) //0.2
//alpha happy_sad sharp_dull ferocious_peaceful wet_dry relaxed_tense bright_dark rough_smooth rugged_delicate,std gen(Factor4) 
// alpha hard_soft kind_cruel loud_soft pleasant_unpleasant honest_dishonest rugged_delicate,std gen(Factor5)

sem (good_bad beautiful_ugly sweet_sour strong_weak clean_dirty tasty_distasteful pleasant_unpleasant happy_sad nice_awful honest_dishonest fresh_stale fair_unfair healthy_sick <- Evaluation) ///
(hard_soft strong_weak deep_shallow high_low valuable_worthless loud_soft bitter_sweet sharp_dull ferocious_peaceful thick_thin active_passive pungent_bland <- Potency) ///
(sweet_sour beautiful_ugly high_low loud_soft ferocious_peaceful wet_dry rich_poor bass_treble angular_rounded fast_slow <- Activity) ///
(happy_sad sharp_dull ferocious_peaceful wet_dry relaxed_tense bright_dark rough_smooth rugged_delicate <-Factor4) ///
// (hard_soft kind_cruel loud_soft pleasant_unpleasant honest_dishonest rugged_delicate <-Factor5 )

sem (good_bad large_small beautiful_ugly yellow_blue hard_soft sweet_sour strong_weak clean_dirty high_low calm_agitated tasty_distasteful valuable_worthless red_green young_old kind_cruel loud_soft deep_shallow pleasant_unpleasant black_white bitter_sweet happy_sad sharp_dull empty_full ferocious_peaceful heavy_light wet_dry sacred_profane relaxed_tense brave_cowardly long_short rich_poor clear_hazy hot_cold thick_thin nice_awful bright_dark bass_treble angular_rounded fragrant_foul honest_dishonest active_passive rough_smooth fresh_stale fast_slow fair_unfair rugged_delicate near_far pungent_bland healthy_sick wide_narrow <- Evaluation)





**** SEM ****
sem (good_bad large_small beautiful_ugly yellow_blue hard_soft sweet_sour strong_weak clean_dirty high_low calm_agitated tasty_distasteful valuable_worthless red_green young_old kind_cruel loud_soft deep_shallow pleasant_unpleasant black_white bitter_sweet happy_sad sharp_dull empty_full ferocious_peaceful heavy_light wet_dry sacred_profane relaxed_tense brave_cowardly long_short rich_poor clear_hazy hot_cold thick_thin nice_awful bright_dark bass_treble angular_rounded fragrant_foul honest_dishonest active_passive rough_smooth fresh_stale fast_slow fair_unfair rugged_delicate near_far pungent_bland healthy_sick wide_narrow <- Evaluation)

**** Confirmatory factor analyis ****
sem (good_bad large_small beautiful_ugly yellow_blue hard_soft sweet_sour strong_weak clean_dirty high_low calm_agitated tasty_distasteful valuable_worthless red_green young_old kind_cruel loud_soft deep_shallow pleasant_unpleasant black_white bitter_sweet happy_sad sharp_dull empty_full ferocious_peaceful heavy_light wet_dry sacred_profane relaxed_tense brave_cowardly long_short rich_poor clear_hazy hot_cold thick_thin nice_awful bright_dark bass_treble angular_rounded fragrant_foul honest_dishonest active_passive rough_smooth fresh_stale fast_slow fair_unfair rugged_delicate near_far pungent_bland healthy_sick wide_narrow <- Evaluation)

sem (pleasant_unpleasant good_bad nice_awful beautiful_ugly tasty_distasteful healthy_sick sweet_sour fair_unfair clean_dirty strong_weak happy_sad honest_dishonest fresh_stale <- Evaluation) //factor1

sem (strong_weak deep_shallow hard_soft bitter_sweet pungent_bland high_low sharp_dull active_passive valuable_worthless loud_soft ferocious_peaceful thick_thin <- Factor2 ) // >0.3


sem (sweet_sour fast_slow wet_dry beautiful_ugly loud_soft angular_rounded bass_treble high_low rich_poor ferocious_peaceful nice_awful <- Factor3) // > 0.18

sem ( bright_dark  happy_sad  young_old  fresh_stale  <- Factor4)

sem (loud_soft hard_soft bitter_sweet long_short   <- Factor5)

sem, standardized
estat gof,stats(all)
estat eqgof
estat mindices

