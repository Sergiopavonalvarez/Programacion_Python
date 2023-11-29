from PySide6.QtWidgets import QMainWindow, QLineEdit, QLabel, QApplication


class copiapega(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Copia y Pega")


        self.escribir=QLineEdit(self)
        self.escribir.setFixedSize(50,30)
        self.escribir.setMaxLength(5)

        self.copia = QLabel(self)
        self.copia.setFixedSize(50,30)
        self.copia.move(60, 0)

        self.escribir.textChanged.connect(self.copia.setText)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = copiapega()
    ventana1.show()
    app.exec()
