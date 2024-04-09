from tkinter import*

raiz=Tk()
raiz.title("01 WidgetLabel")
raiz.geometry("300x150")


miFrame=Frame(raiz, width=200, height=200)

miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red", justify="center")
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=5)


cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1)
cuadroApellido.config(fg="blue", justify="right")
apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1,column=0, sticky="e", padx=10, pady=5)


cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1)
cuadroDireccion.config(fg="green", justify="left")
direccionLabel=Label(miFrame, text="Direccion de casa:")
direccionLabel.grid(row=2,column=0, sticky="e", padx=10, pady=5)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3,column=1)
cuadroPassword.config(show="*", justify="center")
PasswordLabel=Label(miFrame, text="Direccion de casa:")
PasswordLabel.grid(row=3,column=0, sticky="e", padx=10, pady=5)



raiz.mainloop()