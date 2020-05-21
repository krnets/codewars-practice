# 8kyu - Character Frequency

""" In this kata, you will get a message and you will need to get the frequency of each and every character!
Explanation

Your function will be called char_freq and you will get passed a string, you will then return a dictionary 
with as keys the characters, and as values how many times that character is in the string. 
You can assume you will be given valid input.
Example

char_freq("I like cats") // Returns {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1} """


# def char_freq(message):
#     freq = {}
#     for x in message:
#         freq[x] = message.count(x)
#     return freq

# def char_freq(message):
#     freq = {}
#     for x in message:
#         if x in freq:
#             freq[x] += 1
#         else:
#             freq[x] = 1
#     return freq

# from collections import Counter

# def char_freq(message):
#     return Counter(message)

from collections import Counter as char_freq

# {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1})
q = char_freq("I like cats")
q
