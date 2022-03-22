from PySide2.QtWidgets import QApplication
from controllers.main_window import listBookWindows

if __name__ == "__main__":
    app = QApplication()
    window = listBookWindows()
    window.show() #ver ventana

    app.exec_()#ejecuta la aplicacion