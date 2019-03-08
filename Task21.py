from dataclasses import dataclass, field  # requires Python 3.7
from math import ceil


class RangeTree:

    def __init__(self, *values):
        self.root = RangeTree.build(sorted(values))

    @dataclass(order=True)
    class _Node:
        data: int = field(compare=True)
        left: 'typing.Any' = field(default=None, compare=False)
        right: 'typing.Any' = field(default=None, compare=False)

    # def __eq__(self, order)

    @staticmethod
    def build(arr):
        length = len(arr)
        if length < 3:
            root = RangeTree._Node(arr[0])
            if length == 2:
                root.left = RangeTree._Node(arr[0])
                root.right = RangeTree._Node(arr[-1])
            return root
        midp = ceil(length/2) - 1
        left = arr[:midp+1]
        right = arr[midp+1:]
        root = RangeTree._Node(left[-1])
        root.left = RangeTree.build(left)
        root.right = RangeTree.build(right)
        return root

    @staticmethod
    def print2DUtil(root, space):
        # debugging tree print stolen from
        # https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
        COUNT = [2]
        # Base case
        if (root is None):
            return
        # Increase distance between levels
        space += COUNT[0]
        # Process right child first
        RangeTree.print2DUtil(root.right, space)
        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root.data)
        # Process left child
        RangeTree.print2DUtil(root.left, space)

    @staticmethod
    def print2D(root):
        # Wrapper over print2DUtil()
        # space=[0]
        # Pass initial space count as 0
        RangeTree.print2DUtil(root, 0)


"""
        def breadth_first_traversal(self, root=None):
            #In BFS the Node Values at each level of the Tree
             #are traversed before going to next level
            root = self.root if root is None else root
            to_visit = [root]
            while to_visit:
                current = to_visit.pop(0)
                print(current.value)
                if current.left:
                    to_visit.append(current.left)
                if current.right:
                    to_visit.append(current.right)

"""
# def print_tree(self):


def get_root(tree):
    return tree.root


def is_leaf(node):
    return node.left is None or node.right is None


def find_split_node(tree, lbound, ubound):
    node = get_root(tree)
    splitting_value = int(node.data)
    while not is_leaf(node) and (ubound <= splitting_value or
                                 lbound > splitting_value):
        if ubound <= splitting_value:
            node = node.left
        else:
            node = node.right
        splitting_value = node.data
    return node


def get_tree_values(root):
    # modified version of https://code.activestate.com/recipes/579138-simple-breadth-first-depth-first-tree-traversal/
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        if is_leaf(cur_node):
            nodes.append(cur_node.data)
        if cur_node.right is not None:
            stack.append(cur_node.right)
        if cur_node.left is not None:
            stack.append(cur_node.left)
    return nodes


def one_d_range_query(tree, lbound, ubound):
    reported_nodes = []
    split_node = find_split_node(tree, lbound, ubound)
    if is_leaf(split_node):
        if lbound <= split_node.data <= ubound:
            reported_nodes.append(split_node.data)
            return reported_nodes
    node = split_node.left  # repeat start
    while not is_leaf(node):
        if lbound <= node.data:
            # reported_nodes.append(node.data)
            reported_nodes.extend(get_tree_values(node.right))
            node = node.left
        else:
            node = node.right
    if node.data >= lbound:
        reported_nodes.append(node.data)
    node = split_node.right
    while not is_leaf(node):
        if ubound >= node.data:
            reported_nodes.extend(get_tree_values(node.left))
            node = node.right
        else:
            node = node.left
    if node.data <= ubound:
        reported_nodes.append(node.data)
    # check if node should be reported
    # goto node = split_node.left to do same for right
    # subtree of split_node, going to ubound and reporting
    # subtrees to the left of the path
    return reported_nodes


if __name__ == '__main__':
    # should be O(log n)
    from sanitize_input import get_input
    test_object = get_input()
    # test = [3, 10, 19, 23, 30, 49, 57, 59, 62, 70, 80, 89, 100, 105]
    # test = [3, 19, 30, 49, 59, 70, 89, 100]
    a = RangeTree(test_object.elements)
    # RangeTree.print2D(find_split_node(a, 3, 19))
    # print(one_d_range_query(a, 0, 109))
    # print(test[4:-3])
    rangeTree = RangeTree(*test_object.elements)
    for lower, upper in test_object.ranges:
        print(' '.join(map(str, one_d_range_query(rangeTree, lower, upper))))

    # print(sorted(one_d_range_query(a, *test_object.ranges)))
    # nlist = SortedArray(*test_object.elements)
    # for lower, upper in test_object.ranges:
    # print(' '.join(map(str, nlist.get_range(lower, upper))))
