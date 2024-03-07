'''Dado un array de enteros v, escribir un método de clase que:
a) Dadas dos posiciones, izq y der, del array, 0≤izq≤der≤v.length-1, multiplique por 2 el valor de los elementos del array situados entre dichas posiciones.
b) Dadas dos posiciones, izq y der, del array, 0≤izq≤der≤v.length-1, invierta todos los elementos del array situados entre dichas posiciones, esto es, al finalizar la ejecución del método el array contendrá en su posición izq el elemento que inicialmente ocupaba la posición der, en su posición izq+1 el elemento que inicialmente ocupaba la posición der-1 y así sucesivamente.
c ) Cuente el número de elementos impares en posiciones pares.
d) Cuente el número de elementos que son menores que un valor dado x hasta una posición n del array.
e) Determine si dicho array está ordenado ascendentemente.
f) Determine la posición, si existe, de la primera subsecuencia del array que comprenda, al menos tres números consecutivos en posiciones consecutivas del array.
g) Dado un entero x no negativo, determine si la suma de los elementos del array es mayor que x, recorriendo el mínimo imprescindible de elementos.
h) Dados dos valores enteros x y n, devuelva la posición de la primera subsecuencia de n enteros mayores que x, o devuelva -1 en caso de que no exista dicha subsecuencia en el array.
i) Obtenga la posición del último elemento impar del array, si existe.
j) Sume los elementos que aparecen tras el primer impar, si existe.
NOTA: Crear todas las opciones del ejercicio 7 en una única clase, donde la función principal contendrá un menú con todas las opciones necesarias para ejecutar los 10 métodos (a-j).'''
import random

class Array:
    def __init__(self, tamano, minimo, maximo):
        self.tamano = tamano
        self.minimo = minimo
        self.maximo = maximo
        self.numeros = [0] * tamano

    def rellenar(self):
        for i in range(self.tamano):
            self.numeros[i] = random.randint(self.minimo, self.maximo)

    def mostrar(self):
        for i in range(self.tamano):
            print(f"En la posición {i} se encuentra el número {self.numeros[i]}")

    def multiplicar(self, izq, der):
        for i in range(izq, der + 1):
            self.numeros[i] *= 2

    def invertir(self, izq, der):
        while izq < der:
            self.numeros[izq], self.numeros[der] = self.numeros[der], self.numeros[izq]
            izq += 1
            der -= 1

    def impares_pares(self):
        impares = 0
        for i in range(0, self.tamano, 2):
            if self.numeros[i] % 2 != 0:
                impares += 1
        print(f"El número de elementos impares en posiciones pares es {impares}")

    def menores(self, x, n):
        menores = 0
        for i in range(n):
            if self.numeros[i] < x:
                menores += 1
        print(f"El número de elementos menores que {x} hasta la posición {n} es {menores}")

    def ordenado(self):
        for i in range(1, self.tamano):
            if self.numeros[i] < self.numeros[i - 1]:
                print("El array no está ordenado ascendentemente")
                return
        print("El array está ordenado ascendentemente")

    def subsecuencia(self):
        for i in range(self.tamano - 2):
            if self.numeros[i] == self.numeros[i + 1] - 1 == self.numeros[i + 2] - 2:
                print(f"La primera subsecuencia de tres números consecutivos comienza en la posición {i}")
                return
        print("No existe ninguna subsecuencia de tres números consecutivos")

    def suma(self, x):
        suma = 0
        for i in range(self.tamano):
            suma += self.numeros[i]
            if suma > x:
                print(f"La suma de los elementos hasta la posición {i} es mayor que {x}")
                return
        print(f"La suma de todos los elementos es {suma}")

    def subsecuencia_n(self, x, n):
        for i in range(self.tamano - n + 1):
            if self.numeros[i] > x:
                print(f"La primera subsecuencia de {n} números mayores que {x} comienza en la posición {i}")
                return
        print(f"No existe ninguna subsecuencia de {n} números mayores que {x}")

    def ultimo_impar(self):
        for i in range(self.tamano - 1, -1, -1):
            if self.numeros[i] % 2 != 0:
                print(f"El último número impar se encuentra en la posición {i}")
                return
        print("No hay ningún número impar")

    def suma_tras_impar(self):
        for i in range(self.tamano):
            if self.numeros[i] % 2 != 0:
                suma = sum(self.numeros[i + 1:])
                print(f"La suma de los elementos que aparecen tras el primer impar es {suma}")
                return
        print("No hay ningún número impar")

tamano = int(input("Introduce el tamaño del array: "))
minimo = int(input("Introduce el valor mínimo: "))
maximo = int(input("Introduce el valor máximo: "))
array = Array(tamano, minimo, maximo)
array.rellenar()
array.mostrar()
opcion = input("Elige una opción (a-j): ")
if opcion == "a":
    izq = int(input("Introduce la posición izquierda: "))
    der = int(input("Introduce la posición derecha: "))
    array.multiplicar(izq, der)
    array.mostrar()
elif opcion == "b":
    izq = int(input("Introduce la posición izquierda: "))
    der = int(input("Introduce la posición derecha: "))
    array.invertir(izq, der)
    array.mostrar()
elif opcion == "c":
    array.impares_pares()
elif opcion == "d":
    x = int(input("Introduce un valor: "))
    n = int(input("Introduce una posición: "))
    array.menores(x, n)
elif opcion == "e":
    array.ordenado()
elif opcion == "f":
    array.subsecuencia()
elif opcion == "g":
    x = int(input("Introduce un valor: "))
    array.suma(x)
elif opcion == "h":
    x = int(input("Introduce un valor: "))
    n = int(input("Introduce un número: "))
    array.subsecuencia_n(x, n)
elif opcion == "i":
    array.ultimo_impar()
elif opcion == "j":
    array.suma_tras_impar()
else:
    print("Opción incorrecta")
print("Fin del programa")




