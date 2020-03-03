# 8kyu - Double Char

""" Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "       """


# def double_char(s):
#     return ''.join([x + x for x in list(s)])

def double_char(s):
    return ''.join(c * 2 for c in s)


q = double_char("String")  # "SSttrriinngg"
q
q = double_char("Hello World")  # "HHeelllloo  WWoorrlldd"
q
q = double_char("1234!_ ")  # "11223344!!__  "
q
