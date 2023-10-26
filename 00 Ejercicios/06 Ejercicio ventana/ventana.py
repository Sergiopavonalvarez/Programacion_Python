from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import (QAction, QKeySequence)

# Ventana principal

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana princiapl")
# Barra menu
        barra_menu = self.menuBar()
# Añadirla al menu princiapl
        menu = barra_menu.addMenu("Menu")
# Definimos el QActiion con el texto
        accion = QAction("Imprimir por consola",self)

        accion.setShortcut(QKeySequence("ctrl+p"))
# Conectamos la accion con la renura imprimir 

        accion.triggered.connect(self.imprimir_consola)
# Añadir la accion al menu
        menu.addAction(accion)

    def imprimir_consola(self):
        print("Accion lanzanada a traves del menu")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()


