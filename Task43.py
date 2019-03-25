"""
Create a KD-tree from a list of list with k sortable values inside,
where k mandates dimensionality of tree
"""


from operator import itemgetter


class KDTree:
    """ """

    def __init__(self, values):
        self.root = KDTree.BuildKDTree(values, 0)

    class _Node:
        """ """

        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

        def is_leaf(self):
            """maybe should be parameter?"""
            return self.left is None and self.right is None

    @staticmethod
    def BuildKDTree(points, current_depth):
        """

        :param points: List[List[Sortable]] list of lists with k sortable values
        :param current_depth: depth used to track which dimension is being considered for this
                              level of the tree
        :return: root node of newly created tree

        """
        # base case
        if len(points) == 1:
            return KDTree._Node(points[0])

        # recursive case
        axis = current_depth % len(points[0])
        points.sort(key=itemgetter(axis))  # should be precomputed

        medianPoint = points[(len(points)-1) // 2][axis]
        left_points = points[:((len(points)-1) // 2)+1]
        right_points = points[((len(points)-1) // 2)+1:]

        left_child = KDTree.BuildKDTree(left_points, current_depth + 1)
        right_child = KDTree.BuildKDTree(right_points, current_depth + 1)

        return KDTree._Node(medianPoint, left_child, right_child)


def main():
    """ """
    a = KDTree(test_object.elements)
    print(a)


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input('kd')
    main()
