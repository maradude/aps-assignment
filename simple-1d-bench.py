import pickle
import Task11
import Task12
import Task21
from sanitize_input import Tests
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import count


def random_bound1d():
    a = random.randrange(1, 999, 1)
    return a, random.randrange(a, 1000, 1)

def naive_bench(elements, *_):
    bounds = [random_bound1d() for _ in range(100)]
    res = []
    for n in elements:
        bres = []
        b = len(n)
        print(f'---{b}---')
        for l, u in bounds:
            a = get_ipython().run_line_magic('timeit', '-o -r1 list(Task11.get_range(n, l, u))')
            bres.append(a)
        res.append((b,bres))
    return res

def build_range_tree(elements, *_):
    res = []
    for n in elements:
        resb = []
        b = len(n)
        print(f'---{b}---')
        for n in range(100):
            m = [random.randrange(1, 1000, 1) for _ in range(b)]
            a = get_ipython().run_line_magic('timeit', '-o -r1 Task21.RangeTree(m)')
            resb.append(a)
        res.append((b,resb))
    return res

def build_sorted_list(elements, *_):
    res = []
    for n in elements:
        resb = []
        b = len(n)
        print(f'---{b}---')
        for i in range(100):
            m = [random.randrange(1, 1000, 1) for _ in range(b)]
            a = get_ipython().run_line_magic('timeit', '-o -r1 Task12.SortedRangeList(m)')
            resb.append(a)
        res.append((b,resb))
    return res

def tree_search_only(elements, *_):
    objs = (Task21.RangeTree(e) for e in elements)
    bounds = [random_bound1d() for _ in range(100)]
    res = []
    for i, n in enumerate(objs):
        bres  = []
        b = 10**(i+1)
        print(f'---{b}---')
        for l, h in bounds: 
            a = get_ipython().run_line_magic('timeit', '-o -r1 n.one_d_range_query(l, h)')
            bres.append(a)
        res.append((b,bres))
    return res

def b_search_only(elements, *_):
    objs = (Task12.SortedRangeList(e) for e in elements)
    bounds = [random_bound1d() for _ in range(100)]
    res = []
    for i, n in enumerate(objs):
        bres  = []
        b = 10**(i+1)
        print(f'---{b}---')
        for l, h in bounds: 
#            print(l, h)
            a = get_ipython().run_line_magic('timeit', '-o -r1 n.get_range(l, h)')
            bres.append(a)
        res.append((b,bres))
    return res

def try_bounds(es):
    funcs = [naive_bench, # b_search_with_build, tree_search_with_build,
             build_range_tree, build_sorted_list, tree_search_only,
             b_search_only]
    return [(r.__name__, r(es)) for r in funcs if not print(r.__name__)]


if __name__ == '__main__':
    
    log10 = [random.randrange(1, 1000, 1) for n in range(10)]
    log100 = [random.randrange(1, 1000, 1) for n in range(100)]
    log1_000 = [random.randrange(1, 1000, 1) for n in range(1_000)]
    log10_000 = [random.randrange(1, 1000, 1) for n in range(10_000)]
    log100_000 = [random.randrange(1, 1000, 1) for n in range(100_000)]
    log1_000_000 = [random.randrange(1, 1000, 1) for n in range(1_000_000)]
    n_sizes = [log10, log100, log1_000, log10_000, log100_000, log1_000_000] 

    dis_new = try_bounds(n_sizes)

    pickle.dump(dis_new, open("1d.p", "wb"))

