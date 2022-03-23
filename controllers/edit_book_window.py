from tkinter import Widget
from PySide2.QtWidgets import QWidget
from views.editar_libro import editLibroForm 

class editLibroWindow(Widget, editLibroForm):
    
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def populate_inputs(self):
        pass

    def select_file(self):
        pass

    def check_inputs(self):
        pass

    def edit_book(self):
        pass