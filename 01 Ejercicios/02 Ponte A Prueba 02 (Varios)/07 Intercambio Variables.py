import sys
# from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton


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

        # Crea dos cuadros de entrada para los textos y establece texto de marcador de posición
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText("Introduce el texto para A")
        self.input_b.setPlaceholderText("Introduce el texto para B")

        # Agrega etiquetas y cuadros de entrada al diseño vertical
        layout.addWidget(QLabel("Variable A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Variable B"))
        layout.addWidget(self.input_b)

        # Crea un botón de intercambio y lo agrega al diseño vertical
        self.intercambio_Boton = QPushButton("Intercambio")
        layout.addWidget(self.intercambio_Boton)

        # Conecta la señal de clic del botón a la función 'intercambio_variables'
        self.intercambio_Boton.clicked.connect(self.intercambio_variables)

        # Establece el diseño vertical como el diseño del widget central
        central_widget.setLayout(layout)

    # Función que realiza el intercambio de textos entre A y B
    def intercambio_variables(self):
        valor_a = self.input_a.text()
        valor_b = self.input_b.text()
        self.input_a.setText(valor_b)
        self.input_b.setText(valor_a)

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
