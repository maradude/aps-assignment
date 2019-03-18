class SortedRangeList:

    def __init__(self, args):
        self._values = list(sorted(args))
        self._len = len(self._values)

    def __len__(self):
        return self._len

    def get_range(self, lbound, ubound):
        # binary search lower bound, then extract element until upper bound
        min_i = SortedRangeList._findStart(self._values, lbound, 0, len(self))
        # hi_i = SortedRangeList._get_rest(self._values, min_i, ubound) + 1
        hi_i = SortedRangeList._findEnd(self._values, ubound, min_i, len(self))
        return self._values[min_i:hi_i]
        # return SortedRangeList._get_rest(self._values, min_i, ubound)

    def _findEnd(arr, target, lbound, hbound):
        # find the index of the last occurance of k in the array
        if lbound > hbound:
            return lbound
        mid_point = (lbound+hbound) // 2
        if arr[mid_point] > target:
            return SortedRangeList._findEnd(arr, target, lbound, mid_point-1)
        else:
            return SortedRangeList._findEnd(arr, target, mid_point+1, hbound)

    @staticmethod
    def _findStart(arr, target, lbound, ubound):
        # it's the left most k algorithm, lifted from slides pseudocode
        if ubound < lbound:
            return lbound
        mid_point = (lbound+ubound) // 2
        if arr[mid_point] < target:
            return SortedRangeList._findStart(arr, target, mid_point+1, ubound)
        else:
            return SortedRangeList._findStart(arr, target, lbound, mid_point-1)

    @staticmethod
    def _get_rest(arr, low_i, ubound):
        hi_i = low_i
        while arr[hi_i] <= ubound:
            hi_i += 1
        return hi_i


def main():
    nlist = SortedRangeList(test_object.elements)
    for lower, upper in test_object.ranges:
        print(' '.join(map(str, nlist.get_range(lower, upper))))


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input()
    main()
