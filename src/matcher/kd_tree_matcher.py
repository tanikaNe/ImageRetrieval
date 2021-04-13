from sklearn.neighbors import KDTree

#TODO move functionality from constructor to dedicated method
class KDTreeMatcher:

    def __init__(self, dataset):
        self.dataset = dataset
        # dataset is a tuple with vectors on position [1] which we need to build the tree
        # vectors are of size 4096
        self.tree = KDTree(list(map(lambda val: val[1], dataset)), leaf_size=4096)

    def find_neighbours(self, vectors):
        """
        :param vectors: vectors to be matched
        :return: list with matched images' names
        """
        dist, index = self.tree.query([vectors], k=70)
        index = index[0]
        return list(map(self.__map_index, index))

    def __map_index(self, index):
        """
        :param index: tuple's index
        :return: name of the file
        """
        return self.dataset[index][0]
