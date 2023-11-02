from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QStackedLayout,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout apilado")

        layout_principal = QHBoxLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_principal)
        self.setCentralWidget(componente_principal)

        # Creamos un QStackedLayout y añadimos cuatro "capas" al layout apilado
        self.pila = QStackedLayout()
        self.pila.addWidget(QLabel('Capa 1'))
        self.pila.addWidget(QLabel('Capa 2'))
        self.pila.addWidget(QLabel('Capa 3'))

        # Creamos un layout vertical con tres botones
        # Cada botón hará visible una capa a través de la ranura
        layout_botones = QVBoxLayout()
        boton1 = QPushButton("Ver capa 1")
        boton1.clicked.connect(self.activar_capa1)
        boton2 = QPushButton("Ver capa 2")
        boton2.clicked.connect(self.activar_capa2)
        boton3 = QPushButton("Ver capa 3") 
        boton3.clicked.connect(self.activar_capa3)
        layout_botones.addWidget(boton1)
        layout_botones.addWidget(boton2)
        layout_botones.addWidget(boton3)

        # Añadimos los layouts al layout principal
        layout_principal.addLayout(self.pila)
        layout_principal.addLayout(layout_botones)

    def activar_capa1(self):
        self.pila.setCurrentIndex(0)

    def activar_capa2(self):
        self.pila.setCurrentIndex(1)

    def activar_capa3(self):
        self.pila.setCurrentIndex(2)

app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
