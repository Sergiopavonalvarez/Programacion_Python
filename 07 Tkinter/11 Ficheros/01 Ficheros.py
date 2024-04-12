from tkinter import*
from tkinter import filedialog

root=Tk()
root.title("01 Ficheros")
root.geometry("400x300")

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:/", filetypes=(("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()