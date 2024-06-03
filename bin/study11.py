# -*- encoding: utf-8 -*-
'''
@file: study10.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 
# Drawing heat map to show the cosine similarity matrix of social perception dimensions

import matplotlib.pyplot as plt
import numpy as np

def fig_1():
    
    cold = np.array([2.5, 0.1])
    friendly = np.array([1, 1])
    warm = np.array([2, 1])
    hot = np.array([2.2, 0.75])

  
    fig, ax = plt.subplots(figsize=(8, 6))

  
    ax.annotate('cold', (cold + (0.1,0.1)),fontsize=14)
    ax.annotate('friendly', (friendly + (0.1,0.1)),fontsize=14)
    ax.annotate('warm', (warm + (0.1,0.1)),fontsize=14)
    ax.annotate('hot', (hot + (0.1,0.1)),fontsize=14)

   
    ax.arrow(0, 0, cold[0], cold[1], head_width=0.05, head_length=0.05, fc='b', ec='b')
    ax.arrow(0, 0, friendly[0], friendly[1], head_width=0.05, head_length=0.05, fc='b', ec='b')
    ax.arrow(0, 0, warm[0], warm[1], head_width=0.05, head_length=0.05, fc='b', ec='b')
    ax.arrow(0, 0, hot[0], hot[1], head_width=0.05, head_length=0.05, fc='b', ec='b')

   
    ax.set_xlim([- 0.5, 3.5])
    ax.set_ylim([- 0.2, 1.5])
    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')
    ax.set_title('Hypothetical Two-dimensional Semantic Space')

    
    ax.grid(True)
   
    plt.savefig('Integrating_SCM_SD/bin/doc/output/dissertation/fig1.svg', format='svg')
    plt.show()
    
def fig_3():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.metrics.pairwise import cosine_similarity
    import seaborn as sns

    dimensionsVectors_path = "Integrating_SCM_SD/bin/doc/output/dimensions.npy"
    data_all = np.load(dimensionsVectors_path)
    data = data_all[0:6]
    labels = ['Warmth', 'Competence', 'Communion', 'Agency', 'Evaluation', 'Potency']

    cosine_matrix = cosine_similarity(data)


    plt.figure(figsize=(8, 6))  
    sns.heatmap(cosine_matrix, annot=True, fmt=".2f", cmap='Blues', 
                xticklabels=labels, yticklabels=labels)
    plt.tick_params(axis='x', rotation=45)
    plt.title("Cosine Similarity Matrix of Social Perception Dimensions",pad=20)
    plt.tight_layout()
    plt.savefig('Integrating_SCM_SD/bin/doc/output/dissertation/fig3.svg', format='svg')
    plt.show()
    
fig_3()