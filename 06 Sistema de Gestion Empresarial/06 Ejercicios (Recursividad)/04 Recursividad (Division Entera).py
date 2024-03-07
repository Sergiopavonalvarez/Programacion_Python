
class DivisionEntera:
    @classmethod
    def division_entera(cls, a, b):
        if a < b:
            return 0
        else:
            return cls.division_entera(a - b, b) + 1

print(DivisionEntera.division_entera(10, 3))