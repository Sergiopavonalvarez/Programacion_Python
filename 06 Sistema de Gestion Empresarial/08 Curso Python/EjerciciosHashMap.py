#Ejercicio1: Crear diccionario con las frutas y su precio
hashmap ={}
while True:
    fruta = input("Ingrese la fruta ")
    if fruta == "*":
        break
    precio = int(input("ingrese el precio de la fruta: "))
    hashmap[fruta] = precio

for key, value in hashmap.items():
    print(key, value)

ticket = sum(hashmap.values())
print("El precio total de tu ticket es: ", ticket, "€")


