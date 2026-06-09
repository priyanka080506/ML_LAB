import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

# AND Gate Data
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# Train Perceptron
p = Perceptron(max_iter=1000)
p.fit(X, y)

# Predictions
pred = p.predict(X)

print("Inputs:")
print(X)
print("Output:", pred)

# Plot
plt.scatter(X[:,0], X[:,1], c=pred, s=100)
plt.title("Single Layer Perceptron - AND Gate")
plt.xlabel("Input 1")
plt.ylabel("Input 2")
plt.show()
