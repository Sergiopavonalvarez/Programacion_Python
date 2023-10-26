import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QDialog, \
    QGridLayout
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(1000, 250, 400, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText("Usuario")
        self.input_b.setPlaceholderText("Contraseña")

        layout.addWidget(QLabel("Usuario:"), 0, 0)
        layout.addWidget(self.input_a, 0, 1)
        layout.addWidget(QLabel("Contraseña:"), 1, 0)
        layout.addWidget(self.input_b, 1, 1)
        self.entrar_Boton = QPushButton("Entrar")
        self.entrar_Boton.setFixedWidth(200)
        layout.addWidget(self.entrar_Boton, 2, 1, 1, 2)

        self.entrar_Boton.clicked.connect(self.entrar)
        central_widget.setLayout(layout)

    def entrar(self):
        usuario="Sergio"
        contraseña="1234"
        valor_a = self.input_a.text()
        valor_b = self.input_b.text()
        if (usuario==valor_a and contraseña==valor_b):
            self.input_a.clear()
            self.input_b.clear()
            self.input_a.setPlaceholderText("Usuario correcto")
            self.input_b.setPlaceholderText("Usuario correcto")
            ventana_dialogo = QDialog(self)
            ventana_dialogo.setWindowTitle("Ventana de dialogo")
            ventana_dialogo.resize(400, 200)
            etiqueta1 = QLabel("Estas dentro!!!", ventana_dialogo)
            fuente = etiqueta1.font()
            fuente.setPointSize(30)
            etiqueta1.setFont(fuente)
            ventana_dialogo.exec()
        else:
            self.input_a.clear()
            self.input_b.clear()
            self.input_a.setPlaceholderText("Usuario o contraseña incorrecto")
            self.input_b.setPlaceholderText("Usuario o contraseña incorrecto")

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Login()
    ventana1.show()
    sys.exit(app.exec())
