
from random import randint



enteros = [randint(1,100) for i in range(50)]

print("Lista de enteros: ",enteros)
print("****************************")
print("Numeros en la lista de enteros: ",len(enteros))
print("****************************")
multiplos37 = [i for i in enteros if i%3==0 or i%7==0]
print("Los multipos de la lista de enteros:",multiplos37)
print("****************************")
print("Numeros de multiplos de 37: ",len(multiplos37))
print("****************************")


repetidos = []
for i in multiplos37:
    if multiplos37.count(i) > 1 and i not in repetidos:
        repetidos.append(i)

print("Numeros repetidos de 37: ",repetidos)
print("****************************")


