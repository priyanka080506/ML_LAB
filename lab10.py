import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Transformed Data:")
print(X_pca)

# Plot
plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.title("Principal Component Analysis (PCA)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
