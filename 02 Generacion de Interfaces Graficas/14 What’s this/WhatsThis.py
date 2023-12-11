import os
import platform

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QLabel, QDockWidget, QTextEdit, QWhatsThis)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal con menú, barra de herramientas  y barra de estado")

        #Barra de menu

        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        #ruta_a_icono = os.path.join(os.path.dirname(__file__), "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/02 Generacion de Interfaces Graficas/12 What’s this/imagen.png")
        accion = QAction("Imprimir", self)
        accion2=QAction("Modo Ayuda",self)
        accion.setWhatsThis("Al pulsar sobre el botón se imprimirá un texto por consola")
        accion2.setStatusTip("Modo de ayuda")
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion2.setShortcut(QKeySequence("Ctrl+n"))
        accion.triggered.connect(self.imprimir_por_consola)
        accion2.triggered.connect(self.entrar_modo_ayuda)
        menu.addAction(accion)
        menu.addAction(accion2)


        #Barra de herramientas

        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(accion)
        barra_herramientas.addAction(accion2)
        self.addToolBar(barra_herramientas)


        #Arra de estado

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
        
    def entrar_modo_ayuda(self):
        if(QWhatsThis.inWhatsThisMode()):
            QWhatsThis().leaveWhatsThisMode()
        else:
            QWhatsThis().enterWhatsThisMode()



if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
