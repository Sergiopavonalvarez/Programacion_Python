

def palabrasLongitud(frase):
    palabras = frase.split()
    diccionario_resultado = {palabra: len(palabra) for palabra in palabras}
    return diccionario_resultado

frase_ejemplo = 'Hola y adiós'
resultado = palabrasLongitud(frase_ejemplo)

print("Frase original:", frase_ejemplo)
print("Diccionario resultado:", resultado)
