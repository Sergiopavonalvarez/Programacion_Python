#Ejercicio1: rellenar una lista con 10 nums aleatorios
import random
lista = []

for i in range(1, 11):
    numeros = random.randint(1, 100)
    lista.append(numeros)
print(lista)

for i in lista:
    print(i, " ", i ** 2, " ", i**3)

#Ejercicio2: Añadir 5 notas y que muestre la media, la nota mas alta y la menos

listaNotas = []
for i in range(0, 5):
    notas = int(input("Ingrese las notas "))
    listaNotas.append(notas)

suma = sum(listaNotas) / len(listaNotas)
print(suma)
print(max(listaNotas))
print(min(listaNotas))

#Ejercicio3: se introduciran los nombres y las edades de los niños se terminara cuando el programa meta un astrisco

listaNombres1 = []
listaEdades = []


while True:
    nombre = input("Ingrese el nombre")
    if nombre != "*":
        listaNombres1.append(nombre)
    else:
        break
    edad = int(input("Ingrese la edad"))
    listaEdades.append(edad)

for nombre, edad in zip(listaNombres1, listaEdades):
    print(nombre, edad)

#Ejercicio4

listaNums = [[1,2,3]]

