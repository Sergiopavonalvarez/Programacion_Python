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

        # Crea un cuadro de entrada para la cantidad en euros y establece un validador para aceptar solo enteros
        self.input_a = QLineEdit()
        self.input_a.setPlaceholderText("Introduce en euros")
        self.input_a.setValidator(QtGui.QIntValidator())

        # Agrega etiquetas y cuadros de entrada al diseño vertical
        layout.addWidget(QLabel("Euros"))
        layout.addWidget(self.input_a)

        # Crea un botón de cálculo y lo agrega al diseño vertical
        self.Calculo_Boton = QPushButton("CALCULAR A PESETAS")
        layout.addWidget(self.Calculo_Boton)

        # Conecta la señal de clic del botón a la función 'intercambio_variables'
        self.Calculo_Boton.clicked.connect(self.intercambio_variables)

        # Establece el diseño vertical como el diseño del widget central
        central_widget.setLayout(layout)

    # Función que realiza la conversión de euros a pesetas y muestra el resultado en la consola
    def intercambio_variables(self):
        valor_a = int(self.input_a.text())
        valor_b = (valor_a * 1000) / 6
        print(valor_b)

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
