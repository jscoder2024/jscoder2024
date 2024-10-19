import numpy as np
import matplotlib.pyplot as plt

#Generating random height data
heights = np.random.normal(loc=170, scale=10, size=50)

#Creating the box plot
plt.figure(figsize=(10,6))
plt.boxplot(heights, patch_artist=True,
    boxprops=dict(facecolor='lightblue', color='blue'),
    medianprops=dict(color='red', linewidth=2),
    whiskerprops=dict(color='blue'),
    capprops=dict(color='blue'),
    flierprops=dict(marker='o', color='red', alpha=0.5))
plt.title('Distribution of Heights')
plt.ylabel('Height (cm)')
plt.show()
