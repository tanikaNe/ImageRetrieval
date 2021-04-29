from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog, QHBoxLayout, QApplication

from gui.preview import ImagePreview


class ResultElement(QWidget):
    """
    Create view for result item
    Author: Weronika Wolska
    Created: 10.04.2021
    """

    def __init__(self, image, parent):
        super().__init__(parent=parent)
        self.image = image
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(ImagePreview(self.image, 250, 250))

        self.setLayout(layout)
        self.image = image

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        Open full screen image of the selected result image
        :param a0:
        """
        super().mousePressEvent(a0)
        scale = QApplication.desktop().screenGeometry()
        width = scale.width()
        height = scale.height()
        dialog = QDialog()
        dialog.setWindowTitle(self.image)
        layout = QVBoxLayout()
        dialog.setLayout(layout)
        layout.addWidget(ImagePreview(self.image, width - 100, height - 100))
        dialog.exec()
