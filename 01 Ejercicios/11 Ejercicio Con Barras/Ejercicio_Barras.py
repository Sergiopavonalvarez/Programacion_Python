import sys
import platform

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMenuBar, \
    QToolBar, QStatusBar


class Intercambio(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Ejercicio")
        self.setGeometry(1000, 250, 400, 200)

        # Configuración del widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # Cuadros de texto para las variables A y B
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText("Introduce el texto")
        self.input_b.setPlaceholderText("Introduce el texto")

        # Etiquetas y cuadros de texto se añaden al diseño vertical
        layout.addWidget(QLabel("Variable A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Variable B"))
        layout.addWidget(self.input_b)

        # Botón "Intercambio" y conexión a la función correspondiente
        self.intercambio_Boton = QPushButton("Intercambio")
        layout.addWidget(self.intercambio_Boton)
        self.intercambio_Boton.clicked.connect(self.intercambio_variables)

        # Se establece el diseño en el widget central
        central_widget.setLayout(layout)

        # Barra de menú
        menu_bar = self.menuBar()

        # Menú Archivo
        archivo_menu = menu_bar.addMenu("Archivo")
        exit_action = QAction("Salir", self)
        #Cerrará la ventana principal y, por lo tanto, finalizará la aplicación.
        exit_action.triggered.connect(self.close)
        archivo_menu.addAction(exit_action)
   

        # Menú imprimir
        imprimir_menu = menu_bar.addMenu("Imprimir")
        accion_imprimir=QAction("Imprimir",self)
        accion_imprimir.triggered.connect(self.imprimir)
        imprimir_menu.addAction(accion_imprimir)






        # Barra de herramientas
        tool_bar = QToolBar("Herramientas")
        self.addToolBar(tool_bar)

        # Agregar el botón de Salir a la barra de herramientas
        tool_bar.addAction(exit_action)

        # Agregar el botón para el menú Editar a la barra de herramientas
        editar_action = QAction("Imprimir", self)
        tool_bar.addAction(accion_imprimir)

        # Barra de estado
        # Obtenemos la referencia a la barra de estado
        barra_estado = self.statusBar()
        # Agregamos un componente permanente con la plataforma: sale Windows
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        # Mostramos un mensage durante 3 segundos
        # que se sobrescibirá al pasar el puntero por una acción
        barra_estado.showMessage("Listo. Esperando acción ...", 3000)




    def imprimir (self):
        print("Mandando a impresora")

    def intercambio_variables(self):
        # Obtiene los valores actuales de los cuadros de texto A y B
        valor_a = self.input_a.text()
        valor_b = self.input_b.text()
        
        # Intercambia los valores entre los cuadros de texto
        self.input_a.setText(valor_b)
        self.input_b.setText(valor_a)

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Intercambio()
    ventana1.show()
    sys.exit(app.exec())
