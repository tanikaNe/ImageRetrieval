import _pickle


class DirectoriesList:
    def __init__(self, search_connector):
        self.search_connector = search_connector
        try:
            directories = open('directories.ww')
            self.directories = _pickle.read(directories)
            directories.close()
        except FileNotFoundError:
            self.directories = []

    def add_directory(self, directory):
        self.directories.append(directory)
        self.search_connector.process_directory(directory)


