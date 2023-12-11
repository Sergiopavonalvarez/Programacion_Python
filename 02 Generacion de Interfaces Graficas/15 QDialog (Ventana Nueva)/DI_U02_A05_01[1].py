from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con diálogos")
        
        # Crear un botón
        boton = QPushButton("Haz clic para que el diálogo aparezca")
        
        # Conectar el clic del botón al método mostrar_dialogo
        boton.clicked.connect(self.mostrar_dialogo)
        
        # Establecer el botón como el widget central de la ventana
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        print("Clic recibido, se mostrará el diálogo.")
        # Crear una instancia de la clase QDialog
        ventana_dialogo = QDialog(self)
        ventana_dialogo.setWindowTitle("Ventana de diálogo")
        # Lanzar el bucle de eventos del diálogo
        ventana_dialogo.exec()

# Crear una aplicación
app = QApplication([])
# Crear una instancia de la ventana principal
ventana_principal = VentanaPrincipal()
# Mostrar la ventana principal
ventana_principal.show()
# Ejecutar la aplicación
app.exec()
