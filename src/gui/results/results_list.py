from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel, QGridLayout

from gui.results.result_element import ResultElement


class ResultsList(QWidget):
    """
    Create View with results
    Author: Weronika Wolska
    Created: 10.04.2021
    """

    def __init__(self, images):
        super().__init__()

        self.initUI(images)

    def initUI(self, images):
        if len(images) > 0:
            row_index = 0
            column_index = 0
            results_list_layout = QGridLayout()
            if images:
                for img in images:
                    # check if image exists
                    try:
                        open(img, 'rb').close()

                        results_list_layout.addWidget(ResultElement(img, self), row_index, column_index)

                        column_index += 1
                        if column_index == 2:
                            column_index = 0
                            row_index += 1
                    except FileNotFoundError:
                        continue

            label = QLabel()
            label.setText("Results\nClick on the picture to open it")
            label.setAlignment(Qt.AlignCenter)
            list_widget = QWidget()
            list_widget.setLayout(results_list_layout)
            scroll = QScrollArea()
            scroll.setWidget(list_widget)
            scroll.setWidgetResizable(True)

            layout = QVBoxLayout(self)
            layout.addWidget(label)
            layout.addWidget(scroll)
            self.setLayout(layout)
        else:
            layout = QVBoxLayout(self)
            layout.addWidget(QLabel(text="No images found"))
            self.setLayout(layout)
