import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.rand(5, 5)
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, fmt=".2f", cmap="viridis", cbar=True,
linewidths=.5, linecolor='white')
plt.title("Artistic Heatmap of 5x5 Matrix")
plt.show()
