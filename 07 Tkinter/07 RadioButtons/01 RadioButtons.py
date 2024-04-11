from tkinter import *

raiz = Tk()
raiz.title("RadioButtons")
raiz.geometry("300x150")
varOpcion = IntVar()


def imprimir():
    if varOpcion.get() == 1:
        etiqueta.config(text="Masculino", fg="blue", font=("Arial"))
    if varOpcion.get() == 2:
        etiqueta.config(text="Femenino", fg="blue", font=("Arial"))
    if varOpcion.get() == 3:
        etiqueta.config(text="Señor/Señora", fg="blue", font=("Arial"))


titulo = Label(raiz, text="Genero:")
titulo.grid(row=0, column=0)
titulo.config(justify="right")

uno = Radiobutton(raiz, text="Masculino", variable=varOpcion, value=1, command=imprimir)
uno.grid(row=1, column=1)
uno.config(justify="right")

dos = Radiobutton(raiz, text="Femenino", variable=varOpcion, value=2, command=imprimir)
dos.grid(row=2, column=1)


tres = Radiobutton(raiz, text="Señor/Señora", variable=varOpcion, value=3, command=imprimir)
tres.grid(row=3, column=1)


etiqueta = Label(raiz)
etiqueta.grid(row=5, column=1)


raiz.mainloop()




raiz.mainloop()
