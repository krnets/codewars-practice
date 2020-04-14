# 7kyu - Jenny the youngest detective

""" Jenny is 9 years old. She is the youngest detective in North America. 
Jenny is a 3rd grader student, so when a new mission comes up, she gets a code to decipher 
in a form of a sticker (with numbers) in her math notebook and a comment (a sentence) in her writing notebook. 
All she needs to do is to figure out one word, from there she already knows what to do. 
And here comes your role - you can help Jenny find out what the word is!

In order to find out what the word is, you should use the sticker (array of 3 numbers) 
to retrive 3 letters from the comment (string) that create the word.

    Each of the numbers in the array refers to the position of a letter in the string, in increasing order.
    Spaces are not places, you need the actual letters. No spaces.
    The returned word should be all lowercase letters.
    if you can't find one of the letters using the index numbers, return "No mission today". 

Example: input: [5, 0, 3], "I Love You" output: "ivy" (0 = "i", 3 = "v", 5 = "y") """

# def missing(nums, str):
#     res = ''
#     s = ''.join(str.lower().split())
#     for i in sorted(nums):
#         try:
#             res += s[i]
#         except:
#             return 'No mission today'
#     return res


# def missing(nums, str):
#     res = ''
#     str = str.replace(' ', '')
#     for i in sorted(nums):
#         try:
#             res += str[i]
#         except:
#             return 'No mission today'
#     return res

# def missing(nums, s):
#     s = s.lower().replace(' ', '')
#     return 'No mission today' if any(i >= len(s) for i in nums) else ''.join(s[i] for i in sorted(nums))

# def missing(nums, s):
#     s = s.lower().replace(' ', '')
#     return 'No mission today' if max(nums) > len(s) else ''.join(s[i] for i in sorted(nums))

def missing(nums, s):
    s = s.lower().replace(' ', '')
    return ''.join(s[i] for i in sorted(nums)) if max(nums) < len(s) else 'No mission today'


q = missing([5, 0, 3], "I love you")  # "ivy"
q
q = missing([29, 31, 8], "The quick brown fox jumps over the lazy dog")  # "bay"
q
q = missing([12, 4, 6], "Good Morning")  # "No mission today"
q
