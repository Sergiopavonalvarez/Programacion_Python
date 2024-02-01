

from random import randint
import os

u_pwd = input("Introduce la contraseña: ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pw = ""

while pw != u_pwd:
    pw = ""
    for _ in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw = guess_pwd + pw
        print(pw)
        print("Descifrando la contraseña... Por favor espera")
        os.system("cls" if os.name == "nt" else "clear")

print("Tu contraseña es: ", pw)

