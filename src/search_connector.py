import _pickle as pickle
import os

from PyQt5.QtCore import pyqtSignal, QObject, QThread

from extractor.features_extractor import FeatureExtractor
from gui.results.results_list import ResultsList
from matcher.kd_tree_matcher import KDTreeMatcher


class SearchConnector(QObject):
    """
    Class connecting Feature extractor with KD Tree matcher. Create and removes any saved pickle files.
    Author: Weronika Wolska
    Created: 08.03.2021
    """

    process_finished = pyqtSignal(object)
    progress = pyqtSignal(float)

    dataset_path = None

    def run(self):
        if self.dataset_path is not None:
            self.process_directory_sync(self.dataset_path)

    def __init__(self):
        QObject.__init__(self)

        self.thread = QThread()
        self.moveToThread(self.thread)

        self.thread.started.connect(self.run)
        self.process_finished.connect(self.thread.quit)

        self.features_extractor = FeatureExtractor()
        try:
            self.features_tuples = self.__load_features()
        except (FileNotFoundError, EOFError):
            self.features_tuples = []

        self.matcher = KDTreeMatcher(dataset=self.features_tuples)

    def process_directory(self, dataset_path):
        """
        Process the directory with images
        :param dataset_path: path to the directory
        """
        self.dataset_path = dataset_path
        self.thread.start()

    def process_directory_sync(self, dataset_path):
        """
        Find and analyse images from the given path
        :param dataset_path: vectors to be matched
        """
        dataset = [os.path.join(dataset_path, pkl) for pkl in sorted(os.listdir(dataset_path))]
        # save image name and its features
        print("Dataset analysis in progress. Please wait.")
        processed = 0
        all_length = len(dataset)

        for img in dataset:
            img_name = img.lower()
            if (img_name.endswith('.jpg') or img_name.endswith('.png') or img_name.endswith(
                    '.jpeg')) and not self.file_already_processed(self.features_tuples, img):

                print("Analyzing: %s" % img)
                try:
                    img_features = (img, self.features_extractor.extract_features(img))
                    self.features_tuples.append(img_features)
                except OSError:
                    pass

            processed = processed + 1
            self.progress.emit(processed / float(all_length) * 100)

        file = open('vectors.ww', 'wb')
        pickle.dump(self.features_tuples, file)
        file.close()
        self.matcher = KDTreeMatcher(dataset=self.features_tuples)
        self.process_finished.emit('finished')

    def remove_directory(self, directory):
        """
        Remove directory from search
        :param vectors: vectors to be matched
        """
        self.features_tuples = [x for x in self.features_tuples if not x[0].startswith(directory)]
        self.matcher = KDTreeMatcher(dataset=self.features_tuples)

    def find_images(self, image_path):
        """
        Run KD Tree to find results
        :param image_path: query image
        :return: list with matched images
        """
        images_list = self.matcher.find_neighbours(vectors=self.features_extractor.extract_features(image_path))
        return ResultsList(images_list)

    @staticmethod
    def file_already_processed(features_tuple, file):
        """
        Return only file names from tuples containing vectors
        :param features_tuple: feature tuples
        :param file: file to be analysed
        :return: image paths from tuples
        """
        return file in [i[0] for i in features_tuple]

    @staticmethod
    def __load_features():
        """
        Load file with features
        :return: file with feature vectors
        """
        file = open('vectors.ww', 'rb')
        load = pickle.load(file)
        file.close()
        return load
