from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class primerboton (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Primer Boton")
        self.boton1=QPushButton("pulsar")
        self.setCentralWidget(self.boton1)
        self.boton1.clicked.connect(self.aaccion)


    def aaccion(self):
     print("boton pulsado")


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = primerboton()
    ventana1.show()
    app.exec()

