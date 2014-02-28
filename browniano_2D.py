from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys, string, os

n = int(sys.argv[1])
d = np.zeros(n+1)
actual = np.zeros(2)
for i in range(1, n+1):
    x = 1 - 2*np.random.random(2)
    x = x/np.linalg.norm(x)
    actual += x
    d[i] = np.linalg.norm(actual)

e = range(n+1)
fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("Numero de pasos")
ax.set_ylabel("Distancia del origen")
ax.set_title("Movimiento Browniano")
plt.plot(e, d, 'r', zorder=1, lw=1)
filename = 'browniano_2D_n'
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()

