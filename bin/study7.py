# -*- encoding: utf-8 -*-
'''
@file: study7.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 


# Study 7 - Assessing the Feasibility of Model Integration
# Integrating dimensions-preanalysis and dimensions-visualization

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances_argmin_min

def elbow_methods(X):
# Running K-means with a range of k
    sse = []
    k_list = range(1, 11)  # Testing 1 to 10 clusters
    for k in k_list:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        sse.append(kmeans.inertia_)  # Sum of squared distances to closest cluster center

    # Plot SSE for each k
    plt.figure(figsize=(10, 6))
    plt.plot(k_list, sse, marker='o')
    plt.title('The Elbow Method for Determining Number of Clusters')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Sum of Squared Distances')
    plt.xticks(k_list)
    plt.show()


def cluster_group(X,df,number):
    k_optimal = number  # Replace with the number you choose from the plot
    kmeans_opt = KMeans(n_clusters=k_optimal, random_state=42)
    df['cluster'] = kmeans_opt.fit_predict(X)

    # To see which words fall into each cluster
    for i in range(k_optimal):
        print(f"Words in cluster {i}:")
        print(df[df['cluster'] == i]['rp_word_0'].values)

    
    pca = PCA(n_components=2)  # Reduce dimensions to 2 for visualization
    principal_components = pca.fit_transform(X)
    df['pca1'] = principal_components[:, 0]
    df['pca2'] = principal_components[:, 1]

    # Importing plotting library
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(df['pca1'], df['pca2'], c=df['cluster'], cmap='viridis', label=df['cluster'])
    plt.title('PCA of Word Vectors Colored by Cluster')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar(scatter)
    plt.show()
    
if __name__ == "__main__":
    file_path = 'Integrating_SCM_SD/bin/doc/output/all_data.pkl'
    df = pd.read_pickle(file_path)
    print(df.head(),df.keys())

    df = df[df['task'].isin(['warmth_pairs', 'communion_pairs', 'evaluation_pairs'])]
    # df = df[df['task'].isin(['competent_pairs', 'agency_pairs'])]

    # Converting list of dimensions to a numpy array
    X = np.array(df['dimension'].tolist())
    print(X.shape)
    
    # elbow_methods(X)
    
    # cluster_group(X,df,2)
    # Perform K-means clustering with the optimal number of clusters
    from sklearn.metrics import pairwise_distances

# Perform K-means clustering with the optimal number of clusters if not done
    k_optimal = 2
    
    kmeans_opt = KMeans(n_clusters=k_optimal, random_state=42)
    clusters = kmeans_opt.fit_predict(X)
    df['cluster'] = clusters

    # Calculate the centroids
    centroids = kmeans_opt.cluster_centers_

    # Calculate the pairwise distances from every point to every centroid
    distances = pairwise_distances(X, centroids, metric='euclidean')

    # For each cluster, find the indices of the ten words that are closest to its centroid
    for i in range(k_optimal):
        # For each cluster, get the indices of the rows that belong to this cluster
        cluster_distances = distances[:, i]
        # Get the indices of the ten smallest distances
        indices_of_min_distances = np.argsort(cluster_distances)[:30]
        # Select the corresponding words
        closest_words = df.iloc[indices_of_min_distances]['rp_word_0'].values
        print(f"Top 10 words contributing to cluster {i}:")
        print(closest_words)
    
