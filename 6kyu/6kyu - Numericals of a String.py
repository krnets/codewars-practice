# 6kyu - Numericals of a String

""" You are given an input string.

For each symbol in the string if it's the first character occurrence, 
replace it with a '1', else replace it with the amount of times you've already seen it.

But will your code be performant enough?

input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"

There might be some non-ascii characters in the string. """


# def numericals(s):
#     freq = {}
#     res = ''
#     for x in s:
#         if x in freq:
#             freq[x] += 1
#             res += str(freq[x])
#         else:
#             freq[x] = 1
#             res += str(freq[x])
#     return res

def numericals(s):
    freq = {}
    res = ''
    for x in s:
        freq[x] = freq.get(x, 0) + 1
        res += str(freq[x])
    return res


q = numericals("Hello, World!")  # "1112111121311"
q
# "11121111213112111131224132411122"
q = numericals("Hello, World! It's me, JomoPipi!")
q
q = numericals("hello hello")  # "11121122342"
q
q = numericals("Hello")  # "11121"
q
q = numericals("aaaaaaaaaaaa")  # "123456789101112"
q
