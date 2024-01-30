import sys

from PySide6.QtWidgets import QLineEdit, QApplication
from PySide6.QtGui import QIcon, QKeySequence

import DI_U04_A03_03


class editorContrasena(QLineEdit):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)
        self.mostrar = QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/QLineEdit Contraseña/593374.png")
        self.ocultar = QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/QLineEdit Contraseña/oculto_1.png")

        self.setEchoMode(QLineEdit.Password)

        self.setPlaceholderText("Contraseña")
        self.accion_cambiar_visibilidad = self.addAction(self.mostrar, QLineEdit.TrailingPosition)
        self.accion_cambiar_visibilidad.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)
        self.contraseña_visible = False
        self.setWindowIcon(QIcon(
            "C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/QLineEdit Contraseña/593374.png"))



    def cambiar_visibilidad(self):

        if not self.contraseña_visible:
            self.setWindowIcon(self.ocultar)
            self.setEchoMode(QLineEdit.Normal)
            self.accion_cambiar_visibilidad.setIcon(self.ocultar)
            self.contraseña_visible = True
        else:
            self.setWindowIcon(self.mostrar)
            self.setEchoMode(QLineEdit.Password)
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)
            self.contraseña_visible = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = editorContrasena()
    ventana.show()
    sys.exit(app.exec())