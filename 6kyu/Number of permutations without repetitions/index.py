""" 6kyu - Number of permutations without repetitions

Write a function that takes a number or a string and gives back the number of permutations 
without repetitions that can generated using all of its element.; more on permutations here.

For example, starting with:

1
45
115
"abc"

You could respectively generate:

1
45,54
115,151,511
"abc","acb","bac","bca","cab","cba"

So you should have, in turn:

perms(1)==1
perms(45)==2
perms(115)==3
perms("abc")==6 """

from collections import Counter
from functools import reduce
from math import factorial
from operator import mul

# from itertools import permutations

# def perms(element):
#     return len(set(permutations(str(element))))

# def perms(element):
#     s = str(element)
#     n = len(s)
#     uniq_repeated = [factorial(s.count(c)) for c in set(s)]
#     return factorial(n) // reduce(mul, uniq_repeated)


def perms(element):
    s = str(element)
    n = len(s)
    uniq_fct = map(factorial, Counter(s).values())
    return factorial(n) // reduce(mul, uniq_fct)


q = perms(2), 1
q
q = perms(25), 2
q
q = perms(342), 6
q
q = perms(1397), 24
q
q = perms(76853), 120
q
q = perms("a"), 1
q
q = perms("ab"), 2
q
q = perms("abc"), 6
q
q = perms(737), 3
q
q = perms(66666), 1
q
