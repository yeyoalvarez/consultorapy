# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_libros.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_formulario_libros(object):
    def setupUi(self, formulario_libros):
        if not formulario_libros.objectName():
            formulario_libros.setObjectName(u"formulario_libros")
        formulario_libros.resize(800, 600)
        self.boton = QPushButton(formulario_libros)
        self.boton.setObjectName(u"boton")
        self.boton.setGeometry(QRect(90, 490, 161, 61))

        self.retranslateUi(formulario_libros)

        QMetaObject.connectSlotsByName(formulario_libros)
    # setupUi

    def retranslateUi(self, formulario_libros):
        formulario_libros.setWindowTitle(QCoreApplication.translate("formulario_libros", u"lista_libros", None))
        self.boton.setText(QCoreApplication.translate("formulario_libros", u"PushButton", None))
    # retranslateUi

