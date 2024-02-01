def decorador (funcion_original): # Función de nombre decorador que recibe la funcion_original
    def nueva_funcion(): # Definimos una nueva función
        print("Funcionalidad extra")
        funcion_original() # LLamada a la función (línea 8)
    return nueva_funcion # 

@decorador
def funcion():
    print("Funcionalidad original")

funcion() # LLamada a la función (línea 7)
