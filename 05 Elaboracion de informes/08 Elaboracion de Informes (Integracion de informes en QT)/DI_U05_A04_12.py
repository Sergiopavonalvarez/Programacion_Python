from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl, QDir
from PySide6.QtWebEngineWidgets import QWebEngineView


class VentanaInformes(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)

        boton_abrir = QPushButton('Abrir informe')
        boton_abrir.clicked.connect(self.abrir_informe)
        self.layout_vertical.addWidget(boton_abrir)

        ruta_absoluta = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe(Ponte a Prueba).html"

        view = QWebEngineView()
        # view.load(QUrl.fromLocalFile(ruta_absoluta))
        view.setHtml(open(ruta_absoluta).read())

        self.layout_vertical.addWidget(view)

        self.resize(600, 800)

    def abrir_informe(self):
        ruta_absoluta = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/08 Elaboracion de Informes (Integracion de informes en QT)/Informe(Ponte a Prueba).html"
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))


if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()
