# Crea una aplicación que pida un número y calcule su factorial (El factorial de
# un número es el producto de todos los enteros entre 1 y el propio número y se
# representa por el número seguido de un signo de exclamación.
# Por ejemplo 5! = 1x2x3x4x5=120)

resultado = 1
num = int(input("Ingrese el factorial: "))
contador = 2

while contador <= num:
    resultado *= contador
    contador += 1


resultado1 = 1
num1 = int(input("Ingrese el factorial: "))

for i in range(1,num1+1):
    resultado1 *= i
print("Con el bucle for", resultado1)

print("Con el bucle while ", resultado)

# Crea una aplicación que permita adivinar un número. La aplicación genera un
# número aleatorio del 1 al 100. A continuación va pidiendo números y va
# respondiendo si el número a adivinar es mayor o menor que el introducido,
# además de los intentos que te quedan (tienes 10 intentos para acertarlo).
# El programa termina cuando se acierta el número (además te dice en cuantos
# intentos lo has acertado), si se llega al limite de intentos te muestra el
# número que había generado.

import random
intentos = 10;
num_secreto  =  random.randint(1,100);

while intentos > 0:
    num_ingresado = int(input("Adivine el numero (de 1 a 100):"))
    print(num_secreto)
    if num_ingresado == num_secreto:
        print("Correcto")
        break
    if num_ingresado < num_secreto:
        print("mayor")
    if num_ingresado > num_secreto:
        print("menor")
    intentos -= 1
print("fin")

# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
# y la media de todos los números introducidos.

suma = 0
media = 0
contador = 0
numeroIntroducir = int(input("Ingrese numero"))

while numeroIntroducir != 0:
    suma += numeroIntroducir
    contador += 1
    numeroIntroducir = int(input("Ingrese numero o 0 para salir"))
media = suma / contador
print("La media es: ", media, " y la suma es :", suma)

# Realizar un algoritmo que pida números (se pedir� por teclado la cantidad de
# números a introducir). El programa debe informar de cuantos números introducidos
# son mayores que 0, menores que 0 e iguales a 0.

contPos = 0
contNeg = 0
contCero = 0
cantidad = int(input("Cuantos numeros vas a ingresar"))

for i in range(1, cantidad + 1, 1):
    numeroIngresar = int(input("Ingrese el numero pra saber si es + o -, "))
    if numeroIngresar > 0:
        contPos += 1
    if numeroIngresar < 0:
        contNeg += 1
    if numeroIngresar == 0:
        contCero += 1
print("La cantidad de numeros + es: ", contPos)
print("La cantidad de numeros - es: ", contNeg)
print("La cantidad de numeros 0 es: ", contCero)


contPos1 = 0
contNeg1 = 0
contCero1 = 0
cantidad1 = int(input("Cuantos numeros vas a ingresar"))

while cantidad1 > 0:
    numeroIngresar1 = int(input("Ingrese el numero pra saber si es + o -, "))
    if numeroIngresar1 > 0:
        contPos1 += 1
        cantidad1 -= 1
    if numeroIngresar1 < 0:
        contNeg1 += 1
        cantidad1 -= 1
    if numeroIngresar1 == 0:
        contCero1 += 1
        cantidad1 -= 1
print("La cantidad de numeros + es: ", contPos1)
print("La cantidad de numeros - es: ", contNeg1)
print("La cantidad de numeros 0 es: ", contCero1)

# Escribir un programa que imprima todos los números pares entre dos números que
# se le pidan al usuario.

numi1 = int(input("Ingrese numero"))
numi2 = int(input("Ingrese numero"))

for i in range(numi1, numi2 + 1):
    if i % 2 == 0:
        print(i)

# Realizar una algoritmo que muestre la tabla de multiplicar de un número
# introducido por teclado.

tabla = int(input("Ingrese el numero la tabla: "))

for i in range(1, 11):
    resultad = i * tabla
    print(resultad)

