from matplotlib.pyplot import title, hist, show
from numpy.random import normal
numeros_gaussianos = normal(size = 1000)
hist(numeros_gaussianos)
title("Grafica de Historgrama")
show()

# Codigo grafica stem
from matplotlib.pyplot import stem, show
from numpy import pi, arange 
stem( arange(-pi, pi))
show()