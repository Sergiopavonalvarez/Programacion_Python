from random import randint

class Array:
    def __init__(self, tamano, minimo, maximo):
        self.tamano = tamano
        self.minimo = minimo
        self.maximo = maximo
        self.numeros = [0] * tamano

    def rellenar(self):
        for i in range(self.tamano):
            self.numeros[i] = randint(self.minimo, self.maximo)

    def mostrar(self):
        for i in range(self.tamano):
            print(f"En la posición {i} se encuentra el número {self.numeros[i]}")

    def mayor(self):
        mayor = self.numeros[0]
        for i in range(1, self.tamano):
            if self.numeros[i] > mayor:
                mayor = self.numeros[i]
        print(f"El número mayor del array es {mayor}")

tamano = int(input("Introduce el tamaño del array: "))
minimo = int(input("Introduce el valor mínimo: "))
maximo = int(input("Introduce el valor máximo: "))
array = Array(tamano, minimo, maximo)
array.rellenar()
array.mostrar()
array.mayor()



