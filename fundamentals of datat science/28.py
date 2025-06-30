from sklearn.cluster import KMeans
import numpy as np

X = np.array([
    [200, 2],
    [300, 3],
    [800, 7],
    [850, 6],
    [400, 4]
])

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

new_customer = np.array([[500, 4]])
cluster = kmeans.predict(new_customer)

print("Assigned customer segment:", cluster[0])
print("Cluster Centers:\n", kmeans.cluster_centers_)
