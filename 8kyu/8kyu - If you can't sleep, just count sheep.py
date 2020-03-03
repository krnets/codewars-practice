# 8kyu - If you can't sleep, just count sheep!!

""" Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
Input will always be valid, i.e. no negative integers. """


def count_sheep(n):
    return ''.join([str(x) + ' sheep...' for x in list(range(1, n + 1))])


q = count_sheep(1)  # "1 sheep..."
q
q = count_sheep(2)  # "1 sheep...2 sheep..."
q
q = count_sheep(3)  # "1 sheep...2 sheep...3 sheep..."
q
