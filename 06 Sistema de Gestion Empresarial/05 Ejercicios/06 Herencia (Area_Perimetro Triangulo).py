import math
class Poligono:
    def __init__(self, num_lados):
        if num_lados < 3:
            raise ValueError("Un polígono debe tener al menos 3 lados.")
        self.lados = [0] * num_lados
    def darlados(self):
        for i in range(len(self.lados)):
            self.lados[i] = float(input(f"Ingrese el valor del lado {i + 1}: "))
    def verlados(self):
        for i, lado in enumerate(self.lados, 1):
            print(f"Lado {i}: {lado}")
class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)
    def area(self):
        s = sum(self.lados) / 2
        area = math.sqrt(s * (s - self.lados[0]) * (s - self.lados[1]) * (s - self.lados[2]))
        print("Área del triángulo: ",area)
    def perimetro(self):
        perimetro = sum(self.lados)
        print(f"Perímetro del triángulo: ",perimetro)
triangulo1 = Triangulo()
triangulo2 = Triangulo()
print("Ingrese los lados del primer triángulo:")
triangulo1.darlados()
print("\nLados del primer triángulo:")
triangulo1.verlados()
print("\nIngrese los lados del segundo triángulo:")
triangulo2.darlados()
print("\nLados del segundo triángulo:")
triangulo2.verlados()
triangulo1.area()
triangulo1.perimetro()
triangulo2.area()
triangulo2.perimetro()
