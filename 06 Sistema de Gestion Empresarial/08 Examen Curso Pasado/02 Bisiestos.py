
def es_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False
def numbisiestos(año1, año2):
    bisiestos = 0
    dias = 0
    for i in range(año1, año2 + 1):
        if es_bisiesto(i):
            bisiestos += 1
            dias += 366
        else:
            dias += 365
    return bisiestos, dias
año1 = int(input("Dame un año: "))
año2 = int(input("Dame otro año: "))
bisiestos, dias = numbisiestos(año1, año2)
print(f"Entre {año1} y {año2} (ambos incluidos) hubo/hay/habrá {bisiestos} años bisiestos y un total de {dias} días.")
