import pandas as pd
from lib import utils_fun
from lib.middleware import word2vec_fun
import os

Yamlcon = utils_fun.YamlConfig()
data_yaml = Yamlcon.get_yaml()


def create_matrix(ant_pairs_Jenkins):
    """convert data to a new matrix for factor analysis

    Args:
        ant_pairs_Jenkins (array): the antonyms of pairs

    Returns:
        matrix: the transposed matrix for factor analysis
    """
    word_dims = {}
    
    count_pairs = 0
    for _ in range(ant_pairs_Jenkins.shape[0]):
        try:
            rp_word_0 = ant_pairs_Jenkins[_,0]
            rp_word_1 = ant_pairs_Jenkins[_,1]
            rp_word_vec_0, rp_word_vec_1 = word2vec_fun(rp_word_0,rp_word_1)
            
            Antonym_key = "_".join(ant_pairs_Jenkins[_])
            bias_dimension = rp_word_vec_0 - rp_word_vec_1
            word_dims[Antonym_key] = bias_dimension
            
            count_pairs = count_pairs + 1
            
            
        except Exception as err:
            print("Can not find pair:",Antonym_key)
            print("some thing wrong:",err)
            
    print("total pairs are: ",ant_pairs_Jenkins.shape[0])
    print("the counted pairs are:", count_pairs)
    return word_dims



def write_to_dta(filep):
    """write vector of data to .dta format and do transpose

    Args:
        filep (str): the file included pairs 

    Returns:
        bool: all the data procession has finished
    """
    ant_pairs_filep = utils_fun.get_antonym_pairs(filep)
    data = create_matrix(ant_pairs_filep)
    df = pd.DataFrame(data, index=["V" + str(i) for i in range(1, 301)])
    # write to csv
    suffix_filep = filep.split("/")[-1]
    suffix_filep_filep = suffix_filep.split(".")[0]
    filename = "Integrating_SCM_SD/bin/output/factor_analyis/factor_analysis_" + suffix_filep_filep + ".dta"
    df.to_stata(filename)
    return True

def write_to_tsne(filep):
    try:
        ant_pairs_filep = utils_fun.get_antonym_pairs(filep)
        data = create_matrix(ant_pairs_filep)

        # write to csv
        df = pd.DataFrame.from_dict(data=data, orient='index')
        suffix_filep = filep.split("/")[-1]
        suffix_filep_filep = suffix_filep.split(".")[0]
        # filename = "Integrating_SCM_SD/bin/output/tsne/" + suffix_filep_filep + "_tsne.csv"
        # filename = "Integrating_SCM_SD/bin/output/tsne/original_tsne.csv"
        filename = "Integrating_SCM_SD/bin/output/tsne/reduction_tsne.csv"
        df.to_csv(filename, mode='a', header=False)
    except Exception as err:
        print(err)
    return True
    
    

if __name__ == "__main__":
    # Get the path
    # filep = data_yaml["Dir"]["reduction_pairs"]
    
    # dirlist = os.listdir(filep)
    # for dir_ in dirlist:
    #     file_path = filep + dir_
    #     write_to_tsne(file_path)
    #     print(" file {} hass finished".format(file_path))
        
    # print("Finish all tasks.")
    filep = data_yaml["Osgood"]["50_pairs"]
    write_to_dta(filep)
    print("Finish all tasks.")
    