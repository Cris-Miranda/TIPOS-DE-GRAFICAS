from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import title, figure, show, plot, legend
from numpy import linspace, sin, cos, pi
a = figure()
a.gca(projection = '3d')
teta = linspace(-4 * pi, 4 * pi, 100)
r = linspace(0, pi, 100)
z = r
x = r * sin(teta)
y = r * cos(teta)
plot(x, y, z, label = 'Curva Parametrica')
legend()
show()

# La grafica paramétrica se forma con la instruccion plot pero pero previamente tenemos que indicar
# que será gráficada tridimensional con la instruccion Axes 3D que se importa de la biblioteca 
# mpl_toolkids.mplot3d