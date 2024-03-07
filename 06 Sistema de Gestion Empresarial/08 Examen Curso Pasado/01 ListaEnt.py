


n1 = int(input("Dame el número entero inicial: "))
n2 = int(input("Dime cuántos valores quieres: "))
if n2 < 0:
    print("Resultado: ¡La cantidad de valores no puede ser negativa!")
else:
    print("Resultado:", [n1 + i for i in range(n2)])






