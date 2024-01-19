

valor=int(input("Introduce la velocidad: "))
consumo=0

if valor>80:
    consumo=10.00
if valor>100:
    consumo=12.00
if valor>120:
    consumo=15.00

print("El consumo es: ",consumo)