# ''' sirven para ponerlas en varias lineas
cadena1 = 'hola que tal es una cadena'
cadena2 = "Hola"
cadena3 = '''que 
tal estas marica '''

print(cadena1)
print(cadena2)
print(cadena3 + cadena1)

# Para que me imprima un numero de veces ej.
cadena4 = cadena2 * 6
print(cadena4)

# para sacar posiciones de las cadenas
print("El tercer caracter de hola es la: ", cadena2[2])

#para sacar la longitud se usa la funcion len()
print(len(cadena2))

cadena6 = cadena1[3]
print(cadena6)

# NO utiliza ascii utiliza unicode esto es para compara cual es mas mayor que la otra

cadena11 = "a"
cadena22 = "A"
print(cadena11 > cadena22)

cadena33 = "informatica"
cadena44 = "informatica"
print("long", cadena33 > cadena44)
print(cadena33 == cadena44)
print(len(cadena44))










