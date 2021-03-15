from PyQt5.QtGui import QPixmap
from gui.selection.image_label import ImageLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame


class DragAndDrop(QWidget):
    def __init__(self, connector):
        super().__init__()
        self.file_path = None
        self.connector = connector
        self.photo_viewer = ImageLabel()
        self.create_widget()

    def create_widget(self):
        main_layout = QVBoxLayout()
        self.setGeometry(200, 200, 300, 300)
        self.setAcceptDrops(True)
        button = self.create_button()

        main_layout.addWidget(self.photo_viewer)
        main_layout.addWidget(button)
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
            self.file_path = file_path
            self.set_image(file_path)
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photo_viewer.setPixmap(QPixmap(file_path))

    def create_button(self):
        button = QPushButton(self)
        button.setText("Confirm")
        button.clicked.connect(self.clicked)
        return button

    def clicked(self):
        # TODO print images in gui list
        print(self.connector.find_images(self.file_path))
