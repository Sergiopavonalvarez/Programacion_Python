

nota1 = float(input("Introduce la nota del primer examen: "))
nota2 = float(input("¿Qué nota quieres sacar en el trimestre? "))
por1 = (nota1 * 40) / 100
nota3 = (nota2 - por1) / 0.6
print("Para obtener una nota de", nota2, "en el trimestre, necesitas sacar un", nota3, "en el segundo examen.")

