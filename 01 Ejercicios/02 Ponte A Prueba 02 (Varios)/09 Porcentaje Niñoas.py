import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QFrame

# Define una clase llamada Porcentaje que hereda de QMainWindow
class Porcentaje(QMainWindow):
    # Constructor de la clase
    def __init__(self):
        # Llama al constructor de la clase base (QMainWindow)
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Ejercicio 04")
        self.setGeometry(1000, 250, 400, 200)

        # Crea un widget central y lo establece como el widget central de la ventana
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crea un diseño vertical
        layout = QVBoxLayout()

        # Crea dos cuadros de combinación (combobox) para el número de niños y niñas y llena con una lista de números
        self.combo_ninos = QComboBox()
        lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.combo_ninos.addItems(lista)

        # Agrega etiquetas y cuadros de combinación al diseño vertical
        layout.addWidget(QLabel("Número de niños"))
        layout.addWidget(self.combo_ninos)

        self.combo_ninas = QComboBox()
        self.combo_ninas.addItems(lista)
        layout.addWidget(QLabel("Número de niñas"))
        layout.addWidget(self.combo_ninas)

        # Crea un botón de cálculo y lo agrega al diseño vertical
        self.calcular_boton = QPushButton("Calcular")
        layout.addWidget(self.calcular_boton)

        # Conecta la señal de clic del botón a la función 'calcular_porcentaje'
        self.calcular_boton.clicked.connect(self.calcular_porcentaje)

        # Crea una etiqueta para mostrar el resultado
        self.etiqueta1 = QLabel("", self)
        layout.addWidget(self.etiqueta1)

        # Establece el diseño vertical como el diseño del widget central
        central_widget.setLayout(layout)

    # Función que calcula el porcentaje y actualiza la etiqueta con el resultado
    def calcular_porcentaje(self):
        ninos = int(self.combo_ninos.currentText())
        ninas = int(self.combo_ninas.currentText())
        resultado = f"Porcentaje de niños: {ninos / (ninos + ninas) * 100:.2f}%"
        resultado += f"\nPorcentaje de niñas: {ninas / (ninos + ninas) * 100:.2f}%"
        self.etiqueta1.setText(resultado)

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication([])

    # Crea una instancia de la clase Porcentaje
    ventana1 = Porcentaje()

    # Muestra la ventana
    ventana1.show()

    # Ejecuta la aplicación
    sys.exit(app.exec())
