import os
import platform

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel



class completo(QMainWindow):
    def __init__(self):
        super().__init__()

        # Barra Menu
        barra_menu=self.menuBar()
        # Añadimos la opcion menu
        menu=barra_menu.addMenu("&Menu")
        # Creamos la accion
        accion_hola=QAction("&Imprimir Hola", self)
        accion_adios=QAction("&Imprimir Adios", self)
        # Conectamos la accion a la ranura
        accion_hola.triggered.connect(self.imprimirhola)
        accion_adios.triggered.connect(self.imprimiradios)
        # Añadimos accion al menu
        menu.addAction(accion_hola)
        menu.addAction(accion_adios)

        # WhatThis
        accion_adios.setStatusTip("Imprime Adios")
        accion_hola.setStatusTip("Imprime Hola")

        #Barra Herramientas
        barra_herramientas=QToolBar("Barra de herramientas")
        # Añadimos la accion a la barra de herramientas
        barra_herramientas.addAction(accion_hola)
        barra_herramientas.addAction(accion_adios)
        # Añadimos la barra de herramientas
        self.addToolBar(barra_herramientas)

        #Barra de estado
        barra_estado=self.statusBar()
        # Añadimos la barra de estado
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        # Mostramos el mensaje
        barra_estado.showMessage("Cargando...",3000)

    def imprimirhola(self):
        print("Hola")

    def imprimiradios(self):
        print("Adios")


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = completo()
    ventana1.show()
    app.exec()