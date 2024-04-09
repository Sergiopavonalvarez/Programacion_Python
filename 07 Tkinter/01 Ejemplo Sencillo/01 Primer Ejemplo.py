from tkinter import*
#Creamos la raiz
raiz=Tk()
#Le damos titulo
raiz.title("01 Primer Ejemplo")
#Booleanos para decir si cambia de tamaño o no, alto y ancho
raiz.resizable(1,1)
#Añadimos el icono, tiene que ser .icon
raiz.iconbitmap("icon.ico")
#Tamaño, al añadir el frame hay que quitarlo
#raiz.geometry("500x500")
#Color de fondo
raiz.config(bg="green")

#Cremaos un frame
miFrame=Frame()
#Empaquetamos el frame, y decimos que aparezca a la derecha de la raiz
miFrame.pack(side="right")
#Tamaño del frame
miFrame.config(width="500", height="500")
#Color de fondo del frame
miFrame.config(bg="red")
#Borde del frame
miFrame.config(bd=35)
miFrame.config(relief="groove")
#Cursos del frame
miFrame.config(cursor="pirate")


#Bucle para que se vea la raiz
raiz.mainloop()