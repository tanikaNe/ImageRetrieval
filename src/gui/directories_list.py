import _pickle

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDialog, QListWidget, \
    QLayout, QListWidgetItem, QProgressBar


class DirectoriesList(QDialog):
    """
    Create a widget that manages the directories
    Author: Weronika Wolska
    Created: 17.04.2021
    """

    def __init__(self, search_connector, parent):
        super(DirectoriesList, self).__init__(parent)
        self.search_connector = search_connector

        self.search_connector.process_finished.connect(self.processing_finished)
        self.search_connector.progress.connect(self.__update_progress_bar)

        try:
            directories_file = open('directories.ww', 'rb')
            self.__directories = _pickle.load(directories_file)
            directories_file.close()
        except FileNotFoundError:
            self.__directories = []

        self.__create_directories_window()

    def __create_directories_window(self):
        """
        Open widget to manage directories
        """
        self.window = QWidget(parent=self)
        self.__create_layout()

        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle('Directories')
        self.setFixedHeight(250)
        self.exec()

    def __create_layout(self):
        """
        Create layout for directories widget
        """
        self.directories_layout = QVBoxLayout()
        self.window.setLayout(self.directories_layout)
        self.__show_directories()
        self.directories_layout.addWidget(self.directories_widget)
        self.__create_add_button()

    def __create_add_button(self):
        """
        Create a button to add new directories
        """
        button = QPushButton(text='Add')
        button.clicked.connect(self.__open_selector)
        self.directories_layout.addWidget(button)

    def __show_directories(self):
        """
        Display directories included in search
        """
        self.directories_widget = QListWidget(self)
        for directory in self.__directories:
            self.__add_directory_to_view(directory, self.directories_widget)

        self.directories_widget.setMinimumWidth(self.directories_widget.sizeHintForColumn(0) + 50)
        self.setMinimumWidth(self.directories_widget.minimumWidth() + 20)

    def __add_directory_to_view(self, directory, view):
        """
        Add directories to view list
        :param directory: a path to be added to the list in the view
        :param view: parent view to be added
        """
        list_widget = QListWidgetItem()
        line = QWidget()
        line_layout = QHBoxLayout()
        line.setLayout(line_layout)
        line_layout.addWidget(QLabel(directory))
        button = QPushButton(text='Delete')
        button.clicked.connect(lambda _: self.__remove_directory(directory))
        line_layout.addWidget(button)
        line_layout.addStretch()
        line_layout.setSizeConstraint(QLayout.SetFixedSize)
        list_widget.setSizeHint(line.sizeHint())

        view.addItem(list_widget)
        view.setItemWidget(list_widget, line)

    def __add_directory(self, directory):
        """
        Add directory with images to look for matches
        :param directory: directory with images to be added to look for matches
        """
        if directory:
            if not self.__directories.__contains__(directory):
                self.search_connector.process_directory(directory)
                self.__directories.append(directory)
                self.__show_processing(self)
            else:
                info_dialog = QDialog(self)
                info_dialog.setWindowTitle('Already added')
                info_layout = QVBoxLayout()
                info_layout.addWidget(QLabel(text="Directory {} was already added".format(directory)))
                info_dialog.setLayout(info_layout)
                info_dialog.exec()

    def processing_finished(self):
        """
        Inform system that directory analysis is finished
        """
        self.processing_dialog.close()
        self.__store()
        self.__add_directory_to_view(self.__directories[-1], self.directories_widget)

    def __show_processing(self, parent):
        """
        Show dialog with progress bar
        :param parent: parent widget
        """
        processing_layout = QVBoxLayout()
        processing_layout.addWidget(QLabel(text="processing in progress"))
        self.processing_dialog = QDialog(parent)
        self.processing_dialog.setWindowTitle("Processing")
        self.processing_dialog.setLayout(processing_layout)

        self.progress_bar = QProgressBar(self.processing_dialog)
        self.progress_bar.setGeometry(200, 80, 250, 20)
        self.progress_bar.setValue(0)
        processing_layout.addWidget(self.progress_bar)

        self.processing_dialog.exec()

    def __update_progress_bar(self, value):
        """
        Update the progress bar
        :param value: progress
        """
        if self.progress_bar is not None:
            self.progress_bar.setValue(value)

    def __remove_directory(self, directory):
        """
        Remove directory from the list
        :param directory: selected directory
        """
        self.__directories.remove(directory)
        self.search_connector.remove_directory(directory)
        self.__store()
        self.__update_view()

    def __update_view(self):
        """
        Update directories list if one was added or removed
        """
        self.directories_layout.removeWidget(self.directories_widget)
        self.__show_directories()
        self.directories_layout.insertWidget(0, self.directories_widget)

    def __open_selector(self):
        """
        Open system window to choose a directory
        """
        self.__add_directory(QFileDialog.getExistingDirectory())

    def __store(self):
        """
        Save directory to file with directories
        """
        directories = open('directories.ww', 'wb')
        _pickle.dump(self.__directories, directories)
        directories.close()
