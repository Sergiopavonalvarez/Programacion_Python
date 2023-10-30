import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial, \
    QProgressBar
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de volumen")
        contenedor = QWidget()
        self.etiqueta = QLabel("Valor: 0 dB")
        self.etiqueta.setAlignment(Qt.AlignCenter)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.indicador = QProgressBar()
        self.indicador.setMaximum(100)
        self.boton_aumentar = QPushButton("+")
        self.boton_aumentar.setMaximumWidth(30)
        self.boton_disminuir = QPushButton("-")
        self.boton_disminuir.setMaximumWidth(30)
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta)
        layout.addWidget(self.dial)
        layout.addWidget(self.indicador)
        layout.addWidget(self.boton_aumentar)
        layout.addWidget(self.boton_disminuir)
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        self.dial.valueChanged.connect(self.actualizar_valor)
        self.boton_aumentar.clicked.connect(self.aumentar_volumen)
        self.boton_disminuir.clicked.connect(self.disminuir_volumen)
    def actualizar_valor(self):
        self.etiqueta.setText(f"Valor: {self.dial.value()} dB")
        self.indicador.setValue(self.dial.value())
    def aumentar_volumen(self):
        self.dial.setValue(self.dial.value() + 1)
        self.indicador.setValue(self.dial.value())
    def disminuir_volumen(self):
        self.dial.setValue(self.dial.value() - 1)
        self.indicador.setValue(self.dial.value())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())