

mares1=("Mediterraneo","Cantabrico","Baltico","Adriatico","Tirreno","Egeo")
mares2=("rojo","muerto","caspio","negro","arabico","sulu")
mares=mares1+mares2
mares = list(mares)

mares[10]="del norte"
mares[11]="alboran"
print("Lista mares: ")
for i in mares:
    print(i)
print("*****************************+")
mares.append("Baltico")

print("Lista mares con baltico: ")
for i in mares:
    print(i)

print("*****************************+")
mares.pop(4)

print("Lista mares sin el cuarto elemento: ")
for i in mares:
    print(i)

print("Longitud de la lista mares: ",len(mares))
print("*****************************+")
valores_repetidos = set()
valores_unicos = set()

for mar in mares:
    if mar in valores_unicos:
        valores_repetidos.add(mar)
    else:
        valores_unicos.add(mar)
print("Valores repetidos en la lista mares:")
for valor in valores_repetidos:
    print(valor)
print("*****************************+")
mar1=mares[2]
print("mar1: ",mar1)
mares.pop(2)
print("*****************************+")
print("Longitud de la lista mares: ",len(mares))
mar2=mares[10]
print("mar2: ",mar2)
mares.pop(10)
print("*****************************+")
