import sys
from PySide6.QtCore import QCoreApplication, QFile, QIODevice
from PySide6.QtGui import QAction, QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog, QTextEdit, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto plano")

        # Define the text editor widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Define the actions
        self.openAction = QAction(QIcon("C://Users//pavon//Documents//PyCharm//Programacion_Python//00 Ejercicios//04 Ponte A Prueba 04//abrir.png"), "Abrir", self, shortcut="Ctrl+O")
        self.saveAction = QAction(QIcon("C://Users//pavon//Documents//PyCharm//Programacion_Python//00 Ejercicios//04 Ponte A Prueba 04//descarga.png"), "Guardar", self, shortcut="Ctrl+S")


        # Connect the actions to slots
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)


        # Add the actions to the menu bar
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&Archivo")
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)


        # Add the actions to the toolbar
        toolbar = self.addToolBar("Herramientas")
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)





        # Show the window
        self.show()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text files (*.txt)")
        if filename:
            file = QFile(filename)
            if file.open(QIODevice.ReadOnly):
                text = file.readAll().data()
                cursor = QTextCursor()
                cursor.setDocument(self.textEdit.document())
                cursor.insertText(text)
                file.close()

    def saveFile(self):
        filename = "archivo.txt"
        file = QFile(filename)
        if file.open(QIODevice.WriteOnly):
            text = self.textEdit.toPlainText()
            file.write(text.encode())
            file.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = App()
    sys.exit(app.exec())