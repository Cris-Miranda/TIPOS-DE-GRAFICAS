from numpy import pi, arange, linspace
from matplotlib.pyplot import subplot, plot, show, grid, title

teta=arange(0, 3, 0.01) #Generamos los valres de cero
r= 2*pi * teta #Se calcular para cada valor de cero
subplot(111, polar = True) #Creamos la subgráfica polar
plot (r, teta, color = 'r', linewidth = 3) #Creamos la gráfica
grid(True) # Se añade la linea
title("Grafica polar ")
show()
 # La gráfica polar se obtine usando la instrucción plot pero usando componentes (radio vector)
 # y (angulo argumento), cualquiera de los dos o los dos pueden variar en un angulo determinado.