import os
import _pickle as pickle
from extractor.features_extractor import FeatureExtractor
from matcher.kd_tree_matcher import KDTreeMatcher
from gui.results.results_list import ResultsList


class SearchConnector:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.features_extractor = FeatureExtractor()
        dataset = [os.path.join(dataset_path, pkl) for pkl in sorted(os.listdir(dataset_path))]
        # save image name and its features
        features_tuples = []

        try:
            features_tuples = self.__load_features()
        except (FileNotFoundError, EOFError):
            print("Dataset analysis in progress. Please wait.")
            file = open(self.dataset_path + '/vectors.pck', 'wb')
            for img in dataset:
                if img.endswith('.jpg') or img.endswith('.png'):
                    print("Analyzing: %s" % img)
                    try:
                        img_features = (img, self.features_extractor.extract_features(img))
                        features_tuples.append(img_features)
                    except OSError:
                        continue
                else:
                    continue
            pickle.dump(features_tuples, file)
            file.close()

        self.matcher = KDTreeMatcher(dataset=features_tuples)

    def find_images(self, image_path):
        images_list = self.matcher.find_neighbours(vectors=self.features_extractor.extract_features(image_path))
        return ResultsList(images_list)

    def __load_features(self):
        file = open(self.dataset_path + '/vectors.pck', 'rb')
        load = pickle.load(file)
        file.close()
        return load

    def open_file(self, database):
        return open(self.dataset_path + database, 'rb')


# for debugging
if __name__ == '__main__':
    # main = Main('/media/taika/Data1/Pictures/Japan/Japan')
    main = SearchConnector('/media/taika/Data1/Pictures/coil-100')
    query_image = input("Enter name of the image you want to match: ")
    # print(main.find_images('/media/taika/Data1/Pictures/Japan/Japan/' + query_image))
    print(main.find_images('/media/taika/Data1/Pictures/coil-100/' + query_image))
