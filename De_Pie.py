from matplotlib.pyplot import figure, subplot, title, pie, show
figure(1, figsize= (6, 6)) #Hace figura cuadrada
fracs = [15, 30, 40, 5, 10]
pie(fracs, autopct = '%2.1i%%') #Ecribimos los porcentajes de la gráfica
title('Gráfica de pie')
show ()

# Esta gráfica se usa cuando queremos presentar un porcentaje  de los datos se forma con la intruccion pie