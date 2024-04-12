import sqlite3

miConexion=sqlite3.connect("TerceraBase")
miCursor=miConexion.cursor()

#ID automatico
miCursor.execute('''
    CREATE TABLE ALBUMS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ALBUM VARCHAR (50),
    PFECHA INTEGER,
    GRUPO VARCHAR (20))
''')

albums=[
    ("Their Satanic Majestic", 1967, "The Rolling Stones"),
    ("The Velvet Underground and Nico", 1970, "The Velvet Underground"),
    ("Sgt Peppers Lonely Hear Club Band", 1972, "The Beatles"),
    ("The Dark Side of the Moon", 1973, "Pink Floyd")

]

miCursor.executemany("INSERT INTO ALBUMS VALUES(NULL,?,?,?)", albums)


miCursor.execute("SELECT * FROM ALBUMS")
albums=miCursor.fetchall()
for albums in albums:
    print("| ID: ",albums[0],"| ALBUM: ",albums[1],"| FECHA: ",albums[2]," | GRUPO: ",albums[3])


miConexion.commit()
miConexion.close()