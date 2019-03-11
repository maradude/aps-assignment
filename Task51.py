from Task21 import RangeTree


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


def intersect(minMax1, minMax2):
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


def min_max(node):
    # something like (-float(inf), -float(inf),), float(inf), float(inf)
    # for the root and then smaller for each subsequent node
    pass


def vals():
    pass


def SearchKDTree(node, region):
    # TODO: swap extends with appends and then flatMap on return
    reported_nodes = []
    if node.is_leaf():
        if is_point_in_range(node.value, region):
            reported_nodes.append(node.value)
    if contained(vals(node).left, region):
        reported_nodes.extend(get_all_values(node.left))
    elif intersect(vals(node), region):
        reported_nodes.extend(SearchKDTree(node.left, region))
    if contained(vals(node.right), region):
        reported_nodes.extend(get_all_values(node.right))
    elif intersect([], region):
        reported_nodes.extend(SearchKDTree(node.right, region))
    return reported_nodes


def main():
    from sanitize_input import Tests, get_input
    from Task43 import KDTree
    from print_binary_tree import printTree
    test_object = get_input('kd')
    # test_object = Tests(elements=[(3, 2), (10, 4), (23, 6), (30, 10), (62, 8),
    #   (47, 14), (105, 9), (89, 7)],
    # ranges=[([7, 2], [47, 12]), ([3, 8], [12, 50])],
    # dimensions=2)
    tree = KDTree(test_object.elements)
    printTree(tree.root)
    for test in test_object.ranges:
        ranges_by_dimension = list(zip(test[0], test[1]))
        print(ranges_by_dimension)
        # SearchKDTree(tree.root, ranges_by_dimension)


if __name__ == '__main__':
    main()
