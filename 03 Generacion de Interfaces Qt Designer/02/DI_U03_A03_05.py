import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QApplication(sys.argv)
#window = loader.load("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/03 Generacion de Interfaces Qt Designer/02/untitled.ui", None)
#window = loader.load("/Users/sergiopavonalvarez/Documents/Documentos/VS Code/Python/Programacion_Python/03 Generacion de Interfaces Qt Designer/02/untitled.ui", None)
window = loader.load("/Users/sergiopavonalvarez/Programacion/VS Code/Python/Programacion_Python/03 Generacion de Interfaces Qt Designer/02/untitled.ui", None)

window.show()
app.exec()