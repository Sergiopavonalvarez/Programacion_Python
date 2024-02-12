
lista_numeros=[]
for i in range(4):
    n=int(input("Introduce un numero: "))
    lista_numeros.append(n)

print(lista_numeros)
def histograma (lista_numeros):

        print("*" * lista_numeros[0])
        print("*" * lista_numeros[1])
        print("*" * lista_numeros[2])
        print("*" * lista_numeros[3])

resultad=histograma(lista_numeros)
print(resultad)