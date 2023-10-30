import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QFrame


class Porcentaje(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 04")
        self.setGeometry(1000, 250, 400, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.combo_ninos = QComboBox()
        lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.combo_ninos.addItems(lista)
        layout.addWidget(QLabel("Numero de niños"))
        layout.addWidget(self.combo_ninos)
        self.combo_ninas = QComboBox()
        self.combo_ninas.addItems(lista)
        layout.addWidget(QLabel("Numero de niñas"))
        layout.addWidget(self.combo_ninas)

        # Botón
        self.calcular_boton = QPushButton("Calcular")
        layout.addWidget(self.calcular_boton)
        self.calcular_boton.clicked.connect(self.calcular_porcentaje)  # Conecta el botón a la función

        central_widget.setLayout(layout)




        self.etiqueta1 = QLabel("", self)


        layout.addWidget(self.etiqueta1)

        central_widget.setLayout(layout)

    def calcular_porcentaje(self):
        ninos = int(self.combo_ninos.currentText())
        ninas = int(self.combo_ninas.currentText())

        # Realiza los cálculos y muestra el resultado (aquí debes agregar tu lógica)
        resultado = f"Porcentaje de niños: {ninos / (ninos + ninas) * 100:.2f}%"
        resultado += f"\nPorcentaje de niñas: {ninas / (ninos + ninas) * 100:.2f}%"

        self.etiqueta1.setText(resultado)



if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objeto ventana.
    ventana1 = Porcentaje()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana1.show()
    # Iniciamos el bucle de eventos.
    sys.exit(app.exec())