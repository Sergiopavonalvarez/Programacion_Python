import os
import platform

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QLabel, QDockWidget, QTextEdit, QWhatsThis)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Ventana principal con menú, barra de herramientas  y barra de estado")

        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        ruta_a_icono1 = os.path.join(os.path.dirname(__file__),
                                     "/00 Ejercicios/04 Caso Practico 04//ayuda.png")
        ruta_a_icono2 = os.path.join(os.path.dirname(__file__),
                                     "/00 Ejercicios/04 Caso Practico 04//imprimir.png")
        accion = QAction(QIcon(ruta_a_icono2), "Imprimir por consola", self)
        accion2 = QAction(QIcon(ruta_a_icono1), "Que es esto?", self)

        accion.setWhatsThis(
            "“Al ejecutar esta acción, se añadirá el texto “Acción pulsada” en el dock. Se puede lanzar por Menú > Imprimir en dock, con Ctrl+p, o haciendo clic en el botón correspondiente de la barra de herramientas")
        accion.setStatusTip("Modo de ayuda")

        accion.setShortcut(QKeySequence())
        accion.triggered.connect(self.imprimir_por_consola)
        accion2.triggered.connect(self.entrar_modo_ayuda)
        menu.addAction(accion2)
        menu.addAction(accion)

        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(accion)
        barra_herramientas.addAction(accion2)
        self.addToolBar(barra_herramientas)

        self.widget_flotante = QDockWidget()

        self.widget_flotante.setWindowTitle("Componente base 1")

        self.widget_flotante.setWidget(QTextEdit(""))

        self.widget_flotante.setMinimumWidth(50)

        self.addDockWidget(Qt.RightDockWidgetArea, self.widget_flotante)

    def imprimir_por_consola(self):

        self.widget_flotante.setWidget(QTextEdit("pulsado"))

    def entrar_modo_ayuda(self):
        if (QWhatsThis.inWhatsThisMode()):
            QWhatsThis().leaveWhatsThisMode()
        else:
            QWhatsThis().enterWhatsThisMode()


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
