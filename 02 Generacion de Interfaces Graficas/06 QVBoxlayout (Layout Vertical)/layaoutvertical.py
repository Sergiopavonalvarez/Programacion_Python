from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QLabel, QPushButton


class vertical(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("layaout vertical")
        layaout_vertical = QVBoxLayout()
        self.etiquetauno=QLabel("uno",self)
        self.etiquetados = QLabel("dos", self)
        self.etiquetatres = QLabel("tres", self)
        layaout_vertical.addWidget(self.etiquetauno)
        layaout_vertical.addWidget(self.etiquetados)
        layaout_vertical.addWidget(self.etiquetatres)

        componenteprincipal=QWidget()
        componenteprincipal.setLayout(layaout_vertical)
        componenteprincipal.setLayout(layaout_vertical)
        self.setCentralWidget(componenteprincipal)






app = QApplication([])
ventana = vertical()
ventana.show()
app.exec()