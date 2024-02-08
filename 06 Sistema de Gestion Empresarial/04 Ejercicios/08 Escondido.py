



numero=17
a=True

while a:
    numero2=int(input("Introduce un numero del 1 al 100: "))

    if numero2 == numero:
        print("Acertaste!!!!!!")
        a=False
    if numero2 > numero:
        print("El numero es menor, prueba de nuevo")
    if numero2< numero:
        print("El numero es mayor, prueba de nuevo")
