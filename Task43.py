from dataclasses import dataclass
from operator import itemgetter


class KDTree:

    def __init__(self, values):
        self.root = KDTree.BuildKDTree(values, 0)

    @dataclass
    class _Node:
        data: int
        left: '_Node' = None
        right: '_Node' = None

        def is_leaf(self):
            return self.left is None and self.right is None

    @staticmethod
    def BuildKDTree(points, current_depth):
        if len(points) == 1:
            return KDTree._Node(points[0])
        axis = current_depth % len(points[0])
        points.sort(key=itemgetter(axis))
        medianPoint = points[(len(points)-1) // 2][axis]  # choose median
        left_points = points[:((len(points)-1) // 2)+1]
        right_points = points[((len(points)-1) // 2)+1:]

        left_child = KDTree.BuildKDTree(left_points, current_depth + 1)
        right_child = KDTree.BuildKDTree(right_points, current_depth + 1)

        return KDTree._Node(medianPoint, left_child, right_child)

    @staticmethod
    def integer_median(arr):
        """
        median index rounded down
        not using O(n) implementation cuz python sort
        beats python implementation of quickselect
        not to mention variance in lookups of quickselect
        https://bugs.python.org/issue21592
        """
        return sorted(arr)[(len(arr)-1)//2]

    @staticmethod
    def get_median_point(points, axis):
        # this should probably be precomputed for all dimensions
        current_axis_points = [point[axis] for point in points]
        return KDTree.integer_median(current_axis_points)


def main():
    from print_binary_tree import printTree
    a = KDTree(test_object.elements)
    printTree(a.root)


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input('kd')
    main()
