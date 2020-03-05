# 8kyu - Unicode Total

""" You'll be given a string, and have to return the total of all the unicode characters as an int. 
Should be able to handle any characters sent at it.

examples:

uniTotal("a") == 97 uniTotal("aaa") == 291 """


# def uni_total(string):
#     return sum([ord(x) for x in list(string)])

def uni_total(string):
    return sum(map(ord, string))


q = uni_total("a")  # 97
q
q = uni_total("b")  # 98
q
q = uni_total("c")  # 99
q
q = uni_total("")  # 0
q
q = uni_total("aaa")  # 291
q
q = uni_total("abc")  # 294
q
q = uni_total("Mary Had A Little Lamb")  # 1873
q
q = uni_total("Mary had a little lamb")  # 2001
q
q = uni_total("CodeWars rocks")  # 1370
q
q = uni_total("And so does Strive")  # 1661
q
