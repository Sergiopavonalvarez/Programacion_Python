import sys

from PySide6 import QtGui
#from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class Intercambio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio")
        self.setGeometry(1000, 250, 400, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.input_a = QLineEdit()
        self.input_a.setPlaceholderText("Introduce en euros")
        self.input_a.setValidator(QtGui.QIntValidator())
        layout.addWidget(QLabel("Euros"))
        layout.addWidget(self.input_a)
        self.setLayout(layout)
        self.Calculo_Boton = QPushButton("CALCULAR A PESETAS")
        layout.addWidget(self.Calculo_Boton)
        self.Calculo_Boton.clicked.connect(self.intercambio_variables)
        central_widget.setLayout(layout)
    def intercambio_variables(self):
        valor_a = int(self.input_a.text())
        valor_b=(valor_a*1000)/6
        print(valor_b)

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Intercambio()
    ventana1.show()
    sys.exit(app.exec())
