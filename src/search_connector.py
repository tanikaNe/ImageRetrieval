import _pickle as pickle
import os

from extractor.features_extractor import FeatureExtractor
from gui.results.results_list import ResultsList
from matcher.kd_tree_matcher import KDTreeMatcher


class SearchConnector:
    def __init__(self, dataset_path):
        self.features_extractor = FeatureExtractor()
        try:
            self.features_tuples = self.__load_features()
        except (FileNotFoundError, EOFError):
            self.features_tuples = []

        self.matcher = KDTreeMatcher(dataset=self.features_tuples)
        self.process_directory(dataset_path)

    def process_directory(self, dataset_path):
        dataset = [os.path.join(dataset_path, pkl) for pkl in sorted(os.listdir(dataset_path))]
        # save image name and its features
        print("Dataset analysis in progress. Please wait.")
        for img in dataset:
            if (img.endswith('.jpg') or img.endswith('.png')) and not self.file_already_processed(features_tuples, img):
                print("Analyzing: %s" % img)
                try:
                    img_features = (img, self.features_extractor.extract_features(img))
                    self.features_tuples.append(img_features)
                except OSError:
                    continue
            else:
                continue
        file = open('vectors.pck', 'wb')
        pickle.dump(self.features_tuples, file)
        file.close()
        self.matcher = KDTreeMatcher(dataset=self.features_tuples)

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
        file = open('vectors.pck', 'rb')
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
