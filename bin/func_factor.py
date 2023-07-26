import numpy as np
from lib import utils_fun
from lib.middleware import word2vec_fun

Yamlcon = utils_fun.YamlConfig()
data_yaml = Yamlcon.get_yaml()



    

if __name__ == "__main__":
    # Get the path
    Jenkins = data_yaml["Jenkins"]["pairs"]
    ant_pairs_Jenkins = utils_fun.get_antonym_pairs(Jenkins)
    print(ant_pairs_Jenkins.shape)
    
    for _ in range(ant_pairs_Jenkins.shape[0]):
        print(_)
        Jenkins_vec_0,Jenkins_vec_1= word2vec_fun(_)
        bipolar_vec = Jenkins_vec_0 - Jenkins_vec_1
        print(_,bipolar_vec)