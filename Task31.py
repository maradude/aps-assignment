"""
as easy to understand k-dimensional range query for k-dimensional
rectangle queries where each side goes along the x- or y-axis.
"""


def check_in_bound(point, lbound, ubound):
    for d, bound in enumerate(zip(lbound, ubound)):
            if bound[0] <= point[d] <= bound[1]:
                pass
            else:
                return False
    return True


def simple_range_query(points, lbound, ubound):
    # in_range = []
    if len(lbound) != len(points[0]):
        print("points dimension and range erro don't match")
        raise ValueError
        return
    return filter(lambda p: check_in_bound(p, lbound, ubound), points)


if __name__ == '__main__':
    # expected return [10 4] [23 6] [30 10]
    from sanitize_input import get_input, Tests
    test_object = get_input('kd')
    # test_object = Tests(elements=[(3, 2), (10, 4), (23, 6), (30, 10), (62, 8), (47, 14), (105, 9),
                        # (89, 7)], ranges=[[7, 2], [47, 12], [0, 0], [200, 200]], dimensions=2)
    # print(test_object)
    tests = zip(test_object.ranges[::2], test_object.ranges[1::2])
    for test in tests:
        lower, upper = test
        a = [list(e) for e in (simple_range_query(test_object.elements, lower, upper))]
        print(str(a).replace(',', '')[1:-1])
