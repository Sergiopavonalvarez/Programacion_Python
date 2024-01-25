import self
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit
from PySide6.QtCore import Signal

import Empresas


import json

class SelectorEmpresa(QWidget):
    empresa_seleccionada=Signal(str)
    def __init__(self, empresas):
        super().__init__()
        self.empresas=empresas

        layout=QVBoxLayout()
        self.setLayout(layout)
        self.buscar=QLineEdit()
        self.buscar.textChanged.connect(self.filtrar)
        layout.addWidget(self.buscar)
        self.widget_empresas= Empresas(self.empresas, self)
        self.widget_empresas.empresa_seleccionada.connect(self.mostrar_empresa_seleccionada)
        layout.addwidget(self.widget_empresas)


