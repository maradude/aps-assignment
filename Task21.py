from dataclasses import dataclass  # requires Python 3.7
import typing
from math import ceil


class RangeTree:

    def __init__(self, values):
        self.values = sorted(values)
        self.root = _Node(self.values[ceil/len(values)/2])
        self.root.left = _build(self.values[:ceil(/2)])


    @dataclass
    class _Node:
        value: int
        left: 'typing.Any' = None
        right: 'typing.Any' = None

    def _build(self, values):
        n = len(values)
        if n == 0:
            return self([])
        mid_point = ceil(n/2)
        mid_value = values[mid_point]
        left_tree = values[:mid_point]
        right_tree = values[mid_point+1:]
        new_node = RangeTree._Node(mid_value)
        new_node.left = RangeTree._build(left_tree)
        new_node.right = RangeTree._build(right_tree)


def get_root(tree):
    return tree.root


def is_leaf(node):
    return node.left is None or node.right is None


def find_split_node(tree, lbound, ubound):
    node = get_root(tree)
    splitting_value = node
    while not is_leaf(node) and (ubound <= splitting_value or
                                 lbound > splitting_value):
        if ubound <= splitting_value:
            node = node.left
        else:
            node = node.right
        splitting_value = node
    return node


def one_d_range_query(tree, lbound, ubound):
    reported_nodes = []
    split_node = find_split_node(tree, lbound, ubound)
    if split_node.leaf:
        # check if point stored a node_split needs to be reported
        # report it
        return
    node = split_node.left  # repeat start
    while not node.leaf:
        if lbound <= node:
            pass  # add right subtree of node to report
            node = node.left
        else:
            node = node.right
    # check if node should be reported
    # goto node = split_node.left to do same for right
    # subtree of split_node, going to ubound and reporting
    # subtrees to the left of the path
    return reported_nodes


if __name__ == '__main__':
    # should be O(log n)
    from sanitize_input import get_input
    test_object = get_input()

    # nlist = SortedArray(*test_object.elements)
    # for lower, upper in test_object.ranges:
    # print(' '.join(map(str, nlist.get_range(lower, upper))))
