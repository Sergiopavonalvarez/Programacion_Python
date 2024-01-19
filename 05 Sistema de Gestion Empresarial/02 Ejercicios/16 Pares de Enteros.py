

n = int(input("Ingrese un número positivo n: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        resultado = i + j + 2 * i * j
        print(f"Par {i},{j}: {i}+{j}+2*{i}*{j} vale {resultado}")
