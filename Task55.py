"""
KD range search for n-spheres, actual KD-Tree search is done
by building a hypercube around the  n-sphere and then checking
values returned if they really are contained in the circular area
"""

from Task51 import get_range


def point_in_sphere(test, point, radius):
    """

    :param test: List[List[Sortable]] center point of the n-sphere
    :param point: List[List[Sortable]] point in hypercube to be evaluated if in n-sphere
    :param radius: int radius of the n-sphere

    """
    # some math to check if a given point is in radius
    d = sum((a - b)**2 for a, b in zip(test, point))
    return d < radius**2


def spehere_to_square(point, radius):
    """

    :param point: List[List[Sortable]] center point of the n-sphere
    :param radius: int radius of the n-sphere
    :return: List[List[Sortable]] hypercube surrounding the n-sphere
    """
    return [[p-radius, p+radius] for p in point]


def sphere_query(root, test):
    ranges_by_dimension = spehere_to_square(*test)
    a = get_range(root, ranges_by_dimension)
    return [list(e) for e in a if point_in_sphere(test[0], e, test[1])]


def main():
    """
    Create KD tree, box sphere, query box and then filter out
    values in box not in sphere.
    for each range print results in a new line
    """
    from Task43 import KDTree
    tree = KDTree(test_object.elements)
    for test in test_object.ranges:
        b = sphere_query(tree.root, test)
        print(str(b).replace(',', '')[1:-1])


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input('kd')
    main()
