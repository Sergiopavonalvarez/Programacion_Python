

numero1=int(input("Escribe el primer numero negativo o positivo: "))
numero2=int(input("Escribe el segundo numero negativo o positivo: "))

if numero1>=0 and numero2>=0:
    print("El producto de los dos numeros es positivo o nulo")
elif numero1<0 and numero2<0:
    print("El producto de los dos numeros es positivo o nulo")
elif numero1>=0 and numero2<0:
    print("El producto de los dos numeros es negativo")
elif numero1<0 and numero2>=0:
    print("El producto de los dos numeros es negativo")
