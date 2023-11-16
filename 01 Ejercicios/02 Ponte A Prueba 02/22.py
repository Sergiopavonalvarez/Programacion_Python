import sys
# from typing import Optional
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
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText("introdcue el texto")
        self.input_b.setPlaceholderText("introdcue el texto")
        layout.addWidget(QLabel("Variable A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Variable B"))
        layout.addWidget(self.input_b)
        self.intercambio_Boton = QPushButton("intercambio")
        layout.addWidget(self.intercambio_Boton)
        self.intercambio_Boton.clicked.connect(self.intercambio_variables)
        central_widget.setLayout(layout)

    def intercambio_variables(self):
        valor_a = self.input_a.text()
        valor_b = self.input_b.text()
        self.input_a.setText(valor_b)
        self.input_b.setText(valor_a)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Intercambio()
    ventana1.show()
    sys.exit(app.exec())
