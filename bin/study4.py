from lib import utils_fun
import numpy as np  

def get_seed_words():
    import pandas as pd
    seedWords_path = '/Users/xuanlong/Documents/program/python/src/xuanlong/alg/css_word_embedding/stereotype/data/dictionary/osfstorage-archive/Dictionaries/Full Dictionaries.csv'

    df = pd.read_csv(seedWords_path,delimiter=',')
    print(df.shape)
    # reglion
    df['Belief'] = df.apply(lambda x: 0 if x['Religion dictionary'] + x['beliefs_other dictionary'] + x['Politics dictionary'] == 0 else 1,axis = 1)
    df['Geograpgy'] = df.apply(lambda x: 0 if x['inhabitant dictionary'] + x['country dictionary'] == 0 else 1,axis = 1)
    df['Appearance'] = df.apply(lambda x: 0 if x['clothing dictionary'] + x['body_property dictionary'] + x['body_part dictionary'] + x['skin dictionary'] + x['body_covering dictionary'] + x['beauty dictionary'] == 0 else 1,axis = 1) 
    df.to_csv('/Users/xuanlong/Documents/program/python/src/xuanlong/alg/Integrating_SCM_SD/bin/doc/external_study4/all.csv')

def get_similarity(ant_pairs_warmth,ant_pairs_competent,ant_pairs_appearance,ant_pairs_belief,ant_pairs_geography,ant_pairs_status):
    dir_warmth = utils_fun.build_dimensions(ant_pairs_warmth)
    dir_competent = utils_fun.build_dimensions(ant_pairs_competent)
    dir_appearance = utils_fun.build_dimensions(ant_pairs_appearance)
    dir_belief = utils_fun.build_dimensions(ant_pairs_belief)
    dir_geography = utils_fun.build_dimensions(ant_pairs_geography)
    dir_status = utils_fun.build_dimensions(ant_pairs_status)
    vectors = (np.stack([dir_warmth,dir_competent,dir_appearance,dir_belief,dir_geography,dir_status]))
    
    utils_fun.print_similarities(vectors)
    
    from comparison_dimensions import heat_map
    heat_map(vectors,'Google News word embeeding')


if __name__ == "__main__":
    warmth_pairs_path = 'Integrating_SCM_SD/bin/output/contrusting_pairs_mce/scm_warm_mce.csv'
    competent_pairs_path = 'Integrating_SCM_SD/bin/output/contrusting_pairs_mce/scm_competent_mce.csv'
    appearance_pairs_path = 'Integrating_SCM_SD/bin/output/contrusting_pairs_mce/appearance_mce.csv'
    belief_pairs_pair = 'Integrating_SCM_SD/bin/output/contrusting_pairs_mce/belief_mce.csv'
    geography_pairs_pair = 'Integrating_SCM_SD/bin/output/contrusting_pairs_mce/geograpgy_mce.csv'
    status_pairs_pair = 'Integrating_SCM_SD/bin/output/contrusting_pairs_mce/status_mce.csv'
    
    ant_pairs_warmth = utils_fun.get_antonym_pairs(warmth_pairs_path)
    ant_pairs_competent = utils_fun.get_antonym_pairs(competent_pairs_path)
    ant_pairs_appearance = utils_fun.get_antonym_pairs(appearance_pairs_path)
    ant_pairs_belief = utils_fun.get_antonym_pairs(belief_pairs_pair)
    ant_pairs_geography = utils_fun.get_antonym_pairs(geography_pairs_pair)
    ant_pairs_status = utils_fun.get_antonym_pairs(status_pairs_pair)
    
    get_similarity(ant_pairs_warmth,ant_pairs_competent,ant_pairs_appearance,ant_pairs_belief,ant_pairs_geography,ant_pairs_status)

