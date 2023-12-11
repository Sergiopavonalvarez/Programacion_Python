from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton
)




class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout horizontal")

        # Creamos un objeto layout horizontal
        layout_horizontal = QHBoxLayout()

        # Creamos un componente principal para la ventana
        componente_principal = QWidget()
        # Le assignamos el layout horizontal como disposición
        componente_principal.setLayout(layout_horizontal)
        self.setCentralWidget(componente_principal)
        botonuno=QPushButton("UNO")
        botondos = QPushButton("DOS")
        botontres = QPushButton("TRES")
        botoncuatro = QPushButton("CUATRO")



        # Añadimos cuatro botones al layout horizontal
        layout_horizontal.addWidget(botonuno)
        layout_horizontal.addWidget(botondos)
        layout_horizontal.addWidget(botontres)
        layout_horizontal.addWidget(botoncuatro)

        botonuno.clicked.connect(self.resultadouno)
        botondos.clicked.connect(self.resultadodos)
        botontres.clicked.connect(self.resultadotres)
        botoncuatro.clicked.connect(self.resultadocuatro)

    def resultadouno(self):
     print("uno")

    def resultadodos(self):
     print("dos")

    def resultadotres(self):
     print("tres")

    def resultadocuatro(self):
     print("cuatro")


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
