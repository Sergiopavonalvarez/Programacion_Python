#Saber si hay letras
cadena = "Dabale arroz a la zorra el abad"

print("b" in cadena)

if "be" in cadena:
    print("caca")
else:
    print("pis")
#Imprime de la posicion 2 a la 6 corriendo de 2 en 2
print(cadena[2:7:2])

#imprime la posicion hasta el final y al reves desde el principio hasta el final
print(cadena[2:])

#imprime la cadena invertida y el .replace reemplaza lo que le pongas por lo otro
print(cadena[::-1])
cadenaModificada = cadena.replace(" ", "")
if cadenaModificada.upper() == cadenaModificada[::-1].upper():
    print("Palindromooo")
else:
    print("no palindromo")

#Metodos de busqueda

#Busca las letras puestas y las cuenta devuelve un entero
cad = "Bienvenido a mi aplicacion"
print(cad.count("a"))
print(cad.count("a", 10, 15))

#Metodo que devuelve la primera posicion donde encuentra esa cadena -1 sino hy na tb para saber si tiene la subcadena
print(cad.find("a"))

#Metodo que quita espacios por delante y por detras si en los parametros le metes un letra tb eliminia todas esas letras
#solo del principio y del final
cade = "     Hola que tal    "
print(cade.strip())

#separa las informacines de la cadena por el separador que le pongamos y devuelve una lista convertir cadenas de
#carecteres en una lista
hora = "12:34:35"
print(hora.split(":"))
#Crea una lista a partir de los saltos de linea
texto = "Linea 1 \nLinea 2 \nLinea 3"
print(texto.splitlines())

