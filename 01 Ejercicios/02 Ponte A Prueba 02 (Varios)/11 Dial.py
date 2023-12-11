import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial


# Define una clase llamada Ventana que hereda de QMainWindow
class Ventana(QMainWindow):
    # Constructor de la clase
    def __init__(self):
        # Llama al constructor de la clase base (QMainWindow)
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Control de volumen")

        # Crea un contenedor para la ventana
        contenedor = QWidget()

        # Crea una etiqueta, un dial y dos botones para la interfaz
        self.etiqueta_db = QLabel("Valor: 0 dB")
        self.etiqueta_db.setAlignment(Qt.AlignCenter)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.boton_aumentar = QPushButton("+")
        self.boton_aumentar.setMaximumWidth(30)
        self.boton_disminuir = QPushButton("-")
        self.boton_disminuir.setMaximumWidth(30)

        # Crea un diseño vertical y agrega los widgets a la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_db)
        layout.addWidget(self.dial)
        layout.addWidget(self.boton_aumentar)
        layout.addWidget(self.boton_disminuir)
        contenedor.setLayout(layout)

        # Establece el contenedor como el widget central de la ventana
        self.setCentralWidget(contenedor)

        # Conecta las señales de los widgets a las funciones correspondientes
        self.dial.valueChanged.connect(self.actualizar_valor)
        self.boton_aumentar.clicked.connect(self.aumentar_volumen)
        self.boton_disminuir.clicked.connect(self.disminuir_volumen)

    # Función que actualiza la etiqueta con el valor del dial
    def actualizar_valor(self):
        self.etiqueta_db.setText(f"Valor: {self.dial.value()} dB")

    # Funciones para aumentar y disminuir el valor del dial
    def aumentar_volumen(self):
        self.dial.setValue(self.dial.value() + 1)

    def disminuir_volumen(self):
        self.dial.setValue(self.dial.value() - 1)

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication(sys.argv)
    # Crea una instancia de la clase Ventana
    ventana = Ventana()
    # Muestra la ventana
    ventana.show()
    # Ejecuta la aplicación
    sys.exit(app.exec())
