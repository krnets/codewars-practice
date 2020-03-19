# 7kyu - Spot the Differences

""" Mary brought home a "spot the differences" book. 
The book is full of a bunch of problems, and each problem consists of two strings that are similar. 
However, in each string there are a few characters that are different. 
An example puzzle from her book is:

String 1: "abcdefg"
String 2: "abcqetg"

Notice how the "d" from String 1 has become a "q" in String 2, and "f" from String 1 has become a "t" in String 2.

It's your job to help Mary solve the puzzles. 
Write a program spot_diff that will compare the two strings and return a list with the positions where the two strings differ. 
In the example above, your program should return [3, 5] because String 1 is different from String 2 at positions 3 and 5.

• If both strings are the same, return []
• Both strings will always be the same length
• Capitalization and punctuation matter """


# def spot_diff(s1, s2):
#     res = []
#     for i in range(len(s1)):
#         if s1[i] is not s2[i]:
#             res.append(i)
#     return res

def spot_diff(s1, s2):
    return [i for i in range(len(s1)) if s1[i] is not s2[i]]


q = spot_diff('abcdefg', 'abcqetg')  # [3, 5], 'Whoops!'
q
q = spot_diff('Hello World!', 'hello world.')
q
#      [0, 6, 11], 'Capitalization and punctuation matter!'
q = spot_diff('FixedGrey', 'FixedGrey')
q
#      [], 'Should return [] if the strings are the same!'
