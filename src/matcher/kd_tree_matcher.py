from sklearn.neighbors import KDTree


class KDTreeMatcher:
    """
    Creates KD Tree matcher to find resuls
    """
    def __init__(self, dataset):
        self.dataset = dataset
        # dataset is a tuple with vectors on position [1] which we need to build the tree
        # vectors are of size 4096
        if dataset:
            self.tree = KDTree(list(map(lambda val: val[1], dataset)), leaf_size=4096)

    def find_neighbours(self, vectors):
        """
        :param vectors: vectors to be matched
        :return: list with matched images' names
        """
        if self.dataset:
            dist, index = self.tree.query([vectors], k=6)

            index = index[0]
            dist = dist[0]
            return list(map(self.__map_index, self.__filter_by_dist(dist, index)))
        else:
            return []

    def __map_index(self, index):
        """
        :param index: tuple's index
        :return: name of the file
        """
        return self.dataset[index][0]

    @staticmethod
    def __filter_by_dist(dist, indexes):
        """
        :param dist: max distance from the query image
        :param indexes: indexes of files in dataset
        return: accepted files within distance
        """
        accepted = []
        max_dist = 75

        for i in range(len(dist)):
            if dist[i] < max_dist and dist[i] != 0:
                accepted.append(indexes[i])
        if len(accepted) == 6:
            accepted = accepted[:5]
        return accepted
