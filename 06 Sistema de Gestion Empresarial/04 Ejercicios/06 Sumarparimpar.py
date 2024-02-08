numerospares = 0
numerosimpares = 0

for i in range(100):
    numero = i + 1
    print(numero)

    if numero % 2 == 0:
        numerospares += numero
    else:
        numerosimpares += numero

print("La suma de los pares:", numerospares)
print("La suma de los impares:", numerosimpares)