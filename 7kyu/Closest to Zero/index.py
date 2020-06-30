""" 7kyu - Closest to Zero

Simply find the closest value to zero from the list. 
Notice that there are negatives in the list.

List is always not empty and contains only integers. 
Return None if it is not possible to define only one of such values. 
And of course, we are expecting 0 as closest value to zero.

[2, 4, -1, -3]  => -1
[5, 2, -2]      => None
[5, 2, 2]       => 2
[13, 0, -6]     => 0  """


def closest(lst):
    res = min(lst, key=abs)
    return None if res and -res in lst else res


q = closest([2, 4, -1, -3]), -1
q
q = closest([5, 2, -2]), None
q
q = closest([5, 2, 2]), 2
q
q = closest([13, 0, -6]), 0
q
