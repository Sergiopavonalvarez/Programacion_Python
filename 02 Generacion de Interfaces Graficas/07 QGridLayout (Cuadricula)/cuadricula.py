from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel, QApplication, QLineEdit


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        cuadricula=QGridLayout()
        comprincipal=QWidget()
        
        comprincipal.setLayout(cuadricula)
        self.setCentralWidget(comprincipal)

        Usuario=QLabel("usuario")

        cuadricula.addWidget(QLabel("Usuario"),0,0)
        cuadricula.addWidget(QLabel("Contraseña"), 1, 0)
        cuadricula.addWidget(QLineEdit(), 0, 1)
        cuadricula.addWidget(QLineEdit(), 1, 1)

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()




