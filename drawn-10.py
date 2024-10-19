import matplotlib.pyplot as plt
import numpy as np

# Data for the populations
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
populations = [50, 30, 80, 60, 40]  # in millions

# Creating a bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(countries, populations, color=['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#673AB7'])

# Adding a title and labels
plt.title('Population Comparison of Five Countries', fontsize=16, fontweight='bold')
plt.xlabel('Countries', fontsize=14)
plt.ylabel('Population (in millions)', fontsize=14)

# Adding data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval}M', ha='center', va='bottom', fontsize=12)

# Customizing the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Displaying the bar chart
plt.tight_layout()  # Adjusts layout to prevent clipping of ylabel
plt.show()

