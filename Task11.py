from sanitize_input import get_input

# Θ(n) time for both adding n items to the list, and for querying the list.


class Array():

    def __init__(self, *args, length):
        # linear time construction
        self._values = [None]*length  # not really an optimisation in python
        i = 0
        for element in args:
            self._values[i] = element
            i += 1

    def get_range(self, lbound, ubound):
        # linear time range search
        return (element for element in self._values
                if lbound <= element <= ubound)


if __name__ == '__main__':
    test_object = get_input()
    nlist = Array(*test_object.elements, length=len(test_object.elements))
    for lower, upper in test_object.ranges:
        print(' '.join(map(str, nlist.get_range(lower, upper))))

