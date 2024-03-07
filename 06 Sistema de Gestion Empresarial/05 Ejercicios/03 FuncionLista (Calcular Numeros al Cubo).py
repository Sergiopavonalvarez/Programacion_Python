

def funcionLista(funcion, lista):
    resultado = [funcion(elemento) for elemento in lista]
    return resultado


def calcular_cubo(numero):
    return numero ** 3

lista_original = [1, 2, 3, 4, 5]
lista_resultado = funcionLista(calcular_cubo, lista_original)

print("Lista original:", lista_original)
print("Lista resultado (cubo):", lista_resultado)