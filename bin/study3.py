# -*- encoding: utf-8 -*-
'''
@file: study3.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# Study 3- Supplementary: Project word embeddings to 2-dimensional bias dimensions
# Draw the 2D dimensions of social perception

import yaml
import numpy as np

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
     
def project2D_orthogonal(dim_a,dim_b,word_embeddings = 'word2vec'):
    beta1 = dim_a
    a2 = dim_b
    beta2 = a2 - np.dot(a2,beta1) * beta1 / np.dot(beta1,beta1)
    
    # define the orthogonal dimensions
    dimsOrth = np.vstack((beta1,beta2))
    print(dimsOrth.shape)
    
    # project the word embeddings to the bias dimensions
    if word_embeddings == 'word2vec':
        model_path = get_file_path(config_file,["model_path","google_news"]) 
        
        
        model_output_path = get_file_path(config_file,["model_path_output","DPM_google_news_indirect"])
        
        import gensim    
        model = gensim.models.KeyedVectors.load_word2vec_format(model_path,binary=True)
        
        curr_antonmy_vector = np.linalg.pinv(np.transpose(dimsOrth))   
        vocab_list = model.index_to_key

        for each_word in vocab_list:
            new_vector = np.matmul(curr_antonmy_vector,model[each_word])
            new_vector = new_vector/np.linalg.norm(new_vector)
            
            with open(model_output_path,'a+',encoding='utf-8') as f:
                f.write(each_word + ',' + str(new_vector[0]) + ',' + str(new_vector[1]) + '\n')
                f.close()
    else:
        print("The word embeddings is not supported")

    

if __name__ == "__main__":
    # task_list = ['warmth_pairs','competent_pairs','communion_pairs','agency_pairs','evaluation_pairs','potency_pairs','activity_pairs']
    task_list = ['communion_pairs','agency_pairs']
    dimensionsVectors_path = get_file_path(config_file,["pics","dimensionsVectors_indirect"])
    print(dimensionsVectors_path)
    
    data = np.load(dimensionsVectors_path)
    
    print(data.shape,len(data),type(data))
    print(data[0])
    # warmDim = data[0]
    # compeDim = data[1]
    # commDim = data[2]
    # agenDim = data[3]
    # evalDim = data[4]
    # potenDim = data[5]
    # actDim = data[6]
    
    # project_warmth_competent = np.vstack((warmDim,compeDim))
    # project_communion_agency = np.vstack((commDim,agenDim))
    # project_evaluation_potency = np.vstack((evalDim,potenDim))
    
    # warm_comm = np.mean(data[[0, 2, 4]], axis=0)
    # compe_agen = np.mean(data[[1, 3]], axis=0)
    
    project2D_orthogonal(data[0],data[1])
    
    
    