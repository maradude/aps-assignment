from unittest import TestCase
from Task51 import Util
from Task43 import KDTree
from Task31 import simple_range_query
import random


class TestBruteKDsearch(TestCase):

    @staticmethod
    def random_coords(n, d):
        return [[random.randrange(1, 1000, 1) for _ in range(d)] for _ in range(n)]

    def test2(self):
        e = TestBruteKDsearch.random_coords(10**5, 10)
        a = KDTree(e).root
        lbound, ubound = ([250, 350, 450, 200, 150, 50, 500, 500, 500, 500],
                          [600, 700, 800, 300, 500, 400, 1000, 1000, 1000, 1000])
        real = list(simple_range_query(e, lbound, ubound))
        expected = Util(a, list(zip(lbound, ubound)))
        print()
        print(lbound)
        print(real)
        print(expected)
        print(ubound)
        self.assertEqual(sorted(expected), sorted(real))
