# 6kyu - String subpattern recognition III

""" Similar to the previous kata, but this time you need to operate with shuffled strings 
to identify if they are composed repeating a subpattern

Since there is no deterministic way to tell which pattern was really the original one among 
all the possible permutations of a fitting subpattern, return a subpattern with sorted characters, 
otherwise return the base string with sorted characters (you might consider this case as an edge case, 
with the subpattern being repeated only once and thus equalling the original input string).

has_subpattern("a") == "a"; #no repeated pattern, just one character
has_subpattern("aaaa") == "a" #just one character repeated
has_subpattern("abcd") == "abcd" #base pattern equals the string itself, no repetitions
has_subpattern("babababababababa") == "ab" #remember to return the base string sorted"
has_subpattern("bbabbaaabbaaaabb") == "ab" #same as above, just shuffled """

from collections import Counter
from functools import reduce
from fractions import gcd

def has_subpattern(s):
    c = Counter(s)
    m = reduce(gcd, c.values())
    return ''.join(sorted(k*(v//m) for k, v in c.items()))


q = has_subpattern("a")  # "a"
q
q = has_subpattern("aaaa")  # "a"
q
q = has_subpattern("abcd")  # "abcd"
q
q = has_subpattern("babababababababa")  # "ab"
q
q = has_subpattern("bbabbaaabbaaaabb")  # "ab"
q
q = has_subpattern("123a123a123a")  # "123a"
q
q = has_subpattern("123A123a123a")  # "111222333Aaa"
q
q = has_subpattern("12aa13a21233")  # "123a"
q
q = has_subpattern("12aa13a21233A")  # "111222333Aaaa"
q
q = has_subpattern("abcdabcaccd")  # "aaabbccccdd"
q
