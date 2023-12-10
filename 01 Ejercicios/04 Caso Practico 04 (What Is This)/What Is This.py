import os
import platform

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QLabel, QDockWidget, QTextEdit, QWhatsThis)

# Define una clase llamada VentanaPrincipal que hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Llama al constructor de la clase base (QMainWindow)
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Ventana principal con menú, barra de herramientas y barra de estado")

        # Crea la barra de menús
        barra_menus = self.menuBar()

        # Crea un menú llamado "Menu"
        menu = barra_menus.addMenu("&Menu")
    

        # Define las rutas a los iconos
        ruta_a_icono1 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/PyCharm/Programacion_Python/01 Ejercicios/04 Caso Practico 04/ayuda.png")
        ruta_a_icono2 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/PyCharm/Programacion_Python/01 Ejercicios/04 Caso Practico 04/imprimir.png")

        # Crea acciones con iconos y texto para el menú
        accion = QAction(QIcon(ruta_a_icono2), "Imprimir por consola", self)
        accion2 = QAction(QIcon(ruta_a_icono1), "Que es esto?", self)

        # Configura información adicional para la acción 1
        accion.setWhatsThis("Al ejecutar esta acción, se añadirá el texto 'Acción pulsada' en el dock. Se puede lanzar por Menú > Imprimir en dock, con Ctrl+p, o haciendo clic en el botón correspondiente de la barra de herramientas")
        accion.setStatusTip("Modo de ayuda")
        accion.setShortcut(QKeySequence())

        # Conecta las acciones a sus funciones correspondientes
        accion.triggered.connect(self.imprimir_por_consola)
        accion2.triggered.connect(self.entrar_modo_ayuda)

        # Agrega las acciones al menú
        menu.addAction(accion2)
        menu.addAction(accion)

        # Crea una barra de herramientas y agrega las acciones a la barra
        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(accion)
        barra_herramientas.addAction(accion2)
        self.addToolBar(barra_herramientas)

        # Crea un widget flotante (QDockWidget)
        self.widget_flotante = QDockWidget()

        # Configura el widget flotante
        self.widget_flotante.setWindowTitle("Componente base 1")
        self.widget_flotante.setWidget(QTextEdit(""))
        self.widget_flotante.setMinimumWidth(50)

        # Agrega el widget flotante a la derecha de la ventana principal
        self.addDockWidget(Qt.RightDockWidgetArea, self.widget_flotante)

    # Función que se ejecuta al hacer clic en la acción "Imprimir por consola"
    def imprimir_por_consola(self):
        self.widget_flotante.setWidget(QTextEdit("pulsado"))

    # Función que entra o sale del modo de ayuda al hacer clic en la acción "Que es esto?"
    def entrar_modo_ayuda(self):
        if QWhatsThis.inWhatsThisMode():
            QWhatsThis().leaveWhatsThisMode()
        else:
            QWhatsThis().enterWhatsThisMode()


# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication([])

    # Crea una instancia de la clase VentanaPrincipal
    ventana1 = VentanaPrincipal()

    # Muestra la ventana principal
    ventana1.show()

    # Ejecuta la aplicación
    app.exec()

