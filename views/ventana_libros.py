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


class main_ventana_libros(object):
    def setupUi(self, main_ventana_libros):
        if not main_ventana_libros.objectName():
            main_ventana_libros.setObjectName(u"main_ventana_libros")
        main_ventana_libros.resize(800, 600)
        self.frame = QFrame(main_ventana_libros)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 721, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.botonAddLibro = QPushButton(self.frame)
        self.botonAddLibro.setObjectName(u"botonAddLibro")
        self.botonAddLibro.setGeometry(QRect(30, 10, 81, 51))
        self.botonAddLibro.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/iconos/add-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAddLibro.setIcon(icon)
        self.botonAddLibro.setIconSize(QSize(45, 45))
        self.botonAddLibro.setFlat(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 81, 16))
        self.botonAddLibro_2 = QPushButton(self.frame)
        self.botonAddLibro_2.setObjectName(u"botonAddLibro_2")
        self.botonAddLibro_2.setGeometry(QRect(120, 10, 81, 51))
        self.botonAddLibro_2.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/iconos/edit-book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAddLibro_2.setIcon(icon1)
        self.botonAddLibro_2.setIconSize(QSize(45, 45))
        self.botonAddLibro_2.setFlat(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 60, 81, 16))
        self.frame_2 = QFrame(main_ventana_libros)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 110, 721, 81))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 30, 81, 16))
        self.buscarPorComboBox = QComboBox(self.frame_2)
        self.buscarPorComboBox.setObjectName(u"buscarPorComboBox")
        self.buscarPorComboBox.setGeometry(QRect(100, 30, 131, 22))
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 30, 331, 20))
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 20, 91, 25))
        icon2 = QIcon()
        icon2.addFile(u"./assets/iconos/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 50, 91, 25))
        icon3 = QIcon()
        icon3.addFile(u"./assets/iconos/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.tableView = QTableView(main_ventana_libros)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(70, 210, 681, 351))
        self.label_4 = QLabel(main_ventana_libros)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 570, 111, 16))
        self.cantidadLibros = QLabel(main_ventana_libros)
        self.cantidadLibros.setObjectName(u"cantidadLibros")
        self.cantidadLibros.setGeometry(QRect(210, 570, 51, 16))

        self.retranslateUi(main_ventana_libros)

        QMetaObject.connectSlotsByName(main_ventana_libros)
    # setupUi

    def retranslateUi(self, main_ventana_libros):
        main_ventana_libros.setWindowTitle(QCoreApplication.translate("main_ventana_libros", u"lista_libros", None))
        self.botonAddLibro.setText("")
        self.label.setText(QCoreApplication.translate("main_ventana_libros", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">a\u00f1adir libro</span></p></body></html>", None))
        self.botonAddLibro_2.setText("")
        self.label_2.setText(QCoreApplication.translate("main_ventana_libros", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">editar libro</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("main_ventana_libros", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">buscar por:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("main_ventana_libros", u"buscar", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_ventana_libros", u"actualizar", None))
        self.label_4.setText(QCoreApplication.translate("main_ventana_libros", u"<html><head/><body><p><span style=\" font-weight:600;\">cantidad de libros</span></p></body></html>", None))
        self.cantidadLibros.setText(QCoreApplication.translate("main_ventana_libros", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

