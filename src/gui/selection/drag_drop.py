from PyQt5.QtGui import QPixmap
from gui.selection.image_label import ImageLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class DragAndDrop(QWidget):
    def __init__(self, connector):
        size = 900
        super().__init__()
        # self.file_path = None
        self.connector = connector
        self.resize(size, size)
        self.setAcceptDrops(True)
        # button = self.QPushButton(self)
        # button.setText("Confirm")

        main_layout = QVBoxLayout()

        self.photo_viewer = ImageLabel()
        main_layout.addWidget(self.photo_viewer)
        self.setLayout(main_layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            print(self.connector.find_images(file_path))
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photo_viewer.setPixmap(QPixmap(file_path))
