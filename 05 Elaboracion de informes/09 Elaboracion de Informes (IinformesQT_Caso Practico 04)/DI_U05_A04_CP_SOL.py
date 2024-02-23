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
        boton_abrir01.clicked.connect(self.abrir_informe_01)
        self.layout_vertical.addWidget(boton_abrir01)

        boton_abrir02 = QPushButton('Abrir informe 02')
        boton_abrir02.clicked.connect(self.abrir_informe_02)
        self.layout_vertical.addWidget(boton_abrir02)

        boton_abrir03 = QPushButton('Abrir informe 03')
        boton_abrir03.clicked.connect(self.abrir_informe_03)
        self.layout_vertical.addWidget(boton_abrir03)



    def abrir_informe_01(self):
        #ruta_absoluta = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe01.html"
        ruta_absoluta = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/09 Elaboracion de Informes (IinformesQT_Caso Practico 04)/Informe01.html"
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))

    def abrir_informe_02(self):
        #ruta_absoluta = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe02.html"
        ruta_absoluta = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/09 Elaboracion de Informes (IinformesQT_Caso Practico 04)/Informe02.html"
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))

    def abrir_informe_03(self):
        #ruta_absoluta = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe03.html"
        ruta_absoluta = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/09 Elaboracion de Informes (IinformesQT_Caso Practico 04)/Informe03.html"
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))

if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()