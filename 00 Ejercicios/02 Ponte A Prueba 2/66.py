import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial, \
    QProgressBar


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de volumen")

        # Creamos el contenedor principal
        contenedor = QWidget()

        # Creamos la etiqueta
        self.etiqueta = QLabel("Valor: 0 dB")
        self.etiqueta.setAlignment(Qt.AlignCenter)

        # Creamos el QDial
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)

        # Creamos el indicador de volumen
        self.indicador = QProgressBar()
        self.indicador.setMaximum(100)

        # Creamos los botones
        self.boton_aumentar = QPushButton("+")
        self.boton_aumentar.setMaximumWidth(30)
        self.boton_disminuir = QPushButton("-")
        self.boton_disminuir.setMaximumWidth(30)

        # Organizamos los elementos en el contenedor
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta)
        layout.addWidget(self.dial)
        layout.addWidget(self.indicador)
        layout.addWidget(self.boton_aumentar)
        layout.addWidget(self.boton_disminuir)
        contenedor.setLayout(layout)

        # Establecemos el contenedor como el widget central de la ventana
        self.setCentralWidget(contenedor)

        # Conectamos los eventos
        self.dial.valueChanged.connect(self.actualizar_valor)
        self.boton_aumentar.clicked.connect(self.aumentar_volumen)
        self.boton_disminuir.clicked.connect(self.disminuir_volumen)

    def actualizar_valor(self):
        # Actualizamos el valor de la etiqueta y el indicador
        self.etiqueta.setText(f"Valor: {self.dial.value()} dB")
        self.indicador.setValue(self.dial.value())

    def aumentar_volumen(self):
        # Aumentamos el valor del QDial y el indicador
        self.dial.setValue(self.dial.value() + 1)
        self.indicador.setValue(self.dial.value())

    def disminuir_volumen(self):
        # Disminuimos el valor del QDial y el indicador
        self.dial.setValue(self.dial.value() - 1)
        self.indicador.setValue(self.dial.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())