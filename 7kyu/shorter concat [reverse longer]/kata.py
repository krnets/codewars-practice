# 7kyu - shorter concat [reverse longer]

""" Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.

In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

Strings a and b may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).
If a and b have the same length treat a as the longer producing b+reverse(a)+b """


# def shorter_reverse_longer(a, b):
#     return a + b[::-1] + a if len(a) < len(b) else b + a[::-1] + b


def shorter_reverse_longer(a, b):
    if len(a) < len(b):
        a, b = b, a
    return b + a[::-1] + b


q = shorter_reverse_longer("first", "abcde")  # "abcdetsrifabcde"
q
q = shorter_reverse_longer("hello", "bau")  # "bauollehbau"
q
q = shorter_reverse_longer("abcde", "fghi")  # "fghiedcbafghi"
q
