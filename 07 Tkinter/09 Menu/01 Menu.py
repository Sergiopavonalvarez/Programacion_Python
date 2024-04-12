from tkinter import*

root=Tk()
root.title("01 Menu")
root.geometry("400x300")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")


archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Deshacer")
archivoEdicion.add_command(label="Rehacer")



archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Compilar")
archivoHerramientas.add_command(label="Ejecutar")
archivoHerramientas.add_command(label="Depurar")

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Documentacion")
archivoAyuda.add_command(label="Acerca de...")
archivoAyuda.add_command(label="Licencia")




barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




root.mainloop()