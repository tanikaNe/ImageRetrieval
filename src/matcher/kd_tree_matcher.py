from sklearn.neighbors import KDTree


# TODO move functionality from constructor to dedicated method
class KDTreeMatcher:

    def __init__(self, dataset):
        self.dataset = dataset
        # dataset is a tuple with vectors on position [1] which we need to build the tree
        # vectors are of size 4096
        self.tree = KDTree(list(map(lambda val: val[1], dataset)), leaf_size=4096)

    def find_neighbours(self, vectors, dist_wage=1.2):
        """
        :param vectors: vectors to be matched
        :param dist_wage: minimal euclidean to accept
        :return: list with matched images' names
        """
        dist, index = self.tree.query([vectors], k=70)

        index = index[0]
        dist = dist[0]
        return list(map(self.__map_index, self.__filter_by_dist(dist, index, dist_wage)))

    def __map_index(self, index):
        """
        :param index: tuple's index
        :return: name of the file
        """
        return self.dataset[index][0]

    def __filter_by_dist(self, dist, indexes, dist_wage):
        accepted = []
        min_dist = max(dist) * 0.7 * dist_wage

        for i in range(len(dist)):
            if dist[i] < min_dist:
                accepted.append(indexes[i])
        return accepted
