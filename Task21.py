from dataclasses import dataclass  # requires Python 3.7
from math import ceil


class RangeTree:
    # TODO: should probably combine _Node and RangeTree

    def __init__(self, *values):
        self.root = RangeTree.build(sorted(values))

    @dataclass()
    class _Node:
        data: int
        left: '_Node' = None
        right: '_Node' = None

        def is_leaf(self):
            return self.left is None or self.right is None

    @staticmethod
    def build(arr):
        """
        This function based on the following paper
        @inproceedings{lueker1978data,
            title={A data structure for orthogonal range queries},
            author={Lueker, George S},
            booktitle={19th Annual Symposium on Foundations of Computer Science (sfcs 1978)},
            pages={28--34},
            year={1978},
            organization={IEEE}
        }
        """
        length = len(arr)
        if length < 3:
            root = RangeTree._Node(arr[0])
            if length == 2:
                root.left = RangeTree._Node(arr[0])
                root.right = RangeTree._Node(arr[-1])
            return root
        midp = ceil(length / 2) - 1
        left = arr[:midp+1]
        right = arr[midp+1:]
        root = RangeTree._Node(left[-1])
        root.left = RangeTree.build(left)
        root.right = RangeTree.build(right)
        return root

    def find_split_node(self, lbound, ubound):
        node = self.root
        splitting_value = int(node.data)
        while not node.is_leaf() and (ubound <= splitting_value or
                                      lbound > splitting_value):
            if ubound <= splitting_value:
                node = node.left
            else:
                node = node.right
            splitting_value = node.data
        return node

    def one_d_range_query(self, lbound, ubound):
        reported_nodes = []
        split_node = self.find_split_node(lbound, ubound)
        if split_node.is_leaf():
            if lbound <= split_node.data <= ubound:
                reported_nodes.append(split_node.data)
                return reported_nodes
        node = split_node.left
        while not node.is_leaf():
            if lbound <= node.data:
                reported_nodes.extend(RangeTree.get_tree_values(node.right))
                node = node.left
            else:
                node = node.right
        if node.data >= lbound:
            reported_nodes.append(node.data)
        node = split_node.right
        while not node.is_leaf():
            if ubound >= node.data:
                reported_nodes.extend(RangeTree.get_tree_values(node.left))
                node = node.right
            else:
                node = node.left
        if node.data <= ubound:
            reported_nodes.append(node.data)
        return reported_nodes

    @staticmethod
    def get_tree_values(root):
        # modified version of https://code.activestate.com/recipes/579138-simple-breadth-first-depth-first-tree-traversal/
        nodes = []
        stack = [root]
        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            if cur_node.is_leaf():
                nodes.append(cur_node.data)
            if cur_node.right is not None:
                stack.append(cur_node.right)
            if cur_node.left is not None:
                stack.append(cur_node.left)
        return nodes


def main():
    from sanitize_input import get_input
    test_object = get_input()
    rangeTree = RangeTree(*test_object.elements)
    for lower, upper in test_object.ranges:
        print(' '.join(map(str, rangeTree.one_d_range_query(lower, upper))))


if __name__ == '__main__':
    main()
