import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QLineEdit, QVBoxLayout

# Define una clase llamada Conversor que hereda de QWidget
class Conversor(QWidget):
    # Constructor de la clase
    def __init__(self):
        # Llama al constructor de la clase base (QWidget)
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Conversor de euros a pesetas")
        self.resize(400, 200)

        # Crea etiquetas, un control deslizante (slider) y un cuadro de texto para la interfaz
        self.euros_label = QLabel("Euros:", self)
        self.pesetas_label = QLabel("Pesetas:", self)
        self.euros_slider = QSlider(Qt.Horizontal, self)
        self.euros_slider.setMinimum(0)
        self.euros_slider.setMaximum(100)
        self.pesetas_line_edit = QLineEdit(self)
        self.pesetas_line_edit.setReadOnly(True)

        # Conecta la señal de cambio de valor del slider a la función 'actualizar_pesetas'
        self.euros_slider.valueChanged.connect(self.actualizar_pesetas)

        # Crea un diseño vertical y agrega los widgets a la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.euros_label)
        layout.addWidget(self.euros_slider)
        layout.addWidget(self.pesetas_label)
        layout.addWidget(self.pesetas_line_edit)
        self.setLayout(layout)

    # Función que actualiza el valor de las pesetas en función del valor del slider
    def actualizar_pesetas(self):
        euros = self.euros_slider.value()
        pesetas = euros * 166  # Tasa de cambio ficticia
        self.pesetas_line_edit.setText(str(pesetas))
        self.euros_label.setText(str(self.euros_slider.value()))

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication(sys.argv)

    # Crea una instancia de la clase Conversor
    conv = Conversor()

    # Muestra la ventana
    conv.show()

    # Ejecuta la aplicación
    sys.exit(app.exec())
