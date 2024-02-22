
class Binario:
    @classmethod
    def binario(cls, n):
        if n < 2:
            return str(n)
        else:
            return cls.binario(n // 2) + str(n % 2)


print("Binario de 5: ",(Binario.binario(5)))
print("Binario de 31: ",(Binario.binario(31)))
