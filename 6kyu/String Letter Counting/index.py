# 6kyu - String Letter Counting

""" Take a string str and return a string that is made up of the number of occurances of 
each english letter in str, followed by that letter. The string shouldn't contain zeros; leave them out.

An empty string, or one with no letters, should return an empty string.

    Ignore all case
    str will never be null


"This is a test sentence."  =>  "1a1c4e1h2i2n4s4t"
""  =>  ""
"555"  =>  "" """

from collections import Counter

def string_letter_count(s):
    return ''.join(''.join([str(y), x]) for x, y in sorted(Counter(s.lower()).items()) if x.isalpha())



# "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z"
q = string_letter_count("The quick brown fox jumps over the lazy dog.")
q
# "2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y"
q = string_letter_count("The time you enjoy wasting is not wasted time.")
q
q = string_letter_count("./4592#{}()")  # ""
q
