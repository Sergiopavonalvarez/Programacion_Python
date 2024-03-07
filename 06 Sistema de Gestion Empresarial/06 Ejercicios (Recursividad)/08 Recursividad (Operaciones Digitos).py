

class Digitos:
    @classmethod
    def suma(cls, n):
        if n < 10:
            return n
        else:
            return n % 10 + cls.suma(n // 10)

    @classmethod
    def numero(cls, n):
        if n < 10:
            return 1
        else:
            return 1 + cls.numero(n // 10)

    @classmethod
    def inverso(cls, n):
        if n < 10:
            return n
        else:
            return str(n % 10) + str(cls.inverso(n // 10))

print("Suma digitos: ",(Digitos.suma(123)))
print("Numero de digitos: ",(Digitos.numero(123)))
print("Orden Inverso: ",(Digitos.inverso(123)))