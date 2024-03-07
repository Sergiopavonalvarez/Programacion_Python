






diccionario = {"España":"Madrid","Portugal":"Lisboa","Francia":"Paris","Reino Unido":"Londres","Irlanda":"Dublin","Italia":"Roma","Grecia":"Atenas","Alemania":"Berlin"}
pais = input("Introduce un pais: ")

if pais in diccionario:
    print("La capital de",pais,"es",diccionario[pais])
    print("**********************************************")
else:
    print("El pais no existe en el diccionario")
    print("**********************************************")



print("Claves del diccionario:",diccionario.keys())
print("**********************************************")
print("Valores del diccionario son:",diccionario.values())


