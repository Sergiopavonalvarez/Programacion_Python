import sys

from PySide6.QtWidgets import QMainWindow, QComboBox, QApplication, QLabel, QPushButton


class Spinner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.spinner = QComboBox(self)
        lista = ["Meses del año", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.spinner.addItems(lista)

        self.resultado = QLabel(self)

        self.boton = QPushButton("Boton", self)
        self.boton.move(100, 0)
        self.boton.clicked.connect(self.mostrar)

        self.resultado.move(100, 100)

    def mostrar(self):
        # Obtén el índice seleccionado en lugar de imprimir el QLabel directamente
        indice_seleccionado = self.spinner.currentIndex()
        mes_elegido = self.spinner.itemText(indice_seleccionado)
        print("El mes elegido es:", mes_elegido)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana1 = Spinner()
    ventana1.show()
    sys.exit(app.exec())