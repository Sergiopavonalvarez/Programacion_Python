
class Potencia:
    @classmethod
    def potencia(cls, a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        elif b % 2 == 0:
            return cls.potencia(a, b // 2) * cls.potencia(a, b // 2)
        else:
            return cls.potencia(a, b // 2) * cls.potencia(a, b // 2) * a

print(Potencia.potencia(2, 3))
