"""
as easy to understand k-dimensional range query for k-dimensional
rectangle queries where each side goes along the x- or y-axis.
"""


def check_in_bound(point, lbound, ubound):
    """

    :param point: List[Sortable] k-dimensional point being checked
    :param lbound: List[Sortable] upper bound of each dimension
    :param ubound: List[Sortable] lower bound of each dimension
    :return: Bool True if all values in a point are between the same dimensions
             values in the lower and upper bound inclusive

    """
    for d, bound in enumerate(zip(lbound, ubound)):
        if not (bound[0] <= point[d] <= bound[1]):
            return False
    return True


def simple_range_query(points, lbound, ubound):
    """

    :param points: List[List[Sortable]] list of k-dimensional points to be checked
    :param lbound: List[Sortable] k-dimensional lower bound
    :param ubound: List[Sortable] k-dimensional upper bound
    :return: points between lower and upper bound in points
    """
    return filter(lambda p: check_in_bound(p, lbound, ubound), points)


def main():
    """
    for each test in test_objects convert two lists of bounds in to k lists
    of upper lower bound pairs for each (probably unncessary?)
    print each result on a new line after formatting into arrays with spaces between each dimensions point
    """
    for test in test_object.ranges:
        t = zip(test[::2], test[1::2])
        for test2 in t:
            lower, upper = test2
            a = [list(e) for e in (simple_range_query(
                test_object.elements, lower, upper))]
            print(str(a).replace(',', '')[1:-1])


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input('kd')
    main()
