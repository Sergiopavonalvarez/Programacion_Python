import os.path
import sys

from PySide6.QtGui import QIcon, QAction, QKeySequence, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel, QDockWidget, QTextEdit


class comp_flotantes(QMainWindow):
    def __init__(Self):
        super().__init__()


        Self.setWindowTitle("Componente flotante")
        barra_menus=Self.menuBar()
        menu=barra_menus.addMenu("&Menu")
        ruta=os.path.join(os.path.dirname(__file__),"C:/Users/pavon/Documents/PyCharm/Python_Dam/Python/00 Ejercicios/09 Componentes Flotantes/imagen.png")
        accion=QAction(QIcon("C:/Users/pavon/Documents/PyCharm/Python_Dam/Python/00 Ejercicios/09 Componentes Flotantes/imagen.png"),"Imprimir...",Self)
        accion.setShortcut(QKeySequence("ctrl+p"))
        accion.triggered.connect(Self.imprimir_consola)
        menu.addAction(accion)
        barra_herramientas=QToolBar("Barra herramientas1")
        barra_herramientas.addAction(accion)
        Self.addToolBar(barra_herramientas)
        barra_estado=Self.statusBar()
        barra_estado.addPermanentWidget(QLabel("D.I"))
        barra_estado.showMessage("Listo...",5000)

        # Componente flotante
        dock1=QDockWidget()
        # agregamos titulo al componente
        dock1.setWindowTitle("Componente base 1")
        # Asignamos el componente que contendrá
        dock1.setWidget(QTextEdit(""))
        # Asignamos anchura minima
        dock1.setMinimumWidth(50)
        # Ponemos a la derecha
        Self.addDockWidget(Qt.RightDockWidgetArea,dock1)

        Self.setCentralWidget(QLabel("Comp Principal"))

    def imprimir_consola(self):
        print("Get Back Jo Jo")



if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objeto ventana.
    ventana1 = comp_flotantes()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana1.show()
    # Iniciamos el bucle de eventos.
    sys.exit(app.exec())



