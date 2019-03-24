import Task43
import Task55
import random
import pickle


def random_coords(n, d):
    return [[random.randrange(1, 1000, 1) for _ in range(d)] for _ in range(n)]


def create_test_ns(d):
    return [random_coords(10**i, d) for i in range(1, 7)]


def random_boundkd(d):
    a = random_coords(1, d)[0]
    b = random.randrange(0, 500, 1)
    return a, b


random_boundkd(5)


def sphere_query(e, *_, d=2, c=100):
    res = []
    bounds = [random_boundkd(d) for _ in range(c)]
    for n in e:
        bres = []
        d = len(n)
        a = Task43.KDTree(n).root
        print(f'---{d}---')
        for b in bounds:
            c = get_ipython().run_line_magic('timeit', '-o -r1 Task55.sphere_query(a, b)')
            bres.append(c)
        res.append((d, bres))
    return res


def try_bounds2():
    res = []
    funcs = [sphere_query]
    ds = [2, 3, 5, 10, 50]
    es = (random_coords(100_000, d) for d in ds)
    for d, e in zip(ds, es):
        print(d, len(e))
        bres = []
        print(d)
        for f in funcs:
            print(f.__name__)
            bres.append((f.__name__, f([e], d=d)))
        res.append(bres)
    return res


def try_bounds(es, d=2):
    funcs = [sphere_query]
    return [(f.__name__, f(create_test_ns(2), d=d)) for f in funcs if not print(f.__name__)]


if __name__ == '__main__':
    var_ele = try_bounds(create_test_ns(2))
    print(var_ele)
    pickle.dump(var_ele, open("sphere_var_elements2.p", "wb"))
    var_dim = try_bounds2()
    print(var_ele)
    pickle.dump(var_dim, open("sphere_var_dimensions2.p", "wb"))
