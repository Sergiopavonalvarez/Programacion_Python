

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


print(OperacionesString.es_prefijo("hola", "hol"))
print(OperacionesString.es_sufijo("hola", "la"))
print(OperacionesString.es_subcadena("hola", "ol"))
