import random

mano = ["Piedra", "Papel", "Tijera", "Lagarto", "spock"]
mano2 = random.choice(mano)
print(f"La computadora elige: {mano2}")

mano3 = input("Escribe Piedra, Papel, Tijera, Lagarto o Spock: ")

if mano2.casefold() == "piedra":
    if mano3.casefold() == "papel" or mano3.casefold() == "spock":
        print("Ganaste")
    elif mano3.casefold() == "tijera" or mano3.casefold() == "lagarto":
        print("Perdiste")
    elif mano3.casefold() == "piedra":
        print("Empate")
elif mano2.casefold() == "papel":
    if mano3.casefold() == "tijera" or mano3.casefold() == "lagarto":
        print("Ganaste")
    elif mano3.casefold() == "piedra" or mano3.casefold() == "Spock":
        print("Perdiste")
    elif mano3.casefold() == "papel":
        print("Empate")
elif mano2.casefold() == "tijera":
    if mano3.casefold() == "piedra" or mano3.casefold() == "spock":
        print("Ganaste")
    elif mano3.casefold() == "papel" or mano3.casefold() == "lagarto":
        print("Perdiste")
    elif mano3.casefold() == "tijera":
        print("Empate")
elif mano2.casefold() == "lagarto":
    if mano3.casefold() == "piedra" or mano3.casefold() == "tijera":
        print("Ganaste")
    elif mano3.casefold() == "papel" or mano3.casefold() == "pock":
        print("Perdiste")
    elif mano3.casefold() == "lagarto":
        print("Empate")
elif mano2.casefold() == "spock":
    if mano3.casefold() == "piedra" or mano3.casefold() == "tijera":
        print("Ganaste")
    elif mano3.casefold() == "papel" or mano3.casefold() == "lagarto":
        print("Perdiste")
    elif mano3.casefold() == "spock":
        print("Empate")
    else:
        print("Entrada no válida. Por favor, elige entre Piedra, Papel, Tijera, Lagarto o pock.")
