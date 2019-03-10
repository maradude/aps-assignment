from Task21 import RangeTree


def intersect(minMax1, minMax2):
    # list of dimensional sized pairs
    for d in range(len(minMax1)):
        if not (minMax2[d][0] <= minMax1[d][0] <= minMax2[d][1] or
                minMax2[d][0] <= minMax1[d][1] <= minMax2[d][1] or
                minMax1[d][0] <= minMax2[d][0] <= minMax1[d][1] or
                minMax1[d][0] <= minMax2[d][1] <= minMax1[d][1]):
                    return False
    return True


"""
Algorithm 4 Searching a KD-tree
Require: v a (root) node of the KD tree;
R the range or region for which points must be reported.
1: function SearchKDTree(v, R)
2:   if v is a leaf then
3:     check if point stored in v lies in R, and return it if so.
4:   end if
5:   if the region of the left child of v is fully contained in R then
6:     report the subtree of the left child of v
7:   else if the region of the left child of v intersects R then
8:     SearchKDTree(left child of v,R)
9:    end if
10:   if the region of the right child of v is fully contained in R then
11:     report the subtree of the right child of v
12:   else if the region of the right child of v intersects R then
13:     SearchKDTree(right child of v,R)
14:   end if
15: end function
"""


def is_point_in_range(point, range):
    pass


def tree_in_range(node, range):
    pass


def get_all_values(node):
    return RangeTree.get_tree_values(node)


def SearchKDTree(node, region):
    # TODO: swap extends with appends and then flatMap on return
    reported_nodes = []
    if node.is_leaf():
        if is_point_in_range(node.value, region):
            reported_nodes.append(node.value)
    if tree_in_range(node.left, region):
        reported_nodes.extend(get_all_values(node.left))
    elif intersect([], []):
        reported_nodes.extend(SearchKDTree(node.left, region))
    if tree_in_range(node.right, region):
        reported_nodes.extend(get_all_values(node.right))
    elif intersect([], []):
        reported_nodes.extend(SearchKDTree(node.right, region))
    return reported_nodes

