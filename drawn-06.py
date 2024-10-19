import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

matrix = np.random.rand(10, 10)
plt.figure(figsize=(10, 8))
sns.heatmap(matrix, annot=True, fmt=".2f", cmap="coolwarm",
cbar=True)
plt.title("Artistic Heatmap of Random 10x10 Matrix")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
