import sys
from PyQt5.QtWidgets import QApplication
from gui.selection.drag_drop import DragAndDrop
from search_connector import SearchConnector
from gui.main_window import MainWindow


class Runner:
    def __init__(self):
        self.connector = SearchConnector("/media/taika/Data1/Pictures/coil-100")
        app = QApplication(sys.argv)
        main_window = MainWindow(self.connector)
        main_window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    Runner()
