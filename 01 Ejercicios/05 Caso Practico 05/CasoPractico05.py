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

        self.openAction = QAction(QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/01 Ejercicios/05 Caso Practico 05/abrir.png"),"Abrir", self, shortcut="Ctrl+O")
        self.saveAction = QAction(QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/01 Ejercicios/05 Caso Practico 05/descarga.png"),"Guardar", self, shortcut="Ctrl+S")
        self.cerrarAction = QAction(QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/01 Ejercicios/05 Caso Practico 05/salir.png"),"Cerrar archivo", self, shortcut="Ctrl+W", triggered=self.cerrar)

        #self.openAction = QAction(QIcon("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/05 Caso Practico 05/abrir.png"), "Abrir", self, shortcut="Ctrl+O")
        #self.saveAction = QAction(QIcon("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/05 Caso Practico 05/descarga.png"), "Guardar", self, shortcut="Ctrl+S")
        #self.cerrarAction = QAction(QIcon("C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/01 Ejercicios/05 Caso Practico 05/salir.png"),"Cerrar archivo", self, shortcut="Ctrl+W", triggered=self.cerrar)


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
        global archivo_abierto
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text files (*.txt)")
        if filename:
            archivo_abierto = filename
            file = QFile(archivo_abierto)
            if file.open(QIODevice.ReadOnly):
                text = file.readAll().data()
                cursor = QTextCursor()
                cursor.setDocument(self.textEdit.document())
                cursor.insertText(text)
                file.close()

    def saveFile(self):
        global archivo_abierto

        if archivo_abierto:
            file = QFile(archivo_abierto)
            if file.open(QIODevice.WriteOnly):
                text = self.textEdit.toPlainText()
                file.write(text.encode())
                file.close()
        else:
            filename, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text files (*.txt)")
            if filename:
                archivo_abierto = filename
                file = QFile(archivo_abierto)
                if file.open(QIODevice.WriteOnly):
                    text = self.textEdit.toPlainText()
                    file.write(text.encode())
                    file.close()

    def cerrar(self):
        global archivo_abierto
        archivo_abierto = None
        self.textEdit.setPlainText("")
        QCoreApplication.instance().quit()

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = App()
    sys.exit(app.exec())