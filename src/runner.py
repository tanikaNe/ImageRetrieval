import sys

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainWindow
from search_connector import SearchConnector


class Runner:
    def __init__(self):
        app = QApplication(sys.argv)
        self.connector = SearchConnector()
        main_window = MainWindow(self.connector)
        main_window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    Runner()
