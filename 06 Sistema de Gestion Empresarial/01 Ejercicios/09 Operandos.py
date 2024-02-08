

cont = 10
limite = 10
valor = False

if cont == 0 and limite < 20:
    print("A")
elif limite >= 20 or cont < 5:
    print("B")
elif cont != 10 and (limite / (cont - 10)) > 7 or limite < 20:
    print("C")
elif limite <= 20 or (limite / (cont - 10)) > 7:
    print("D")
elif (limite / (cont - 10)) > 7 and limite < 0:
    print("E")
elif limite < 0 and (limite / (cont - 10)) > 7:
    print("F")


