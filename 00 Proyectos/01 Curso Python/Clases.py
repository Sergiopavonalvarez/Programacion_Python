

class Circulo():
    def __init__(self, radio):
        self.__establecer_radio(radio)

    @property
    def radio(self):
        print("Estoy dando el radio")
        return self.__radio

    def __establecer_radio(self, radio):
        if radio >= 0:
            self.__radio = radio
        else:
            print("El radio debe ser positivo")
            self.__radio = 0

c1 = Circulo(-5)
print(c1.radio)

