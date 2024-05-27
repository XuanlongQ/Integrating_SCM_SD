# -*- encoding: utf-8 -*-
'''
@file: study5.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# study5- Assessing the Feasibility of Model Integration
# Clustering the words in the bias dimensions
# Evaluating the clustering by PCA-1,2

file_path = 'Integrating_SCM_SD/bin/doc/output/all_data.pkl'
import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

def reduce_dimension(df, column_name, n_components):
    # 提取指定列的数据
    dim_matrix = [] 
    column_data = df[column_name].values
    for i in column_data:
        dim_matrix.append(i)
    dim_matrix = np.array(dim_matrix)
    
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(dim_matrix)
    print("Reduced data shape:", reduced_data.shape)  # 输出 (100, 2)
    print("Reduced data:", reduced_data)
    
    matrix_as_tuples = [tuple(row) for row in reduced_data]
    df['reduced_dimension'] = matrix_as_tuples

    print(df.head())
    return df

def draw_2Ddimensiona_allPAirs(df):
    df.loc[:, 'x'] = df['reduced_dimension'].apply(lambda coord: coord[0])
    df.loc[:, 'y'] = df['reduced_dimension'].apply(lambda coord: coord[1])  
    # Create a scatter plot
    fig, ax = plt.subplots()
    for classification in df['task'].unique():
        subset = df[df['task'] == classification]
        ax.scatter(subset['x'], subset['y'], label=classification, s=100)  # s is the size of each point

    # Add labels for each point
    for i, txt in enumerate(df['rp_word_0']):
        ax.annotate(txt, (df['x'][i], df['y'][i]))

    # Title and labels
    ax.set_title('2D Space Point Plot by Classification')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')

    # Legend
    ax.legend(title='Classification')

    # Show the plot
    plt.show()

def calculate_optimal_clusters(df, max_clusters=10):
    """
    Calculates the optimal number of clusters using the Elbow Method.

    Parameters:
        df (pd.DataFrame): DataFrame containing the 'x' and 'y' coordinates.
        max_clusters (int): Maximum number of clusters to consider.

    Returns:
        None. Displays a matplotlib plot showing the elbow plot.
    """
    from sklearn.cluster import KMeans
    inertias = []
    K = range(1, max_clusters + 1)

    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df[['x', 'y']])
        inertias.append(kmeans.inertia_)

    plt.figure(figsize=(8, 4))
    plt.plot(K, inertias, 'bo-')
    plt.xlabel('Number of Clusters, k')
    plt.ylabel('Inertia')
    plt.title('Elbow Method For Optimal k')
    plt.grid(True)
    # plt.savefig('Integrating_SCM_SD/bin/doc/output/cluster/elbow_plot_3groups.png')
    plt.savefig('Integrating_SCM_SD/bin/doc/output/cluster/elbow_plot_2groups.png')

    plt.show()

def cluster_and_plot(df, n_clusters):
    from sklearn.cluster import KMeans
    """
    Applies K-means clustering to the DataFrame and plots the results.

    Parameters:
        df (pd.DataFrame): DataFrame containing the 'Coordinates' and 'Classification'.
        n_clusters (int): Number of clusters to form.

    Returns:
        None. Displays a matplotlib plot.
    """
    # Extract x and y coordinates
    df.loc[:, 'x'] = df['reduced_dimension'].apply(lambda coord: coord[0])
    df.loc[:, 'y'] = df['reduced_dimension'].apply(lambda coord: coord[1]) 
    calculate_optimal_clusters(df)

    # Applying K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df[['x', 'y']])
    # df.to_csv('Integrating_SCM_SD/bin/doc/output/cluster/cluster_3groups.csv', index=False)
    # df.to_csv('Integrating_SCM_SD/bin/doc/output/cluster/cluster_2groups.csv', index=False)
    # df.to_csv('Integrating_SCM_SD/bin/doc/output/cluster/cluster_2groups_combine_com_agen.csv', index=False)

    print(df.head())
    
    # Plotting
    plt.figure(figsize=(10, 6))
    colors = {'warmth_pairs': 'blue', 'competent_pairs': 'green', 'communion_pairs': 'yellow', 'agency_pairs': 'grey', 'competent-agency':'purple',
              'evaluation_pairs': 'magenta','potency_pairs': 'cyan'}

 
    for classification in df['task'].unique():
        # Filter data by classification
        classified_data = df[df['task'] == classification]
        plt.scatter(classified_data['x'], classified_data['y'], color=colors.get(classification, 'magenta'), label=classification, s=100)
    
    # Mark the cluster centers
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, color='red', label='Centroids', marker='*')
    
    plt.title('Cluster of Coordinates with Classification')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    # plt.savefig('Integrating_SCM_SD/bin/doc/output/cluster/3groups.png')
    # plt.savefig('Integrating_SCM_SD/bin/doc/output/cluster/2groups.png')
    plt.show()

def generate_combing_agency_competence(df):
    # Find rows where classification is 'competence' or 'agency'
    competence_agency_df = df[df['task'].isin(['competent_pairs', 'agency_pairs'])].copy()

    # Optionally, you could concatenate the values in some way, here just duplicating
    competence_agency_df['task'] = 'competent-agency'

    # Append these new rows to the original dataframe
    df_competence_agency = pd.concat([df, competence_agency_df], ignore_index=True)
    return df_competence_agency
    

if __name__ == '__main__':
    df = pd.read_pickle(file_path)

    print(df.keys())
    new_dataset = reduce_dimension(df, 'dimension', 2)
    # print(new_dataset.head())
    
    # unwanted_classifications = ['evaluation_pairs', 'potency_pairs', 'activity_pairs']
    unwanted_classifications = ['activity_pairs']
    df_filtered = df[~df['task'].isin(unwanted_classifications)].copy()
    
    print(df_filtered.shape)
    
    # draw_2Ddimensiona_allPAirs(df_filtered)
    cluster_and_plot(df_filtered,2)
    
    ### combining agency and competence
    ##df_combinging = generate_combing_agency_competence(df_filtered)
    # unwanted_classifications = ['competent_pairs', 'agency_pairs']
    # df_filtered_2 = df_combinging[~df_combinging['task'].isin(unwanted_classifications)].copy()
    # cluster_and_plot(df_filtered_2,2)
    
  

