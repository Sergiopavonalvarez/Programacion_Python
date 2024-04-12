import sqlite3

miConexion=sqlite3.connect("SegundaBase")
miCursor=miConexion.cursor()
"""
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR (4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR (50),
    PRECIO INTEGER,
    SECCION VARCHAR (20))
''')
"""
productos=[
    ("AR01","Pelota", 20, "Jugueteria"),
    ("AR02","Pantalon", 15, "Confeccion"),
    ("AR03","Destornillador", 25, "Ferreteria"),
    ("AR04","Jarron", 45, "Ceramica")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", productos)
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05','Camiseta', 10, 'Deportes')")

miCursor.execute("SELECT * FROM PRODUCTOS")
productos=miCursor.fetchall()
for producto in productos:
    print("| Codigo articulo: ",producto[0],"| Nombre articulo: ",producto[1],"| Precio: ",producto[2]," Euros | Seccion: ",producto[3])


miConexion.commit()
miConexion.close()