# -*- encoding: utf-8 -*-
'''
@file: study10.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# Robustness check for three embeddings


from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yaml

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

def plot_heatmap(ax, data, labels, title):
    """ 在指定的Axes上绘制热力图，并添加标签。"""
    cosine_matrix = cosine_similarity(data)
    
   
    sns.heatmap(cosine_matrix, annot=True, fmt=".2f", cmap='Blues',  ax=ax, 
                xticklabels=labels, yticklabels=labels)
    ax.tick_params(axis='x', rotation=45)
    ax.set_title(title)
    # ax.set_title("Cosine Similarity Matrix of Social Perception Dimensions")
    fig.tight_layout()
    # Save picture
    # figureP = heatmap_path
    # plt.savefig(figureP)


    
if __name__ == "__main__":
    
    # dimensionsVectors_path = get_file_path(config_file,["pics","dimensionsVectors"])
    dimensionsVectors_path_go = 'Integrating_SCM_SD/bin/doc/output/dimensions_googlenews.npy'
    dimensionsVectors_path2_fa = 'Integrating_SCM_SD/bin/doc/output/dimensions_fasttext.npy'
    dimensionsVectors_path3_gl = 'Integrating_SCM_SD/bin/doc/output/dimensions_glove.npy'
    
    heatmap_path = get_file_path(config_file,["pics","heatmap"])
    # quadrant_path = get_file_path(config_file,["pics","quadrant"])
   
    data_go = np.load(dimensionsVectors_path_go)
    data_fa = np.load(dimensionsVectors_path2_fa)
    data_gl = np.load(dimensionsVectors_path3_gl)
    
    data1 = data_go[0:6]
    data2 = data_fa[0:6]
    data3 = data_gl[0:6]
    task_list = ['Warmth','Competence','Communion','Agency','Evaluation','Potency']
    
    
 
    fig, axes = plt.subplots(3, 1, figsize=(6,14))

 
    plot_heatmap(axes[0], data1, task_list, "Google News Word2Vec Embeddings")
    plot_heatmap(axes[1], data2, task_list, "Fasttext Word2Vec Embeddings")
    plot_heatmap(axes[2], data3, task_list, "Glove Word2Vec Embeddings")

   
    fig.suptitle("Cosine Similarity of Social Perception Dimensions", fontsize=16)


    fig.tight_layout()
    fig.subplots_adjust(top=0.94)  # Adjust the top of the subplots to fit the suptitle

    figureP = heatmap_path
    plt.savefig('Integrating_SCM_SD/bin/doc/output/dissertation/fig8.svg', format='svg')
    # plt.savefig(figureP)
 
    plt.show()
    
    
    
