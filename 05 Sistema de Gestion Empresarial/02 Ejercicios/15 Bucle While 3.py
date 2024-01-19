

resultado = 0.0
i = 0

n = int(input("Introduce el numero n: "))
if n < 0:
    i = -n
else:
    i = n

while i >= 1:
    resultado = resultado + (1 / i)
    i = i - 1

print(resultado)