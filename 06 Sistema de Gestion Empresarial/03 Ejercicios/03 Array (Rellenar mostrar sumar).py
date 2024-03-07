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
    def suma(self):
        suma = 0
        for i in range(self.tamano):
            suma += self.numeros[i]
        print(f"La suma de los números del array es {suma}")
tamano = int(input("Introduce el tamaño del array: "))
minimo = int(input("Introduce el valor mínimo: "))
maximo = int(input("Introduce el valor máximo: "))
array = Array(tamano, minimo, maximo)
array.rellenar()
array.mostrar()
array.suma()
