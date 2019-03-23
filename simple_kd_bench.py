import Task31
import Task43
import Task51
import Task53
from sanitize_input import Tests
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import count
import pickle


def random_coords(n,d):
    return [[random.randrange(1, 1000, 1) for _ in range(d)] for _ in range(n)]


def create_test_ns(d):
    return [random_coords(10**i, d) for i in range(1,7)]


def random_boundkd(d):
    a = [random.randrange(1, 999, 1) for _ in range(d)]
    b = [random.randrange(i, 1000, 1) for i in a]
    return a,b


def bruteforce(n, *_, d=2, c=100):
    res = []
    bounds = [random_boundkd(d) for _ in range(c)]
    for e in n:
        bres = []
        b = len(e)
        print(f'---{b}---')
        for l, u in bounds:        
            a = get_ipython().run_line_magic('timeit', '-o -r1 list(Task31.simple_range_query(e, l, u))')
            bres.append(a)
        res.append((b,bres))
    return res


def build_kd_tree(n, *_, d=2, c=100):
    res = []
    for e in n:
        bres = []
        b = len(e)
        print(f'---{b}---')
        for i in (random_coords(b, d) for _ in range(c)):
            a = get_ipython().run_line_magic('timeit', '-o -r1 Task43.KDTree(i)')
            bres.append(a)
        res.append((b,bres))
    return res


def kd_tree_without_contained(e, *_, d=2, c=100):
    res = []
    bounds = [random_boundkd(d) for _ in range(c)]
    for n in e: 
        d = len(n)
        a = Task43.KDTree(n).root
        bres = []
        print(f'---{d}---')
        for l, u in bounds:
            b = list(zip(l, u))
            c = get_ipython().run_line_magic('timeit', '-o -r1 Task53.get_range(a, b)')
            bres.append(c)
        res.append((d, bres))
    return res


def kd_tree_with_contained(e, *_, d=2, c=100):
    res = []
    bounds = [random_boundkd(d) for _ in range(c)]
    for n in e:
        bres = []
        d = len(n)
        a = Task43.KDTree(n).root
        print(f'---{d}---')
        for l, u in bounds:
            b = list(zip(l, u))
            c = get_ipython().run_line_magic('timeit', '-o -r1 Task51.get_range(a, b)')
            bres.append(c)
        res.append((d, c))
    return res


def try_bounds2():
    res = []
    funcs = [bruteforce, build_kd_tree, kd_tree_without_contained, kd_tree_with_contained]
    ds= [2,3,5,10,50]
    es = (random_coords(100_000, d) for d in ds)
    for d, e in zip(ds, es):
        print(d,len(e))
        bres = []
        print(d)
        for f in funcs:
            print(f.__name__)
            bres.append((f.__name__, f([e], d=d)))
        res.append(bres)
    return res


def try_bounds(es, d=2):
    funcs = [bruteforce, build_kd_tree, kd_tree_without_contained, kd_tree_with_contained]
    return [(f.__name__, f(create_test_ns(2), d=d)) for f in funcs if not print(f.__name__)]


if __name__ == '__main__':

	var_ele = try_bounds(create_test_ns(2))
	pickle.dump( var_ele, open( "variable_elements.p", "wb" ) )
	var_dim = try_bounds2()
	pickle.dump( var_dim, open( "variable_dimensions.p", "wb"))





