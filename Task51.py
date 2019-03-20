"""
Find all points in KD-tree between lower and upper bound
"""
from Task21 import RangeTree
from copy import deepcopy


def intersect(minMax1, minMax2):
    """

    :param minMax1: List[Sortable] row major indexed min and max region in k-dimensions
    :param minMax2: List[List[Sortable]] k lists each containing the lower and upper bound of that dimension
    :return: Bool True if regions overlap

    """
    # each dimensions lowest value, highest value
    for d in range(len(minMax2)):
        if not (minMax2[d][0] <= minMax1[val(0, d)] <= minMax2[d][1] or
                minMax2[d][0] <= minMax1[val(1, d)] <= minMax2[d][1] or
                minMax1[val(0, d)] <= minMax2[d][0] <= minMax1[val(1, d)] or
                minMax1[val(0, d)] <= minMax2[d][1] <= minMax1[val(1, d)]):
            return False
    return True


def is_point_in_range(point, region):
    """

    :param point: List[Sortable] k-dimensional point being evaluated
    :param region: List[List[Sortable]] query upper and lower bounds
    :return: Bool True if for each value in point it's dimensional
             counterparts in region contain the point inclusive
    """
    def check(d): return region[d][0] <= point[d] <= region[d][1]
    return all(map(check, range(len(region))))


def contained(super_set, sub_set):
    """

        :param super_set: List[List[Sortable]] query region of k lists each with that dimensions upper and lower bound
        :param sub_set: List[Sortable] row major indexed region with min and max for each dimensions known lower and upper bounds
        :return: Bool True if sub_set is a sub set of super_set

    """
    def check(d, region, point): return (
        region[d][0] <= point[val(0, d)] <= point[val(1, d)] <= region[d][1])
    return all(check(d, super_set, sub_set) for d in range(len(super_set)))


def get_all_values(array, node):
    """
        Perform DFS traversal to add all values of subtree to array
        :param array: List[List[Sortable]] array to be added nodes to
        :param node: _Node root of subtree
        :return: Void all values are added to array
    """
    RangeTree.get_tree_values(array, node)


def get_range(node, region):
    """
    wrapper for SearchKDTree to set initial parameters
    :param node: KDTree._Node root of tree to be searched
    :param region: List[List[Sortable]] k lists with lower and upper bound of each dimension
    :return: all values in given KDTree that fall between values of region inclusive

    bounds is a single list in row major instead of of a list of list due to
    improved performance of not needing to deepcopies for finding each nodes region
    """
    bounds = [float('-inf'), float('inf')]*len(region)
    return SearchKDTree(node, region, current_region=bounds, current_depth=0)


def val(bound, dimension):
    """
    Get row major index of search query
    :param bound: 0 or 1 is either lower or upper bound
    :param dimension: current dimension being evaluated

    """
    # row-major indexing
    return dimension*2 + bound


def new_region(value, region, dimension, bound):
    """
    create the split for a given internal node that shows potential values that decendants of the node can have
    :param value: Sortable value to be inserted in region
    :param region: List[Sortable] row major indexed lower and upper bounds for k dimensions
    :param dimension: int current dimension starts from 0
    :param bound: 0 or 1 to indicate if region being evaluated is for a right or left node

    """
    # funky indexing so I don't have to make deepcopies
    new_region = []
    new_region.extend(region)
    new_region[val(bound, dimension)] = value.data
    return new_region


def SearchKDTree(node, target_region, current_region, current_depth):
    """
    Recursive function to find values between given ranges
    :param node: KDTree._Node root of tree that will be searched
    :param target_region: List[List[Sortable]] k lists with the upper and lower bound of it's dimension
    :param current_region: List[Sortable] currently know bounds for this nodes decendants
    :param current_depth: int value to keep track of which dimension current root's value is
    :return: List[List[Sortable]] values in KDTree that are between bounds decared in target_region
    """
    reported_nodes = []

    # base case
    if node.is_leaf():
        if is_point_in_range(node.data, target_region):
            reported_nodes.append(node.data)
        return reported_nodes

    # recursive case
    axis = current_depth % len(target_region)

    # left child
    left_region = new_region(node, current_region, axis, 1)
    if contained(target_region, left_region):
        get_all_values(reported_nodes, node.left)

    elif intersect(left_region, target_region):
        reported_nodes.extend(SearchKDTree(
            node.left, target_region, left_region, current_depth+1))

    # right child
    right_region = new_region(node, current_region, axis, 0)
    if contained(target_region, right_region):
        get_all_values(reported_nodes, node.right)

    elif intersect(right_region, target_region):
        reported_nodes.extend(SearchKDTree(
            node.right, target_region, right_region, current_depth+1))

    return reported_nodes


def main():
    """
    Create a KD-Tree from the values given by test_object
    print results of get_range for each region given by test_object on a new line
    """
    from Task43 import KDTree
    # from print_binary_tree import printTree
    tree = KDTree(test_object.elements)
    # printTree(tree.root)
    for test in test_object.ranges:
        ranges_by_dimension = list(zip(test[0], test[1]))
        a = get_range(tree.root, ranges_by_dimension)
        b = [list(e) for e in (a)]
        print(str(b).replace(',', '')[1:-1])


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input('kd')
    main()
