# 7kyu - Tail Swap

""" You'll be given a list of two strings, and each will contain exactly one colon (":") 
in the middle (but not at beginning or end). 
The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), 
but with the characters after each colon swapped.

["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"] """

# def tail_swap(strings):
#     a, b = [x.split(':') for x in strings]
#     a1, a2 = a
#     b1, b2 = b
#     return [':'.join([a1, b2]), ':'.join([b1, a2])]

# def tail_swap(strings):
#     (a, b), (c, d) = [x.split(':') for x in strings]
#     return [':'.join([a, d]), ':'.join([c, b])]


def tail_swap(strings):
    (a, b), (c, d) = [s.split(':') for s in strings]
    return list(map(':'.join, ((a, d), (c, b))))


q = tail_swap(['abc:123', 'cde:456'])
q
#      ['abc:456', 'cde:123'])

q = tail_swap(['a:12345', '777:xyz'])
q
#      ['a:xyz', '777:12345'])
