from PySide6.QtWidgets import QMainWindow, QFormLayout, QWidget, QApplication, QLabel, QLineEdit, QSpinBox, \
    QDoubleSpinBox, QPushButton





class form (QMainWindow):
    def __init__(self):
        super().__init__()

        layoutform=QFormLayout()
        comprin=QWidget()
        comprin.setLayout(layoutform)
        self.setCentralWidget(comprin)

        boton=QPushButton("Enviar")
        self.texto=QLineEdit()
        self.entero=QSpinBox()
        self.double=QDoubleSpinBox()
        boton.clicked.connect(self.accionboton)

        layoutform.addRow(QLabel("Texto"),self.texto)
        layoutform.addRow(QLabel("Entero"), self.entero)
        layoutform.addRow(QLabel("Decimal"), self.double)
        layoutform.addRow(boton)




    def accionboton(self):
        # Obtener el texto del QLineEdit y luego imprimirlo
        texto1 = self.texto.text()
        entero1 = self.entero.text()
        double1 = self.double.text()
        print(texto1)
        print(entero1)
        print(double1)


app = QApplication([])
ventana = form()
ventana.show()
app.exec()
