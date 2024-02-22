
class OperacionesArrayString:
    @classmethod
    def es_capicua(cls, v, idx=None):
        if idx is None:
            idx = 0

        if idx >= len(v) // 2:
            return True
        else:
            if v[idx] == v[-idx - 1]:
                return cls.es_capicua(v, idx + 1)
            else:
                return False

    @classmethod
    def existe_palabra_entre_posiciones(cls, v, pal, ini, fin, idx=None):
        if idx is None:
            idx = ini

        if idx > fin:
            return -1
        else:
            if v[idx] == pal:
                return idx
            else:
                return cls.existe_palabra_entre_posiciones(v, pal, ini, fin, idx + 1)



v = ["hola", "mundo", "hola"]
print("a) ¿El array es capicúa?", OperacionesArrayString.es_capicua(v))
pal = "mundo"
ini, fin = 0, 2
print(f"b) ¿En que posicion esta {pal} entre las posiciones {ini} y {fin}?", OperacionesArrayString.existe_palabra_entre_posiciones(v, pal, ini, fin))
