"""
Create a balanced binary search tree from a sorted list of values.
Each internal node is given the value of the median index (rounded down) and are not
returned by range search are only used for guiding search.
Leaves contain actual values returned by range searches.
"""


from dataclasses import dataclass  # requires Python 3.7
from math import ceil


class RangeTree:
    """ """
    # TODO: should probably combine _Node and RangeTree

    def __init__(self, values):
        self.root = RangeTree.build(sorted(values))

    @dataclass()
    class _Node:
        """ """
        data: int
        left: '_Node' = None
        right: '_Node' = None

        def is_leaf(self):
            """
            maybe should be a parameter?
            """
            return self.left is None or self.right is None

    @staticmethod
    def build(arr):
        """This function based on the following paper
        @inproceedings{lueker1978data,
            title={A data structure for orthogonal range queries},
            author={Lueker, George S},
            booktitle={19th Annual Symposium on Foundations of Computer Science (sfcs 1978)},
            pages={28--34},
            year={1978},
            organization={IEEE}
        }

        :param arr: List[Sortable]
        :return: root node of newly created tree

        """
        length = len(arr)

        # base case
        if length < 3:
            root = RangeTree._Node(arr[0])
            if length == 2:
                root.left = RangeTree._Node(arr[0])
                root.right = RangeTree._Node(arr[-1])
            return root

        # recursive case
        midp = ceil(length / 2) - 1
        left = arr[:midp+1]
        right = arr[midp+1:]
        root = RangeTree._Node(left[-1])
        root.left = RangeTree.build(left)
        root.right = RangeTree.build(right)
        return root

    def find_split_node(self, lbound, ubound):
        """

        :param lbound: Sortable lower bound
        :param ubound: Sortable upper bound
        :return: _Node, smallest shared ancestor of of all range query results
        """
        node = self.root
        splitting_value = int(node.data)
        # check if largest common ancestor has been found
        while not node.is_leaf() and (ubound <= splitting_value or
                                      lbound > splitting_value):
            if ubound <= splitting_value:
                node = node.left
            else:
                node = node.right
            splitting_value = node.data
        return node

    def one_d_range_query(self, lbound, ubound):
        """

        :param lbound: Sortable lower bound
        :param ubound: Sortable upper bound
        :result: List[Sortable] all values in tree between lbound and ubound inclusive

        """
        reported_nodes = []
        # get largest common ancestor
        split_node = self.find_split_node(lbound, ubound)

        # return early if it doesn't have decendants
        if split_node.is_leaf():
            if lbound <= split_node.data <= ubound:
                reported_nodes.append(split_node.data)
            return reported_nodes

        # get relevant values from left child
        node = split_node.left
        while not node.is_leaf():
            if lbound <= node.data:
                RangeTree.get_tree_values(reported_nodes, node.right)
                node = node.left
            else:
                node = node.right
        if node.data >= lbound:
            reported_nodes.append(node.data)

        # get relevant values from right child
        node = split_node.right
        while not node.is_leaf():
            if ubound >= node.data:
                RangeTree.get_tree_values(reported_nodes, node.left)
                node = node.right
            else:
                node = node.left
        if node.data <= ubound:
            reported_nodes.append(node.data)

        return reported_nodes

    @staticmethod
    def get_tree_values(array, root):
        """
        Perform DFS traversal to get all leaf values from subtree
        :param array: List[Sortable], list to populate with values from subtree
        :param root: _Node to use as root of subtree
        :return: array with newly added values from subtree
        """
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node.is_leaf():
                array.append(cur_node.data)
            else:
                if cur_node.right is not None:
                    stack.append(cur_node.right)
                if cur_node.left is not None:
                    stack.append(cur_node.left)
        return array


def main():
    """
    perform range query for all ranges in test_object
    print each query result in a new line
    """
    rangeTree = RangeTree(test_object.elements)
    for lower, upper in test_object.ranges:
        print(' '.join(map(str, rangeTree.one_d_range_query(lower, upper))))


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input()
    main()
