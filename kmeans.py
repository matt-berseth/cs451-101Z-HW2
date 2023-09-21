import logging
import os
import warnings

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


def main():
    logging.info("Loading data ...")
    X = np.loadtxt("X.txt")
    logging.info(f"X.shape: {X.shape} ...")

    # TODO(Task #2): Using the value of 'k' that was identified using the 
    # elbow plot, cluster the data. Plot the data and cluster centers.

    # TODO: fill this in with the right 'k' value
    n_clusters=1
    kmeans = KMeans(n_clusters=n_clusters) 
    
    # assign the cluster id to each data point
    cluster_labels = kmeans.fit_predict(X)
    logging.info(f"Cluster centroids: {kmeans.cluster_centers_}")
    logging.info(f"WCSS: {kmeans.inertia_}")

    # Plot current state
    plt.figure(figsize=(6, 6))
    plt.xlabel("X0")
    plt.ylabel("X1")
    
    # plot the cluster centroids
    # TODO: the list of colors should match the number of 'k'
    # i.e. if you have n_clusters is '5', you need to have exactly 5 colors listed
    colors = ["blue", "orange", "green", "purple", "pink"]

    # plot the points
    for i in range(n_clusters):
        # TODO: adapt from here: https://github.com/matt-berseth/cs451-101Z-MODULE2/blob/main/kmeans_iris.py#L41
        pass

    # plot the cluster centroids:
    # TODO: adapt from here: https://github.com/matt-berseth/cs451-101Z-MODULE2/blob/main/kmeans_iris.py#L38

    # save the figure
    plt.savefig(f"kmeans.png")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()
