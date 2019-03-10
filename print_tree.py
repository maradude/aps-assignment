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
    print2DUtil(root.right, space)
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)
    # Process left child
    print2DUtil(root.left, space)


def print2D(root):
    # Wrapper over print2DUtil()
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
