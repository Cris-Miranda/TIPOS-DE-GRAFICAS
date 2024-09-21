from matplotlib import cm
from matplotlib.pyplot import plot, figure, show, title
from numpy import arange, sqrt, sin, meshgrid

fig = figure()
ax = fig.gca(projection = '3d')

X = arange(-5, 5, 0.25)
Y = arange(-5, 5, 0.25)
X, Y = meshgrid(X, Y)
Z = sin( sqrt(X**2 + Y**2))
A = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.coolwarm)
title('Grafica de Superficie')
show() 