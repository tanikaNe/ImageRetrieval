from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDialog, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt

from src.gui.results.preview import ImagePreview


class ResultElement(QWidget):
    def __init__(self, image, parent):
        super().__init__(parent=parent)
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        image_label = QLabel(self)
        image_label.setPixmap(QPixmap(image).scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(image_label)
        self.setLayout(layout)

        self.image = image

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(a0)
        dialog = QDialog()
        dialog.setWindowTitle(self.image)
        layout = QVBoxLayout()
        dialog.setLayout(layout)
        layout.addWidget(ImagePreview(self.image))
        dialog.exec()


