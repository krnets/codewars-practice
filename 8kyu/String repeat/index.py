# 8kyu - String repeat

""" Write a function called repeatString which repeats the given String src exactly count times. """


def repeat_str(repeat, string):
    return string * repeat


q = repeat_str(6, "I")  # "IIIIII"
q
q = repeat_str(5, "Hello")  # "HelloHelloHelloHelloHello"
q
q = repeat_str(4, 'a')  # 'aaaa'
q
q = repeat_str(3, 'hello ')  # 'hello hello hello '
q
q = repeat_str(2, 'abc')  # 'abcabc'
q
