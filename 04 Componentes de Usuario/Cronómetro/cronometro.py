
import os

from DI_U04_A02_01 import CronometroUI
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PySide6.QtCore import Slot

import DI_U04_A03_01_0
import DI_U04_A03_03
import DI_U04_A02_03
import DI_U04_A02_01

Slot()
def mostrar_ocultar():
    if DI_U04_A03_01_0.isHidden():
        DI_U04_A03_01_0.show()
    else:
        DI_U04_A03_01_0.hide()


if __name__=="__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/Cronómetro/icons/cronometro"))
    app.setQuitOnLastWindowClosed(False)
    icon=QIcon(QIcon(("C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/Cronómetro/icons/cronometro")))
    tray=QSystemTrayIcon()
    tray.setVisible(True)
    tray.activated.connect(mostrar_ocultar)






