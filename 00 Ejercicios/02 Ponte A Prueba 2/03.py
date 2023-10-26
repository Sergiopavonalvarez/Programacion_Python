import sys

from PySide6 import QtGui
#from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class Intercambio(QMainWindow):
    def __init__(self):
        super().__init__()
        # Propiedades Ventana
        self.setWindowTitle("Ejercicio")
        self.setGeometry(1000, 250, 400, 200)

        # Layout Vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Campos de Entrada para A y B



        self.input_a = QLineEdit()
        self.input_b = QLineEdit()

        # Configura las propiedades para aceptar solo números enteros
        self.input_a.setPlaceholderText("Introduce un número para A")
        self.input_b.setPlaceholderText("Introduce un número para B")

        self.input_a.setValidator(QtGui.QIntValidator())  # Acepta solo números enteros
        self.input_b.setValidator(QtGui.QIntValidator())  # Acepta solo números enteros

        layout.addWidget(QLabel("Variable A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Variable B"))
        layout.addWidget(self.input_b)

        self.setLayout(layout)




        # Boton intercambio
        self.Calculo_Boton = QPushButton("CALCULAR")
        layout.addWidget(self.Calculo_Boton)
        self.Calculo_Boton.clicked.connect(self.intercambio_variables)

        central_widget.setLayout(layout)





    def intercambio_variables(self):

        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())


        valor_suma = valor_a + valor_b
        valor_division = valor_a / valor_b
        valor_resta = valor_a - valor_b
        valor_multiplicacion = valor_a * valor_b


        print(f"La suma de A y B es: ",valor_suma)
        print(f"La division de A y B es: ", valor_division)
        print(f"La resta de A y B es: ", valor_resta)
        print(f"La multiplicación de A y B es: ", valor_multiplicacion)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Intercambio()
    ventana1.show()
    sys.exit(app.exec())
