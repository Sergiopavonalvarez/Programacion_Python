import os
import platform

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QLabel, QDockWidget, QTextEdit)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal con menú, barra de herramientas y barra de estado")

        #Barra de menu
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        #ruta_a_icono = os.path.join(os.path.dirname( __file__), "images/console.png")
        #accion = QAction(QIcon(ruta_a_icono), "Imprimir por consola", self)
        accion = QAction("Imprimir por consola", self)
        accion.setWhatsThis( "Al pulsar sobre el botón se imprimirá un texto por consola")
        accion.setStatusTip("Imprimir por consola")
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(accion)

        #Barra de herramientas
        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(accion)
        self.addToolBar(barra_herramientas)

        # Barra de estado
        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        barra_estado.showMessage("Listo. Esperando acción ...", 3000)

        # Creamos un componente flotante
        dock1 = QDockWidget()
        # Agregamos título a este componente
        dock1.setWindowTitle("Componente base 1")
        # Asignamos el componente que contendrà
        dock1.setWidget(QTextEdit(""))
        # Le asignamos una anchura mínima de 50
        dock1.setMinimumWidth(50)
        # Lo posicionamos a la derecha de la ventana principal
        self.addDockWidget(Qt.RightDockWidgetArea, dock1)

        self.setCentralWidget(QLabel("Componente principal"))

    def imprimir_por_consola(self):
        print("Acción lanzada a través del menú, del atajo o de la barra de herramientas")


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
