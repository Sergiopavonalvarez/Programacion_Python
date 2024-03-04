from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QIcon, QKeySequence

import componente.recursos as recursos

class EditorContraseña(QLineEdit):

    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(self.parent)

        self.mostrar = QIcon(':/recursos/mostrar')
        self.ocultar = QIcon(':/recursos/ocultar')

        self.setEchoMode(QLineEdit.Password)
        self.accion_cambiar_visibilidad = self.addAction(self.mostrar, QLineEdit.TrailingPosition)
        self.accion_cambiar_visibilidad.setShortcut(QKeySequence("Ctrl+m"))
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)
        self.contraseña_visible = False

    def cambiar_visibilidad(self):
        if not self.contraseña_visible:
            self.setEchoMode(QLineEdit.Normal)
            self.contraseña_visible = True
            self.accion_cambiar_visibilidad.setIcon(self.ocultar)
        else:
            self.setEchoMode(QLineEdit.Password)
            self.contraseña_visible = False
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)