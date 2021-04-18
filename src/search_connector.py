import _pickle as pickle
import os

from PyQt5.QtCore import pyqtSignal, QObject, QThread

from extractor.features_extractor import FeatureExtractor
from gui.results.results_list import ResultsList
from matcher.kd_tree_matcher import KDTreeMatcher


class SearchConnector(QObject):
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
        self.dataset_path = dataset_path
        self.thread.start()

    def process_directory_sync(self, dataset_path):
        dataset = [os.path.join(dataset_path, pkl) for pkl in sorted(os.listdir(dataset_path))]
        # save image name and its features
        print("Dataset analysis in progress. Please wait.")
        processed = 0
        all_length = len(dataset)

        for img in dataset:
            if (img.endswith('.jpg') or img.endswith('.png')) and not self.file_already_processed(self.features_tuples,
                                                                                                  img):
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
        self.features_tuples = [x for x in self.features_tuples if not x[0].startswith(directory)]

    def find_images(self, image_path):
        images_list = self.matcher.find_neighbours(vectors=self.features_extractor.extract_features(image_path))
        return ResultsList(images_list)

    @staticmethod
    def file_already_processed(features_tuple, file):
        return file in [i[0] for i in features_tuple]

    @staticmethod
    def __load_features():
        file = open('vectors.ww', 'rb')
        load = pickle.load(file)
        file.close()
        return load


# for debugging
if __name__ == '__main__':
    # main = Main('/media/taika/Data1/Pictures/Japan/Japan')
    main = SearchConnector('/media/taika/Data1/Pictures/coil-100')
    query_image = input("Enter name of the image you want to match: ")
    # print(main.find_images('/media/taika/Data1/Pictures/Japan/Japan/' + query_image))
    print(main.find_images('/media/taika/Data1/Pictures/coil-100/' + query_image))
