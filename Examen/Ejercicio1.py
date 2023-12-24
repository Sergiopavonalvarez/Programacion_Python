import sys
import platform
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton
)
from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel, QApplication, QLineEdit
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QLineEdit, QVBoxLayout
import sys
import platform
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDial
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QDateTimeEdit



class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarea Examen")
        self.etiqueta_db2 = QLabel("0 %")
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(50)
        self.dial.setValue(0)

        self.slider = QSlider(Qt.Vertical, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.elabel = QLabel("0%")

        self.ciudades = QComboBox()
        lista = ["Madrid", "Almeria", "Tnerife", "Barcelona"]
        self.ciudades.addItems(lista)
        self.hora=QDateTimeEdit()

        cuadricula=QGridLayout()
        comprincipal=QWidget()        
        comprincipal.setLayout(cuadricula)
        self.setCentralWidget(comprincipal)

        cuadricula.addWidget(self.dial, 0, 0)
        cuadricula.addWidget(self.etiqueta_db2, 0, 1)
        cuadricula.addWidget(self.slider, 1, 0)
        cuadricula.addWidget(self.elabel, 1, 1)
        cuadricula.addWidget(self.ciudades, 2, 0)
        cuadricula.addWidget(self.hora, 3, 0)

        self.dial.valueChanged.connect(self.actualizar_valor)
        self.slider.valueChanged.connect(self.actualizar_valores)


    def actualizar_valores(self):
        self.elabel.setText(str(self.slider.value()))


    def actualizar_valor(self):
        self.etiqueta_db2.setText(f"{self.dial.value()}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())