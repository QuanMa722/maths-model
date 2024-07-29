# -*- coding: utf-8 -*-

from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

silhouette_scores = []
K_max = 15
for k in range(2, K_max):

    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(score)

best_k_num = list(range(2, K_max))[silhouette_scores.index(max(silhouette_scores))]
print("-" * 20)
print(f"The best k-num: {best_k_num}")
print("-" * 20)

plt.plot(range(2, K_max), silhouette_scores, marker='o')
plt.title('Silhouette Coefficients')
plt.xlabel('Number of clusters')
plt.ylabel('Average silhouette score')
plt.grid()

kmeans = KMeans(n_clusters=best_k_num)
kmeans.fit(X)

labels = kmeans.predict(X)

plt.figure(figsize=(8, 6))
for i in range(4):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], cmap='viridis', marker='o', label=f'Cluster {i+1}', edgecolor='k')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200, label='Centroids')

plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

