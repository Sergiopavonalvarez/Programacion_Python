#Se pueden guardar varios elementos
li = [1,"hola", True]
# Recorrer normal
lista = [1, 2, 3, 4, 5, 6]
for i in lista:
    print(i)

print(lista[::-1])

#Para recorrer 2 listas de diferente estilo se pone en el for la 1 lista y despues la 2 y con
#el metodo ZIP las unimos

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = ["a", "b", "c", "d", "e", "f"]

for num, letra in zip(lista1, lista2):
    print(num, ":", letra)
#Concatenar listas con el mas y duplicarla * 2
listas1 = [1, 2, 3, 4, 5, 6] + [7, 8, 9]
print(listas1)

#Esto da el ultimo elemento
print(listas1[-1])

#para obtener varias posiciones
print(listas1[2:5])

#Calcula el maximo valor de la lista
print(max(listas1))

#Calcular el minimo de la lista
print(min(listas1))

#Sumar los valores de la lista
print(sum(listas1))

#ordenar la lista de menor a mayor
print(sorted(listas1))
#Al reves
print(sorted(listas1, reverse=True))

#Para una lista bidimensional e imprimirla con un doble for
listaBidi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in listaBidi:
    for j in i:
        print(j)

#Los metodos de las listas modifican las listas no es como las cadenas que solo la muestran modificadas
#cuando igualas una lista a otra y las modificas se modifican las 2 Ej.
listi = [1, 2, 3]
listi2 = listi
listi.append(100)
print(listi, "\n", listi2)

#para que te devuelva otra lista para poder modificar 1 en concreto.

listi1 = [1, 2, 3]
listi3 = listi1[:]
listi1.append(200)
print(listi1, "\n", listi3)

#Metodos mas comunes de las listas con el .append ya utilizado mas arriba y añadir en una posicion determinada
#metodos para eliminar
numerosLista = [1, 2, 3, 2]
numerosLista.insert(2, 200)
print(numerosLista)
#pop devuelve el ultimo elemento y lo quita si le metes en parametros el numero a eliminar de la lista
numerosLista.pop()
print(numerosLista)
#Este metodo elimina todos los elementos que sean igual al paramtro en este caso los que sean un 2
numerosLista.remove(2)
print(numerosLista)

#Metodo extends para añadir otra lista y unirlas
listaa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaaa = [1, 2, 3]
listaa.extend(listaaa)
print(listaa)

#Metodos de busqueda este cuenta cuantas apariciones tiene dicho numero
numerosLista1 = [1, 2, 3, 4, 5, 6, 5, 8, 5]
print(numerosLista1.count(5))

#Este metodo me dice en numero aparece la primera posicion de lo que busquemos
print(numerosLista1.index(5))

#Metodo para quitar los repetidos de unas listas con el set
# Lista con elementos duplicados
mi_lista = [1, 2, 3, 1, 2, 4, 5, 6, 5]

# Convertir la lista a un conjunto para eliminar duplicados
conjunto_sin_duplicados = set(mi_lista)

# Convertir el conjunto de nuevo a una lista
lista_sin_duplicados = list(conjunto_sin_duplicados)

# Imprimir la lista sin elementos duplicados
print(lista_sin_duplicados)


