from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PIL import Image


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('Drop Image Here')

    def setPixmap(self, image):
        size = 900
        super().setPixmap(image.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
