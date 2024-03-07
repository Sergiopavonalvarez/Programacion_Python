

mares1=("Mediterraneo","Cantabrico","Baltico","Adriatico","Tirreno","Egeo")
mares2=("rojo","muerto","caspio","negro","arabico","sulu")
mares=mares1+mares2

print("Numero d eposiciones de la lista mares1: ",len(mares1))
print("Contenido mares1: ")
for i in mares1:
    print(i)
print("Numero d eposiciones de la lista mares2: ",len(mares2))
print("Contenido mares2: ")
for r in mares2:
    print(r)
print("Numero d eposiciones de la lista mares: ",len(mares))
print("Contenido mares: ")
for t in mares2:
    print(t)

print("Tres primeros de mares1: ")
for i in mares1[:3]:
    print(i)

print("La posicion del mar egeo es: ",mares1.index("Egeo"))
print("Cuarta posición de mares2:", mares2[3])
print("Quinta posición de mares2:", mares2[4])
print("Sexta posición de mares2:", mares2[5])
print("La posicion del mar egeo en mares2 es: ",mares2.index("caspio"))
print("La posicion del mar egeo en mares es: ",mares.index("caspio"))