import sys

from PySide6 import QtGui
#from typing import Optional
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

        # Crea dos cuadros de entrada para los números A y B, y establece un validador para aceptar solo enteros
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText("Introduce un número para A")
        self.input_b.setPlaceholderText("Introduce un número para B")
        self.input_a.setValidator(QtGui.QIntValidator())
        self.input_b.setValidator(QtGui.QIntValidator())

        # Agrega etiquetas y cuadros de entrada al diseño vertical
        layout.addWidget(QLabel("Variable A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Variable B"))
        layout.addWidget(self.input_b)

        # Crea un botón de cálculo y lo agrega al diseño vertical
        self.Calculo_Boton = QPushButton("CALCULAR")
        layout.addWidget(self.Calculo_Boton)

        # Conecta la señal de clic del botón a la función 'calculos'
        self.Calculo_Boton.clicked.connect(self.calculos)

        # Establece el diseño vertical como el diseño del widget central
        central_widget.setLayout(layout)

    # Función que realiza cálculos e imprime los resultados en la consola
    def calculos(self):
        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())
        valor_suma = valor_a + valor_b
        valor_division = valor_a / valor_b
        valor_resta = valor_a - valor_b
        valor_multiplicacion = valor_a * valor_b
        print(f"La suma de A y B es: ", valor_suma)
        print(f"La división de A y B es: ", valor_division)
        print(f"La resta de A y B es: ", valor_resta)
        print(f"La multiplicación de A y B es: ", valor_multiplicacion)

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
