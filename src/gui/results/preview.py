from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImagePreview(QLabel):
    def __init__(self, img):
        super().__init__()
        geometry = QApplication.desktop().screenGeometry()
        self.setPixmap(QPixmap(img).scaled(geometry.width() - 200, geometry.height() - 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
