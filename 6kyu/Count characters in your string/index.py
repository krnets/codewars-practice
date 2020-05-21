# 6kyu - Count characters in your string

""" The main idea is to count all the occurring characters(UTF-8) in string. 
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { } """

from collections import Counter

def count(string):
    return Counter(string)

# from collections import Counter as count

q = count('aba') # {'a': 2, 'b': 1}
q
q = count('') # {}
q