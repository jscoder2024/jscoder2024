import numpy as np
import matplotlib.pyplot as plt

## Generate random points within a unit circle
num_points = 500
angles = np.random.uniform(0, 2 * np.pi, num_points) # Random angles
radii = np.sqrt(np.random.uniform(0, 1, num_points)) # Random radii
x_points = radii * np.cos(angles)
y_points = radii * np.sin(angles)

## Plot the points
plt.figure(figsize=(8, 8))
plt.scatter(x_points, y_points, c='blue', alpha=0.6, edgecolors='w', s=80)
plt.title('Scatter Plot of Random Points in a Unit Circle')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
