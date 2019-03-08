from math import ceil

def build(L, D):
    # L = sorted_list
    # list of n keys, in ascending order according to component d.
    # The routine reutrns a d-fold BB(1/3) for the keys in L. Also, if d > 1,
    # L is resorted according to component d-1;
    n = len(L)
    if n == 0:
        return Tree()
    m = ceil(n/2)
    LL = L[:m]
    k = L[m]
    LR = L[m+1:]
    x = Tree.Node()
    x.value = k
    x.left = build(LL, d)
    x.right = build(LR, d)
    if d=1:
        AUX(x)
    else:
        #

