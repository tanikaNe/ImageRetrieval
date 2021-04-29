from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QLabel


class ImageLabel(QLabel):
    """
    Create widget for query image drop
    Author: Weronika Wolska
    Created: 10.03.2021
    """

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('Drop Image Here')
        self.rotated = False

    def setPixmap(self, image):
        """
        Show the uploaded query image in place of a label
        :param image: query image
        """
        scale = 500

        if self.rotated:
            rotate = QTransform().rotate(90)
            image = image.transformed(rotate)
            super().setPixmap(image.scaled(scale, scale, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            super().setPixmap(image.scaled(scale, scale, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def image_format(self, rotated):
        """
        .jpg vertical images are rotated, check if this is the case
        :param rotated:
        """
        self.rotated = rotated
