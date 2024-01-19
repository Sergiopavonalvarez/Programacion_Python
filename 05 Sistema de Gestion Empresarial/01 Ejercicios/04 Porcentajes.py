
niños=int(input("Introduce el numero de niños: "))
niñas=int(input("Introduce el numero de niñas: "))

total_personas = niños + niñas

porcentaje_niños = (niños / total_personas) * 100
porcentaje_niñas = (niñas / total_personas) * 100

print("El porcentaje de niños es:", porcentaje_niños,"%")
print("El porcentaje de niñas es:", porcentaje_niñas,"%")