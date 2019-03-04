"""
Require: A tree T, an interval [x s , x f ]
function FindSplitNode(T, x s , x f )
    v ← root(T)
    x v ← value stored in v
    while v is not a leaf and ( x f ≤ x v or x s > x v ) do
        if x f ≤ x v then
            v ← left child of v
        else
            v ← right child of v
        end if
        x v ← value stored in v
    end while
    return v
end function
"""


def find_split_node(tree, lbound, ubound):
    v = tree.root
    xv = v
    # while v.is_branch and
    pass


"""
Require: A tree T, an interval [x s , x f ]
function OneDRangeQuery(T, x s , x f )
    v split ← FindSplitNode(T, x s , x f )
    if v split is a leaf then
        check if the point stored at v split must be reported (and if so, report it).
        return
    end if
    v ← left child of v split . Follow the path to x s and report the points in subtrees right of the path
    while v is not a leaf do
        if x s ≤ value stored in node v then
            add the right subtree of v to the report
            v ← left subtree of v
        else
            v ← right subtree of v
        end if
    end while
    check if v should be reported
    Repeat lines 7-16 for the right subtree of v split , going to x f and reporting subtrees to the left of the path.
    return reported nodes
end function
"""


def one_d_range_query(tree, lbound, ubound):
    pass


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input()
    # nlist = SortedArray(*test_object.elements)
    # for lower, upper in test_object.ranges:
        # print(' '.join(map(str, nlist.get_range(lower, upper))))
