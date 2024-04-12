from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("01 Menu")
root.geometry("400x300")

def infoAdicional():
    messagebox.showinfo("Procesador de texto", "Procesador de texto version 2020")
def cerrar():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
    else:
        pass
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor==False:
        root.destroy()
    else:
        pass
def copiarTexto():
    textoSeleccionado=textoLabel.get("sel.first", "sel.last")
    textoLabel.clipboard_clear()
    textoLabel.clipboard_append(textoSeleccionado)
def pegarTexto():
    textoPegado=textoLabel.clipboard_get()
    textoLabel.insert(INSERT, textoPegado)
def cortarTexto():
    textoSeleccionado=textoLabel.get("sel.first", "sel.last")
    textoLabel.clipboard_clear()
    textoLabel.clipboard_append(textoSeleccionado)
    textoLabel.delete("sel.first", "sel.last")

miFrame=Frame(root)
miFrame.pack()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=cerrar)


archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar", command=copiarTexto)
archivoEdicion.add_command(label="Cortar", command=cortarTexto)
archivoEdicion.add_command(label="Pegar", command=pegarTexto)
archivoEdicion.add_command(label="Deshacer")
archivoEdicion.add_command(label="Rehacer")



archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Compilar")
archivoHerramientas.add_command(label="Ejecutar")
archivoHerramientas.add_command(label="Depurar")

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Documentacion")
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)




barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

textoLabel=Text(miFrame)
textoLabel.config(width=39, height=15, fg="black", bg="white", font=("Arial", 12))
textoLabel.grid(row=0,column=0, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoLabel.yview)
scrollVert.grid(row=0,column=1, sticky="nsew")
textoLabel.config(yscrollcommand=scrollVert.set)






root.mainloop()