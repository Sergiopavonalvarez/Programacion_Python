#El input siempre devuelve una cadena de caracteres entonces hay que castearlo
saludo = input("Dime hola ")
print(saludo)

#esto para enteros
numero = int(input("Dime un muero del 1 al 5 "))
print("la suma del numero + 1 es ", numero + 1)

#imprimir con comodines %S => String, %d => Entero, %f => Float(Decimal) y para mostrar solo 2 decimales => %.2f
print("El producto %s cantidad = %d precio = %.2f" % ("Lemons", numero, 12.5))