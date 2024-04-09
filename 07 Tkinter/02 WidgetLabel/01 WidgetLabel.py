from tkinter import*

root=Tk()

root.title("01 WidgetLabel")
miFrame=Frame(root, width=500, height=500)
miFrame.pack()

miLabel=Label(miFrame, text="The Rolling Stones", fg="red", font=("Comic Sans MS", 18))
miLabel.place(x=100, y=100)

miImagen=PhotoImage(file="images.png")
miLabel2=Label(miFrame, image=miImagen)
miLabel2.place(x=100, y=200)

root.mainloop()