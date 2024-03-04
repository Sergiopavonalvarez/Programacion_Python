from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QComboBox
from PySide6.QtWebEngineWidgets import QWebEngineView


class VentanaInformes(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)

        self.combo_informes = QComboBox()
        self.combo_informes.addItem("Informe 1")
        self.combo_informes.addItem("Informe 2")
        self.combo_informes.addItem("Informe 3")
        self.combo_informes.currentIndexChanged.connect(self.abrir_informe_seleccionado)
        self.layout_vertical.addWidget(self.combo_informes)

        self.web_view = QWebEngineView()
        self.layout_vertical.addWidget(self.web_view)
        self.resize(1500, 800)

    def cargar_informe(self, ruta_absoluta):
        self.web_view.setHtml(open(ruta_absoluta).read())

    def abrir_informe_seleccionado(self, index):

        if index == 0:
            ruta_absoluta = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/09 Elaboracion de Informes (InformesQT ComboBox)/Informe01.html")
        elif index == 1:
            ruta_absoluta = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/09 Elaboracion de Informes (InformesQT ComboBox)/Informe02.html")
        elif index == 2:
            ruta_absoluta = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/09 Elaboracion de Informes (InformesQT ComboBox)/Informe03.html")
        self.cargar_informe(ruta_absoluta)


if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()
