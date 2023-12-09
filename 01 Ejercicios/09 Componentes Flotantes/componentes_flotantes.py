import os.path
import sys

from PySide6.QtGui import QIcon, QAction, QKeySequence, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel, QDockWidget, QTextEdit


# Define una clase llamada comp_flotantes que hereda de QMainWindow
class comp_flotantes(QMainWindow):
    # Constructor de la clase
    def __init__(self):
        # Llama al constructor de la clase base (QMainWindow)
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Componente flotante")

        # Crea una barra de menús y un menú
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")

        # Crea una acción para el menú con un atajo de teclado y conecta la acción a la función imprimir_consola
        accion = QAction(QIcon("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/09 Componentes Flotantes/imagen.png"), "Imprimir...", self)
        accion.setShortcut(QKeySequence("ctrl+p"))
        accion.triggered.connect(self.imprimir_consola)
        menu.addAction(accion)

        # Crea una barra de herramientas y agrega la acción a la barra de herramientas
        barra_herramientas = QToolBar("Barra herramientas1")
        barra_herramientas.addAction(accion)
        self.addToolBar(barra_herramientas)

        # Crea una barra de estado con una etiqueta permanente y muestra un mensaje temporal
        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget(QLabel("D.I"))
        barra_estado.showMessage("Listo...", 5000)

        # Crea un componente flotante (dock)
        dock1 = QDockWidget()

        # Agrega un título al componente flotante
        dock1.setWindowTitle("Componente base 1")

        # Asigna un componente (en este caso, un cuadro de texto vacío) al componente flotante
        dock1.setWidget(QTextEdit(""))

        # Asigna un ancho mínimo al componente flotante
        dock1.setMinimumWidth(50)

        # Coloca el componente flotante a la derecha de la ventana principal
        self.addDockWidget(Qt.RightDockWidgetArea, dock1)

        # Establece un widget de etiqueta como widget central de la ventana principal
        self.setCentralWidget(QLabel("Comp Principal"))

    # Función que se llama cuando se activa la acción de imprimir en la consola
    def imprimir_consola(self):
        print("Get Back Jo Jo")

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication([])

    # Crea una instancia de la clase comp_flotantes
    ventana1 = comp_flotantes()

    # Muestra la ventana
    ventana1.show()

    # Ejecuta la aplicación
    sys.exit(app.exec())



