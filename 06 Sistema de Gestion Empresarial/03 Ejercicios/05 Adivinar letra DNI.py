

def letra_dni(dni):
    tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return tabla[int(dni) % 23]

dni = input("Introduce tu DNI sin letra: ")
print(f"Tu DNI completo es {dni}{letra_dni(dni)}")
