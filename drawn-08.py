import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 4 * np.pi, 1000)
r = theta
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color='purple', linewidth=2)
ax.set_title('Polar Plot of r = θ', va='bottom')
plt.show()
