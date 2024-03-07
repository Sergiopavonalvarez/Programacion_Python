'''Escribe un programa en Python llamado mascotas.py que contenga una Clase llamada Mascota que permita crear mascotas con un nombre, una especie y una edad. La aplicación guardará toda la información de las mascotas creadas.
• En la Clase se definirán los métodos para ver el nombre ver_nombre(), ver la especie ver_especie(),
y ver la edad ver_edad(). Además, la Clase tendrá un método __str__ () que devolverá un mensaje del tipo: "%s es un %s" % (nombre, especie)
• Crea otra Clase llamada Perro que va a heredar de la clase Mascota, para poder ver este comportamiento particular en diferentes perros (objetos Perro).
• Algunas mascotas pueden ser perros y a la mayoría de ellos les gusta perseguir gatos y, tal vez, queramos saber a qué perro le gusta perseguir gatos y a qué perro no. Añade un método llamado __persigue_gatos__() que muestre si a un Perro determinado le gusta perseguir gatos o no.
• Crea las siguientes mascotas con sus datos:
nombre especie edad Persigue Tobi Perro 3 persigue gatos Persi Gato 1 Moli Perro 2 no persigue gatos Cani Canario 4 Anki Gato 2 Chuski Perro 3 persigue gatos
• Una vez creadas las mascotas y guardados sus datos en la aplicación, se realizarán las siguientes acciones de forma automática:
1. El programa mostrará todos los datos (nombre, especie, edad) introducidos anteriormente.
2. El programa mostrará sólo la información completa asociada a los gatos.
3. El programa mostrará sólo los datos completos de la mascota más vieja de forma automática.
4. El programa mostrará si a una mascota Perro le gusta perseguir gatos o no.'''
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def ver_nombre(self):
        return self.nombre
    def ver_especie(self):
        return self.especie
    def ver_edad(self):
        return self.edad
    def __str__(self):
        return "%s es un %s" % (self.nombre, self.especie)




class Perro(Mascota):
    def __init__(self, nombre, especie, edad, persigue_gatos):
        super().__init__(nombre, especie, edad)
        self.persigue_gatos = persigue_gatos
    def __persigue_gatos__(self):
        return self.persigue_gatos
Tobi = Perro("Tobi", "Perro", 3, "persigue gatos")
Persi = Mascota("Persi", "Gato", 1)
Moli = Perro("Moli", "Perro", 2, "no persigue gatos")
Cani = Mascota("Cani", "Canario", 4)
Anki = Mascota("Anki", "Gato", 2)
Chuski = Perro("Chuski", "Perro", 3, "persigue gatos")
print("Datos de las mascotas:")
print(Tobi.ver_nombre(), Tobi.ver_especie(), Tobi.ver_edad(), Tobi.__persigue_gatos__())
print(Persi.ver_nombre(), Persi.ver_especie(), Persi.ver_edad())
print(Moli.ver_nombre(), Moli.ver_especie(), Moli.ver_edad(), Moli.__persigue_gatos__())
print(Cani.ver_nombre(), Cani.ver_especie(), Cani.ver_edad())
print(Anki.ver_nombre(), Anki.ver_especie(), Anki.ver_edad())
print(Chuski.ver_nombre(), Chuski.ver_especie(), Chuski.ver_edad(), Chuski.__persigue_gatos__())
print("Datos de los gatos:")
print(Persi.ver_nombre(), Persi.ver_especie(), Persi.ver_edad())
print(Anki.ver_nombre(), Anki.ver_especie(), Anki.ver_edad())
print("Datos de la mascota más vieja:")
if Persi.ver_edad() > Anki.ver_edad():
    print(Persi.ver_nombre(), Persi.ver_especie(), Persi.ver_edad())
else:
    print(Anki.ver_nombre(), Anki.ver_especie(), Anki.ver_edad())
print("¿A Tobi le gusta perseguir gatos?")
print(Tobi.__persigue_gatos__())

print("¿A Moli le gusta perseguir gatos?")
print(Moli.__persigue_gatos__())


print("¿A Chuski le gusta perseguir gatos?")
print(Chuski.__persigue_gatos__())
