import sys
from dataclasses import dataclass  # requires Python 3.7
from typing import List, Tuple


def get_input():
    """
    Read tests from stdin
    return object with elements and ranges
    """
    try:
        tests = (line for line in sys.stdin)
    except TypeError as e:
        print(e)
        sys.exit()

    len_elements, len_ranges = next(tests).split(' ')
    elements = [int(next(tests)) for _ in range(int(len_elements))]
    ranges = [parse_range(next(tests)) for _ in range(int(len_ranges))]
    return Tests(elements=elements, ranges=ranges)


def parse_range(range_string):
    return tuple(int(e) for e in range_string.split(' '))


@dataclass
class Tests:
    """
    just a record to hold elements list and range tuples
    """
    elements: List[int]
    ranges: List[Tuple[int]]


if __name__ == '__main__':
    a = get_input()
    print(a.elements)
    print(a.ranges)

# 8 2 3 10 23 30 62 47 105 89 7 47 10 89
# expect output 10 23 30 47
# or 10 23 30 62 47 89
