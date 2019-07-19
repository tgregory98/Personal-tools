import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = []
Y = []
Z = []
for x in np.arange(-1, 1, 0.1):
    for y in np.arange(-1, 1, 0.1):
        z = x**2 + y**2
        X.append(x)
        Y.append(y)
        Z.append(z)
ax.scatter(X, Y, Z)

plt.show()
