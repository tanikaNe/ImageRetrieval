from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QDesktopWidget

from src.gui.results.results_list import ResultsList
from src.gui.selection.drag_drop import DragAndDrop


class MainWindow(QMainWindow):

    def __init__(self, connector):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Similar Image Finder")
        self.center()
        self.resize(1000, 1000)

        self.connector = connector

        drag_and_drop = DragAndDrop(self.connector, self)
        self.layout = QHBoxLayout()
        self.layout.addWidget(drag_and_drop)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)
        self.result_widget = None

    def setResults(self, results):
        if self.result_widget:
            self.layout.removeWidget(self.result_widget)

        self.result_widget = results
        self.layout.addWidget(self.result_widget)

    def center(self):
        frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())