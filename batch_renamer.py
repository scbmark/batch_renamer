import qdarktheme
from PySide6 import QtWidgets

from app.controller import MainWindow_controller

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    qdarktheme.setup_theme("dark")

    window = MainWindow_controller()
    window.show()

    sys.exit(app.exec())
