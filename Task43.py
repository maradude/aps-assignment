"""
Algorithm 3 Building a KD tree.
Require: A set of points P, a current depth, d
  1: function BuildKDTree(P, d)
  2:    if P contains only one point then
  3:       return a leaf storing this point
  4:    end if
  5:    axis = d modulo the dimensionality of space
  6:    select a medianPoint from pointlist on dimension axis
  7:    P l = {p|p ∈ P and p ≤ medianPoint on dimension axis}
  8:    P r = {p|p ∈ P and p > medianPoint on dimension axis}
  9:    V l =BuildKDTree(P l , d + 1)
  10:   V r =BuildKDTree(P r , d + 1)
  11:   return a node with value medianPoint, left child V l , right child V r
  12: end function
"""


class Node:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def median():
    pass


def BuildKDTree(points, current_depth):
    if len(points) == 1:
        return  # should return the leaf
    axis = current_depth % 0  # should be the space dimensionality
    medianPoint = median(points[axis])  # a median pointin current dimension
    left_points = filter(lambda p: p[d] <= medianPoint, points)
    right_points = filter(lambda p: p[d] > medianPoint, points)
    left_child = BuildKDTree(left_points, current_depth + 1)
    right_child = BuildKDTree(right_points, current_depth + 1)
    return Node(medianPoint, left_child, right_child)
