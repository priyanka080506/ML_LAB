import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

file = input("Enter dataset file: ")

data = pd.read_csv(file)

X = data.iloc[:, :2]   # First two columns

k = int(input("Enter number of clusters: "))

kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X)

print("Cluster Labels:")
print(clusters)

plt.scatter(X.iloc[:,0], X.iloc[:,1], c=clusters)
plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1],
            marker='X', s=200)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
