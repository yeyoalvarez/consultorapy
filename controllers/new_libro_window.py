from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.nuevo_libro import nuevoLibroForm


class nuevoLibroWindow(QWidget, nuevoLibroForm):

    def __init__(self, parametro = None):
        super().__init__(parametro)

        self.setupUi(self)
        #abre en una ventana separada la nueva ventana
        self.setWindowFlag(Qt.Window) 

    def check_inputs(self):
        pass

    def add_book(self):
        pass

    def clean_inputs(self):
        pass

    def select_files(self):
        pass

    def undo(self):
        pass
