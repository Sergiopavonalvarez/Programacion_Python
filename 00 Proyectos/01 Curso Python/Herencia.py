class punto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def mostrar(self):
        return f"({self.__x}, {self.__y})"

class punto3d(punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.__z = z

    @property
    def z(self):
        print("Doy z")
        return self.__z

    @z.setter
    def z(self, z):
        print("Cambio z")
        self.__z = z

    def mostrar(self):
        return super().mostrar() + f": {self.__z}"

    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.__z - otro.z
        return (dx*dx + dy*dy + dz*dz)**0.5

p3d = punto3d(4, 5, 6)
print(p3d.mostrar())
print(p3d.distancia(punto3d(1, 2, 3)))


