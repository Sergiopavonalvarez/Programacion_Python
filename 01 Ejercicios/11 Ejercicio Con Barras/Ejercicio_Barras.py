import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMenuBar, \
    QToolBar, QStatusBar


class Intercambio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio")
        self.setGeometry(1000, 250, 400, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText("Introduce el texto")
        self.input_b.setPlaceholderText("Introduce el texto")
        layout.addWidget(QLabel("Variable A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Variable B"))
        layout.addWidget(self.input_b)
        self.intercambio_Boton = QPushButton("Intercambio")
        layout.addWidget(self.intercambio_Boton)
        self.intercambio_Boton.clicked.connect(self.intercambio_variables)
        central_widget.setLayout(layout)

        # Barra de menú
        menu_bar = self.menuBar()

        # Menú Archivo
        archivo_menu = menu_bar.addMenu("Archivo")
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)
        archivo_menu.addAction(exit_action)

        # Menú Editar
        editar_menu = menu_bar.addMenu("Editar")

        # Barra de herramientas

        tool_bar = QToolBar("Herramientas")
        self.addToolBar(tool_bar)

        # Agregar el botón de Salir a la barra de herramientas
        tool_bar.addAction(exit_action)

        # Agregar el botón para el menú Editar a la barra de herramientas
        editar_action = QAction("Editar", self)
        tool_bar.addAction(editar_action)

        # Barra de estado
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

    def intercambio_variables(self):
        valor_a = self.input_a.text()
        valor_b = self.input_b.text()
        self.input_a.setText(valor_b)
        self.input_b.setText(valor_a)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Intercambio()
    ventana1.show()
    sys.exit(app.exec())
