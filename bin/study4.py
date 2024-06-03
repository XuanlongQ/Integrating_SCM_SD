# -*- encoding: utf-8 -*-
'''
@file: study4.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# Draw the picture for all studies
# Draw the heatmap of the cosine similarity matrix of social perception dimensions
# Draw the 2D dimensions of social perception


import yaml
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns

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


import numpy as np
from scipy.spatial.distance import euclidean

def drawHeatMap(dimensionsSP,tasklist):
    """_summary_

    Args:
        dimensionsSP (array): dimensions of social perceptions
        tasklist (list): all the tasks
    """
    vectors = (np.stack(dimensionsSP))
    # Compute the cosine similarity matrix
    similarities = np.dot(vectors, vectors.T) / (np.linalg.norm(vectors, axis=1) * np.linalg.norm(vectors, axis=1)[:, np.newaxis])

    # Plot the heatmap
    fig, ax = plt.subplots()
    im = ax.imshow(similarities)
    
    # Set the tick labels
    ax.set_xticks(np.arange(len(vectors)))
    ax.set_yticks(np.arange(len(vectors)))
    ax.set_xticklabels([x for x in tasklist])
    ax.set_yticklabels([y for y in tasklist])
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over the data and add text annotations
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            text = ax.text(j, i, "{:.2f}".format(similarities[i, j]), ha="center", va="center", color="w")
            
    ax.set_title("Cosine Similarity Matrix of Social Perception Dimensions")
    fig.tight_layout()
    # Save picture
    # figureP = heatmap_path
    # plt.savefig(figureP)
    plt.show()

def dimensionReduction(dimensionsSP):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    dimensionsSP_reduced = pca.fit_transform(dimensionsSP)
    print("Reduced data shape:", dimensionsSP_reduced.shape) 
    print("Reduced data:", dimensionsSP_reduced)
    return dimensionsSP_reduced

def plot_vectors_and_points(data, labels):
    
    dimensionsSPreduced = dimensionReduction(data)

    fig, ax = plt.subplots()

  
    for point, label in zip(dimensionsSPreduced, labels):
        
        ax.plot(point[0], point[1], 'o')  
        
        ax.quiver(0, 0, point[0], point[1], angles='xy', scale_units='xy', scale=1, color='r')
        
        ax.text(point[0], point[1], f' {label}', color='blue', fontsize=12, ha='right', va='bottom')

   
    max_val = np.max(np.abs(dimensionsSPreduced)) + 1
    ax.set_xlim(-1, max_val)
    ax.set_ylim(-1, max_val)
    ax.axhline(y=0, color='k') 
    ax.axvline(x=0, color='k') 


    plt.title("2-dimensional Configuration for content dimensions")
    plt.grid(True)
    
    # figureP = quadrant_path 
    # plt.savefig(figureP)

    
    # plt.show()

def plot_vectors_and_points_sub(ax, data, labels, show_grid=True):
    """
    在指定的Axes上绘制向量和点。
    
    :param ax: matplotlib的Axes对象，用于绘制图形。
    :param data: 数据集，应该是二维或更高维度的数据。
    :param labels: 数据点的标签。
    :param show_grid: 是否显示网格，默认为True。
    """

    # 进行降维
    dimensions_reduced = dimensionReduction(data)
    
    # 对于数据集中的每一个点
    for point, label in zip(dimensions_reduced, labels):
        # 画点
        ax.plot(point[0], point[1], 'o')  # 'o' 是点的标记
        # 画向量
        ax.quiver(0, 0, point[0], point[1], angles='xy', scale_units='xy', scale=1, color='r')
        # 添加标签
        ax.text(point[0], point[1], f' {label}', color='blue', fontsize=8, ha='right', va='bottom')

    # 设置图的范围
    # max_val = np.max(np.abs(dimensions_reduced)) + 1
    # ax.set_xlim(-1, max_val)
    # ax.set_ylim(-1, max_val)
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-0.75, 0.75)
    ax.axhline(y=0, color='k')  # 横轴
    ax.axvline(x=0, color='k')  # 纵轴
    # ax.set_title("2-dimensional Configuration for Content Dimensions")
    # 是否显示网格
    if show_grid:
        ax.grid(True)
        
def plot_heatmap(ax, data, labels):
    """ 在指定的Axes上绘制热力图，并添加标签。"""
    dimensions_reduced = dimensionReduction(data)
    cosine_matrix = cosine_similarity(dimensions_reduced)
    
  
    sns.heatmap(cosine_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax, 
                xticklabels=labels, yticklabels=labels)
    ax.tick_params(axis='x', rotation=45)

def dim_red_3(data):
    # select first 6 rows in data
    data_no_activity = data[0:6]
    task_list = ['Warmth','Competence','Communion','Agency','Evaluation','Potency']
    
    print(data_no_activity
          ,len(data_no_activity),type(data_no_activity))
    
    data_no_SD = data[0:4]
    task_list_no_SD = ['Warmth','Competence','Communion','Agency']

    print(data_no_SD
          ,len(data_no_SD),type(data_no_SD))
    
   
    datasets =[data, data_no_activity, data_no_SD]
    labels_list = [task_list_all, task_list, task_list_no_SD]

    fig, axes = plt.subplots(2, len(datasets), figsize=(5 * len(datasets), 9))
    # fig, axes = plt.subplots(2, 3, figsize=(18, 12), gridspec_kw={'width_ratios': [1, 1, 1.2]})
    
    for idx, (data, labels) in enumerate(zip(datasets, labels_list)):
        plot_vectors_and_points_sub(axes[0, idx], data, labels)  
        plot_heatmap(axes[1, idx], data, labels) 
        
       
        axes[0, idx].set_xlabel(f'({chr(97 + idx)})')
        axes[1, idx].set_xlabel(f'({chr(97 + idx)})')


   
    # fig.suptitle("PCA Dimension Reduction and Cosine Similarity", fontsize=14, y=0.95)
    axes[0, 1].set_title("2-dimensional Configuration for Content Dimensions", pad=20)  # 第一行中部添加标题，并增加pad
    axes[1, 1].set_title("Cosine Similarity Heatmap", pad=20) 
    plt.tight_layout(rect=[0, 0, 1, 0.95])  
    # plt.savefig('Integrating_SCM_SD/bin/doc/output/2-dimensional Configuration for content dimensions.png')
    plt.savefig('Integrating_SCM_SD/bin/doc/output/dissertation/fig6.svg', format='svg')
    plt.show()

if __name__ == "__main__":
    # study = "study1"
    # draw_figure(study)
    dimensionsVectors_path = get_file_path(config_file,["pics","dimensionsVectors_googlenews"])
    heatmap_path = get_file_path(config_file,["pics","heatmap"])
    # quadrant_path = get_file_path(config_file,["pics","quadrant"])
   
    data = np.load(dimensionsVectors_path)
    task_list_all = ['Warmth','Competence','Communion','Agency','Evaluation','Potency','Activity']
    # fig3
    # drawHeatMap(data[0:6],task_list_all[0:6])
    dim_red_3(data)
     
    
    