import math

saludo = input("Dime tu nombre ")
print("Hola ",saludo)

#Ejercicio2

largo = float(input("Dime el largo "))
ancho = float(input("Dime el ancho "))
area = largo * ancho
perimetro = 2 * (largo + ancho)
print("El area es ", area)
print("El perimetro es ", perimetro)

#Ejercicio3

catetoA = int(input("Dime el cateto A "))
catetoB = int(input("Dime el cateto B "))
hipotenusa = math.sqrt((catetoA**2) + (catetoB**2))
print("La hipotenusa del triangulo rectangulo es: ", hipotenusa)

#Ejercicio4

num1 = int(input("Dime el numero 1 "))
num2 = int(input("Dime el numero 2 "))

resta = num1 - num2
suma = num1 + num2
multiplicacion = num1 * num2
division = num1 / num2

print(resta)
print(suma)
print(multiplicacion)
print(round(division, 2))

#Ejercicio 5

farenhait = float(input("Dime los ºF para pasarlos a ºC "))
aCelsius = (farenhait - 32) * (5 / 9)
print(farenhait, "ºF son: ", round(aCelsius, 2), " ºC")

#Ejercico 6

media1 = int(input("Dime el numero 1 "))
media2 = int(input("Dime el numero 2 "))
media3 = int(input("Dime el numero 3 "))

media = (media1 + media2 + media3) / 3
print("La media es: ", media)

#Ejercicio 7

tiempo = int(input("Dime los minutos para pasarlo a horas "))
horas = tiempo // 60
minutos = tiempo % 60
print("El tiempo en horas es: ", horas, " horas y ", minutos, " minutos")

#Ejercicio 8

sueldoBase = float(input("Dime el sueldo "))
producto1 = float(input("Dime el precio de la venta 1 "))
producto2 = float(input("Dime el precio de la venta 2 "))
producto3 = float(input("Dime el precio de la venta 3"))
sumatorio = producto1 + producto2 + producto3
comision = 0.10 * sumatorio
sueldoTotal = sueldoBase + comision
print("El salario que tiene es: ", sueldoBase, "€ ha vendido un total de 3 productos con la cantidad de: ",
      producto1, "€, ", producto2, "€, ", producto3, "€ su comision aplicada del 10% es ", comision, " €", " que hace un total de: ",
      sueldoTotal, "€")

#Ejercicio 9

precio = float(input("Dime el precio "))
descuento = precio * 0.15
precioFinal = precio - descuento
print("El precio final es ", precioFinal, "€")

#Ejercicio 10

parcial1 = float(input("Dime la nota del parcial 1:"))
parcial2 = float(input("Dime la nota del parcial 2:"))
parcial3 = float(input("Dime la nota del parcial 3:"))
examen = float(input("Dime la nota del examen:"))
trabajo = float(input("Dime la nota del trabajo:"))
nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + 0.3 * examen + 0.15 * trabajo
print("nota final= %.2f" %nota)

#Ejercicio 15

a = int(input("Ingrese un numero"))
b = int(input("Ingrese otro numero"))
aux = a
a = b
b = aux
print("El valor de a es: ", b, " y el valor de b es; ", a)

#Ejercicio 15

nombre = input("Dime tu numebre ")
apellido = input("dime tu apellido ")

print("Tu nick de inicio sesion es ", nombre[0].upper(), apellido[0].upper())

#Ejercicio 1 Ifs

a = int(input("Ingrese un numero"))
b = int(input("ingrese otro numero"))
c = int(input("ingrese otro numero"))

if a > b and a > c :
      if b > c:
            print(a,b,c)
      else:
            print (a,c,b)
if b > a and b > c :
      if a > c:
            print(b,c,a)
      else:
            print (b,a,c)
if c > a and c > b :
      if a > b:
            print(c,b,a)
      else:
            print (c,a,b)







