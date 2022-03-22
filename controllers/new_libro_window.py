from tkinter import Widget

from views.nuevo_libro import nuevoLibroForm


class nuevoLibroWindow(Widget, nuevoLibroForm):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

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
