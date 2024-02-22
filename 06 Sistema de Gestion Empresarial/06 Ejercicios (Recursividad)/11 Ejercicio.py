'''
Escribir un método de clase recursivo que, datos dos String s1 y s2 y sin hacer uso de los métodos definidos en la clase String que resuelven el mismo problema, determine:
a) si s2 es prefijo de s1.
b) si s2 es sufijo de s1.
c) si s2 es una subcadena de s1.
'''
#

class OperacionesString:
    @classmethod
    def es_prefijo(cls, s1, s2, idx=None):
        if idx is None:
            idx = 0

        if idx == len(s2):
            return True
        else:
            if s1[idx] == s2[idx]:
                return cls.es_prefijo(s1, s2, idx + 1)
            else:
                return False

    @classmethod
    def es_sufijo(cls, s1, s2, idx=None):
        if idx is None:
            idx = 0

        if idx == len(s2):
            return True
        else:
            if s1[-idx - 1] == s2[-idx - 1]:
                return cls.es_sufijo(s1, s2, idx + 1)
            else:
                return False

    @classmethod
    def es_subcadena(cls, s1, s2, idx=None):
        if idx is None:
            idx = 0

        if idx == len(s1):
            return False
        else:
            if cls.es_prefijo(s1[idx:], s2):
                return True
            else:
                return cls.es_subcadena(s1, s2, idx + 1)

# Ejemplo de uso
print(OperacionesString.es_prefijo("hola", "hol"))
print(OperacionesString.es_sufijo("hola", "la"))
print(OperacionesString.es_subcadena("hola", "ol"))
