from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QDesktopWidget, QLabel

from gui.selection.drag_drop import DragAndDrop


class MainWindow(QMainWindow):
    """
    Create window with widgets for query image and results
    Author: Weronika Wolska
    Created: 20.03.2021
    """

    def __init__(self, connector):
        super(MainWindow, self).__init__()

        self.connector = connector
        self.result_widget = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Similar Image Finder")
        self.center()
        self.resize(1500, 1000)

        drag_and_drop = DragAndDrop(self.connector, self)
        self.layout = QHBoxLayout()
        self.layout.addWidget(drag_and_drop)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

    def setResults(self, results):
        """
        Create widget to display the results
        :param: image widgets to be displayed
        """
        if self.result_widget:
            self.layout.removeWidget(self.result_widget)

        self.result_widget = results
        self.layout.addWidget(self.result_widget)

    def center(self):
        """
        Open window in the center of the screen
        """
        frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def print_label(self):
        """
        Show information label
        """
        resubmit_label = QLabel()
        resubmit_label.setText("To start a new search, drag and drop a new image and click confirm")
        resubmit_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(resubmit_label)
