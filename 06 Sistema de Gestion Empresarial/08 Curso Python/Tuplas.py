#Las tuplas no permiten añadir ni eliminar y pueden guardar varios valores algunos metodos son iguales que las listas
tupla = (1, 2, 3)
tupla[1] = 7
print(tupla[0])
print(len(tupla))

#para guardar los datos de una division que devuelve un tuple se hace de la siguiente manera
cociente, resto = divmod(13, 2)
print("cociente es: ", cociente, " el resto es ", resto)