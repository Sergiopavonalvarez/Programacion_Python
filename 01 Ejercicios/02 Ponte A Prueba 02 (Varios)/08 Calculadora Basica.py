import sys

from PySide6 import QtGui
# from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton


# Define una clase llamada Intercambio que hereda de QMainWindow
class Intercambio(QMainWindow):
    # Constructor de la clase
    def __init__(self):
        # Llama al constructor de la clase base (QMainWindow)
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Ejercicio")
        self.setGeometry(1000, 250, 400, 200)

        # Crea un widget central y lo establece como el widget central de la ventana
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crea un diseño vertical
        layout = QVBoxLayout()

        # Crea dos cuadros de entrada para los números y establece validadores para aceptar solo enteros
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setValidator(QtGui.QIntValidator())
        self.input_b.setValidator(QtGui.QIntValidator())

        # Agrega etiquetas y cuadros de entrada al diseño vertical
        layout.addWidget(QLabel("Número A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Número B"))
        layout.addWidget(self.input_b)

        # Crea una etiqueta para mostrar el resultado
        self.etiqueta1 = QLabel("", self)
        layout.addWidget(self.etiqueta1)

        # Crea botones para realizar diferentes operaciones matemáticas
        self.Calculo_sumar = QPushButton("Sumar")
        layout.addWidget(self.Calculo_sumar)
        self.Calculo_sumar.clicked.connect(self.sumar)

        self.Calculo_restar = QPushButton("Restar")
        layout.addWidget(self.Calculo_restar)
        self.Calculo_restar.clicked.connect(self.restar)

        self.Calculo_multi = QPushButton("Multiplicar")
        layout.addWidget(self.Calculo_multi)
        self.Calculo_multi.clicked.connect(self.multi)

        self.Calculo_div = QPushButton("Dividir")
        layout.addWidget(self.Calculo_div)
        self.Calculo_div.clicked.connect(self.divi)

        # Establece el diseño vertical como el diseño del widget central
        central_widget.setLayout(layout)

    # Funciones que realizan operaciones matemáticas y muestran el resultado en la etiqueta
    def sumar(self):
        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())
        valor_suma = valor_a + valor_b
        self.etiqueta1.setText(str(valor_suma))

    def restar(self):
        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())
        valor_resta = valor_a - valor_b
        self.etiqueta1.setText(str(valor_resta))

    def divi(self):
        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())
        valor_division = valor_a / valor_b
        self.etiqueta1.setText(str(valor_division))

    def multi(self):
        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())
        valor_multiplicacion = valor_a * valor_b
        self.etiqueta1.setText(str(valor_multiplicacion))

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication([])

    # Crea una instancia de la clase Intercambio
    ventana1 = Intercambio()

    # Muestra la ventana
    ventana1.show()

    # Ejecuta la aplicación
    sys.exit(app.exec())
