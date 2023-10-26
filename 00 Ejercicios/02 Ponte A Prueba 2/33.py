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


        self.input_a.setValidator(QtGui.QIntValidator())  # Acepta solo números enteros
        self.input_b.setValidator(QtGui.QIntValidator())  # Acepta solo números enteros

        layout.addWidget(QLabel("Numero A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Numero B"))
        layout.addWidget(self.input_b)

        self.setLayout(layout)

        central_widget.setLayout(layout)




        self.etiqueta1 = QLabel("", self)


        layout.addWidget(self.etiqueta1)

        central_widget.setLayout(layout)





        self.Calculo_sumar = QPushButton("Sumar")
        layout.addWidget(self.Calculo_sumar)
        self.Calculo_sumar.clicked.connect(self.sumar)

        central_widget.setLayout(layout)

        self.Calculo_restar = QPushButton("Restar")
        layout.addWidget(self.Calculo_restar)
        self.Calculo_restar.clicked.connect(self.restar)

        central_widget.setLayout(layout)

        self.Calculo_multi = QPushButton("Multiplicar")
        layout.addWidget(self.Calculo_multi)
        self.Calculo_multi.clicked.connect(self.multi)

        central_widget.setLayout(layout)

        self.Calculo_div = QPushButton("Dividir")
        layout.addWidget(self.Calculo_div)
        self.Calculo_div.clicked.connect(self.divi)

        central_widget.setLayout(layout)





    def sumar(self):

        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())


        valor_suma = valor_a + valor_b

        self.etiqueta1.setText((str)(valor_suma))

    def restar(self):

        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())


        valor_suma = valor_a - valor_b

        self.etiqueta1.setText((str)(valor_suma))


    def divi(self):

        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())


        valor_suma = valor_a / valor_b

        self.etiqueta1.setText((str)(valor_suma))

    def multi(self):

        valor_a = int(self.input_a.text())
        valor_b = int(self.input_b.text())


        valor_suma = valor_a * valor_b

        self.etiqueta1.setText((str)(valor_suma))







if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Intercambio()
    ventana1.show()
    sys.exit(app.exec())