import os
import platform

from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QToolBar
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMenuBar, \
    QToolBar, QStatusBar




#Definición de la Clase VentanaPrincipal
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Configuración inicial de la ventana
        self.setWindowTitle("Ventana principal con menú, barra de herramientas y barra de estado")
        
        #Barra de menú
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")  # "&" indica el atajo de teclado Alt + M
        #Creación de la acción "Imprimir por consola"
        accion = QAction("Imprimir", self)
        #Configuración adicional de la acción
        accion.setWhatsThis("Al pulsar sobre el botón se imprimirá un texto por consola")
        accion.setStatusTip("Imprimir por consola")
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion.triggered.connect(self.imprimir_por_consola)
        #Agregar la acción al menú
        menu.addAction(accion)
        #Menu salir
        menu2=barra_menus.addMenu("&Salir")
        accion_salir=QAction("Salir",self)
        accion_salir.triggered.connect(self.close)
        menu2.addAction(accion_salir)

        #Barra de herramientas
        barra_herramientas = QToolBar("Barra de herramientas 1")
        self.addToolBar(barra_herramientas)
        barra_herramientas.addAction(accion)
        # Agregar la barra de herramientas a la ventana
        self.addToolBar(barra_herramientas)

        #Barra de estado
        barra_estado = self.statusBar()
        # Agregar un componente permanente con la plataforma (en este caso, el nombre del sistema operativo)
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        # Mostrar un mensaje en la barra de estado durante 3 segundos
        barra_estado.showMessage("Listo. Esperando acción...", 3000)

    # Método llamado cuando se activa la acción "Imprimir por consola"
    def imprimir_por_consola(self):
        print("Acción lanzada a través del menú, del atajo o de la barra de herramientas")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
