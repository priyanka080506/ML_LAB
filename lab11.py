import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)

print("Transformed Data:")
print(X_lda)

# Plot
plt.scatter(X_lda[:,0], X_lda[:,1], c=y)
plt.title("Linear Discriminant Analysis (LDA)")
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.show()
