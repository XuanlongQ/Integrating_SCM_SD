import numpy as np
import sys
from lib import utils_fun,middleware,remain

Yamlcon = utils_fun.YamlConfig()
data_yaml = Yamlcon.get_yaml()
    

if __name__ == "__main__":
    # Get the path
    warmth_pairs_path = data_yaml["SCM"]["warmth_pairs"]
    competent_pairs_path = data_yaml["SCM"]["competent_pairs"]
    evaluation_pairs_path = data_yaml["SD"]["evaluation"]
    potency_pairs_path = data_yaml["SD"]["potency"]
    activity_pairs_path = data_yaml["SD"]["activity"]
    
    trustworthy_pairs_path = data_yaml["Trust"]["20_paris"]
    
    # SCM dimensions
    ant_pairs_warmth = utils_fun.get_antonym_pairs(warmth_pairs_path)
    ant_pairs_competent = utils_fun.get_antonym_pairs(competent_pairs_path)
    # SD dimensions
    ant_pairs_evaluation = utils_fun.get_antonym_pairs(evaluation_pairs_path)
    ant_pairs_potency = utils_fun.get_antonym_pairs(potency_pairs_path)
    ant_pairs_activity = utils_fun.get_antonym_pairs(activity_pairs_path)
    ant_pairs_trustworthy = utils_fun.get_antonym_pairs(trustworthy_pairs_path)
    
    # filter pairs, condition cossim < 0.5
    # warm_pair = middleware.filter_pairs(ant_pairs_warmth)
    # competent_pair = middleware.filter_pairs(ant_pairs_competent)
    # evaluation_pair = middleware.filter_pairs(ant_pairs_evaluation)
    # potency_pair = middleware.filter_pairs(ant_pairs_potency)

    
    ## build SCM dimensions , warmth and competent
    dir_warmth = utils_fun.build_dimensions(ant_pairs_warmth)
    dir_competent = utils_fun.build_dimensions(ant_pairs_competent)

    # build SD dimensions, evaluation and potency
    dir_evaluation = utils_fun.build_dimensions(ant_pairs_evaluation)
    dir_potency = utils_fun.build_dimensions(ant_pairs_potency)
    dir_activity = utils_fun.build_dimensions(ant_pairs_activity)
    dir_trustworthy = utils_fun.build_dimensions(ant_pairs_trustworthy)
    
    vectors = (np.stack([dir_warmth,dir_competent,dir_evaluation,dir_potency,dir_activity,dir_trustworthy]))
    from comparison_dimensions import heat_map
    heat_map(vectors)
    
    # calcute cossim
    cos_sim_w_c = remain.cosine_similarity(dir_warmth,dir_competent)
    cos_sim_e_p = remain.cosine_similarity(dir_evaluation,dir_potency)
    
    cos_sim_e_c = remain.cosine_similarity(dir_evaluation,dir_competent)
    cos_sim_e_w = remain.cosine_similarity(dir_evaluation,dir_warmth)
    cos_sim_e_a = remain.cosine_similarity(dir_evaluation,dir_activity)

    cos_sim_p_c = remain.cosine_similarity(dir_potency,dir_competent)
    cos_sim_p_w = remain.cosine_similarity(dir_potency,dir_warmth)
    cos_sim_p_a = remain.cosine_similarity(dir_potency,dir_activity)
    
    cos_sim_a_w = remain.cosine_similarity(dir_activity,dir_warmth)
    cos_sim_a_c = remain.cosine_similarity(dir_activity,dir_competent)
 
    
    print("The cosine similarity between different dimensions.")
    print("warmth and competent: ", cos_sim_w_c, utils_fun.get_angel(cos_sim_w_c))
    print("evaluation and potency: ", cos_sim_e_p, utils_fun.get_angel(cos_sim_e_p))
    print("**** Comparison ****")
    print("evaluation and competent: ", cos_sim_e_c, utils_fun.get_angel(cos_sim_e_c))
    print("evaluation and warmth: ", cos_sim_e_w, utils_fun.get_angel(cos_sim_e_w))
    print("evaluation and activity: ", cos_sim_e_a, utils_fun.get_angel(cos_sim_e_a))
    
    print("potency and competent: ", cos_sim_p_c, utils_fun.get_angel(cos_sim_p_c))
    print("potency and warmth: ", cos_sim_p_w, utils_fun.get_angel(cos_sim_p_w))
    print("potency and activity: ", cos_sim_p_a, utils_fun.get_angel(cos_sim_p_a))
      
    print("activity and warmth: ", cos_sim_a_w, utils_fun.get_angel(cos_sim_a_w))
    print("activity and competent: ", cos_sim_a_c, utils_fun.get_angel(cos_sim_a_c))
    

    
    