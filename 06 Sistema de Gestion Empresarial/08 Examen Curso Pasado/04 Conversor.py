

from tkinter import *
from tkinter import messagebox

def convertir():
    cantidad = float(cantidad_text.get())
    if seleccion.get() == 1:
        resultado = cantidad * 1.054883
        resultado_text.set(f"{resultado:.2f} $")
    else:
        resultado = cantidad * 0.947983
        resultado_text.set(f"{resultado:.2f} €")

ventana = Tk()
ventana.title("Conversor Euro – Dólar USA")
ventana.geometry("400x300")
ventana.resizable(0, 0)




etiqueta = Label(ventana, text="Conversión de divisas Euro - Dólar USA", font=("Arial", 14))
etiqueta.pack()

cantidad_label = Label(ventana, text="Cantidad a convertir")
cantidad_label.pack()
cantidad_text = StringVar()
cantidad_entry = Entry(ventana, textvariable=cantidad_text)
cantidad_entry.pack()

conversion_label = Label(ventana, text="Conversión")
conversion_label.pack()
seleccion = IntVar()
euro_button = Radiobutton(ventana, text="Euro a Dólar USA", variable=seleccion, value=1)
euro_button.pack()
dolar_button = Radiobutton(ventana, text="Dólar USA a Euro", variable=seleccion, value=2)
dolar_button.pack()

convertir_button = Button(ventana, text="Convertir", command=convertir)
convertir_button.pack()

resultado_label = Label(ventana, text="Valor de la conversión")
resultado_label.pack()
resultado_text = StringVar()
resultado_entry = Entry(ventana, textvariable=resultado_text, state="readonly")
resultado_entry.pack()

ventana.mainloop()
