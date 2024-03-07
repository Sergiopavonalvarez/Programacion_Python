#Ejercicio1: Averiguar si la cadena y la subcadena empiezan por la misma letra
cadena = input("Ingrese una cadena ")
subCadena = input("Ingrese una subcadena ")

if cadena.startswith(subCadena):
    print("True")
else:
    print("false")

#Ejercicio2: Pide una cadena por teclado y una letra y muestra cuantas veces aparece en esa cadena

cad = input("Ingrese una cadena ")
letraBuscar = input("Ingrese un caracter a buscar en la cadena ")

if len(letraBuscar) > 1:
    print("introduce un caracter no varios")
else:
    print(cad)
    print(cad.count(letraBuscar))

#Ejercicio4: Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
# realiza un programa que cuente cuantas palabras tiene.

cadena1 = input("Ingrese una cadena")
cadena2 = cadena1.split(" ")
print(cadena2)
print(len(cadena2))

#Ejericico5: Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

nombre = input("Ingrese una cadena")
cadena22 = nombre.split(" ")
cadena33 = ""
cadena34 = ""

if len(cadena22) > 0:
    cadena33 = cadena22[0]
if len(cadena22) > 1:
    cadena34 = cadena22[1]
print(cadena33[0], cadena34[0])
