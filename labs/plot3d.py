#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#necessários pra fazer a animação funcionar no ambiente do google colab
#capture faz com que o notebook não tente plotar a animação quando a variável é definida
#%%capture
#%matplotlib inline
#from IPython.display import HTML

#imports básicos
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


def colorizer(x, y):
    r = min(1, 1-y/3)
    g = min(1, 1+y/3)
    b = 1/4 + x/16
    return (abs(r), abs(g), abs(b))

#faz uma interpolação de transformações para criar o efeito da animação
def stepwise_transform(a, points, nsteps=30):
    transgrid = np.zeros((nsteps+1,) + np.shape(points))
    for j in range(nsteps+1):
      intermediate = np.eye(3) + j/nsteps*(a - np.eye(3))
      transgrid[j] = np.dot(intermediate, points)
    return transgrid

np.random.seed(19680801)
random_numbers=False

if __name__ == '__main__':
    #### A matriz
    a = np.column_stack([[-2,0,0],[2,2,0],[0,0,0]]) # Matriz utilizada para fazer a transformação

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if random_numbers:
        #quantidade de pontos aleatórios gerados
        n = 100
        #listas no formato: ["cor", "formato do ponto", valor minimo, valor máximo]
        for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
            xs = randrange(n, 23, 32)
            ys = randrange(n, 0, 100)
            zs = randrange(n, zlow, zhigh)
            ax.scatter(xs, ys, zs, c=c, marker=m)

    else:
        #usando uma estrutura parescida com a do laboratório
        #Define dados de entrada
        xvals = np.linspace(-3, 3,5) # Define os pontos que vão ser transformados
        yvals = np.linspace(-3, 3,5) # Define os pontos que vão ser transformados
        zvals = np.linspace(-3, 3,5) # Define os pontos que vão ser transformados
        xyzgrid = np.column_stack([[x, y, z] for x in xvals for y in yvals for z in zvals])

        #mapeia as cores para coordenadas usando a função colorizer acima
        colors = list(map(colorizer, xyzgrid[0], xyzgrid[1]))

        #cria as transformações que serão animadas
        steps = 30
        transform = stepwise_transform(a, xyzgrid, nsteps=steps)

        def animate(i):
            transform_scat = list(zip(*transform[i]))
            pts.set_offsets(transform_scat)


        pts=ax.scatter(xyzgrid[0],xyzgrid[1],xyzgrid[2], c = colors)

    #print points
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
