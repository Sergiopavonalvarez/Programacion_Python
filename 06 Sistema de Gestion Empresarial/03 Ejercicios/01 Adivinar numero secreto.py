


import random
numero_secreto = random.randint(1, 100)
print("Adivina el número secreto")
intentos = 0
while True:
    intentos += 1
    numero = int(input("Introduce un número del uno al 100: "))
    if numero == numero_secreto:
        print(f"¡Felicidades! Has acertado en {intentos} intentos")
        break
    elif numero < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")
print("Fin del juego")
