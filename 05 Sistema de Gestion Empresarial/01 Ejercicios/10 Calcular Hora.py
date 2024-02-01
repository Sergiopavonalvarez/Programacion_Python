

durmedia=15
horaSalida=input("Introduce la hora de salida: ")
minSalida=input("Introduce los minutos de salida: ")
horaLlegada=input("Introduce la hora de llegada: ")
minLlegada=input("Introdduce el minuto de llegada: ")
reduccionporcentaje=15
tiempoTotal=(horaLlegada * 60 + minLlegada) - (horaSalida * 60 + minSalida)
reduccion=tiempoTotal*reduccionporcentaje/100

print("Duracion inicial: ",tiempoTotal, " minutos")
print("Duracion del viaje: ",tiempoTotal-reduccion," minutos")


