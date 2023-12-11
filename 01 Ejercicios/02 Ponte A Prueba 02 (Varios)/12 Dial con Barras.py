import sys
import platform
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel


#Define una clase llamada Ventana que hereda de QMainWindow
class Ventana(QMainWindow):
    #Constructor de la clase
    def __init__(self):
        super().__init__()

        #Configura la ventana principal
        self.setWindowTitle("Control de volumen")


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

        #Crea una etiqueta, un dial y dos botones para la interfaz
        self.etiqueta_db = QLabel("Valor: 0 dB")
        self.etiqueta_db.setAlignment(Qt.AlignCenter)
        self.etiqueta_db2 = QLabel("Porcentaje: 0 %")
        self.etiqueta_db2.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(50)
        self.dial.setValue(0)
        self.boton_aumentar = QPushButton("+")
        self.boton_aumentar.setMaximumWidth(30)
        self.boton_disminuir = QPushButton("-")
        self.boton_disminuir.setMaximumWidth(30)

        #Crea un diseño vertical y agrega los widgets a la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_db)
        layout.addWidget(self.dial)
        layout.addWidget(self.boton_aumentar)
        layout.addWidget(self.boton_disminuir)
        layout.addWidget(self.etiqueta_db2)
        
        contenedor.setLayout(layout)

        #Establece el contenedor como el widget central de la ventana
        self.setCentralWidget(contenedor)

        #Conecta las señales de los widgets a las funciones correspondientes
        self.dial.valueChanged.connect(self.actualizar_valor)
        self.dial.valueChanged.connect(self.porcentaje)
        self.boton_aumentar.clicked.connect(self.aumentar_volumen)
        self.boton_disminuir.clicked.connect(self.disminuir_volumen)

    #Función que actualiza la etiqueta con el valor del dial
    def actualizar_valor(self):
        self.etiqueta_db.setText(f"Valor: {self.dial.value()} dB")

    #Funciones para aumentar y disminuir el valor del dial
    def aumentar_volumen(self):
        self.dial.setValue(self.dial.value() + 1)
    def disminuir_volumen(self):
        self.dial.setValue(self.dial.value() - 1)

    def porcentaje(self):
     valor_dial = self.dial.value()
     porcentaje = (valor_dial / 50) * 100
     self.etiqueta_db2.setText(f"Porcentaje: {porcentaje:.2f} %")    

    #Funcion imprimir por consola
    def imprimir_por_consola(self):
        dato = f"Valor: {self.dial.value()} dB"
        print("Imprimiendo", dato)  

#Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication(sys.argv)
    # Crea una instancia de la clase Ventana
    ventana = Ventana()
    # Muestra la ventana
    ventana.show()
    # Ejecuta la aplicación
    sys.exit(app.exec())