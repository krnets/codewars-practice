# 6kyu - Find the missing letter

""" Write a method that takes an array of consecutive (increasing) letters as input and 
that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"

(Use the English alphabet with 26 letters!) """


# def find_missing_letter(chars):
#     seq = list(map(ord, chars))
#     return chr([x for x in range(min(seq), max(seq)) if x not in seq].pop())

# def find_missing_letter(chars):
#     for i in range(len(chars)-1):
#         if ord(chars[i+1])-1-ord(chars[i]) != 0:
#             return chr(ord(chars[i])+1)

# def find_missing_letter(chars):
#     for i in range(1, len(chars)):
#         if ord(chars[i]) - ord(chars[i-1]) != 1:
#             return chr(ord(chars[i])-1)

def find_missing_letter(chars):
    return set(map(chr, range(ord(chars[0]), ord(chars[-1]) + 1))).difference(set(chars)).pop()


q = find_missing_letter(['a', 'b', 'c', 'd', 'f'])  # 'e'
q
q = find_missing_letter(['O', 'Q', 'R', 'S'])  # 'P'
q
