import sys

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainWindow
from search_connector import SearchConnector


class Runner:
    """
    Class that starts the software by creating MainWindow
    Author: Weronika Wolska
    Created: 01.04.2021
    """

    def __init__(self):
        app = QApplication(sys.argv)
        self.connector = SearchConnector()
        main_window = MainWindow(self.connector)
        main_window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    Runner()
