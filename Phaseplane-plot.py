import math as m
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.05)
y = np.arange(-2, 2, 0.05)
X, Y = np.meshgrid(x, y)
U = Y
V = (Y * (2 * Y - 5) - X * (1 - X)) / (1 - X)
speed = np.sqrt(U**2 + V**2)
lw = 2 * speed / speed.max() + 0.2
plt.streamplot(X, Y, U, V, density=2, linewidth=lw, color=U, cmap='cool')

plt.show()
