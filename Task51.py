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


def min_max(node):
    # something like (-float(inf), -float(inf),), float(inf), float(inf)
    # for the root and then smaller for each subsequent node
    pass


def vals():
    pass


def Util(node, region):
    bounds = [[0, float('inf')] for _ in range(len(region))]
    return SearchKDTree(node, region, current_region=bounds, current_depth=0)


def SearchKDTree(node, target_region, current_region, current_depth):
    # TODO: swap extends with appends and then flatMap on return
    # if node.data in [(10, 4), (23, 6), (30, 10)]:
        # print('wow')
    reported_nodes = []
    axis = current_depth % len(target_region)
    if node.is_leaf():
        if is_point_in_range(node.data, target_region):
            reported_nodes.append(node.data)
        return reported_nodes

    if node.left.is_leaf():
        left_region = current_region
    else:
        left_region = current_region.copy()
        left_region[axis][1] = node.data
    # if contained(left_region, target_region):
        # reported_nodes.extend(get_all_values(node.left))
    if intersect(left_region, target_region):
        reported_nodes.extend(SearchKDTree(
            node.left, target_region, left_region, current_depth+1))

    if node.right.is_leaf():
        right_region = current_region
    else:
        right_region = current_region.copy()
        right_region[axis][0] = node.data
    # if contained(right_region, target_region):
        # reported_nodes.extend(get_all_values(node.right))
    if intersect(right_region, target_region):
        reported_nodes.extend(SearchKDTree(
            node.right, target_region, right_region, current_depth+1))

    return reported_nodes


def main():
    from sanitize_input import get_input, Tests
    from Task43 import KDTree
    from print_binary_tree import printTree
    test_object = get_input('kd')
    # test_object = Tests(elements=[(3, 2), (10, 4), (23, 6), (30, 10), (62, 8),
    #   (47, 14), (105, 9), (89, 7)],
    # ranges=[([7, 2], [47, 12]), ([3, 8], [12, 50]), ([0, 0], [100, 100])],
    # dimensions=2)
    tree = KDTree(test_object.elements)
    printTree(tree.root)
    # expected (10,4), (23,6), (30,10)
    for test in test_object.ranges:
        ranges_by_dimension = list(zip(test[0], test[1]))
        print('query:', *ranges_by_dimension)
        a=Util(tree.root, ranges_by_dimension)
        print(a)


if __name__ == '__main__':
    main()
