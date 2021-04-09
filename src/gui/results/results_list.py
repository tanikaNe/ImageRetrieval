from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel


class ResultsList(QWidget):
    def __init__(self, images):
        super().__init__()
        self.vbox = QVBoxLayout()
        # self.scroll = QScrollArea()
        self.initUI(images)

    def initUI(self, images):
        size = 100
        for img in images:
            image_label = QLabel(self)
            image_label.setPixmap(QPixmap(img).scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.vbox.addWidget(image_label)
            self.setLayout(self.vbox)

            # Scroll Area
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setWidget(self)
