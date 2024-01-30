from tkinter import Widget

import self
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QMainWindow, QPushButton
from PySide6.QtCore import Signal

import Empresas
import DI_U04_A02_PP_SOL_02
import DI_U04_A03_03



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

    def mostrar_empresa_seleccionada(selfself, empresa_recibida):
        for empresa in self.empresas:
            json_empresa=json.loads(empresa)
            json_empresa_recibida=json.loads(empresa_recibida.replace('\n','\\n'))
            if json_empresa_recibida['nombre']==json_empresa['nombre']:
                self.empresa_seleccionada.emit(empresa_recibida)
    def filtrar(self, texto):
        for empresa in self.widget_empresas.empresas:
            if texto.lower() in empresa.nombre.lower():
                empresa.show()
            else:
                empresa.hide()

class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.layout=QVBoxLayout()
        widget=QWidget()
        widget.setLayout(self.layout)
        self.widget_empresa=None
        self.setCentralWidget(widget)
        self.boton=QPushButton("Selecciona una empresa")
        self.layout.addWidget(self.boton)
        #self.selector=SelectorEmpresa(datos_empresa.empresas)







