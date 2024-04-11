from tkinter import*

raiz = Tk()
raiz.title("Calculadora")
raiz.resizable(0,0)
# raiz.geometry("500x450")

miFrame = Frame(raiz)
miFrame.pack()

operacion=""
resultado=0

#----------------------------------Pantalla----------------------------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=0,column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right",width=12, font=("Arial", 50))


#---------------------------------Fila 0-----------------------------------

botonrestar=Button(miFrame, text="<-", width=15,height=5, command=lambda :borrar())
botonrestar.grid(row=1,column=4)

def borrar():
    numeroPantalla.set(numeroPantalla.get()[:-1])



#---------------------------------Fila 1-----------------------------------
boton7=Button(miFrame, text="7", width=15,height=5, command=lambda:numeroPulsado("7"))
boton7.config(bg="#A9A9A9")
boton8=Button(miFrame, text="8", width=15,height=5, command=lambda:numeroPulsado("8"))
boton8.config(bg="#A9A9A9")
boton9=Button(miFrame, text="9", width=15,height=5, command=lambda:numeroPulsado("9"))
boton9.config(bg="#A9A9A9")
botonMultiplicar=Button(miFrame, text="x", width=15,height=5, command=lambda:multiplicacion(numeroPantalla.get()))

boton7.grid(row=2,column=1)
boton8.grid(row=2,column=2)
boton9.grid(row=2,column=3)
botonMultiplicar.grid(row=2,column=4)



# ---------------------------------Fila 2-----------------------------------
boton4=Button(miFrame, text="4", width=15,height=5, command=lambda:numeroPulsado("4"))
boton4.config(bg="#A9A9A9")
boton5=Button(miFrame, text="5", width=15,height=5, command=lambda:numeroPulsado("5"))
boton5.config(bg="#A9A9A9")
boton6=Button(miFrame, text="6", width=15,height=5, command=lambda:numeroPulsado("6"))
boton6.config(bg="#A9A9A9")
botonDividir=Button(miFrame, text="/", width=15,height=5, command=lambda:division(numeroPantalla.get()))
boton4.grid(row=3,column=1)
boton5.grid(row=3,column=2)
boton6.grid(row=3,column=3)
botonDividir.grid(row=3,column=4)
# ---------------------------------Fila 3-----------------------------------
boton1=Button(miFrame, text="1", width=15,height=5, command=lambda:numeroPulsado("1"))
boton1.config(bg="#A9A9A9")
boton2=Button(miFrame, text="2", width=15,height=5, command=lambda:numeroPulsado("2"))
boton2.config(bg="#A9A9A9")
boton3=Button(miFrame, text="3", width=15,height=5, command=lambda:numeroPulsado("3"))
boton3.config(bg="#A9A9A9")
botonSumar=Button(miFrame, text="+", width=15,height=5, command=lambda:suma(numeroPantalla.get()))
boton1.grid(row=4,column=1)
boton2.grid(row=4,column=2)
boton3.grid(row=4,column=3)
botonSumar.grid(row=4,column=4)
# ---------------------------------Fila 4-----------------------------------
boton0=Button(miFrame, text="0", width=15,height=5, command=lambda:numeroPulsado("0"))
boton0.config(bg="#A9A9A9")
botonComa=Button(miFrame, text=",", width=15,height=5, command=lambda:numeroPulsado("."))
botonIgual=Button(miFrame, text="=", width=15,height=5, command=lambda:elresultado())
botonRestar=Button(miFrame, text="-", width=15,height=5, command=lambda:resta(numeroPantalla.get()))
boton0.grid(row=5,column=2)
botonComa.grid(row=5,column=4)
botonIgual.grid(row=5,column=3)
botonRestar.grid(row=5,column=1)

#---------------------------------Funcion numeroPulsado-----------------------------------
def numeroPulsado(num):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else:
     numeroPantalla.set(numeroPantalla.get()+num)
#---------------------------------Funcion suma-----------------------------------
def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion="suma"
    numeroPantalla.set(resultado)
#---------------------------------Funcion resta-----------------------------------
def resta(num):
    global operacion
    global resultado
    resultado -= int(num)
    operacion = "resta"
    numeroPantalla.set(resultado)
#---------------------------------Funcion multiplicacion-----------------------------------
def multiplicacion(num):
    global operacion
    global resultado
    if resultado == 0:
        resultado = int(num)
    else:
        resultado *= int(num)
    operacion = "multiplicacion"
    numeroPantalla.set(resultado)
#---------------------------------Funcion division-----------------------------------
def division(num):
    global operacion
    global resultado
    resultado=resultado/int(num)
    operacion="division"
    numeroPantalla.set(resultado)
#---------------------------------Funcion elresultado-----------------------------------
def elresultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0
    operacion=""


raiz.mainloop()