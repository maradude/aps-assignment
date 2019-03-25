#!/usr/bin/env python3

"""
Check each value in a unsorted list if they are between a lower bound
and a uppper bound inclusive, return those which are.
"""


def get_range(arr, lbound, ubound):
    """

    :param arr: List[Sortable]
    :param lbound: Sortable lower bound
    :param ubound: Sortable upper bound
    :return List[Sortable] all elements of arr that are between lbound and ubound inclusive

    """
    return (element for element in arr if lbound <= element <= ubound)


def main():
    """
    run get_range for all ranges provided in test_object
    print results of get_range() on a new line for each range
    """
    for lower, upper in test_object.ranges:
        result = get_range(test_object.elements, lower, upper)
        print(' '.join(map(str, result)))


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input()
    main()
