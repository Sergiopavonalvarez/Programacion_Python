import os.path
import sys
from PySide6.QtWidgets import QHBoxLayout

from PySide6.QtGui import QIcon, QAction, QKeySequence, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel, QDockWidget, QTextEdit
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial


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
        accion = QAction("Imprimir...", self)
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
        dock1.setWindowTitle("Componente Flotante")
        widget_contenedor = QWidget()


        # Crea una etiqueta, un dial y dos botones para la interfaz
        self.etiqueta_db = QLabel("Valor: 0 dB")
        self.etiqueta_db.setAlignment(Qt.AlignCenter)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.boton_aumentar = QPushButton("+")
        self.boton_aumentar.setMaximumWidth(30)
        self.boton_disminuir = QPushButton("-")
        self.boton_disminuir.setMaximumWidth(30)

        # Crea un diseño vertical y agrega los widgets a la interfaz
        layout = QVBoxLayout(widget_contenedor)
        layout.addWidget(self.etiqueta_db)
        layout.addWidget(self.dial)
        layout.addWidget(self.boton_aumentar)
        layout.addWidget(self.boton_disminuir)
        #Agrega al componente flotante el widget que contiene los layout

        dock1.setWidget(widget_contenedor)

        # Asigna un ancho mínimo al componente flotante
        dock1.setMinimumWidth(50)

        # Coloca el componente flotante a la derecha de la ventana principal
        self.addDockWidget(Qt.RightDockWidgetArea, dock1)

        # Establece un widget de etiqueta como widget central de la ventana principal
        self.setCentralWidget(QLabel("Comp Principal"))

        self.dial.valueChanged.connect(self.actualizar_valor)
        self.boton_aumentar.clicked.connect(self.aumentar_volumen)
        self.boton_disminuir.clicked.connect(self.disminuir_volumen)

    # Función que actualiza la etiqueta con el valor del dial
    def actualizar_valor(self):
        self.etiqueta_db.setText(f"Valor: {self.dial.value()} dB")

    # Funciones para aumentar y disminuir el valor del dial
    def aumentar_volumen(self):
        self.dial.setValue(self.dial.value() + 1)

    def disminuir_volumen(self):
        self.dial.setValue(self.dial.value() - 1)

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
