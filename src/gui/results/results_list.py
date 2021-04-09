from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QVBoxLayout, QScrollArea, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets
import sys
import os


class ResultsList(QWidget):
    def __init__(self, images):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.widget = QWidget()
        self.scroll = QScrollArea()
        self.initUI(images)

    def initUI(self, images):
        size = 100
        print(images)
        for img in images:
            image_label = QLabel(self)
            print(os.getcwd())
            image_label.setPixmap(QPixmap(img).scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.vbox.addWidget(image_label)
            self.widget.setLayout(self.vbox)

            #Scroll Area
            self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scroll.setWidgetResizable(True)
            self.scroll.setWidget(self.widget)

            self.setGeometry(600, 100, 1000, 900)
            self.show()

            return

