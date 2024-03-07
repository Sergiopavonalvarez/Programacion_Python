intents = 0
clave1 = "miguel"
while intents < 4:
    clave = input("Dime tu clave ")
    intents += 1
    if clave == clave1:
        break
if intents > 3:
    print("Has superado el limite de intentos")
else:
    print("bienvenuto en ", intents, " intentos")

for var in range(0, 11, 5):
    print(var)