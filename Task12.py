#!/usr/bin/env python3


"""
Sort list of values, perform binary search to find smallest element
that is larger or equal to a given lower bound, then using that as a lower bound
perform binary search to find the largest element smaller or equalt to a given upper bound
return all values in the list between the two.
"""


class SortedRangeList:
    """ """

    def __init__(self, args):
        self._values = list(sorted(args))
        self._len = len(self._values)

    def __len__(self):
        return self._len

    def get_range(self, lbound, ubound):
        """

        :param lbound: Sortable lower bound
        :param ubound: Sortable upper bound
        :return List[Sortable] all values contained in self, between lower and upper bound inclusive

        """
        largest_element = self._values[-1]
        # helps with index errors
        if largest_element < lbound:
            min_i = len(self)
        else:
            min_i = SortedRangeList._findStart(self._values, lbound, 0, len(self))
        if largest_element <= ubound:
            hi_i = len(self)
        else:
            hi_i = SortedRangeList._findEnd(self._values, ubound, min_i, len(self))

        return self._values[min_i:hi_i]

    def _findEnd(arr, target, lbound, hbound):
        """

        :param arr: List[Sortable] to perform binary search on
        :param target: Sortable used for comparisons
        :param lbound: Sortable lower bound
        :param hbound: Sortable upper bound
        :return int index position of largest element smaller or equal to target
        """
        # find the index of the last occurance of k in the array

        # base case 1
        if lbound > hbound:
            return lbound

        mid_point = (lbound+hbound) // 2

        # recursive case
        if arr[mid_point] > target:
            return SortedRangeList._findEnd(arr, target, lbound, mid_point-1)
        else:
            return SortedRangeList._findEnd(arr, target, mid_point+1, hbound)

    @staticmethod
    def _findStart(arr, target, lbound, ubound):
        """

        :param arr: List[Sortable] to perform binar search on
        :param target: Sortable used for comparisions
        :param lbound: Sortable lower bound
        :param ubound: Sortable upper bound
        :return int index position of smallest element larger or equal to target

        """
        # it's the left most k algorithm, lifted from slides pseudocode

        # base case
        if ubound < lbound:
            return lbound

        # recursive case
        mid_point = (lbound+ubound) // 2
        if arr[mid_point] < target:
            return SortedRangeList._findStart(arr, target, mid_point+1, ubound)
        else:
            return SortedRangeList._findStart(arr, target, lbound, mid_point-1)


def main():
    """
    perform range query for all ranges
    print query results on new lines
    """
    nlist = SortedRangeList(test_object.elements)
    for lower, upper in test_object.ranges:
        print(' '.join(map(str, nlist.get_range(lower, upper))))


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input()
    main()
