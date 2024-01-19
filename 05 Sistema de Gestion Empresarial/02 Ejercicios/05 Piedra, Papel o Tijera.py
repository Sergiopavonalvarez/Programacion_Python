
import random

mano = ["Piedra", "Papel", "Tijera"]
mano2 = random.choice(mano)


mano3 = input("Escribe Piedra, Papel o Tijera: ")
print(f"La computadora elige: {mano2}")

if mano2.casefold() == "piedra" and mano3.casefold() == "papel":
    print("Ganaste")
elif mano2.casefold() == "piedra" and mano3.casefold() == "tijera":
    print("Perdiste")
elif mano2.casefold() == "piedra" and mano3.casefold() == "piedra":
    print("Empate")
elif mano2.casefold() == "papel" and mano3.casefold() == "piedra":
    print("Perdiste")
elif mano2.casefold() == "papel" and mano3.casefold() == "papel":
    print("Empate")
elif mano2.casefold() == "papel" and mano3.casefold() == "tijera":
    print("Ganaste")
elif mano2.casefold() == "tijera" and mano3.casefold() == "piedra":
    print("Ganaste")
elif mano2.casefold() == "tijera" and mano3.casefold() == "papel":
    print("Perdiste")
elif mano2.casefold() == "tijera" and mano3.casefold() == "tijera":
    print("Empate")
else:
    print("Tu entrada no válida. Por favor, elige entre Piedra, Papel o Tijera.")
