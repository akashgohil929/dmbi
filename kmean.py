import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = pd.read_csv("expt7.csv")
try:
    num_clusters = int(input("Enter the number of clusters: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data)
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
data["Cluster"] = labels
plt.scatter(data["a"], data["b"], c=labels, cmap="rainbow")
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c="black",
marker="x", s=100, label="Centroids")
plt.xlabel("a")
plt.ylabel("b")
plt.title(f"K Means Clustering with {num_clusters} clusters")
plt.legend()
plt.show()