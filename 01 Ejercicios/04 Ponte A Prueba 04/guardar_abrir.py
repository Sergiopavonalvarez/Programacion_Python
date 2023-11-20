import sys
from PySide6.QtCore import QCoreApplication, QFile, QIODevice
from PySide6.QtGui import QAction, QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog, QTextEdit, QMainWindow
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto plano")
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.openAction = QAction(QIcon("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04/abrir.png"), "Abrir", self, shortcut="Ctrl+O")
        self.saveAction = QAction(QIcon("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04/descarga.png"), "Guardar", self, shortcut="Ctrl+S")
        self.cerrarAction = QAction(QIcon("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04/salir.png"),"Cerrar archivo", self, shortcut="Ctrl+W", triggered=self.cerrar)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.cerrarAction.triggered.connect(self.cerrar)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&Archivo")
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.cerrarAction)
        toolbar = self.addToolBar("Herramientas")
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)
        toolbar.addAction(self.cerrarAction)
        self.show()


    def openFile(self):

     filename = "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04/archivo_04PonteAPrueba.txt"

     if filename:
        file = QFile(filename)
        if file.open(QIODevice.ReadOnly):
            text = file.readAll().data().decode('utf-8')  # Read file content as utf-8
            cursor = QTextCursor(self.textEdit.document())  # Pass the document to QTextCursor constructor
            cursor.insertText(text)
            file.close()
  




    def saveFile(self):
        filename = "C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/04 Ponte A Prueba 04/archivo_04PonteAPrueba.txt"
        file = QFile(filename)
        if file.open(QIODevice.WriteOnly):
            text = self.textEdit.toPlainText()
            file.write(text.encode())
            file.close()

    def cerrar(self):
        self.textEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = App()
    sys.exit(app.exec())