import numpy as np
import csv
from lib import utils_fun
from lib.middleware import word2vec_fun

Yamlcon = utils_fun.YamlConfig()
data_yaml = Yamlcon.get_yaml()



    

if __name__ == "__main__":
    # Get the path
    Jenkins = data_yaml["Jenkins"]["pairs"]
    ant_pairs_Jenkins = utils_fun.get_antonym_pairs(Jenkins)
    print(ant_pairs_Jenkins.shape)
    
    for _ in ant_pairs_Jenkins:
        print(_)
        Jekins_key = "-".join(_)
        print(Jekins_key)
        Jenkins_vec_0,Jenkins_vec_1= word2vec_fun(_[0],_[1])
        bipolar_vec = Jenkins_vec_0 - Jenkins_vec_1
        print(Jekins_key,bipolar_vec)