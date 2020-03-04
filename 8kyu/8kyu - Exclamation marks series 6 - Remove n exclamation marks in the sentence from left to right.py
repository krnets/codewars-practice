# 8kyu - Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right

""" Remove n exclamation marks in the sentence from left to right. n is positive integer. """


# def remove(s, n):
#     while (n > 0):
#         s = s.replace('!', '', 1)
#         n -= 1
#     return s

def remove(s, n):
    return s.replace('!', '', n)


q = remove("Hi!", 1)  # "Hi"
q
q = remove("Hi!", 100)  # "Hi"
q
q = remove("Hi!!!", 1)  # "Hi!!"
q
q = remove("Hi!!!", 100)  # "Hi"
q
q = remove("!Hi", 1)  # "Hi"
q
q = remove("!Hi!", 1)  # "Hi!"
q
q = remove("!Hi!", 100)  # "Hi"
q
q = remove("!!!Hi !!hi!!! !hi", 1)  # "!!Hi !!hi!!! !hi"
q
q = remove("!!!Hi !!hi!!! !hi", 3)  # "Hi !!hi!!! !hi"
q
q = remove("!!!Hi !!hi!!! !hi", 5)  # "Hi hi!!! !hi"
q
q = remove("!!!Hi !!hi!!! !hi", 100)  # "Hi hi hi"
q
