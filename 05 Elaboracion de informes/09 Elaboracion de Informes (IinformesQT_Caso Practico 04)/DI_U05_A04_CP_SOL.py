from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl, QDir
from PySide6.QtWebEngineWidgets import QWebEngineView

class VentanaInformes(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)

        boton1 = QPushButton('DI_U05_A02_03.html')
        boton1.clicked.connect(self.abrir_informe)
        self.layout_vertical.addWidget(boton1)

        boton2 = QPushButton('DI_U05_A02_08.html')
        boton2.clicked.connect(self.abrir_informe)
        self.layout_vertical.addWidget(boton2)

        boton3 = QPushButton('DI_U05_A03_11.html')
        boton3.clicked.connect(self.abrir_informe)
        self.layout_vertical.addWidget(boton3)
        
    def abrir_informe(self):
        boton = self.sender()        
        ruta_absoluta = QDir().absoluteFilePath('./' + boton.text())        
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))
        

if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()