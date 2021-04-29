from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTransform


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('Drop Image Here')
        self.orientation = ""

    def setPixmap(self, image):
        scale = 500

        if self.orientation == 'rotated':
            rotate = QTransform().rotate(90)
            image = image.transformed(rotate)
            super().setPixmap(image.scaled(scale, scale, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            super().setPixmap(image.scaled(scale, scale, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def image_format(self, orientation):
        self.orientation = orientation
