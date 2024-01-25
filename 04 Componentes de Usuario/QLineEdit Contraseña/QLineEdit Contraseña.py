from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QLineEdit
from PySide6.QtGui import QIcon, QKeySequence

import DI_U04_A03_03


class EditorContrasena(QLineEdit):
    def _init_(self,parent=None):
        super()._init_(parent)
        self.mostrar = QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/QLineEdit/593374.png")
        self.ocultar = QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/QLineEdit/images.png")

        self.laber=self.setEchoMode(QLineEdit.Password)

        self.setPlaceholderText("Introduce tu contraseña")
        self.accion_cambiar_visibilidad = self.addAction(self.mostrar, QLineEdit.TrailingPosition)

        self.accion_cambiar_visibilidad.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)

        self.contraseña_visible=False
        self.setWindowIcon(QIcon('self.mostrar'))

    def cambiar_visibilidad(self):
        if not self.contraseña_visible:
            self.setEchoMode(QLineEdit.Normal)
            self.contraseña_visible=True
            self.accion_cambiar_visibilidad.setIcon(self.ocultar)
            self.setWindowIcon(QIcon('self.ocultar'))
        else:
            self.setEchoMode(QLineEdit.Password)
            self.contraseña_visible=False
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)
            self.setWindowIcon(QIcon('self.mostrar'))

if __name__ == "_main_":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    ventana = EditorContrasena()
    ventana.show()
    sys.exit(app.exec_())










