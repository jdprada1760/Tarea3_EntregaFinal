from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys

#radio de la esfera a escapar
r = 100
#numero de fotones a analizar
n = int(sys.argv[1])
#variable de iteracion de los fotones
p = 0
#guarda el numero de pasos requerido por cada foton para salir del sol
d = np.zeros(n)
for p in range(n):
    #guarda la posicion actual de un foton inicia en cualquier parte 
    actual = 1 - 2*np.random.random(3)
    actual = r*np.random.random(1)*actual/np.linalg.norm(actual)
    #contador del numero de pasos
    npasos = 0
    #iteracion hasta salir del sol
    while np.sqrt(actual[0]**2 + actual[1]**2 + actual[2]**2) < r:
        #vector aleatorio
        x = 1 - 2*np.random.random(3)
        #normalizacion del vector
        x = x/np.linalg.norm(x)
        #actualiza el vector posicion y el numero de pasos
        actual += x
        npasos += 1
    #guarda el numero de pasos requerido por el foton
    d[p] = npasos

i = 0
if(n >= 100):
    numBarras = int( n/10 )
else:
    numBarras = 10

min = int(np.min(d))
max = int(np.max(d))

plt.hist(d, bins=[min + i*max/(numBarras) for i in range(numBarras)])
filename = 'histo_difusion_solar_homogenea_n'
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()
