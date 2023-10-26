import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, QVBoxLayout


class layouts_anidados(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts anidados")
        self.setGeometry(1000, 250, 400, 100)

        layout_horizontal1=QHBoxLayout()


        componente_principal = QWidget()
        componente_principal.setLayout(layout_horizontal1)
        self.setCentralWidget(componente_principal)



        layout_vertical = QVBoxLayout()


        layout_horizontal1.addLayout(layout_vertical)
        layout_vertical.addWidget(QPushButton('V1'))
        layout_vertical.addWidget(QPushButton('V2'))
        layout_vertical.addWidget(QPushButton('V3'))
        layout_vertical.addWidget(QPushButton('V4'))

        layout_horizontal = QHBoxLayout()
        layout_horizontal1.addLayout(layout_horizontal)




        layout_horizontal.addWidget(QPushButton("H1"))
        layout_horizontal.addWidget(QPushButton("H2"))
        layout_horizontal.addWidget(QPushButton("H3"))
        layout_horizontal.addWidget(QPushButton("H4"))













app = QApplication([])
ventana = layouts_anidados()
ventana.show()
app.exec()