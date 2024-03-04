from select import select
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Signal

from DI_U04_A03_CPE_SOL_02 import Empresa, Empresas
import DI_U04_A02_PP_SOL_02
import json

class SelectorEmpresa(QWidget):
    empresa_seleccionada = Signal(str)
    def __init__(self, empresas):
        super().__init__()
        self.empresas = empresas


        layout = QVBoxLayout()
        self.setLayout(layout)

        self.buscar = QLineEdit()
        self.buscar.textChanged.connect(self.filtrar)
        layout.addWidget(self.buscar)

        self.widget_empresas = Empresas(self.empresas, self)
        self.widget_empresas.empresa_seleccionada.connect(self.mostrar_empresa_seleccionada)
        layout.addWidget(self.widget_empresas)

    def mostrar_empresa_seleccionada(self, empresa_recibida):
        for empresa in self.empresas:
            json_empresa = json.loads(empresa)
            json_empresa_recibida = json.loads(empresa_recibida.replace('\n','\\n'))
            if json_empresa_recibida['nombre'] == json_empresa['nombre']:
                self.empresa_seleccionada.emit(empresa_recibida)            

    def filtrar(self, texto):
        for empresa in self.widget_empresas.empresas:
            if texto.lower() in empresa.nombre.lower():
                empresa.show()
            else:
                empresa.hide()



class Ventana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(self.layout)
        self.widget_empresa = None
        self.setCentralWidget(widget)
        self.boton = QPushButton("Seleccionar empresa")
        self.layout.addWidget(self.boton)
        self.selector = SelectorEmpresa(DI_U04_A02_PP_SOL_02.empresas)
        self.selector.empresa_seleccionada.connect(self.seleccionada)
        self.boton.clicked.connect(self.mostrar_selector)

    def mostrar_selector(self):
        self.selector.buscar.setFocus()
        self.selector.show()

    def seleccionada(self, empresa_recibida):
        json_empresa_recibida = json.loads(empresa_recibida.replace('\n','\\n'))
        if self.widget_empresa == None:
            self.widget_empresa = Empresa(json_empresa_recibida)
            self.layout.addWidget(self.widget_empresa)
        else:
            self.widget_empresa.nombre = json_empresa_recibida['nombre']
            self.widget_empresa.direccion = json_empresa_recibida['direccion']
            self.widget_empresa.logo = json_empresa_recibida['logo']
        
        self.selector.buscar.clear()
        self.selector.hide()


if __name__ == "__main__":

    app = QApplication([])

    ventana = Ventana()
    ventana.show()

    app.exec()
