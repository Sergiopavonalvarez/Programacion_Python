import sys

from PySide6.QtWidgets import QLabel, QWidget, QApplication


class ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hola mundo")
        self.eetiqueta1 = QLabel("Hola Mundo", self)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = ventana()
    ventana1.show()
    sys.exit(app.exec())






