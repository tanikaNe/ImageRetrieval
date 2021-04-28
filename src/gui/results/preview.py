from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication


class ImagePreview(QLabel):
    def __init__(self, img):
        super().__init__()
        geometry = QApplication.desktop().screenGeometry()
        self.setPixmap(QPixmap(img).scaled(geometry.width() - 100, geometry.height() - 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
