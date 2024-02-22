
class NumerosNaturales:
    @classmethod
    def mostrar_naturales(cls, n):
        if n > 0:
            cls.mostrar_naturales(n - 1)
            print(n)

class NumerosNaturalesInversos:
    @classmethod
    def mostrar_inversos(cls, n):
        if n > 0:
            print(n)
            cls.mostrar_inversos(n - 1)

print("Metodo: a")
NumerosNaturalesInversos.mostrar_inversos(5)
print("Metodo: b")
NumerosNaturales.mostrar_naturales(5)