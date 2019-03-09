"""
as easy to understand k-dimensional range query for k-dimensional
rectangle queries where each side goes along the x- or y-axis.
"""


def check_in_bound(point, lbound, ubound):
    for d, bound in enumerate(zip(lbound, ubound)):
        if not (bound[0] <= point[d] <= bound[1]):
            return False
    return True


def simple_range_query(points, lbound, ubound):
    return filter(lambda p: check_in_bound(p, lbound, ubound), points)


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input('kd')
    tests = zip(test_object.ranges[::2], test_object.ranges[1::2])
    for test in tests:
        lower, upper = test
        a = [list(e) for e in (simple_range_query(
            test_object.elements, lower, upper))]
        print(str(a).replace(',', '')[1:-1])
