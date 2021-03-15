import sys
from PyQt5.QtWidgets import QApplication
from gui.selection.drag_drop import DragAndDrop
from search_connector import SearchConnector


class Runner:
    def __init__(self):
        self.connector = SearchConnector("/media/taika/Data1/Pictures/coil-100")
        app = QApplication(sys.argv)
        drag_n_drop = DragAndDrop(self.connector)
        drag_n_drop.show()
        sys.exit(app.exec_())


Runner()
