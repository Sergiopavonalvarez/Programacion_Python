import json
import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSpacerItem, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal, Property


class Empresa(QWidget):
    doble_clic = Signal(str)
    def __init__(self, empresa:str, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
                
        self.__logo = os.path.join(os.path.dirname(__file__), empresa['logo'])
        self.__etiqueta_logo = QLabel()
        self.__etiqueta_logo.setMaximumSize(60, 60)
        self.__etiqueta_logo.setScaledContents(True)
        self.__etiqueta_logo.setPixmap(QPixmap(self.__logo))
    
        layout.addWidget(self.__etiqueta_logo)

        layout_secundario = QVBoxLayout()
        layout.addLayout(layout_secundario)
        self.__nombre = QLabel(empresa['nombre'])
        self.__direccion = QLabel(empresa['direccion'])
        layout_secundario.addWidget(self.__nombre)
        layout_secundario.addWidget(self.__direccion)

    def mouseDoubleClickEvent(self, e):
        self.doble_clic.emit(
            f'{{"nombre":"{self.nombre}","direccion":"{self.direccion}","logo":"{self.logo}"}}'
        )

    @Property(str)
    def logo(self):
        return self.__logo

    @Property(str)
    def nombre(self):
        return self.__nombre.text()

    @Property(str)
    def direccion(self):
        return self.__direccion.text()

    @logo.setter
    def logo(self, logo):
        self.__logo = os.path.join(os.path.dirname(__file__), logo)
        self.__etiqueta_logo.setPixmap(QPixmap(self.__logo))
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre.setText(nombre)

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion.setText(direccion)


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