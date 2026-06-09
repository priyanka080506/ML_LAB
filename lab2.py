import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter Plot
plt.scatter(x, y)
plt.show()

# Box Plot
plt.boxplot([x, y])
plt.show()

# Heatmap
data = np.random.rand(5, 5)
sns.heatmap(data)
plt.show()

# Contour Plot
X, Y = np.meshgrid(np.arange(-5, 5, 0.5), np.arange(-5, 5, 0.5))
Z = X**2 + Y**2
plt.contour(X, Y, Z)
plt.show()

# 3D Surface Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()
