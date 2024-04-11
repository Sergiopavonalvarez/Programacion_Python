from tkinter import *

raiz = Tk()
raiz.title("CheckButton")
raiz.geometry("435x400")

pista=IntVar()
tribuna=IntVar()
palco=IntVar()

def opcion ():
    opcionEscogida=""
    if pista.get()==1:
        opcionEscogida+="Pista"
        textoFinal.config(text=opcionEscogida)
    if tribuna.get()==1:
        opcionEscogida+=" Tribuna"
        textoFinal.config(text=opcionEscogida)
    if palco.get()==1:
        opcionEscogida+=" Palco"
        textoFinal.config(text=opcionEscogida)
    if pista.get()==0 and tribuna.get()==0 and palco.get()==0:
        textoFinal.config(text="")
    print(opcionEscogida)


titulo = Label(raiz, text="Concierto de The Rolling Stones")
titulo.grid(row=0, column=0, columnspan=3)
titulo.config(font=("Arial", 20), pady=20, padx=20, fg="red")

imagen = PhotoImage(file="images.png")
miLabel2 = Label(raiz, image=imagen)
miLabel2.grid(row=1, column=0, columnspan=3)
miLabel2.config(pady=20, padx=20)

ch1 = Checkbutton(raiz, text="Pista", variable=pista, onvalue=1, offvalue=0, command=opcion)
ch1.grid(row=2, column=0)

ch2 = Checkbutton(raiz, text="Tribuna", variable=tribuna, onvalue=1, offvalue=0, command=opcion)
ch2.grid(row=2, column=1)

ch3 = Checkbutton(raiz, text="Palco", variable=palco, onvalue=1, offvalue=0, command=opcion)
ch3.grid(row=2, column=2)

textoFinal=Label(raiz, text="")
textoFinal.grid(row=3, column=0, columnspan=3)
textoFinal.config(font=("Arial", 10), pady=20, padx=20, fg="red")


raiz.mainloop()