from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QLineEdit

import DI_U04_A03_03

class EditorContraseña(QLineEdit):


    def __init__(self, parent=None):
        self.parent=parent
        super().__init__(parent)

        self.mostrar=QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/QLineEdit/593374.png")
        self.ocultar=QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/QLineEdit/images.png")

        self.label=self.setEchoMode(QLineEdit.Password)

        self.label=self.setPlaceholderText(("Introduce tu contraseña..."))
        self.accion_cambiar_visibilidad=self.addAction(self.mostrar, QLineEdit.TrailingPosition)#Agrega una accion (un icono con el enlace)
        #Al QLineEdit en la posicion del final (trailing)
        #Esta accion se utiliza para cambiar entre mostrar y ocultar la contrasela

        self.accion.cambiar_visibilidad.selShortcut(QKeySequence("Ctrl+M"))
        self.accion_cambiar_visibilidad.triggered.connect(self.accion_cambiar_visibilidad)

        self.contraseña_visible=False
        self.setWindowIcon(QIcon('self.mostrar'))
    def cambiar_visibilidad(self):
        if not self.contraseña_visible:
            self.setEchoMode(QLineEdit.Normal)
            self.contraseña_visible=True
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)
            self.setWindowIcon(QIcon('self.ocultar'))
        else:
            self.setEchoMode(QLineEdit.Password)
            self.contraseña_visible=False
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)
            self.setWindowIcon(QIcon('self.mostrar'))



