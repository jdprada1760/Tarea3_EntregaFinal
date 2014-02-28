from __future__ import division
import numpy as np
import matplotlib.pyplot as plt 
import sys

#numero de iteraciones
k = int(sys.argv[1])
#resolucion
tam = 1024

#matriz que guarda el conjunto de mandelbrot, y la velocidad de convergencia del resto de puntos
a = np.zeros((tam, tam))
x = y = 0

#intervalo del eje real distribuido uniformemente en del intervalo (-2, 1)  de acuardo a la resolucion
Re = np.array([[ (-2 + 3*x/tam) for x in range(tam)] for y in range(tam)])
#intervalo del eje imaginario distribuido uniformemente en el intervalo (-1, 1) de acuerdo a la resolucion
x = y = 0
Im = np.array([[ (-1 + 2*y/tam) for x in range(tam)] for y in range(tam)])

x = 1
#matriz del plano complejo
c = Re + 1j*Im
#matriz de la sucesion de mandelbrot, empieza en z1 = c, n = 1
zn = Re + 1j*Im
#iteracion que calcula los siguientes terminos de la sucesion para los c que no divergen
for x in range(k):
    #indices de los c que no divergen
    conv = np.where( abs(zn) <= 2 )
    #siguiente termino de la sucesion
    zn[conv] = zn[conv]**2 + c[conv]
    #guarda la velocidad de divergencia, o si converge
    a[conv] += 1

#grafica
fig1 = plt.figure()
ax1 = plt.axes()
ax1.set_title("Mandelbrot Fractal")
plt.imshow( a , cmap=plt.cm.gist_stern)
filename = 'mandelbrot_n'
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()
