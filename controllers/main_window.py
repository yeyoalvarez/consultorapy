from PySide2.QtWidgets import QWidget

from views.ventana_libros import main_ventana_libros


class listBookWindows(QWidget, main_ventana_libros):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def open_new_book_window(self):
        pass

    def open_edit_window(self):
        pass

    def populate_table(self):
        pass

    def populate_combobox(self):
        pass

    def search_book_title(self):
        pass

    def search_book_autor(self):
        pass

    # verifica que opcion de busqueda selecciono el user
    def search(self):
        pass

    def cantidad_libros(self):
        pass
