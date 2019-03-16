from Task11 import get_range
from Task12 import SortedRangeList
from Task21 import RangeTree
from sanitize_input import get_input

test_object = get_input()


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("get_range(test_object.elements, *test_object.ranges[0])", globals=globals()))
