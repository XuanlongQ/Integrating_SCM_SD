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
    # calculate the eigenvalues
    explained_variance = pca.explained_variance_ratio_
    eigenvalues = pca.explained_variance_
    
    print("Eigenvalues:", eigenvalues)
    print("Explained variance by each component:", explained_variance) 
    

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

def plot_vectors_and_points_sub(ax, data, labels,subplot_label, show_grid=True):
    """Plot reduced dimension vectors and points."""
    dimensions_reduced = dimensionReduction(data)
    for point, label in zip(dimensions_reduced, labels):
        ax.plot(point[0], point[1], 'o')
        ax.quiver(0, 0, point[0], point[1], angles='xy', scale_units='xy', scale=1, color='r')
        ax.text(point[0], point[1], f' {label}', color='blue', fontsize=8, ha='right', va='bottom')
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-0.75, 0.75)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    if show_grid:
        ax.grid(True)
    # Set the labels for the axes
    ax.set_xlabel("PCA 1")  # Label for the x-axis
    ax.set_ylabel("PCA 2")  # Label for the y-axis
    ax.set_title(subplot_label, loc='center', y=-0.2, fontsize=12)


        
def plot_heatmap(ax, data, labels):
    dimensions_reduced = dimensionReduction(data)
    cosine_matrix = cosine_similarity(dimensions_reduced)
    
  
    sns.heatmap(cosine_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax, 
                xticklabels=labels, yticklabels=labels)
    ax.tick_params(axis='x', rotation=45)

def dim_red_3(data):
    # select first 6 rows in data
    data_no_activity = data[0:6]
    task_list = ['Warmth','Competence','Communion','Agency','Evaluation','Potency']
    
    print(data_no_activity,len(data_no_activity),type(data_no_activity))
    
    data_no_SD = data[0:4]
    task_list_no_SD = ['Warmth','Competence','Communion','Agency']

    print(data_no_SD,len(data_no_SD),type(data_no_SD))
    
    datasets =[data_no_SD, data_no_activity, data  ]
    labels_list = [task_list_no_SD, task_list, task_list_all]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    subplot_labels = ['(a)', '(b)', '(c)']  # 子图标签列表


        
     # 使用 enumerate 来迭代子图索引和数据
    for idx, (dataset, labels) in enumerate(zip(datasets, labels_list)):
        subplot_label = subplot_labels[idx]
        plot_vectors_and_points_sub(axes[idx], dataset, labels, subplot_label)

    # fig.suptitle('Projecting Content Dimensions of Social Perception Models on Two-dimensional PCA Space', fontsize=16, color='black')
    plt.tight_layout() 
    plt.savefig('Integrating_SCM_SD/bin/doc/output/dissertation/fig6.svg', format='svg')
    plt.show()

if __name__ == "__main__":
    # study = "study1"
    # draw_figure(study)
    dimensionsVectors_path = get_file_path(config_file,["pics","dimensionsVectors_googlenews"])
    heatmap_path = get_file_path(config_file,["pics","heatmap"])
   
    data = np.load(dimensionsVectors_path)
    task_list_all = ['Warmth','Competence','Communion','Agency','Evaluation','Potency','Activity']
    # write to csv 
    # np.savetxt("Integrating_SCM_SD/bin/doc/output/dissertation/data.csv", data, delimiter=",")
    # JSC Figure 4 and SSCR Figure 2
    # drawHeatMap(data[0:6],task_list_all[0:6])
    # SSCR Figure 3
    dim_red_3(data)
     
    
    