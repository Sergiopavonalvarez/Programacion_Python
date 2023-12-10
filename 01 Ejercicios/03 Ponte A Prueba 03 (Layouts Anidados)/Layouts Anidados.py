import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, QVBoxLayout

# Define una clase llamada layouts_anidados que hereda de QMainWindow
class layouts_anidados(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Layouts anidados")
        self.setGeometry(1000, 250, 400, 100)

        # Crea un layout horizontal principal
        layout_horizontal1 = QHBoxLayout()

        # Crea un componente principal (QWidget) y establece el layout horizontal como su diseño
        componente_principal = QWidget()
        componente_principal.setLayout(layout_horizontal1)
        self.setCentralWidget(componente_principal)

        # Crea un layout vertical y agrégalo al layout horizontal principal
        layout_vertical = QVBoxLayout()
        layout_horizontal1.addLayout(layout_vertical)

        # Agrega botones al layout vertical
        layout_vertical.addWidget(QPushButton('V1'))
        layout_vertical.addWidget(QPushButton('V2'))
        layout_vertical.addWidget(QPushButton('V3'))
        layout_vertical.addWidget(QPushButton('V4'))

        # Crea un layout horizontal y agrégalo al layout horizontal principal
        layout_horizontal = QHBoxLayout()
        layout_horizontal1.addLayout(layout_horizontal)

        # Agrega botones al layout horizontal
        layout_horizontal.addWidget(QPushButton("H1"))
        layout_horizontal.addWidget(QPushButton("H2"))
        layout_horizontal.addWidget(QPushButton("H3"))
        layout_horizontal.addWidget(QPushButton("H4"))

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication([])

    # Crea una instancia de la clase layouts_anidados
    ventana = layouts_anidados()

    # Muestra la ventana
    ventana.show()

    # Ejecuta la aplicación
    app.exec()
