

import json
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QScrollArea, QSpacerItem, QSizePolicy
from PySide6.QtCore import Signal, Property, Qt


class Empresa (QWidget):

    doble_clic=Signal(str)
    #Señal llamada doble clic. Se emite una señal cuando se produce docble clic en una instancia de la clase Empresa
    def __init__(self,empresa:str,parent=None):
        super().__init__(parent)

        layout=QHBoxLayout(self)#Nos permite agregar widget horizontales
        self._logo=os.path.join(os.path.dirname(__file__),'..'.empresa['logo'])
        self.__etiqueta_logo=QLabel()
        self.__etiqueta_logo.setMaximunSize(60,60)
        self.__etiqueta_logosetScaledContents(True)
        #La imagen se establece a traves del SetPixmap()
        #y se aclarará automaticamente para ajustarse al tamaño de la etiqueta.
        #nos aseguramos que el logotipo de la empresa se ajusta correctamente.
        #QPixmap crea un objeto QPixmap con la ruta proporcionada. Luego se establece como la imagen de la etiqueta mediante setPixMap()

        self.__etiqueta_logo.setPixmap(QPixmap(self.__logo))

        layout.addWidget(self.__etiqueta_logo) #Añadimos la etiqueta al layout
        layout_secundario=QVBoxLayout()
        layout.addLayout(layout_secundario)#Añadimos el layout_secundario al layout principal
        self.__nombre=QLabel(empresa['nombre'])#Etiqueta con el nombre d ela empresa
        self.__direccion=QLabel(empresa['direccion'])#Etiqueta con la direccion de la empresa
        layout_secundario.addWidget(self.__nombre)#Añadimos etiqueta al layout_secundario
        layout_secundario.addWidget(self.__direccion)
    def mouseDoubleClickEvent(self, e):
        self.double_clic.emit(
            f'{{"nombre":"{self.nombre}","direccion":"{self.direccion}","logo":"{self.logo}"}}'
        )
    @Property(str) #Decoradores que permiten modificar los comportamientos de los métodos
    def logo(self): #getter
        return self.__logo

    @Property(str) #Decoradores que permiten modificar los comportamientos de los métodos
    def nombre(self): #getter
        return self.__nombre.text()

    @Property(str) #Decoradores que permiten modificar los comportamientos de los métodos
    def direccion(self): #getter
        return self.__direccion.text()
    
    @logo.setter #Setter
    def logo(self,logo):
        self.__logo=os.path.join(os.path.dirname(__file__),logo)
        self.__etiqueta_logo.setPixmap(QPixmap(self.__logo))
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre.setText(nombre)
    @direccion.setter
    def nombre(self,direccion):
        self.__direccion.setText(direccion)
        
    class Empresas(QScrollArea):
        empresa_seleccionada=Signal(str)
        def __init__(self, empresas, parent=None):
            super().__init__(parent)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.setWidgetResizable(True)

            self.empresas=[]
            self.widget=QWidget()
            self.setWidget(self.widget)
            self.empresasLayout=QVBoxLayout()

            for empresa in empresas:
                nueva_empresa=Empresa(json.loads(empresa))
                nueva_empresa.doble_clic.connect(self.doble_clic_empresa)
                self.empresasLayout.addWidget(nueva_empresa)
                self.empresas.append(nueva_empresa)

            espaciador=QSpacerItem(5, 1, QSizePolicy.Minimun, QSizePolicy.Expanding)
            self.empresasLayoutaddSpacerItem(espaciador)
            self.widget.setLayout(self.empresasLayout)

        def docble_clic_empresa(self, json_empresas):
            self.empresa_seleccionada.emit(json_empresas)
        


