import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QDialog, \
    QGridLayout
# Define una clase llamada Login que hereda de QMainWindow
class Login(QMainWindow):
    # Constructor de la clase
    def __init__(self):
        # Llama al constructor de la clase base (QMainWindow)
        super().__init__()
        
        # Configura la ventana principal
        self.setWindowTitle("Login")
        self.setGeometry(1000, 250, 400, 200)
        
        # Crea un widget central y lo establece como el widget central de la ventana
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Crea un diseño de cuadrícula para organizar los elementos
        layout = QGridLayout()
        
        # Crea dos cuadros de entrada (line edits) para el usuario y la contraseña
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText("Usuario")
        self.input_b.setPlaceholderText("Contraseña")
        
        # Agrega etiquetas y cuadros de entrada al diseño de cuadrícula
        layout.addWidget(QLabel("Usuario:"), 0, 0)
        layout.addWidget(self.input_a, 0, 1)
        layout.addWidget(QLabel("Contraseña:"), 1, 0)
        layout.addWidget(self.input_b, 1, 1)
        
        # Crea un botón de entrada y lo agrega al diseño
        self.entrar_Boton = QPushButton("Entrar")
        self.entrar_Boton.setFixedWidth(200)
        layout.addWidget(self.entrar_Boton, 2, 1, 1, 2)
        
        # Conecta la señal de clic del botón a la función 'entrar'
        self.entrar_Boton.clicked.connect(self.entrar)
        
        # Establece el diseño de cuadrícula como el diseño del widget central
        central_widget.setLayout(layout)

    # Función llamada cuando se hace clic en el botón de entrada
    def entrar(self):
        # Valores de usuario y contraseña esperados
        usuario = "Sergio"
        contraseña = "1234"
        
        # Obtiene los valores ingresados en los cuadros de entrada
        valor_a = self.input_a.text()
        valor_b = self.input_b.text()
        
        # Verifica si los valores coinciden con el usuario y la contraseña esperados
        if (usuario == valor_a and contraseña == valor_b):
            # Si coincide, limpia los cuadros de entrada y muestra un mensaje de éxito
            self.input_a.clear()
            self.input_b.clear()
            self.input_a.setPlaceholderText("Usuario correcto")
            self.input_b.setPlaceholderText("Contraseña correcta")
            
            # Crea y muestra una ventana de diálogo con un mensaje de éxito
            ventana_dialogo = QDialog(self)
            ventana_dialogo.setWindowTitle("Ventana de dialogo")
            ventana_dialogo.resize(400, 200)
            etiqueta1 = QLabel("¡Estás dentro!", ventana_dialogo)
            fuente = etiqueta1.font()
            fuente.setPointSize(30)
            etiqueta1.setFont(fuente)
            ventana_dialogo.exec()
        else:
            # Si no coincide, limpia los cuadros de entrada y muestra un mensaje de error
            self.input_a.clear()
            self.input_b.clear()
            self.input_a.setPlaceholderText("Usuario o contraseña incorrecto")
            self.input_b.setPlaceholderText("Usuario o contraseña incorrecto")

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crea una aplicación Qt
    app = QApplication([])
    # Crea una instancia de la clase Login
    ventana1 = Login()
    # Muestra la ventana
    ventana1.show()
    # Ejecuta la aplicación
    sys.exit(app.exec())
