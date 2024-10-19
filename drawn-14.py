import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random weights data
weights = np.random.normal(70, 10, 50)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a box plot
sns.boxplot(weights, ax=ax, color='skyblue')

# Add title and labels
ax.set_title('Distribution of Weights of 50 People', fontsize=16,
weight='bold')
ax.set_xlabel('Weights (kg)', fontsize=14)

# Customize the appearance
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f7f7f7')

# Show the plot
plt.show()

