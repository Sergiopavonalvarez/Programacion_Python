import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QToolBar, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton
from PySide6.QtGui import QAction, QColor, QIcon, QKeySequence, QToolBarChangeEvent

class PorcentajeNinosNinasApp(QMainWindow):
    def __init__(self):
        super().__init__()

        ruta_a_icono1 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/Examen 1º Evaluacion Desarrollo de Interfaces/lupa.png")
        ruta_a_icono2 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/Examen 1º Evaluacion Desarrollo de Interfaces/cubo-azul.png")
        ruta_a_icono3 = os.path.join(os.path.dirname(__file__), "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/Examen 1º Evaluacion Desarrollo de Interfaces/cubo-rojo.png")
        barra_menu=self.menuBar()
        menu1=barra_menu.addMenu("&Archivo")
        menu2=barra_menu.addMenu("&Editar")
        menu3=barra_menu.addMenu("&Ver")
        menu4=barra_menu.addMenu("&Insertar")
        accion2 = QAction("Salir",self)
        accion2.setShortcut(QKeySequence("ctrl+Q"))
        accion2.triggered.connect(self.close)
        accion3 = QAction(QIcon(ruta_a_icono3),"Rojo",self)
        accion4 = QAction(QIcon(ruta_a_icono2),"Azul",self)
        accion3.triggered.connect(self.fondo_rojo)
        accion4.triggered.connect(self.fondo_azul)
        accion5 = QAction(QIcon(ruta_a_icono1),"Mostrar Resultado",self)
        accion5.triggered.connect(self.calcular_porcentaje)
        menu1.addAction(accion2)
        menu2.addAction(accion3)
        menu2.addAction(accion4)
        menu3.addAction(accion5)

        barra_herramientas=QToolBar("Barra de herramientas")
        barra_herramientas.addAction(accion5)
        barra_herramientas.addAction(accion3)
        barra_herramientas.addAction(accion4)
        self.addToolBar(barra_herramientas)




        barra_estado=self.statusBar() 
        barra_estado.addPermanentWidget(QLabel("Desarrollo de Interfaces"))
        barra_estado.addPermanentWidget(QLabel("Version 1.0"))

        self.setWindowTitle("Porcentaje de Niños y Niñas")
        self.setGeometry(100, 100, 400, 200)

        # Crear un widget central y un layout vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # QComboBox para seleccionar el número de niños
        self.combo_ninos = QComboBox()
        # Lista de strings para pasarsela a cada QComboBox
        lista = ["0", "1", "2", "3", "4", "5","6","7","8","9","10"] 
        self.combo_ninos.addItems(lista)

        layout.addWidget(QLabel("Número de Niños:"))
        layout.addWidget(self.combo_ninos)

        # QComboBox para seleccionar el número de niñas
        self.combo_ninas = QComboBox()
        self.combo_ninas.addItems(lista)
        layout.addWidget(QLabel("Número de Niñas:"))
        layout.addWidget(self.combo_ninas)

        # Botón para calcular el porcentaje
        self.calcular_boton = QPushButton("Calcular Porcentaje")
        layout.addWidget(self.calcular_boton)
        self.calcular_boton.clicked.connect(self.calcular_porcentaje)

        # Etiqueta para mostrar el resultado
        self.resultado_label = QLabel("")
        resultado_estilo = (
            "background-color: red;" # Color de fondo: Rojo
            "color: white;"          # Color de letras: Blanco
            "font-weight: bold;"     # Negrita
            "font-family: 'Arial';"  # Letra: Arial
            "font-size: 14px;"       # Tamaño: 14 pixeles

        )
        self.resultado_label.setStyleSheet(resultado_estilo)
        layout.addWidget(self.resultado_label)

        central_widget.setLayout(layout)

    def calcular_porcentaje(self):
        ninos = int(self.combo_ninos.currentText())
        ninas = int(self.combo_ninas.currentText())
        total = ninos + ninas

        if total > 0:
            porcentaje_ninos = (ninos / total) * 100
            porcentaje_ninas = (ninas / total) * 100
            self.resultado_label.setText(f"Porcentaje de Niños: {porcentaje_ninos:.2f}%\nPorcentaje de Niñas: {porcentaje_ninas:.2f}%")
        else:
            self.resultado_label.setText("Por favor, seleccione el número de niños y niñas.")
            
    def fondo_rojo(self):
        resultado_estilo = (
            "background-color: red;" # Color de fondo: Rojo
            "color: white;"          # Color de letras: Blanco
            "font-weight: bold;"     # Negrita
            "font-family: 'Arial';"  # Letra: Arial
            "font-size: 14px;"       # Tamaño: 14 pixeles

        )
        self.resultado_label.setStyleSheet(resultado_estilo)
        
    def fondo_azul(self):
        resultado_estilo = (
            "background-color: blue;" # Color de fondo: Azul
            "color: white;"          # Color de letras: Blanco
            "font-weight: bold;"     # Negrita
            "font-family: 'Arial';"  # Letra: Arial
            "font-size: 14px;"       # Tamaño: 14 pixeles

        )
        self.resultado_label.setStyleSheet(resultado_estilo)
            
    def salir(self):
        sys.exit(0)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PorcentajeNinosNinasApp()
    window.show()
    sys.exit(app.exec_())
