# 6kyu - More Zeros than Ones

""" Create a moreZeros function which will receive a string for input, and return an array containing only 
the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.

You should remove any duplicate characters, keeping the first occurence of any such duplicates, so they are 
in the same order in the final array as they first appeared in the input string.

Examples

'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False

        --> ['a','b','d']

'DIGEST'--> ['D','I','E','T']

All input will be valid strings of length > 0. Leading zeros in binary should not be counted. """

# def more_zeros(s):
#     res = []
#     dedup = list(dict.fromkeys(s))
#     for x in dedup:
#         b = bin(ord(x))[2:]
#         if b.count('0') > b.count('1'):
#             res.append(x)
#     return res


# def more_zeros(s):
#     res = []
#     for x in s:
#         b = bin(ord(x))[2:]
#         if b.count('0') > b.count('1') and x not in res:
#             res.append(x)
#     return res

def more_zeros(s):
    return list(dict.fromkeys(a for a, b in zip(s, map(bin, map(ord, s))) if len(b) < b.count('0') << 1))


q = more_zeros('abcde')
q
#      ['a', 'b', 'd']
q = more_zeros('thequickbrownfoxjumpsoverthelazydog')
q
#      ['h', 'b', 'p', 'a', 'd']
q = more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG')
q
#      ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D']
q = more_zeros(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_')
q
#      ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0']
q = more_zeros('DIGEST')
q
#      ['D', 'I', 'E', 'T']
