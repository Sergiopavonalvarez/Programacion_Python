import os 
from PySide6.QtWidgets import (QMainWindow, 
                               QApplication, QToolBar)

from PySide6.QtGui import (QAction, 
                           QKeySequence, QIcon)

#Ventana Principal

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        #Titulo Ventana
        self.setWindowTitle("Ventana con Menú")

        ruta_icono = os.path.join(os.path.dirname(__file__),"C://Users//pavon//Documents//VS Code//Python//00 Ejercicios//07 Ejercicio barra de herramientas//descarga.png")

        #Añadimos a la accion un icono
        accion = QAction(QIcon(ruta_icono),"&Imprimir",self)
        accion.setShortcut(QKeySequence("ctrl+p"))
        accion.triggered.connect(self.imprimir_consola)

        #Creamos la barra herramientas 
        barra_herramientas = QToolBar("Barra herramientas")

        #Añadimosel QAction a la barra herramientas
        barra_herramientas.addAction(accion)

        #Añadimos la barra de herramientas a la aplicacion
        self.addToolBar(barra_herramientas)

    def imprimir_consola(self):
        print("Accion lanzada a traves del menu")


if __name__ == '__main__':
    app = QApplication([])

    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()
