
class Producto:
    @classmethod
    def producto(cls, a, b):
        if b == 0:
            return 0
        else:
            return cls.producto(a, b - 1) + a

print(Producto.producto(5, 3))

