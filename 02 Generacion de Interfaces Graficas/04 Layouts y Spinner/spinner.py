import sys

from PySide6.QtWidgets import QMainWindow, QComboBox, QApplication, QLabel, QPushButton


class spinner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.spinner=QComboBox(self)
        lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.spinner.addItems(lista)
        self.resultado=QLabel(self)

        self.boton=QPushButton("boton", self)
        self.boton.move(100, 0)
        self.boton.clicked.connect(self.mostrar)

        self.resultado.move(100, 100)


    def mostrar(self):
        self.resultado.setText(self.spinner.currentText())

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = spinner()
    ventana1.show()
    sys.exit(app.exec())


