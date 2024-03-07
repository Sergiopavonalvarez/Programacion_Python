#HashMap

hashmap = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 'Miguel'}
print(type(hashmap))

print(hashmap)

#Recorrerlos
#Recorrerlo con clave-Valor
for key, value in hashmap.items():
    print(key, value)

#Recorrerlo con la clave
for key in hashmap.keys():
    print(key)

#Recorrerlo con el valor
for value in hashmap.values():
    print(value)