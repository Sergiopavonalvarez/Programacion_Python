import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
import tu_archivo_rc
#pyside6-rcc tu_archivo.qrc -o tu_archivo_rc.py

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo PySide6")

        # Crear dos campos de texto
        self.text_edit1 = QLineEdit()
        self.text_edit2 = QLineEdit()

        # Crear un botón
        self.button = QPushButton()
        self.button.setIcon(QIcon(":/mano.png"))

        self.button.setStyleSheet("""
                    QPushButton {
                        font-size: 20px; /* Tamaño del texto */
                        min-width: 100px; /* Ancho mínimo del botón */
                        min-height: 100px; /* Altura mínima del botón */
                        border: none; /* Quitar el borde */
                        background-color: transparent; /* Fondo transparente */
                        background-position: center; /* Posición del fondo */
                        background-repeat: no-repeat; /* No repetir el fondo */
                    }
                    QPushButton:hover {
                        background-color: #e6e6e6; /* Cambiar el color de fondo al pasar el ratón */
                    }
                """)

        # Conectar el botón a una función
        self.button.clicked.connect(self.mostrar_texto)

        # Configurar el diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit1)
        layout.addWidget(self.text_edit2)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def mostrar_texto(self):
        # Obtener el texto de los campos de texto y mostrarlos en la consola
        texto1 = self.text_edit1.text()
        texto2 = self.text_edit2.text()
        print("Texto 1:", texto1)
        print("Texto 2:", texto2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
