import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QApplication(sys.argv)
window = loader.load("C:/Users/pavon/Documents/DI_U03_A03_02.ui", None)
window.show()
app.exec()