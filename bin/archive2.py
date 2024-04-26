import numpy as np
from lib import utils_fun

Yamlcon = utils_fun.YamlConfig()
data_yaml = Yamlcon.get_yaml()
    

def run_mec_fun(ant_pairs_warmth,ant_pairs_competent,ant_pairs_evaluation,ant_pairs_potency,ant_pairs_activity,ant_pairs_trustworthy,METHOD):
    dir_warmth = utils_fun.build_dimensions_mce(ant_pairs_warmth)
    dir_competent = utils_fun.build_dimensions_mce(ant_pairs_competent)
    dir_evaluation = utils_fun.build_dimensions_mce(ant_pairs_evaluation)
    dir_potency = utils_fun.build_dimensions_mce(ant_pairs_potency)
    dir_activity = utils_fun.build_dimensions_mce(ant_pairs_activity)
    dir_trustworthy = utils_fun.build_dimensions_mce(ant_pairs_trustworthy)
    vectors = (np.stack([dir_warmth,dir_competent,dir_evaluation,dir_potency,dir_activity,dir_trustworthy]))
    from Integrating_SCM_SD.bin.archive1 import heat_map
    heat_map(vectors,METHOD)
    utils_fun.print_similarities(vectors)
    print ("MCE well done!")

def run_google_fun(ant_pairs_warmth,ant_pairs_competent,ant_pairs_evaluation,ant_pairs_potency,ant_pairs_activity,METHOD):
    dir_warmth = utils_fun.build_dimensions(ant_pairs_warmth)
    dir_competent = utils_fun.build_dimensions(ant_pairs_competent)
    dir_evaluation = utils_fun.build_dimensions(ant_pairs_evaluation)
    dir_potency = utils_fun.build_dimensions(ant_pairs_potency)
    dir_activity = utils_fun.build_dimensions(ant_pairs_activity)
    vectors = (np.stack([dir_warmth,dir_competent,dir_evaluation,dir_potency,dir_activity]))
    from Integrating_SCM_SD.bin.archive1 import heat_map
    heat_map(vectors,METHOD)
    utils_fun.print_similarities(vectors)
    # utils_fun.print_Bhattacharyya_measure(vectors)
    print ("Google Word2Vec well done!")

def run_glove_fun(ant_pairs_warmth,ant_pairs_competent,ant_pairs_evaluation,ant_pairs_potency,ant_pairs_activity,METHOD):
    dir_warmth = utils_fun.build_dimensions_glove(ant_pairs_warmth)
    dir_competent = utils_fun.build_dimensions_glove(ant_pairs_competent)
    dir_evaluation = utils_fun.build_dimensions_glove(ant_pairs_evaluation)
    dir_potency = utils_fun.build_dimensions_glove(ant_pairs_potency)
    dir_activity = utils_fun.build_dimensions_glove(ant_pairs_activity)
    vectors = (np.stack([dir_warmth,dir_competent,dir_evaluation,dir_potency,dir_activity]))
    from Integrating_SCM_SD.bin.archive1 import heat_map
    heat_map(vectors,METHOD)
    # utils_fun.print_similarities(vectors)
    print ("GLOVE well done!")

def run_fasttext_fun(ant_pairs_warmth,ant_pairs_competent,ant_pairs_evaluation,ant_pairs_potency,ant_pairs_activity,METHOD):
    dir_warmth = utils_fun.build_dimensions_fasttext(ant_pairs_warmth)
    dir_competent = utils_fun.build_dimensions_fasttext(ant_pairs_competent)
    dir_evaluation = utils_fun.build_dimensions_fasttext(ant_pairs_evaluation)
    dir_potency = utils_fun.build_dimensions_fasttext(ant_pairs_potency)
    dir_activity = utils_fun.build_dimensions_fasttext(ant_pairs_activity)
    vectors = (np.stack([dir_warmth,dir_competent,dir_evaluation,dir_potency,dir_activity]))
    from Integrating_SCM_SD.bin.archive1 import heat_map
    heat_map(vectors,METHOD)
    # utils_fun.print_similarities(vectors)
    print ("Fastetext Word2Vec well done!")
    
if __name__ == "__main__":
    # Get the path
    warmth_pairs_path = data_yaml["SCM"]["scm_warmth_mce"]
    competent_pairs_path = data_yaml["SCM"]["scm_competent_mce"]
    evaluation_pairs_path = data_yaml["SD"]["evaluation"]
    potency_pairs_path = data_yaml["SD"]["potency"]
    activity_pairs_path = data_yaml["SD"]["activity"]
    
    # SCM dimensions
    ant_pairs_warmth = utils_fun.get_antonym_pairs(warmth_pairs_path)
    ant_pairs_competent = utils_fun.get_antonym_pairs(competent_pairs_path)
    ant_pairs_evaluation = utils_fun.get_antonym_pairs(evaluation_pairs_path)
    ant_pairs_potency = utils_fun.get_antonym_pairs(potency_pairs_path)
    ant_pairs_activity = utils_fun.get_antonym_pairs(activity_pairs_path)
      
    # METHOD = "GLOVE"
    # METHOD = "FASTTEXT"
    METHOD = "GOOGLE"
    
    if METHOD ==  "GOOGLE":
        run_google_fun(ant_pairs_warmth,ant_pairs_competent,ant_pairs_evaluation,ant_pairs_potency,ant_pairs_activity,METHOD)
    elif METHOD == "GLOVE":
        run_glove_fun(ant_pairs_warmth,ant_pairs_competent,ant_pairs_evaluation,ant_pairs_potency,ant_pairs_activity,METHOD)
    elif METHOD == "FASTTEXT":
        run_fasttext_fun(ant_pairs_warmth,ant_pairs_competent,ant_pairs_evaluation,ant_pairs_potency,ant_pairs_activity,METHOD)
    else:
        print("We dont have this method yet!")
    
    
    
    
    

    

    
    