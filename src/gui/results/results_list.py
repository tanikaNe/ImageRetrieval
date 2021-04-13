from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel, QScrollBar, QListWidget, QGroupBox, QGridLayout, \
    QListWidgetItem, QHBoxLayout


class ResultsList(QWidget):
    def __init__(self, images):
        super().__init__()

        self.initUI(images)

    def initUI(self, images):
        size = 100
        row_index = 0
        column_index = 0
        results_list_layout = QGridLayout()
        if images:
            for img in images:
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(img).scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                image_widget = QWidget()
                image_layout = QHBoxLayout()
                image_layout.setAlignment(Qt.AlignCenter)
                image_layout.addWidget(image_label)
                image_widget.setLayout(image_layout)
                results_list_layout.addWidget(image_widget, row_index, column_index)

                column_index += 1
                if column_index == 2:
                    column_index = 0
                    row_index += 1

            print(results_list_layout)

        label = QLabel()
        label.setText("Results")
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
