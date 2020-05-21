# 7kyu - letters only, please!

""" Let's assume we need "clean" strings. Clean means a string should only contain letters a-z, A-Z and spaces. 
We assume that there are no double spaces or line breaks.

Write a function that takes a string and returns a string without the unnecessary characters.

remove_chars('.tree1')    ==> 'tree'
remove_chars("that's a pie$ce o_f p#ie!")  ==> 'thats a piece of pie'
remove_chars('john.dope@dopington.com')    ==> 'johndopedopingtoncom'
remove_chars('my_list = ["a","b","c"]')    ==> 'mylist  abc'
remove_chars('1 + 1 = 2')    ==> '    ' (string with 4 spaces)
remove_chars("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_")  ==> '' (empty string) """

import re

def remove_chars(s):
    return re.sub(r'[^a-z\sA-Z]', '', s)

# def remove_chars(s):
#     return re.sub(r'(?i)[^a-z\s]', '', s)

# def remove_chars(s):
#     return ''.join(c for c in s if c.isalpha() or c == ' ')


q = remove_chars("test for error!")  # "test for error"
q
q = remove_chars(".tree1")  # 'tree'
q
q = remove_chars('co_ol f0un%(c)t-io"n')  # 'cool function'
q
q = remove_chars("that's a pie&ce o_f p#ie!")  # 'thats a piece of pie'
q
