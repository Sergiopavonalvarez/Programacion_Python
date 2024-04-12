import sqlite3
#Creamos la base de datos y su conexion
miConexion=sqlite3.connect("PrimeraBase")
#Creamos el cursor o puntero
miCursor=miConexion.cursor()

#Creamos una tabla
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#Insertamos un producto, uno a uno
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('ESPINILLERAS', 20, 'DEPORTES')")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BOTAS NIKE', 150, 'DEPORTES')")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Iphone 14', 1500, 'TECNOLOGIA')")

#Creamos una lista de tuplas para insertar varios productos
"""variosProductos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]
#Insertamos varios productos
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)"""

#Leer los datos de la tabla
miCursor.execute("SELECT * FROM PRODUCTOS")
#Guardamos los datos de la tabla en una variable, fetchall() devuelve una lista con los datos
variosProductos=miCursor.fetchall()
#Imprimimos los datos
for producto in variosProductos:
    print("| Nombre articulo: ",producto[0],"| Precio: ",producto[1], " Euros | Seccion: ",producto[2])


#Guardamos los cambios
miConexion.commit()
#Cerramos la conexion
miConexion.close()