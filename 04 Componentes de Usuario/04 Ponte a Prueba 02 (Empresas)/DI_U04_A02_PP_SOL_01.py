import json
import os
from signal import signal

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSpacerItem, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Qt, Signal, Property


class Empresa(QWidget):
    doble_clic = Signal(str)
    def __init__(self, empresa:str, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
                
        self.logo = QLabel()
        self.logo.setMaximumSize(60, 60)
        self.logo.setScaledContents(True)
        self.path_logo = os.path.join(os.path.dirname(__file__), empresa['logo'])
        self.logo.setPixmap(QPixmap(self.path_logo))
        layout.addWidget(self.logo)

        layout_secundario = QVBoxLayout()
        layout.addLayout(layout_secundario)
        self.nombre = QLabel(empresa['nombre'])
        self.direccion = QLabel(empresa['direccion'])
        layout_secundario.addWidget(self.nombre)
        layout_secundario.addWidget(self.direccion)

    def mouseDoubleClickEvent(self, e):
        self.doble_clic.emit(
            f'{{"nombre":"{self.nombre.text()}","direccion":"{self.direccion.text()}","logo":"{self.path_logo}"}}'
        )


class Empresas(QScrollArea):
    empresa_seleccionada = Signal(str)
    def __init__(self, empresas, parent=None):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        self.empresas = []

        self.widget = QWidget()
        self.setWidget(self.widget)
        self.empresasLayout = QVBoxLayout()

        for empresa in empresas:
            nueva_empresa = Empresa(json.loads(empresa))
            nueva_empresa.doble_clic.connect(self.doble_clic_empresa)
            self.empresasLayout.addWidget(nueva_empresa)
            self.empresas.append(nueva_empresa)

        # Para que una empresa ocupe verticalmente lo que le corresponde aunque se redimensione el scrollarea
        espaciador = QSpacerItem(5, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)  
        self.empresasLayout.addSpacerItem(espaciador)

        self.widget.setLayout(self.empresasLayout)

    def doble_clic_empresa(self, json_empresa):
        self.empresa_seleccionada.emit(json_empresa)