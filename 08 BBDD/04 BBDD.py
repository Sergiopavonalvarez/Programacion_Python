import sqlite3

miConexion=sqlite3.connect("CuartaBase")

miCursor=miConexion.cursor()
"""
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR (50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR (20))
''')

productos=[
    ("Pelota", 20, "Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)
"""

miCursor.execute("INSERT INTO PRODUCTOS VALUES(5,'Pantalon', 150, 'Ropa')")
productos=miCursor.fetchall()


print("****************UPDATE********************")
#UPDATE
miCursor.execute("Select * FROM PRODUCTOS WHERE NOMBRE_ARTICULO='Pantalon'")
productos=miCursor.fetchall()

print(productos)


miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pantalon'")


miCursor.execute("Select * FROM PRODUCTOS WHERE NOMBRE_ARTICULO='Pantalon'")
productos=miCursor.fetchall()
print(productos)

print("****************DELETE********************")
#DELETE
miCursor.execute("Select * FROM PRODUCTOS")
productos=miCursor.fetchall()
print(productos)

miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='Pantalon'")

miCursor.execute("Select * FROM PRODUCTOS")
productos=miCursor.fetchall()
print(productos)





miConexion.commit()
miConexion.close()
