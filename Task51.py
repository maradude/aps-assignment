from Task21 import RangeTree
from copy import deepcopy


def intersect(minMax1, minMax2):
    # each dimensions lowest value, highest value
    for d in range(len(minMax1)):
        if not (minMax2[d][0] <= minMax1[d][0] <= minMax2[d][1] or
                minMax2[d][0] <= minMax1[d][1] <= minMax2[d][1] or
                minMax1[d][0] <= minMax2[d][0] <= minMax1[d][1] or
                minMax1[d][0] <= minMax2[d][1] <= minMax1[d][1]):
            return False
    return True


def is_point_in_range(point, region):
    def check(d): return region[d][0] <= point[d] <= region[d][1]
    return all(map(check, range(len(region))))


def contained(super_set, sub_set):
    def check(d, region, point): return (region[d][0] <= point[d][0]
                                         <= point[d][1] <= region[d][1])
    return all(check(d, super_set, sub_set) for d in range(len(sub_set)))


def get_all_values(node):
    return RangeTree.get_tree_values(node)


def Util(node, region):
    bounds = [[float('-inf'), float('inf')] for _ in range(len(region))]
    return SearchKDTree(node, region, current_region=bounds, current_depth=0)


def new_region(node, region, dimension, bound):
    region[dimension][bound] = node.data
    return region


def SearchKDTree(node, target_region, current_region, current_depth):
    # TODO: swap extends with appends and then flatMap on return
    # if node.data in [(10, 4), (23, 6), (30, 10)]:
    # TODO: replace hardcopy() with something more efficient
    reported_nodes = []
    axis = current_depth % len(target_region)

    if node.is_leaf():
        if is_point_in_range(node.data, target_region):
            reported_nodes.append(node.data)
        return reported_nodes

    left_region = new_region(node, deepcopy(current_region), axis, 1)
    if contained(target_region, left_region):
        reported_nodes.extend(get_all_values(node.left))

    elif intersect(left_region, target_region):
        reported_nodes.extend(SearchKDTree(
            node.left, target_region, left_region, current_depth+1))

    right_region = new_region(node, deepcopy(current_region), axis, 0)
    if contained(target_region, right_region):
        reported_nodes.extend(get_all_values(node.right))

    elif intersect(right_region, target_region):
        reported_nodes.extend(SearchKDTree(
            node.right, target_region, right_region, current_depth+1))

    return reported_nodes


def main():
    from Task43 import KDTree
    # from print_binary_tree import printTree
    tree = KDTree(test_object.elements)
    # printTree(tree.root)
    for test in test_object.ranges:
        ranges_by_dimension = list(zip(test[0], test[1]))
        a = Util(tree.root, ranges_by_dimension)
        b = [list(e) for e in (a)]
        print(str(b).replace(',', '')[1:-1])


if __name__ == '__main__':
    from sanitize_input import get_input, Tests
    test_object = get_input('kd')
    main()
