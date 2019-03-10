"""
Algorithm 5 Algorithm for ﬁnding the intersection.
Require: minMax1,minMax2 a list with d pairs (where d is the dimension of the space).
Each pair has the minimum and maximum values for that dimension for the region.
1: function intersect(minMax1, minMax2)
2:   for all d in the number of dimensions do
3:       if not ( minMax2[d][0] ≤ minMax1[d][0] ≤ minMax2[d][1] or
                  minMax2[d][0] ≤ minMax1[d][1] ≤ minMax2[d][1] or
                  minMax1[d][0] ≤ minMax2[d][0] ≤ minMax1[d][1] or
                  minMax1[d][0] ≤ minMax2[d][1] ≤ minMax1[d][1] ) then
4:          return false
5:       end if
6:   end for
7:   return true
8: end function
"""
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
