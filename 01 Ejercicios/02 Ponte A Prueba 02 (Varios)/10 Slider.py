import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QLineEdit, QVBoxLayout
import sys
import platform
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel

# Define una clase llamada Conversor que hereda de QWidget
class Conversor(QMainWindow):
    # Constructor de la clase
    def __init__(self):
        # Llama al constructor de la clase base (QWidget)
        super().__init__()

        # Configura la ventana principal
        self.setWindowTitle("Conversor de euros a pesetas")
        self.resize(400, 200)


        barra_menus = self.menuBar()
        #Añadimos la opción "Menu" al menú principal
        menu = barra_menus.addMenu("&Menu")
        #Definimos el QAction con el texto "Imprimir por consola"
        accion = QAction("&Imprimir", self)
        #Asignamos un atajo de teclado a la acción
        accion.setShortcut(QKeySequence("Ctrl+p"))
        #Connectamos la accion con la ranura "imprimir_por_consola"
        accion.triggered.connect(self.imprimir_por_consola)
        #Añadimos la acción al menú
        menu.addAction(accion)


        #Barra Herramientas
        barra_herramientas=QToolBar("Barra de herramientas")
        #Añadimos la accion a la barra de herramientas
        barra_herramientas.addAction(accion)
        #Añadimos la barra de herramientas
        
        accion2=QAction("&Salir",self)
        accion2.triggered.connect(self.close)
        barra_herramientas.addAction(accion2)


        #Añadimos la barra de herramientas
        self.addToolBar(barra_herramientas)


        #Barra de estado
        #Creamos la barra de estado
        barra_estado=self.statusBar()
        #Añadimos la barra de estado
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        #Mostramos el mensaje
        barra_estado.showMessage("Cargando...",3000)


                #Crea un contenedor para la ventana
        contenedor = QWidget()



        # Crea etiquetas, un control deslizante (slider) y un cuadro de texto para la interfaz
        self.euros_label = QLabel("Euros:", self)
        self.pesetas_label = QLabel("Pesetas:", self)
        self.euros_slider = QSlider(Qt.Horizontal, self)
        self.euros_slider.setMinimum(0)
        self.euros_slider.setMaximum(100)
        self.pesetas_line_edit = QLineEdit(self)
        self.pesetas_line_edit.setReadOnly(True)

        # Conecta la señal de cambio de valor del slider a la función 'actualizar_pesetas'
        self.euros_slider.valueChanged.connect(self.actualizar_pesetas)

        # Crea un diseño vertical y agrega los widgets a la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.euros_label)
        layout.addWidget(self.euros_slider)
        layout.addWidget(self.pesetas_label)
        layout.addWidget(self.pesetas_line_edit)


        contenedor.setLayout(layout)

        #Establece el contenedor como el widget central de la ventana
        self.setCentralWidget(contenedor)

    # Función que actualiza el valor de las pesetas en función del valor del slider
    def actualizar_pesetas(self):
        euros = self.euros_slider.value()
        pesetas = euros * 166  # Tasa de cambio ficticia
        self.pesetas_line_edit.setText(str(pesetas))
        self.euros_label.setText(str(self.euros_slider.value()))

    def imprimir_por_consola(self):
        print("Imprimiendo")      

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication(sys.argv)
    # Crea una instancia de la clase Conversor
    conv = Conversor()
    # Muestra la ventana
    conv.show()
    # Ejecuta la aplicación
    sys.exit(app.exec())
