
import platform

from PySide6.QtGui import QAction, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel, QDockWidget, QTextEdit


class compflotante(QMainWindow):
    def __init__(self):
        super().__init__()

        #Barra de menu
        barra_menu=self.menuBar()
        barra_menu.addMenu("&Menu")
        imprimir=QAction("&Imprimir",self)
        imprimir.triggered.connect(self.imprimir_hola)
        barra_menu.addAction(imprimir)

        #Barra de herramientas
        barra_herramientas=QToolBar("Barra herramientas")
        barra_herramientas.addAction(imprimir)
        self.addToolBar(barra_herramientas)

        #Barra de estado
        barra_estado=self.statusBar()
        barra_estado.addPermanentWidget(QLabel("Barra de estado"))
        barra_estado.showMessage("Cargando...",3000)



        # Componente flotante
        # Lo creamos
        cFlotante=QDockWidget()
        # Agregamos titulo
        cFlotante.setWindowTitle("Componente flotante")
        # Asignamos el componente que contendra
        cFlotante.setWidget(QTextEdit(""))
        # Anchura
        cFlotante.setMinimumWidth(50)
        # Posicion
        self.addDockWidget(Qt.LeftDockWidgetArea, cFlotante)
        # Componente principal
        self.setCentralWidget(QLabel("Componente principal"))


    def imprimir_hola(self):
        print("Hola")


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = compflotante()
    ventana1.show()
    app.exec()
