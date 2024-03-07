

x=int(input("Escribe la coordenada x: "))
y=int(input("Escribe la coordenada y: "))

if x > 0 and y > 0:
    print("Esta en el primer cuadrante")
elif x < 0 and y > 0:
    print("Esta en el segundo cuadrante")
elif x < 0 and y < 0:
    print("Esta en el tercer cuadrante")
elif x > 0 and y < 0:
    print("Esta en el cuarto cuadrante")
elif x!=0 and y!=0:
    print("Esta en el eje de abscisas")
elif x==0 and y!=0:
    print("Esta en el eje de ordenadas")
elif x==0 and y==0:
    print("Esta en el eje de coordenadas")