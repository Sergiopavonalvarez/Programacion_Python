

class OperacionesString:
    @classmethod
    def orden_inverso(cls, s, idx=None):
        if idx is None:
            idx = len(s) - 1

        if idx == -1:
            return ""
        else:
            return s[idx] + cls.orden_inverso(s, idx - 1)

    @classmethod
    def orden_inverso_string(cls, s):
        if len(s) == 0:
            return ""
        else:
            return s[-1] + cls.orden_inverso_string(s[:-1])


print(OperacionesString.orden_inverso("hola"))
print(OperacionesString.orden_inverso_string("hola"))
