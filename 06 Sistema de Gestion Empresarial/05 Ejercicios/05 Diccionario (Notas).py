
def calificaPalabras(diccionario):
    calificaciones = {'Suspenso': 5,'Aprobado': 7,'Notable': 9,'Sobresaliente': 10}

    resultado = {}
    for asignatura, nota in diccionario.items():
        asignatura_mayusculas = asignatura.upper()

        for calificacion, limite in calificaciones.items():
            if nota < limite:
                resultado[asignatura_mayusculas] = calificacion
                break
        else:
            resultado[asignatura_mayusculas] = 'Sobresaliente'

    return resultado


notas_ejemplo = {'Android': 8.2, 'Hilos': 5, 'Python': 9.3, 'Interfaces': 4.4}
resultado = calificaPalabras(notas_ejemplo)

print("Diccionario original:", notas_ejemplo)
print("Diccionario resultado:", resultado)
