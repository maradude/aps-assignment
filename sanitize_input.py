import sys
from dataclasses import dataclass  # requires Python 3.7
from typing import List
from re import sub
from json import loads


def get_input(type="1d"):
    if type == "1d":
        return _get_1d_input()
    if type == "kd":
        return _get_kd_input()


def _get_kd_input():
    """
    Read k numbers per line from stdin,
    first line needs to have amount of points, number of dimensions,
    and number of test ranges, where ranges are points inside square
    brackets where 2 brackets for each query denoting min and max values
    for each dimension.

    e.g. [9 20 5] [99 1000 9] for a 3-dimensional range query

    return object with points and ranges
    """
    try:
        tests = (line for line in sys.stdin)
    except TypeError as e:
        print(e)
        sys.exit()
    len_points, k_dimensions, len_ranges = map(int, next(tests).split(' '))
    points = []
    for _ in range(len_points):
        points.append(tuple(int(n) for n in next(tests).split(' ')))
    array = sub(' ', ',', next(tests))
    ranges = loads(f"[{array}]")
    return Tests(elements=points, ranges=ranges, dimensions=k_dimensions)


def _get_1d_input():
    """
    Read 1 number per line from stdin,
    first line needs to have amount of points and ranges
    return object with elements and ranges
    """
    try:
        tests = (line for line in sys.stdin)
    except TypeError as e:
        print(e)
        sys.exit()

    len_elements, len_ranges = map(int, next(tests).split(' '))
    elements = [int(next(tests)) for _ in range(len_elements)]
    ranges = [parse_range(next(tests)) for _ in range(len_ranges)]
    return Tests(elements=elements, ranges=ranges)


def parse_range(range_string):
    return tuple(int(e) for e in range_string.split(' '))


@dataclass
class Tests:
    """
    just a record to hold elements list and range tuples
    """
    elements: List[int]
    ranges: any
    dimensions: int = 1


if __name__ == '__main__':
    a = get_input()
    print(a.elements)
    print(a.ranges)

# 8 2 3 10 23 30 62 47 105 89 7 47 10 89
# expect output 10 23 30 47
# or 10 23 30 62 47 89
