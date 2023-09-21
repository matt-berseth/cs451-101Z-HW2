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

    # TODO(Task #1): Run k-means clustering over the X data. Use an elbow plot
    # to determine the best value for K.
    # adapt from here: https://github.com/matt-berseth/cs451-101Z-MODULE2/blob/main/kmeans_iris_elbow.py


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()
