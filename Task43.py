from dataclasses import dataclass


class KDTree:

    def __init__(self, values):
        self.root = KDTree.BuildKDTree(values, 0)

    @dataclass
    class _Node:
        data: int
        left: '_Node' = None
        right: '_Node' = None

    @staticmethod
    def BuildKDTree(points, current_depth):
        if len(points) == 1:
            return KDTree._Node(points[0])

        axis = current_depth % len(points[0])
        medianPoint = KDTree.get_median_point(points, axis)

        left_points = [p for p in points if p[axis] <= medianPoint]
        right_points = [p for p in points if p[axis] > medianPoint]

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
        current_axis_points = [point[axis] for point in points]
        return KDTree.integer_median(current_axis_points)


def main():
    from sanitize_input import get_input
    from print_tree import print2D
    test_object = get_input('kd')
    a = KDTree(test_object.elements)
    print2D(a.root)


if __name__ == '__main__':
    main()
