# 7kyu - Reversing Fun

""" You are going to be given a string. Your job is to return that string in a certain order that I will explain below:

Let's say you start with this: 012345

The first thing you do is reverse it:543210
Then you will take the string from the 1st position and reverse it again:501234
Then you will take the string from the 2nd position and reverse it again:504321
Then you will take the string from the 3rd position and reverse it again:504123

Continue this pattern until you have done every single position, and then you will return the string you have created. 
For this particular number, you would return:504132

#Input: A string of length 1 - 1000

#Output: A correctly reordered string. """

# 012345
# 5 43210
# 50 1234
# 504 321
# 5041 23
# 50413 2
# 504132

def reverse_fun(s):
    res = ''
    for i in range(len(s)):
        res += s[-1]
        s = s[:-1]
        s = s[::-1]
    return res


# short but slow when str length is large
# def reverse_fun(s):
#     for i in range(len(s)):
#         s = s[:i] + s[i:][::-1]
#     return s


q = reverse_fun('012345')  # '504132'
q
q = reverse_fun('jointhedarkside')  # 'ejdoiisnktrhaed'
q
