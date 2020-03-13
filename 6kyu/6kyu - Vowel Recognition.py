# 6kyu - Vowel Recognition

""" {a, e, i, o, u, A, E, I, O, U}

Natural Language Understanding is the subdomain of Natural Language Processing where people 
used to design AI based applications have ability to understand the human languages. 
HashInclude Speech Processing team has a project named Virtual Assistant. 
For this project they appointed you as a data engineer (who has good knowledge of creating 
clean datasets by writing efficient code). As a data engineer your first task is to make vowel recognition dataset. 
In this task you have to find the presence of vowels in all possible substrings of the given string. 
For each given string you have to return the total number of vowels.

Given a string "baceb" you can split it into substrings: b, ba, bac, bace, baceb, a, ac, ace, aceb, c, ce, ceb, e, eb, b. 
The number of vowels in each of these substrings:        0, 1, 1, 2, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 0; 
if you sum up these number, you get 16 - the expected output.

Note: your solution should have linear time complexity. """

# import re

# def vowel_recognition(s):
#     vowel = re.compile('[aeiou]', re.IGNORECASE)
#     n = len(s)
#     arr = []
#     sum = 0
#     for i in range(n):
#         if (i == 0):
#             arr.append(n)
#         else:
#             arr.append((n - i) + arr[i - 1] - i)
#     for i in range(n):
#         if vowel.match(s[i]):
#             sum += arr[i]
#     return sum

# def vowel_recognition(s):
#     vowels = set('aeiouAEIOU')
#     total = acc = 0
#     for i, c in enumerate(s, 1):
#         if c in vowels:
#             acc += i
#         total += acc
#     return total

def vowel_recognition(s):
    return sum((len(s) - i) * (i + 1) for i, c in enumerate(s) if c in 'aeiouAEIOU')


q = vowel_recognition("bbbb")  # 0
q
q = vowel_recognition("baceb")  # 16
q
q = vowel_recognition("aeiou")  # 35
q
q = vowel_recognition("aeiouAEIOU")  # 220
q
