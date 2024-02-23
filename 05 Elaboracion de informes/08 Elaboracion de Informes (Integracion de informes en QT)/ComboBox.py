from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl, QDir
from PySide6.QtWebEngineWidgets import QWebEngineView



class VentanaInformes(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)

        boton_abrir01 = QPushButton('Abrir informe 01')
        boton_abrir01.clicked.connect(self.abrir_informe01)
        self.layout_vertical.addWidget(boton_abrir01)

        boton_abrir02 = QPushButton('Abrir informe 02')
        boton_abrir02.clicked.connect(self.abrir_informe02)
        self.layout_vertical.addWidget(boton_abrir02)

        boton_abrir03 = QPushButton('Abrir informe 03')
        boton_abrir03.clicked.connect(self.abrir_informe03)
        self.layout_vertical.addWidget(boton_abrir03)


        self.view = QWebEngineView()
        self.layout_vertical.addWidget(self.view)
        self.resize(1500, 800)

    def cargar_informe(self, ruta_absoluta):
        self.view.setHtml(open(ruta_absoluta).read())

    def abrir_informe01(self):
        ruta_absoluta = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe01.html"
        self.cargar_informe(ruta_absoluta)

    def abrir_informe02(self):
        ruta_absoluta = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe02.html"
        self.cargar_informe(ruta_absoluta)

    def abrir_informe03(self):
        ruta_absoluta = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe03.html"
        self.cargar_informe(ruta_absoluta)

if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()

