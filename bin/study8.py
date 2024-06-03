# -*- encoding: utf-8 -*-
'''
@file: study8.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 


# Study8, Integrating social perception models and generate the 2D dimensions of social perception
# create the 30 seed words for WCE and CA



import yaml
import numpy as np
import pandas as pd
from numpy.linalg import norm

# Global configration
config_file = "Integrating_SCM_SD/bin/conf/config.yaml" # the path of the config file

def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

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
     
def find_top_unique_similar_words(df, compared_vector, top_n=30):
    """
    Find top N unique words with the highest cosine similarity to a given vector in a dataframe.

    Parameters:
        df (pd.DataFrame): DataFrame containing words and their vector representations.
        compared_vector (np.array): The vector to compare against.
        top_n (int): Number of top entries to return.

    Returns:
        pd.DataFrame: DataFrame containing the top N unique words and their cosine similarities.
    """
    if 'dimension' not in df or 'rp_word_pairs' not in df:
        raise ValueError("DataFrame must contain 'dimension' and 'rp_word_pairs' columns")
    
    # Removing duplicates based on 'rp_word_0'
    df = df.drop_duplicates(subset='rp_word_pairs')

    # Compute cosine similarity for each row
    df.loc[:, 'cosine_similarity'] = df['dimension'].apply(lambda x: cosine_similarity(x, compared_vector))
    
    
    # Sort by cosine similarity in descending order and select the top N entries
    result = df.sort_values(by='cosine_similarity', ascending=False).head(top_n)

    return result[['rp_word_pairs', 'cosine_similarity']]

     
if __name__ == "__main__":
    task_list = ['warmth_pairs','competent_pairs','communion_pairs','agency_pairs','evaluation_pairs','potency_pairs','activity_pairs']
    dimensionsVectors_path = get_file_path(config_file,["pics","dimensionsVectors_googlenews"])
    print(dimensionsVectors_path)
    
    data = np.load(dimensionsVectors_path)
    
    print(data.shape,len(data),type(data))
    # warmDim = data[0]
    # compeDim = data[1]
    # commDim = data[2]
    # agenDim = data[3]
    # evalDim = data[4]
    # potenDim = data[5]
    average_w_c_e = np.mean(data[[0, 2, 4]], axis=0)
    average_a_c = np.mean(data[[1, 3]], axis=0)
    
    # print("Average of the 1st, 3rd, and 5th rows:")
    # print(average_w_c_e)
    # print("\nAverage of the 2nd and 4th rows:")
    # print(average_a_c)
    
    file_path = 'Integrating_SCM_SD/bin/doc/output/all_data.pkl'
    df = pd.read_pickle(file_path)
    df['rp_word_pairs'] = df['rp_word_0'] + '_' + df['rp_word_1']
    
    top_30_words = find_top_unique_similar_words(df, average_a_c)
    # top_30_words.to_csv('wce_top30.csv', index=False)
    top_30_words.to_csv('ac_top30.csv', index=False)
    print(top_30_words)

