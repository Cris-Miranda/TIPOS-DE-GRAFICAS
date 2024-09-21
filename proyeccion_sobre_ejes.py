# En ocaciones deseamos realizar una proyeccion sobre el planoo x, y de una superficie
# tridimencional. Esto lo hacemos gráficando la superficie y el contorno lo ue podemos hacer con
# plot_suface y contourf

from pylab import arange, sin, sqrt, meshgrid, figure, cm  
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import show
 
fig = figure()
ax = Axes3D(fig)
X = arange(-4, 4, 0.25)
Y = arange(-4, 4, 0.25)
X, Y = meshgrid(X, Y)

R = sqrt( abs(X**3 + Y**2))
Z = sin(R)

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.hot)
ax.contourf(X, Y, Z, zdir = 'z', offset = -2, cmap = cm.hot)
ax.set_zlim(-2, 2)
show()