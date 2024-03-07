import math

base=float(input("Introduce la base: "))
altura=float(input("Introduce la altura: "))

area=(base*altura)/2
hipotenusa = math.sqrt(base**2 + altura**2)
perimetro = base + altura + hipotenusa
print("Área: ", area)
print("Perímetro: ", perimetro)