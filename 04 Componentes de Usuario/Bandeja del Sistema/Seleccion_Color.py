import sys
from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QColorDialog, QMainWindow, QPushButton, QSystemTrayIcon, QMenu
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con diálogos")
        self.boton = QPushButton("Haz clic para que el diálogo aparezca")
        self.boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(self.boton)
    def mostrar_dialogo(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f"background-color: {color.name()}")
    def closeEvent(self, event):
        self.hide()
        event.ignore()
def cargar_traductor(app):
    translator = QTranslator(app)
    translations = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    iconoBandeja = QSystemTrayIcon(QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/Ocultar cosas/colores.png"))
    menu_bandeja = QMenu()
    mostrar_accion = menu_bandeja.addAction("Mostrar")
    salir_accion = menu_bandeja.addAction("Salir")
    mostrar_accion.triggered.connect(ventana_principal.show)
    salir_accion.triggered.connect(app.quit)
    iconoBandeja.setContextMenu(menu_bandeja)
    iconoBandeja.activated.connect(ventana_principal.show)
    iconoBandeja.show()
    sys.exit(app.exec())
