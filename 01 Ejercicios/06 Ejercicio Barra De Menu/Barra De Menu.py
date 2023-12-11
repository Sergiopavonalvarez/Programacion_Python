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
        accion2 = QAction("Salir",self)
        accion2.setShortcut(QKeySequence("ctrl+w"))
        # Conectamos la accion con la renura imprimir
        accion.triggered.connect(self.imprimir_consola)
        accion2.triggered.connect(self.close)
        # Añadir la accion al menu
        menu.addAction(accion)
        menu.addAction(accion2)

        
        # Añadir menú "Guardar"
        menu_guardar = barra_menu.addMenu("Guardar")
        # Definir QAction para guardar
        accion_guardar = QAction("Guardar", self)
        accion_guardar.setShortcut(QKeySequence("Ctrl+S"))
        # Conectar acción con la ranura guardar
        accion_guardar.triggered.connect(self.guardar)
        # Añadir acción al menú "Guardar"
        menu_guardar.addAction(accion_guardar)



    def imprimir_consola(self):
        print("Accion lanzanada a traves del menu")

    def guardar(self):
        print("Accion guardada")    

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()


