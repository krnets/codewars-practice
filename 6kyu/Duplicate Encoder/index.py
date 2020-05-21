# 6kyu - Duplicate Encoder

""" The goal of this exercise is to convert a string to a new string where each character in the new string is 
"(" if that character appears only once in the original string, 
or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

Assertion messages may be unclear about what they display in some languages. 
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input! """


# def duplicate_encode(word):
#     res = []
#     dup = []
#     word = word.lower()
#     [dup.append(v) for v in word if word.index(v) is not word.rindex(v)]
#     [res.append(')') if v in dup else res.append('(') for v in word]
#     return ''.join(res)

# def duplicate_encode(word):
#     table = {}
#     for c in word.lower():
#         table[c] = ')' if c in table else '('
#     return word.lower().translate(str.maketrans(table))

from collections import Counter

def duplicate_encode(word):
    freq = Counter(word.lower())
    return ''.join('(' if freq[x] == 1 else ')' for x in word.lower())


q = duplicate_encode("din")  # "((("
q
q = duplicate_encode("recede")  # "()()()"
q
q = duplicate_encode("Success")  # ")())())"
q
q = duplicate_encode("(( @")  # "))(("
q
