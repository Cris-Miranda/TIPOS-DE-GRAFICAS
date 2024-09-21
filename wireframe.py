from matplotlib import cm
from matplotlib.pyplot import plot, figure, show, title
from numpy import arange, sqrt, sin, meshgrid

fig = figure()
ax = fig.gca(projection = '3d')

X = arange(-5, 5, 0.50)
Y = arange(-5, 5, 0.50)
X, Y = meshgrid(X, Y)
Z = sin( sqrt(X**2 + Y**2))
A = ax.plot_wireframe(X, Y, Z)
title('Grafica de Superficie de Alambre')
show() 