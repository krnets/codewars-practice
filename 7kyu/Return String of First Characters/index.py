# 7kyu - Return String of First Characters

""" In this exercise, a string is passed to a method and a new string has to be returned with the 
first character of each word in the string.

For example:

"This Is A Test" ==> "TIAT" """


# def make_string(s):
#     return ''.join(word[0] for word in s.split())

from operator import itemgetter

def make_string(s):
    return ''.join(map(itemgetter(0), s.split()))


q = make_string("sees eyes xray yoat")
q
#     "sexy"
q = make_string("brown eyes are nice")
q
#     "bean"
q = make_string("cars are very nice")
q
#     "cavn"
q = make_string("kaks de gan has a big head")
q
#     "kdghabh"
