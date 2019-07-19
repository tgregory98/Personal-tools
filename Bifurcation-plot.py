import math as m
import numpy as np
import matplotlib.pyplot as plt

R1 = []
U1 = []
R2 = []
U2 = []

D = np.arange(3, 4, 0.000001)

def func(r, u):
    return r * u * (1 - u)

for r in D:
    u = np.random.random()
    for n in range(1000):
        u = func(r, u)
    if abs(u - func(r, u)) < 0.01:
        R1.append(r)
        U1.append(u)
    else:
        R2.append(r)
        U2.append(u)

for r in D:  # Checking stability of zero-steady state
    u = 0.01
    for n in range(1000):
        u = func(r, u)
    if abs(u) < 0.01:
        R1.append(r)
        U1.append(0)
    else:
        R2.append(r)
        U2.append(0)

plt.scatter(R1, U1, s=0.05, c='gray')
plt.scatter(R2, U2, s=0.05, c='deepskyblue')

plt.xlabel('r')
plt.ylabel('u')
plt.show()
