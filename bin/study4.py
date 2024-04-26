# -*- encoding: utf-8 -*-
'''
@file: study4.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# Study 4: Constructing contrasting pairs and Comparing the similarity of the dimensions
# Draw the heatmap of the cosine similarity matrix of social perception dimensions


import numpy as np  
import yaml
from lib.middleware import WordembeddingModels
from lib.utils_fun import normalize_vector

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
   
def drawHeatMap(dimensionsSP,tasklist):
    """_summary_

    Args:
        dimensionsSP (array): dimensions of social perceptions
        tasklist (list): all the tasks
    """
    
    import matplotlib.pyplot as plt
    vectors = (np.stack(dimensionsSP))
    # Compute the cosine similarity matrix
    similarities = np.dot(vectors, vectors.T) / (np.linalg.norm(vectors, axis=1) * np.linalg.norm(vectors, axis=1)[:, np.newaxis])

    # Plot the heatmap
    fig, ax = plt.subplots()
    im = ax.imshow(similarities)
    
    # Set the tick labels
    ax.set_xticks(np.arange(len(vectors)))
    ax.set_yticks(np.arange(len(vectors)))
    ax.set_xticklabels(tasklist)
    ax.set_yticklabels(tasklist)
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over the data and add text annotations
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            text = ax.text(j, i, "{:.2f}".format(similarities[i, j]), ha="center", va="center", color="w")
            
    ax.set_title("Cosine Similarity Matrix of Social Perception Dimensions")
    fig.tight_layout()
    plt.show()
    
    # Save picture
    # figureP = "Integrating_SCM_SD/bin/output/figure_cosine_simlarity/" + METHOD + ".png" 
    # plt.savefig(figureP)
    
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

def build_dimensions(contrastingPairsArray,wordembedding = 'word2vec_fun'):
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
                rp_word_vec_0, rp_word_vec_1 = WordembeddingModels.word2vec_glove(str(rp_word_0),str(rp_word_1))
                # print(rp_word_vec_0, rp_word_vec_1)
            else:
                print("wordembedding is not correct")
                return None
            
            word_dims[_,] = rp_word_vec_0 - rp_word_vec_1
            
        except Exception as err:
            print("something wrong, the err is{}".format(err))
    dim_ave = np.nanmean(word_dims,axis=0)
    dim_ave_n = normalize_vector(dim_ave)
    return dim_ave_n
    
if __name__ == "__main__":
    
    model = 'word2vec_fun' # word2vec_fun, word2vec_fasttext, word2vec_glove
    task_list = ['warmth_pairs','competent_pairs','communion_pairs','agency_pairs','evaluation_pairs','potency_pairs','activity_pairs']
    
    for task in task_list:
        
        dimensionsSP = []
        seed_path = get_file_path(config_file, ['contrasting_pairs',task])
        print(seed_path)
        # put the pairs in an array from csv file
        contrastingPairsArray = contrasting_pairs_array(seed_path)
        if contrastingPairsArray is None:
            print("contrastingPairsArray is None")
        else:
            dimensions = build_dimensions(contrastingPairsArray)
            print(dimensions.shape())
        dimensionsSP.append(dimensions)
        
    drawHeatMap(dimensionsSP,task_list)