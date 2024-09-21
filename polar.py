from numpy import pi, arange, linspace
from matplotlib.pyplot import subplot, plot, show, grid, title

tetat=range(0, 3, 0.01) #Generamos los valroes de cero
r= 2*pi * teta #Se calcula r para cada valor de cero
subplot(111, polar = true) #Creamo la subgráfica polar
plot (r, teta, color = 'r', linewidth = 3) #Creamos la gráfica