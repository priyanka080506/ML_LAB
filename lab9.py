import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

file = input("Enter dataset file: ")

data = pd.read_csv(file)

X = data.iloc[:, :2]   # First two columns

# Single Linkage
single = linkage(X, method='single')

plt.figure(figsize=(8,4))
dendrogram(single)
plt.title("Single Linkage")
plt.show()

# Complete Linkage
complete = linkage(X, method='complete')

plt.figure(figsize=(8,4))
dendrogram(complete)
plt.title("Complete Linkage")
plt.show()
