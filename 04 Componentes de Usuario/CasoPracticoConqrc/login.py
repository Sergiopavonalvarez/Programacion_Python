import os
import sys
from PySide6.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QApplication, QPushButton
from PySide6.QtGui import QPixmap, QIcon, QAction
import recursos_rc


class VentanaPrincipal(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setEchoMode(QLineEdit.Password)
        self.mostrar = QIcon(":/nover.png")
        self.ocultar = QIcon(":/ver.jpeg")

        self.boton = QPushButton()
        self.boton.setIcon(QIcon(":/nover.png"))  # Agregamos un icono al botón
        self.boton.setFlat(True)

        self.cambiarVisibilidad = self.addAction(self.ocultar, QLineEdit.TrailingPosition)
        self.cambiarVisibilidad.triggered.connect(self.visivilidad)

    def visivilidad(self):
        if self.echoMode() == QLineEdit.Password:
            self.setEchoMode(QLineEdit.Normal)
            self.cambiarVisibilidad.setIcon(self.ocultar)
        else:
            self.setEchoMode(QLineEdit.Password)
            self.cambiarVisibilidad.setIcon(self.mostrar)

        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.setWindowTitle("Contraseña")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
