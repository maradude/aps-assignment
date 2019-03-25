#!/usr/bin/env python3

import sys
from dataclasses import dataclass  # requires Python 3.7
from json import loads
from re import sub
from typing import List


def get_input(type="1d"):
    """

    :param type: type of input request (Default value = "1d")
                 '1d' = 1-dimensional
                 'kd' = k-dimensional
                 'pkd' = polygonal k-dimensional
    """
    if type == "1d":
        return _get_1d_input()
    if type == "kd":
        return _get_kd_input()
    if type == "pkd":
        return _get_polygonal_kd_input()


def _get_polygonal_kd_input():
    """ """
    pass


def _get_kd_tree_parts():
    """
    read standard input for
    :return tests, points and dimensionality of given input
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
    return tests, points, k_dimensions, len_ranges


def _get_kd_input():
    """Read k numbers per line from stdin,
    first line needs to have amount of points, number of dimensions,
    and number of test ranges, subsequent r lines are points,
    lines after r are the tests cases where each test case needs
    be made of 2 elements per line, either a pairs of brackets for each query
    denoting min and max values for each dimension or for spherical
    cases brackets with kd point followed by a integer denoting radius

    e.g. "[9 20 5] [99 1000 9]" for a 3-dimensional rectange range query
    "[10 -20 30 40] 5" for a 4-dimensional sphere range suery

    :return: Test data object with points, ranges and dimensionality


    """
    tests, points, k_dimensions, len_ranges = _get_kd_tree_parts()
    arrays = [f"[{sub(' ', ',', next(tests))}]" for _ in range(len_ranges)]
    r = [loads(arr) for arr in arrays]
    return Tests(elements=points, ranges=r, dimensions=k_dimensions)


def _get_1d_input():
    """
    Read from standard input values and ranges
    first line is an interger value of how many values x and ranges y
    next x lines are integer values to be used as points
    next y lines have integer range pairs

    :return: Tets data object with points and ranges
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
    """

    :param range_string: String
    :return: Tuple[int]

    """
    return tuple(int(e) for e in range_string.split(' '))


@dataclass
class Tests:
    """just a record to hold elements list and range tuples"""
    elements: List
    ranges: List
    dimensions: int = 1


if __name__ == '__main__':
    a = get_input()
    print(a.elements)
    print(a.ranges)
