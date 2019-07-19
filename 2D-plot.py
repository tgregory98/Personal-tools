import math as m
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []
for x in np.arange(0, 6.18, 0.01):
    y = m.sin(x / 2)**2
    X.append(x)
    Y.append(y)
plt.plot(X, Y)

plt.xlabel('theta')
plt.ylabel('sin^2(theta/2)')
plt.show()
