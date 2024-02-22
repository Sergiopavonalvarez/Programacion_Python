
class OperacionesString:
    @classmethod
    def es_palindromo(cls, s, idx=None):
        if idx is None:
            idx = 0

        if idx >= len(s) // 2:
            return True
        else:
            if s[idx] == s[-idx - 1]:
                return cls.es_palindromo(s, idx + 1)
            else:
                return False


print(OperacionesString.es_palindromo("hola"))
print(OperacionesString.es_palindromo("ojo"))
