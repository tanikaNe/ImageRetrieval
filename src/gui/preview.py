import exifread
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QLabel


class ImagePreview(QLabel):
    """
    Create image preview using Pixmap
    Author: Weronika Wolska
    Created: 29.04.2021
    """

    def __init__(self, img, width, height):
        super().__init__()

        if self.check_rotation(img):
            rotate = QTransform().rotate(90)
            img = QPixmap(img)
            img = img.transformed(rotate)

        self.setPixmap(QPixmap(img).scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def check_rotation(self, image):
        """
        .jpg vertical images are rotated by 90 degrees, if the file is rotated, fix it
        :param image: image path to be checked
        :return: boolean True if image is rotated, False if not
        """
        if image.endswith(".jpg"):
            # only .jpg vertical files are broken
            file = open(image, 'rb')
            image_data = exifread.process_file(file)
            rotate = image_data['Image Orientation']

            if str(rotate) == 'Rotated 90 CW':
                return True
            else:
                return False
