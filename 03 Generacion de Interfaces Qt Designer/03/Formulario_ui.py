# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Formulario.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(509, 465)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 10, 171, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 380, 151, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 380, 151, 31))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(340, 380, 151, 31))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 420, 221, 31))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(260, 420, 231, 31))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 40, 471, 331))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.textEdit.copy)
        self.pushButton_3.clicked.connect(self.textEdit.paste)
        self.pushButton_4.clicked.connect(self.textEdit.selectAll)
        self.pushButton_5.clicked.connect(self.textEdit.clear)
        self.pushButton_2.clicked.connect(self.textEdit.cut)
        self.pushButton.clicked.connect(self.textEdit.selectAll)
        self.pushButton_2.clicked.connect(self.textEdit.selectAll)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Editor de texto", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Copiar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cortar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Pegar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Seleccionar todo", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Eliminar Texto", None))
    # retranslateUi

