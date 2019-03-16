# build square surrounding spehere, O(n) aditional cost


def point_in_sphere(test, point, radius):
    d = sum(abs(a - b) for a, b in zip(test, point))
    return d < radius


def spehere_to_square(point, radius):
    return [[p-radius, p+radius] for p in point]


def main():
    from Task51 import Util
    from Task43 import KDTree
#     from print_binary_tree import printTree
    tree = KDTree(test_object.elements)
    # printTree(tree.root)
    for test in test_object.ranges:
        ranges_by_dimension = spehere_to_square(*test)
        a = Util(tree.root, ranges_by_dimension)
        b = [list(e) for e in a if point_in_sphere(test[0], e, test[1])]
        print(str(b).replace(',', '')[1:-1])


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input('kd')
    main()
