from unittest import TestCase
from sanitize_input import Tests
import Task21
from Task11 import get_range
import random


class TestRangeTree(TestCase):
    """ """

    # def test1(self):
    #     a = Tests(elements=[3, 10, 23, 30, 62, 47, 105, 89],
    #               ranges=[(7, 47), (10, 89)], dimensions=1)
    #     expected = [10, 23, 30, 62, 47, 89]
    #     real = Task21.RangeTree(a.elements).one_d_range_query(*a.ranges[1])
    #     self.assertEqual(sorted(expected), sorted(real))

    def test2(self):
        """ """
        # b = [random.randrange(0, 1000, 1) for e in range(1000)]
        b = [623, 661, 691, 116, 333, 366, 631, 423, 712, 764]
        c = [(0, 100)]
        a = Tests(elements=b,
                  ranges=c, dimensions=1)
        expected = get_range(b, *c[0])
        real = Task21.RangeTree(a.elements).one_d_range_query(*a.ranges[0])
        self.assertEqual(sorted(expected), sorted(real))

