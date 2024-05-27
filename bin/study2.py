# -*- encoding: utf-8 -*-
'''
@file: study2.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# Study 2 - methods: Constructing contrasting pairs and building dimensions


import numpy as np  
import yaml
from lib.middleware import WordembeddingModels
from lib.utils_fun import normalize_vector
import pandas as pd

# Global configration
config_file = "Integrating_SCM_SD/bin/conf/config.yaml" # the path of the config file

def get_file_path(yaml_file, keys):
    """get file path from config file

    Args:
        yaml_file (str): the path of the yaml file
        keys (list): the keys of the file path

    Returns:
        str: the file path
    """
    try:
        with open(yaml_file, 'r') as f:
            config = yaml.safe_load(f)
            file_path = config[keys[0]][keys[1]]
            return file_path
    except yaml.YAMLError as exc:
            print("YAML error:", exc)
    except KeyError as exc:
            print("Key error:", exc)
    except TypeError as exc:
            print("Type error, possibly due to incorrect keys:", exc)
    except Exception as exc:
            print("Error occurred:", exc)
     
    
def contrasting_pairs_array(seed_path):
    import numpy as np
    array_contrasting = []
    try:
        with open(seed_path, 'r') as f: 
            for line in f:
                line = line.strip()
                array_contrasting.append(line.split(','))
        contra_pairs_array = np.vstack(array_contrasting)
        return contra_pairs_array
    except Exception as err:
        print(" the err is: {} ".format(err))
        return None
    
    
# Only Once
def append_to_dataframe(task,rp_word_0, rp_word_1, rp_word_vec_0, rp_word_vec_1, dim):
    # Check if the pickle file exists and load the DataFrame if it does, otherwise create an empty DataFrame
    try:
        df = pd.read_pickle('Integrating_SCM_SD/bin/doc/output/all_data.pkl')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['task','rp_word_0', 'rp_word_1', 'rp_word_vec_0', 'rp_word_vec_1', 'dimension'])

    # Create a new DataFrame with the data to be appended
    new_row = pd.DataFrame([[task, rp_word_0, rp_word_1, rp_word_vec_0, rp_word_vec_1, dim]], 
                           columns=['task','rp_word_0', 'rp_word_1', 'rp_word_vec_0', 'rp_word_vec_1', 'dimension'])
    
    # Concatenate the new DataFrame with the existing DataFrame
    df = pd.concat([df, new_row], ignore_index=True)

    # Save the DataFrame to the pickle file
    df.to_pickle('Integrating_SCM_SD/bin/doc/output/all_data.pkl')
   
    
    
def build_dimensions(contrastingPairsArray,wordembedding):
    word_dims = np.full((contrastingPairsArray.shape[0], 300), np.nan) # create matrix
    for _ in range(contrastingPairsArray.shape[0]):
        print(_)
        rp_word_0 = contrastingPairsArray[_,0]
        rp_word_1 = contrastingPairsArray[_,1]
        
        print(rp_word_0, rp_word_1)
        try:
            if wordembedding == 'word2vec_fun':
                rp_word_vec_0, rp_word_vec_1 = WordembeddingModels.word2vec_fun(str(rp_word_0),str(rp_word_1))
                # print(rp_word_vec_0, rp_word_vec_1,len(rp_word_vec_0),len(rp_word_vec_1))
                
            elif wordembedding == 'word2vec_fasttext':
                rp_word_vec_0, rp_word_vec_1 = WordembeddingModels.word2vec_fasttext(str(rp_word_0),str(rp_word_1))
                # print(rp_word_vec_0, rp_word_vec_1)
                
            elif wordembedding == 'word2vec_glove':
                rp_word_vec_0 = WordembeddingModels.word2vec_glove(str(rp_word_0))
                rp_word_vec_1 = WordembeddingModels.word2vec_glove(str(rp_word_1))
                # print(rp_word_vec_0, rp_word_vec_1)
            else:
                print("wordembedding is not correct")
                return None
            
            # dim = rp_word_vec_0 - rp_word_vec_1
            # append_to_dataframe(task,rp_word_0,rp_word_1,rp_word_vec_0,rp_word_vec_1,dim)
            
            word_dims[_,] = rp_word_vec_0 - rp_word_vec_1
            
        except Exception as err:
            print("something wrong, the err is{}".format(err))
    dim_ave = np.nanmean(word_dims,axis=0)
    dim_ave_n = normalize_vector(dim_ave)
    return dim_ave_n

if __name__ == "__main__":
    
    model = 'word2vec_glove' # word2vec_fun, word2vec_fasttext, word2vec_glove
    # models = ['word2vec_fun','word2vec_fasttext','word2vec_glove']
    if model == "word2vec_glove":
        task_list = ['warmth_pairs','competent_pairs','communion_pairs','agency_pairs','evaluation_pairs','potency_pairs','activity_pairs']
        dimensionsSP = []
        for task in task_list:
            seed_path = get_file_path(config_file, ['contrasting_pairs',task])
            print(seed_path)
            # put the pairs in an array from csv file
            contrastingPairsArray = contrasting_pairs_array(seed_path)
            if contrastingPairsArray is None:
                print("contrastingPairsArray is None")
            else:
                dimensions = build_dimensions(contrastingPairsArray,model)
                dimensionsSP.append(dimensions)
                
            print(dimensionsSP,len(dimensionsSP))
        with open ('Integrating_SCM_SD/bin/output/dimensions_glove.npy', 'wb') as f:
            np.save(f,dimensionsSP)
        print("all data has been saved")
        
